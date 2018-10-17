
from pages.basepage import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    usermessage_loc=(By.NAME,'message')
    logout_btn_loc=(By.NAME,'logoutbtn')
    # the following is used for register
    home_btn_loc=(By.NAME,'homebtn')


    #the following is optional
    def open(self,mylog,base_url):
        self._open(self.base_url, self.pagetitle)
        mylog.info("open link: %s " % base_url)

    def show_usermessage(self,mylog):
        usermessage=self.myelement(mylog,*self.usermessage_loc).text
        mylog.info("current user message : %s " % usermessage)
        return usermessage

    def logout_from_login(self,mylog):
        self.myelement(mylog,*self.logout_btn_loc).click()
        mylog.info("logout from application")

#the following is used for register
    def go_to_indexpage(self,mylog):
        self.myelement(mylog,*self.home_btn_loc).click()
        mylog.info("in indexpage")