from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestHome():
    def setup(self):
        chromeOptions = Options()
        chromeOptions.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        self.driver = webdriver.Chrome(options=chromeOptions)

    def test_home(self):
        self.driver.find_element(By.CSS_SELECTOR, '#js_openapiDocHref').click()
        d = self.driver.window_handles
        self.driver.switch_to.window(d[1])
