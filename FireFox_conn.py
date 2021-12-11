try:
    import sys
    import os
    from selenium import webdriver
    from selenium.webdriver import Firefox
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from selenium.webdriver.firefox.options import Options
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.support import expected_conditions as ec
    from selenium.common.exceptions import TimeoutException
    from selenium.webdriver.common.proxy import Proxy, ProxyType
    from selenium.webdriver.firefox.service import Service
    import time
    # from webdriverdownloader import GeckoDriverDownloader
    print('FireFox_conn: all module are loaded ')

except Exception as e:

    print("Error ->>>: {} ".format(e))

class ff_WebDriver:
    def __init__(self):
        print('ff_WebDriver init')

        gd_path = 'C:\\Users\\ChopperDave64\\bin\\geckodriver.exe'
        ff_service = Service(gd_path)
        
        # my_proxy_addr = '127.0.0.1:1080'
        ff_options = Options()
        ff_options.add_argument('--single-process')
        ff_options.add_argument('--disable-dev-shm-usage')
        ff_options.add_argument("--incognito")
        ff_options.add_argument('--disable-blink-features=AutomationControlled')
        ff_options.add_argument('--disable-blink-features=AutomationControlled')
        # ff_options.add_argument('useAutomationExtension', False)
        # ff_options..add_experimental_option("excludeSwitches", ["enable-automation"])
        ff_options.add_argument("disable-infobars")
        ff_options.add_argument('user-agent=')
        self.driver = webdriver.Firefox(service=ff_service, options=ff_options)
        # self.driver = webdriver.Firefox(executable_path=gd_path, options=ff_options)


def main():
    print('FireFox_conn start')
    ff_conn = ff_WebDriver()

    time.sleep(10)


if __name__ == "__main__":
    main()
