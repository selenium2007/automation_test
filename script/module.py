from  xlrd import open_workbook

import os.path
import time
from selenium import webdriver
from pages.mainpage import MainPage
from pages.loginpage import LoginPage
from pages.registerpage import RegisterPage
from pages.indexpage import IndexPage

from common.removeuser import removeUser
from common.myscreenshot import cappic


#############################################################################
def getUrl(url):
    print url
    urls=url.split('/')
    url=urls[0]+"/"+urls[1]+'/'+urls[2]+'/'+urls[3]+'/'
    return url
#############################################################################
def readTestCase(testcase_dir,testcasename,mylog):

    read_testcase = True
    testcasefile = testcase_dir + testcasename + '.xls'
    if os.path.exists(testcasefile):
        mylog.info("=====================================================================")
        mylog.info('test case file %s is found,now begin to read test case' % testcasefile)
        wbexcel = open_workbook(testcasefile)
        ws = wbexcel.sheet_by_index(0)
        testdriver=None

        for irow in range(1, ws.nrows):
            testpage = ws.cell(irow, 0).value
            teststep = ws.cell(irow, 1).value
            testdata = ws.cell(irow, 3).value
            testmsg = ws.cell(irow, 4).value

            if irow == 1:
                mylog.info('start browser')
                testdriver = getDriver(testpage, teststep, testdata, mylog)
            else:
                flag=execStep(testdriver, testpage, teststep, testdata,testmsg, mylog)

        testdriver.quit()
    else:
        mylog.info('test case file %s is not found' % testcasefile)
        read_testcase = False
    return read_testcase
#############################################################################
def execStep(driver,testpage,teststep,testdata,testmsg,mylog):

    exec_step=True
    try:
        if testpage == 'login':
            # url = driver.current_url
            # url = getUrl(url) + '/require_login'
            # if driver.current_url != url:
            #     driver.get(url)

            userlogin = LoginPage(driver)
            if teststep == 'username':
                userlogin.input_username(mylog,testdata)
            if teststep == 'password':
                userlogin.input_password(mylog,testdata)
            if teststep == 'login':
                userlogin.submit_click(mylog)
                time.sleep(3)

                if driver.current_url == testdata:
                    assert (userlogin.show_errormessage(mylog) == testmsg)

                    url = getUrl(driver.current_url)
                    mylog.info("current url %s" % url)
                    driver.get(url)

                    # userlogin.go_to_indexpage(mylog)
                    # time.sleep(3)
                    # indexpage = IndexPage(driver)
                    # indexpage.go_to_login(mylog)

                time.sleep(1)

        if testpage == 'login_success':
            mylog.info("now in login_success page")
            mainpage=MainPage(driver)
            if teststep == 'logout':

                assert (mainpage.show_usermessage(mylog)).startswith(testdata)
                mainpage.logout_from_login(mylog)
                assert driver.title=="login"
                mylog.info("current page has title %s" % driver.title)
                time.sleep(3)
######################################################################################################
        if testpage == 'register':
            # url=driver.current_url
            # url=getUrl(url) + '/require_register'
            # if driver.current_url != url:
            #     driver.get(url)

            userreg=RegisterPage(driver)
            if teststep == 'username':
                userreg.input_username(mylog,testdata)
            if teststep == 'email':
                userreg.input_email(mylog,testdata)
            if teststep == 'password':
                userreg.input_password(mylog,testdata)
            if teststep == 'confirmation':
                userreg.input_password2(mylog,testdata)
            if teststep == 'register':
                userreg.submit_click(mylog)
                time.sleep(3)

                if driver.current_url == testdata:
                    assert (userreg.show_errormessage(mylog) == testmsg)

                    url = getUrl(driver.current_url)
                    mylog.info("current url %s" % url)
                    driver.get(url)

                    # userreg.go_to_indexpage(mylog)
                    # time.sleep(3)
                    # indexpage = IndexPage(driver)
                    # indexpage.go_to_register(mylog)

                time.sleep(1)

        if testpage == 'register_success':
            mylog.info("now in register_success page")
            #url=driver.current_url

            mainpage=MainPage(driver)
            if teststep == 'home':
                assert (mainpage.show_usermessage(mylog)).startswith(testdata)
                mainpage.go_to_indexpage(mylog)
                assert driver.title=="myuser"

                mylog.info("in index page to click register button")
                indexpage = IndexPage(driver)
                indexpage.go_to_register(mylog)
                # mylog.info("go to index page to click register button")
                #     indexpage=IndexPage(driver)
                #     if teststep == 'register':
                #         indexpage.go_to_register(mylog)
                #         assert driver.title == "index"
                #         mylog.info("current page has title %s" % driver.title)
                #         time.sleep(3)
                mylog.info("current page has title %s" % driver.title)
                time.sleep(3)
                result = removeUser(testdata)  # cleanup for signup related test cases
                mylog.info("remove ")

        # if testpage == 'index':
        #     mylog.info("go to index page to click register button")
        #     indexpage=IndexPage(driver)
        #     if teststep == 'register':
        #         indexpage.go_to_register(mylog)
        #         assert driver.title == "index"
        #         mylog.info("current page has title %s" % driver.title)
        #         time.sleep(3)

        if testpage == 'other page':
            pass

    except:
        exec_step=False
        cappic(driver)
        url=getUrl(driver.current_url)
        mylog.info("current url %s" % url)
        driver.get(url)

    return exec_step
#############################################################################
def getDriver(testpage,teststep,testdata,mylog):
    if testpage == 'browser':
        if teststep == 'firefox':
            driver=webdriver.Firefox()
            mylog.info("We are using Firefox")
        elif teststep == 'chrome':
            driver=webdriver.Chrome()
            mylog.info("We are using Chrome")
        else:
            mylog.info("Unknown browser,by default we use Firefox")
            driver = webdriver.Firefox()
        driver.get(testdata)
        getdriver=driver
    else:
        mylog.info("wrong test page info %s "% testpage )
        getdriver=None
    return getdriver
#############################################################################
