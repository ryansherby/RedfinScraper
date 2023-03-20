from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

class _Selenium:
    def __init__(self,url,path=None):
        if path==None:
            path=""

        self.url=url
        self.path=path
        self.proxies=[]

        self.webpage=None

    def install(self):
        self.path=ChromeDriverManager.install()


    def download_proxies(self):
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)

        driver = webdriver.Chrome(options=options, service=ChromeService(self.path))
        driver.get("https://sslproxies.org/")

        driver.execute_script("return arguments[0].scrollIntoView(true);", WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//table[@class='table table-striped table-bordered']//th[contains(., 'IP Address')]"))))
        ips = [my_elem.get_attribute("innerHTML") for my_elem in WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "//table[@class='table table-striped table-bordered']//tbody//tr/td[position() = 1]")))]
        ports = [my_elem.get_attribute("innerHTML") for my_elem in WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "//table[@class='table table-striped table-bordered']//tbody//tr/td[position() = 2]")))]
        driver.quit()

        for i in range(0, len(ips)):
            self.proxies.append(ips[i]+':'+ports[i])


    def set_webpage(self,proxy=False):
        if proxy:
            for i in range(len(self.proxies)):
                try:
                    options = webdriver.ChromeOptions()
                    options.add_argument('--no-startup-window')
                    options.add_argument('--proxy-server={}'.format(self.proxies[i]))
                    driver = webdriver.Chrome(options=options,service=ChromeService(self.path))
                    driver.set_window_position(-10000,0)
                    driver.get(self.url)
                    if WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.btn-primary"))):
                        self.webpage=driver.page_source
                        driver.quit()
                        break
                except:
                    driver.quit()
        else:
            driver = webdriver.Chrome(options=options,service=ChromeService(self.path))
            driver.set_window_position(-10000,0)
            driver.get(self.url)
            if WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.btn-primary"))):
                self.webpage=driver.page_source
                driver.quit()
            else:
                driver.quit()




    def get_webpage(self):
        return self.webpage



    


