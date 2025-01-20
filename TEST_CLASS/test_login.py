import pytest
from selenium import webdriver

# from POM_CLASS import Login
from POM_CLASS.Login import loginPage


class TestLogin:
    def test_login(self):
        driver=webdriver.Chrome()
        driver.get("http://www.automationpractice.pl/index.php?controller=authentication&back=my-account")
        driver.implicitly_wait(5)
        driver.maximize_window()
        lp=loginPage(driver)
        lp.setUserName("shrutimahajan1626@gmail.com")
        lp.setUserPasswd("shruti")
        lp.click_button()
        act_title=driver.title
        assert act_title=="My account - My Shop"
# C:\Users\Asus\PycharmProjects\SDET_10\Framework\TEST_CLASS\test_login.py