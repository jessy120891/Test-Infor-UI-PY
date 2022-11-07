from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from datetime import datetime, timedelta
import pytest

class Test_case_2():

  def setup_method(self, method):
    self.driver = webdriver.Chrome()

    global tomorrow_date
    global yesterday_date
    global today_date
    self.selector={}

    today_date = datetime.now().strftime("%Y-%m-%d")
    yesterday_date = (datetime.now() - timedelta(1)).strftime("%Y-%m-%d")
    tomorrow_date = (datetime.now() + timedelta(1)).strftime("%Y-%m-%d")

    self.selector["today"] = '//td[@data-date="'+today_date+'"]/span'
    self.selector["tomorrow"] = '//*[@data-date="'+tomorrow_date+'"]/span'
    self.selector["yesterday"] = '//*[@data-date="'+yesterday_date+'"]/span'


  def test_checkInCheckOutDates(self):

    self.driver.maximize_window()
    self.driver.get("https://www.booking.com")
    self.driver.delete_all_cookies()
    self.driver.execute_script('localStorage.clear();')
    
    WebDriverWait(self.driver, 5000).until(expected_conditions.visibility_of(self.driver.find_element(By.CLASS_NAME,"xp__dates-inner")))
    self.driver.find_element(By.CLASS_NAME,"xp__dates-inner").click()
    WebDriverWait(self.driver, 5000).until(expected_conditions.visibility_of(self.driver.find_element(By.CLASS_NAME,"bui-calendar__main.b-a11y-calendar-contrasts")))
    assert(self.driver.find_element(By.CLASS_NAME,"bui-calendar__main.b-a11y-calendar-contrasts").is_displayed() == True)

    self.driver.find_element(By.XPATH, self.selector["today"]).click()
    checked_today = self.driver.find_element(By.XPATH, self.selector['today']).get_attribute("aria-checked")
    assert(checked_today == 'true')
    self.driver.find_element(By.XPATH, self.selector["yesterday"]).click()
    checked_yesterday = self.driver.find_element(By.XPATH, self.selector["yesterday"]).get_attribute("aria-checked")
    assert(checked_yesterday == 'false')
    self.driver.find_element(By.XPATH, self.selector["tomorrow"]).click()
    checked_tomorrow = self.driver.find_element(By.XPATH, self.selector["tomorrow"]).get_attribute("aria-checked")
    assert(checked_tomorrow == 'true')
    self.driver.find_element(By.CLASS_NAME,"bui-calendar__main.b-a11y-calendar-contrasts")
    assert(self.driver.find_element(By.CLASS_NAME,"bui-calendar__main.b-a11y-calendar-contrasts").is_displayed() == False)

  def teardown_method(self, method):
    self.driver.quit()