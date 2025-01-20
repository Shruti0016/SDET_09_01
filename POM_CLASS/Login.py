from selenium.webdriver.common.by import By
class loginPage:
    txt_useremail_id="email"
    txt_passwd_id="passwd"
    btn_signin_xpath="//*[@id='SubmitLogin']/span"

    #CONSTRUCTOR
    def __init__(self,driver):
        self.driver=driver

        #ACTIONS
    def setUserName(self,username):
        usertxt=self.driver.find_element(By.ID, self.txt_useremail_id)
        usertxt.send_keys(username)

    def setUserPasswd(self,pwd):
        passtxt=self.driver.find_element(By.ID,self.txt_passwd_id)
        passtxt.send_keys(pwd)

    def click_button(self):
        clickbutn=self.driver.find_element(By.XPATH,self.btn_signin_xpath)
        clickbutn.click()