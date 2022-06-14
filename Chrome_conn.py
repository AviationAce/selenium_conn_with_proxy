# Google Chrome	96.0.4664.93 (Official Build)(64-bit)(cohort: Stable)
# chrome://version/
# Chromium	98.0.4715.0 (Developer Build)(64-bit)

try:
    from selenium import webdriver
    from selenium.webdriver import Chrome
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.support import expected_conditions as ec
    from selenium.common.exceptions import TimeoutException
    # from selenium.webdriver.common.proxy import Proxy, ProxyType
    from selenium.webdriver.chrome.service import Service
    import time
    # from webdriverdownloader import GeckoDriverDownloader
    import GenericUtils as GU
    print('Chrome_conn: all modules are loaded ')
    import pickle
    # from webdriverdownloader import GeckoDriverDownloader
    import os

except Exception as e:
    print("Error ->>>: {} ".format(e))

myGU = GU.GenericUtils()

class cr_Options:
    def __init__(self):
        print('cr_Options init')
        self.cr_options = webdriver.ChromeOptions()
        # my_proxy_addr = '127.0.0.1:1080'
        # self.cr_options.add_argument('--proxy-server=socks5://' + my_proxy_addr)
        self.cr_options.add_argument('--no-sandbox')
        self.cr_options.add_argument('--start-maximized')
        # self.cr_options.add_argument('--start-fullscreen')
        # self.cr_options.add_argument('--single-process')
        self.cr_options.add_argument('--disable-dev-shm-usage')
        # self.cr_options.add_argument("--incognito")
        self.cr_options.add_argument(
            '--disable-blink-features=AutomationControlled')
        self.cr_options.add_argument(
            '--disable-blink-features=AutomationControlled')
        self.cr_options.add_experimental_option('useAutomationExtension', False)
        self.cr_options.add_experimental_option(
            "excludeSwitches", ["enable-automation"])
        self.cr_options.add_argument("disable-infobars")
        print('cr_options init... done')

    def get(self):
        return self.cr_options


class cr_WebDriver:
    def __init__(self):
        print('cr_WebDriver init')
        self.int_done = False
        cr_options = cr_Options()
        cr_options = cr_options.get()
        cr_Service = Service("chromedriver.exe")
        self.driver = webdriver.Chrome(
            service=cr_Service, options=cr_options)
        # self.driver = webdriver.Chrome(service=cr_Service)
        # self.driver = webdriver.Chrome(service=cr_Service)
        print('driver done')
        print('cr_WebDriver init... done')
        self.int_done = True

    def BrowserCookies(self, RorW, cookie_file):
        if os.path.exists(cookie_file):
            cookies = self.driver.get_cookies()
            if RorW == 'R':
                print(cookie_file + ' reading cookies...', end='')
                cookies = pickle.load(open(cookie_file, "rb"))
                for cookie in cookies:
                    try:
                        self.driver.add_cookie(cookie)
                    except Exception as e:
                        print("Error ->>>: {} ".format(e))
                print('done!')
        else:
            print(cookie_file + ': does not exist')

        if RorW == 'W':
            print(cookie_file + ' writing cookies...', end='')
            pickle.dump(self.driver.get_cookies(),
                        open(cookie_file, "wb"))
            print('done!')


def main():
    print('Chrome_conn start')
    cr_conn = cr_WebDriver()
    cr_driver = cr_conn.driver
    # cr_driver.get('https://www.whatismyip.com/')
    cr_driver.get('https://www.fieldnation.com/login')

    a = input()
    myGU.SleepFor(3, 'will quit after pause')

    cr_driver.quit()


if __name__ == "__main__":
    main()
