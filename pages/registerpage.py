from pages.basepage import BasePage
from selenium.webdriver.common.by import By

class RegisterPage(BasePage):
    username=(By.NAME,'username')
    email=(By.NAME,'email')
    password=(By.NAME,'password')
    confirmpwd=(By.NAME,'password2')
    submit=(By.NAME,'registerbtn')
    err_msg = (By.NAME, 'errormsg')
    home_btn_loc = (By.NAME, 'homebtn')

    def input_username(self,mylog,uname):
        self.myelement(mylog,*self.username).send_keys(uname)
        mylog.info("input user name: %s" % uname)

    def input_email(self,mylog,myemail):
        self.myelement(mylog,*self.email).send_keys(myemail)
        mylog.info("input email: %s" % myemail)

    def input_password(self,mylog,pwd):
        self.myelement(mylog,*self.password).send_keys(pwd)
        mylog.info("input password: %s" % pwd)

    def input_password2(self,mylog,pwd2):
        self.myelement(mylog,*self.confirmpwd).send_keys(pwd2)
        mylog.info("confirm password: %s" % pwd2)

    def submit_click(self,mylog):
        self.myelement(mylog,*self.submit).click()
        mylog.info("click register button")

    def show_errormessage(self, mylog):
        errormessage = self.myelement(mylog, *self.err_msg).text
        mylog.info("current user message : %s " % errormessage)
        return errormessage

    def go_to_indexpage(self,mylog):
        self.myelement(mylog,*self.home_btn_loc).click()
        mylog.info("in indexpage")