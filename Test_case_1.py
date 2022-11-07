from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC


class Test_case_1():


  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.driver.maximize_window()
    self.driver.get("https://www.booking.com")

  def test_searchDestinationFieldPlaceholder(self):
    attribute = self.driver.find_element(By.NAME,'ss').get_dom_attribute('placeholder')
    assert(attribute == "Where are you going?")


  def test_searchMessageErrors(self):
    self.driver.delete_all_cookies()
    self.driver.execute_script('localStorage.clear();')
    self.driver.find_element(By.XPATH, "//span[contains(.,'Search')]").click()
    WebDriverWait(self.driver, 5000).until(expected_conditions.visibility_of(self.driver.find_element(By.XPATH,'//form/div/div/div/div[2]/div')))
    poptext = self.driver.find_element(By.XPATH, '//form/div/div/div/div[2]/div').text
    assert("enter a destination to start searching.") in poptext 

  def teardown_method(self, method):
    self.driver.quit()
