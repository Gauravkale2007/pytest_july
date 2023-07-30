import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class Test_pytest_02():
    def test_sub(self):
        a = 20
        b = 5
        sub = a - b
        print("Substraction :",sub)
        if sub==15:
            assert True
        else:
            assert False
    def test_order_verification(self):

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get('https://automation.credence.in/login')

        driver.find_element(By.XPATH, "//input[@id='email']").send_keys('credencetest@test.com')

        driver.find_element(By.XPATH, "//input[@id='password']").send_keys('Credence@123')

        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        driver.find_element(By.XPATH, "//h3[normalize-space()='Apple iPad Retina']").click()

        driver.find_element(By.XPATH, "//input[@value='Add to Cart']").click()

        driver.find_element(By.XPATH, "//a[@class='btn btn-primary btn-lg']").click()

        driver.find_element(By.XPATH, "//h3[normalize-space()='Speakers']").click()

        driver.find_element(By.XPATH, "//input[@value='Add to Cart']").click()

        driver.find_element(By.XPATH, "//a[@class='btn btn-primary btn-lg']").click()

        driver.find_element(By.XPATH, "//h3[normalize-space()='Playstation 4']").click()

        driver.find_element(By.XPATH, "//input[@value='Add to Cart']").click()

        Product_1 = Select(driver.find_element(By.XPATH, "//tbody//tr[1]//td[3]/select"))
        Product_1.select_by_index(3)

        Product_2 = Select(driver.find_element(By.XPATH, "//tbody//tr[2]//td[3]/select"))
        Product_2.select_by_index(2)

        Product_3 = Select(driver.find_element(By.XPATH, "//tbody//tr[3]//td[3]/select"))
        Product_3.select_by_index(3)
        time.sleep(2)

        # print('Money to be paid:-', grand_total)

        # click on proceed to checkout
        driver.find_element(By.XPATH, "//a[@class='btn btn-success btn-lg']").click()

        driver.find_element(By.XPATH, "//input[@id='first_name']").send_keys('Credence')  # first name

        driver.find_element(By.XPATH, "//input[@id='last_name']").send_keys('Pune')  # last name

        driver.find_element(By.XPATH, "//input[@id='phone']").send_keys('9091929355')  # phoneno

        driver.find_element(By.XPATH, "//textarea[@id='address']").send_keys('Dhankawdi,Pune')  # address

        driver.find_element(By.XPATH, "//input[@id='zip']").send_keys('411013')  # zipcode

        driver.find_element(By.XPATH, "//select[@id='state']").send_keys('Pune')  # state

        driver.find_element(By.XPATH, "//input[@id='owner']").send_keys('Tushar')

        driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys('4716')  # 4716 1089 9971 6531
        driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys('1089')
        driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys('9971')
        driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys('6531')

        driver.find_element(By.XPATH, "//input[@id='cvv']").send_keys('257')

        year = Select(driver.find_element(By.XPATH, "//select[@id='exp_year']"))
        year.select_by_index(2)
        month = Select(driver.find_element(By.XPATH, "//select[@id='exp_month']"))
        month.select_by_index(3)

        driver.find_element(By.XPATH, "//button[@id='confirm-purchase']").click()
        if driver.title=="CredKart":
            print("Payment Successful Order is on your way")
            assert True
        else:
            print("lavdya paise ahet kaa")
            driver.close()
            assert False


