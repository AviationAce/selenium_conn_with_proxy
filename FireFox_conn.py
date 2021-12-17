try:
    from selenium import webdriver
    from selenium.webdriver import Firefox
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from selenium.webdriver.firefox.options import Options
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.support import expected_conditions as EC
    # from selenium.common.exceptions import TimeoutException
    from selenium.webdriver.common.proxy import Proxy, ProxyType
    from selenium.webdriver.firefox.service import Service
    # from selenium.webdriver.firefox import firefox_profile
    # import time
    import pickle
    # from webdriverdownloader import GeckoDriverDownloader
    import GenericUtils as GU
    print('FireFox_conn: all module are loaded ')

except Exception as e:
    print("Error ->>>: {} ".format(e))


class ff_Options:
    def __init__(self):
        print('  ff_Options init')
        self.ff_options = Options()
        self.ff_options.add_argument('--single-process')
        self.ff_options.add_argument('--disable-dev-shm-usage')
        self.ff_options.add_argument("--incognito")
        self.ff_options.add_argument(
            '--disable-blink-features=AutomationControlled')
        self.ff_options.add_argument(
            '--disable-blink-features=AutomationControlled')
        self.ff_options.add_argument("disable-infobars")
        self.ff_options.add_argument('user-agent=')
        # NOTE: Using ShadowSocks on Windows.  That's why there is not username and password
        my_proxy_addr = '127.0.0.1:1080'
        ip, port = my_proxy_addr.split(':')
        self.ff_options.set_preference('network.proxy.type', 1)
        self.ff_options.set_preference('network.proxy.socks', ip)
        self.ff_options.set_preference('network.proxy.socks_port', int(port))

        print('  ff_Options init... done')

    def get(self):
        return self.ff_options


class ff_WebDriver:
    def __init__(self):
        print('ff_WebDriver init')
        ff_options = ff_Options()
        ff_options = ff_options.get()

        gd_path = 'C:\\Users\\ChopperDave64\\bin\\geckodriver.exe'
        ff_service = Service()
        ff_service.path = gd_path

        self.driver = webdriver.Firefox(options=ff_options, service=ff_service)
        print('ff_WebDriver init... done')

    def BrowserCookies(self, RorW):
        cookie_file = "ff_cookies.pkl"
        cookies = self.driver_instance.get_cookies()
        if RorW == 'R':
            print('reading cookies...', end='')
            cookies = pickle.load(open(cookie_file, "rb"))
            for cookie in cookies:
                self.driver_instance.add_cookie(cookie)
            print('done!')

        if RorW == 'W':
            print('writing cookies...', end='')
            pickle.dump(self.driver_instance.get_cookies(),
                        open(cookie_file, "wb"))
            print('done!')


def main():
    print('FireFox_conn start')
    ff_conn = ff_WebDriver()
    ff_driver = ff_conn.driver
    ff_driver.get('https://www.whatismyip.com/')
    GU.GenericUtils.SleepFor(10, 'will quit after pause')
    
    ff_driver.quit()


if __name__ == "__main__":
    main()
