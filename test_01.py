from selenium.webdriver.common.by import By
from selenium import webdriver

class Test_pytest01():
    def test_add(self):
        a = 10
        b = 20
        sum =  a + b
        print("Addition :",sum)
        if sum == 30:
            assert True
        else:
            assert False

    def test_credence_url(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://automation.credence.in/login")
        if driver.title=='CredKart':
            print("Welcome to credence")
            assert True
            driver.close()
        else:
            print("Niyojan Failed")
            driver.close()
            assert False
