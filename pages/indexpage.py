
from pages.basepage import BasePage
from selenium.webdriver.common.by import By

class IndexPage(BasePage):

    register_btn_loc=(By.NAME,'registerbtn')
    login_btn_loc=(By.NAME,'loginbtn')

    #the following is optional
    def open(self,mylog,base_url):
        self._open(self.base_url, self.pagetitle)
        mylog.info("open link: %s " % base_url)

    def go_to_register(self,mylog):
        self.myelement(mylog,*self.register_btn_loc).click()
        mylog.info("now in register page")

    def go_to_login(self,mylog):
        self.myelement(mylog,*self.login_btn_loc).click()
        mylog.info("now in login page")