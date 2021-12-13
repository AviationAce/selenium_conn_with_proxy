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
    print('Chrome_conn: all module are loaded ')

except Exception as e:

    print("Error ->>>: {} ".format(e))

class crm_Options:
    def __init__(self):
        print('crm_Options init')
        self.crm_options = webdriver.ChromeOptions()
        my_proxy_addr = '127.0.0.1:1080'
        self.crm_options.add_argument('--proxy-server=socks5://' + my_proxy_addr)
        self.crm_options.add_argument('--no-sandbox')
        self.crm_options.add_argument('--start-maximized')
        self.crm_options.add_argument('--start-fullscreen')
        self.crm_options.add_argument('--single-process')
        self.crm_options.add_argument('--disable-dev-shm-usage')
        self.crm_options.add_argument("--incognito")
        self.crm_options.add_argument(
            '--disable-blink-features=AutomationControlled')
        self.crm_options.add_argument(
            '--disable-blink-features=AutomationControlled')
        self.crm_options.add_experimental_option('useAutomationExtension', False)
        self.crm_options.add_experimental_option(
            "excludeSwitches", ["enable-automation"])
        self.crm_options.add_argument("disable-infobars")
        print('crm_options init... done')

    def get(self):
        return self.crm_options


class crm_WebDriver:
    def __init__(self):
        print('crm_WebDriver init')
        crm_options = crm_Options()
        crm_options = crm_options.get()
        # cromium_path = 'C:\\Users\\ChopperDave64\\Downloads\\chrome-win\\chrome-win\\chrome.exe'
        cromium_path = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
        crm_Service = Service()
        crm_Service.path = cromium_path
        
        self.driver = webdriver.Chrome(service=crm_Service, options=crm_options)
        # self.driver = webdriver.Chrome(service=crm_Service)
        my_driver = webdriver.Chrome(cromium_path)
        print('driver done')
        self.driver = my_driver
        print('crm_WebDriver init... done')


def main():
    print('FireFox_conn start')
    crm_conn = crm_WebDriver()
    crm_driver = crm_conn.driver
    crm_driver.get('https://www.whatismyip.com/')

    print('sleeping...')
    time.sleep(10)
    GU.GenericUtils.SleepFor(10, 'will quit after pause')

    crm_driver.quit()


if __name__ == "__main__":
    main()
