try:
    # import sys
    # import os
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
    # from selenium.webdriver.firefox.service import Service
    from selenium.webdriver.firefox import firefox_profile
    import time
    # from webdriverdownloader import GeckoDriverDownloader
    print('FireFox_conn: all module are loaded ')

except Exception as e:

    print("Error ->>>: {} ".format(e))

class ff_Options:
    def __init__(self):
        print('ff_Options init')
        self.ff_options = Options()
        self.ff_options.add_argument('--single-process')
        self.ff_options.add_argument('--disable-dev-shm-usage')
        self.ff_options.add_argument("--incognito")
        self.ff_options.add_argument(
            '--disable-blink-features=AutomationControlled')
        self.ff_options.add_argument(
            '--disable-blink-features=AutomationControlled')
        # ff_options.add_argument('useAutomationExtension', False)
        # ff_options..add_experimental_option("excludeSwitches", ["enable-automation"])
        self.ff_options.add_argument("disable-infobars")
        self.ff_options.add_argument('user-agent=')
        

    def get(self): 
        return self.ff_options

class ff_Profile:
    def __init__(self):
        print('ff_Profile init')
        my_proxy_addr = '127.0.0.1:1080'
        ip, port = my_proxy_addr.split(':')
        self.ff_profile = webdriver.FirefoxProfile()
        self.ff_profile.set_preference('network.proxy.type', 1)
        self.ff_profile.set_preference('network.proxy.socks', ip)
        self.ff_profile.set_preference('network.proxy.socks_port', int(port))

    def get(self):
        return self.ff_profile

class ff_WebDriver:
    def __init__(self):
        print('ff_WebDriver init')
        ff_options = ff_Options()
        ff_options = ff_options.get()

        ff_profile = ff_Profile()
        ff_profile = ff_profile.get()

        gd_path = 'C:\\Users\\ChopperDave64\\bin\\geckodriver.exe'
        self.driver = webdriver.Firefox(executable_path=gd_path, options=ff_options, firefox_profile=ff_profile)


def main():
    print('FireFox_conn start')
    ff_conn = ff_WebDriver()
    ff_driver = ff_conn.driver
    ff_driver.get('https://www.whatismyip.com/')
    print('sleeping...')
    time.sleep(10)

    ff_driver.quit()

if __name__ == "__main__":
    main()
