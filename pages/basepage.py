
from selenium.webdriver.support.wait import WebDriverWait
from common.myscreenshot import cappic
from selenium.webdriver.support import expected_conditions as EC

class BasePage():
    def __init__(self,driver):
        self.driver = driver

    def on_page(self, pagetitle):
        return pagetitle in self.driver.title

    def _open(self, url, pagetitle):
        self.driver.get(url)
        self.driver.maximize_window()
        assert self.on_page(pagetitle), "fail to open page %s" % url

    def myelement(self,mylog, *loc):

        try:

            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            #WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except:
            cappic(self.driver)
            mylog.info(" page %s has no element %s " % (self, loc))
###################################################################################
    # def send_keys(self,mylog,loc,value):
    #     try:
    #         loc=getattr(self,"_%s" % loc)
    #         self.myelement(mylog,*loc).send_keys(value)
    #     except AttributeError:
    #         cappic(self.driver)
    #         mylog.info(" page %s has no element %s " % (self, loc))
    #
    # def click(self,mylog,loc):
    #     try:
    #         loc = getattr(self, "_%s" % loc)
    #         self.myelement(mylog,*loc).click()
    #     except AttributeError:
    #         cappic(self.driver)
    #         mylog.info(" page %s has no element %s " % (self, loc))
