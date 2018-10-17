import time,os
from selenium import webdriver
from pages.basepage import BasePage
from selenium.webdriver.common.by import By
from common.mylog import LogGen

class LoginPage(BasePage):

    username = (By.NAME, 'username')
    password = (By.NAME, 'password')
    submit = (By.NAME, 'loginbtn')
    err_msg = (By.NAME, 'errormsg')
    home_btn_loc = (By.NAME, 'homebtn')

    def clear_username(self,mylog):
        self.myelement(*self.username).clear()
        mylog.info("clear user name")

    def input_username(self,mylog,uname):
        self.myelement(mylog,*self.username).send_keys(uname)
        mylog.info("input user name: %s" % uname)

    def clear_password(self,mylog):
        self.myelement(*self.password).clear()
        mylog.info("clear user password")


    def input_password(self,mylog,pwd):
        self.myelement(mylog,*self.password).send_keys(pwd)
        mylog.info("input user password: %s" % pwd)

    def submit_click(self,mylog):
        self.myelement(mylog,*self.submit).click()
        mylog.info("click login button")

    def show_errormessage(self,mylog):
        errormessage=self.myelement(mylog,*self.err_msg).text
        mylog.info("current error message : %s " % errormessage)
        return errormessage

    def go_to_indexpage(self,mylog):
        self.myelement(mylog,*self.home_btn_loc).click()
        mylog.info("in indexpage")

if __name__=="__main__":
  now = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
  logname = os.path.dirname(os.path.abspath('.')) + '\\logs\\' + now + '.log'
  mylog = LogGen("TestSuite", logname).getLog()
  driver = webdriver.Firefox()

  driver.get("http://192.168.1.159:8080/require_login")
  userlogin = LoginPage(driver)
  userlogin.input_username(mylog,"curtis")
  userlogin.input_password(mylog,"qqqq")
  userlogin.submit_click(mylog)
  time.sleep(5)
