try:
    import FireFox_conn
    import Chrome_conn
    from time import sleep
    from colorama import Fore, Back, Style
    import GenericUtils as GU

    print('selenium_overlord: all modules are loaded ')

except Exception as e:
    print("Error ->>>: {} ".format(e))

myGU = GU.GenericUtils()


class selenium_overlord:
    def __init__(self) -> None:
        # has driver obj been init
        self.b_conn_est: bool = False
        # using the FireFox driver
        self.b_using_ff: bool = False
        # using the Crome driver
        self.b_using_cr: bool = False
        # handel for FN tab
        self.hdl_FN = None
        # handel for WM tab
        self.hdl_WM = None
        # handel for working tab
        self.hdl_working = None
        print('selenium_overlord init... done')

    # This will init a conn with the spcified engine
    # The self.stat and the self.b_stat vars will be set
    def init_conn(self, s_driver_in: str):
        ret = False
        self.s_stat: str = 'not-init'
        self.b_stat: bool = False
        match s_driver_in:
            case 'ff':
                print(Fore.GREEN + '***** Init Firefox Webdriver *****')
                self.da_conn = FireFox_conn.ff_WebDriver()
                if self.da_conn.int_done == False:
                    myGU.SleepFor(
                        10, Fore.LIGHTRED_EX + 'The FireFox driver failed to init.  Waite 10 seconds and try just one more time.')
                    self.da_conn = FireFox_conn.ff_WebDriver()

            case 'cr':
                print(Fore.GREEN + '***** Init Chrome Webdriver *****')
                self.da_conn = Chrome_conn.cr_WebDriver()
                if self.da_conn.int_done == False:
                    myGU.SleepFor(
                        10, Fore.LIGHTRED_EX + 'The Chrome driver failed to init.  Waite 10 seconds and try just one more time.')
                    self.da_conn = Chrome_conn.cr_WebDriver()

        if self.da_conn.int_done == False:
            self.stat = 'bad-init'
        else:
            self.stat = 'init'
            self.b_stat = True
            self.da_driver = self.da_conn.driver
            ret = True

        return ret

    def get_tab_count(self):
        return len(self.da_driver.window_handles)

    # close tab by number

    def close_tab_by_number(self, number):
        ret = False
        try:
            self.da_driver.switch_to.window(
                self.da_driver.window_handles[number])
            self.da_driver.close()
        except Exception as e:
            print("Error ->>>: {} ".format(e))

        return ret

    # close tab by handel
    def close_tab_by_handel(self, handel_to_close):
        self.da_driver.switch_to.window(handel_to_close)
        self.da_driver.close()

    def get_tab_hdl_by_title(self, tab_title):
        ret = 'not found'
        for so_tab in self.da_driver.window_handles:
            self.da_driver.switch_to.window(so_tab)
            # print(self.da_driver.title)
            if str(self.da_driver.title).find(tab_title) > -1:
                ret = so_tab
                break
        return ret

    # open new tab and return tab posistion

    def open_new_tab(self, s_url: str = ''):
        old_tabs = self.da_driver.window_handles
        if s_url == '':
            self.da_driver.execute_script(
                '''window.open("", "_blank");''')
        else:
            self.da_driver.execute_script(
                '''window.open("''' + s_url + '''", "_blank");''')
        new_tabs = self.da_driver.window_handles
        for tab in new_tabs:
            if tab in old_tabs:
                pass
            else:
                new_tab = tab
        self.da_driver.switch_to.window(new_tab)

        return new_tab

    def BringBrowserToFocus(self):
        self.da_driver.minimize_window()
        self.da_driver.maximize_window()

    # will return the handel, 'quit' or 'not found'
    def get_past_captcha(self, title_of_tab):
        ret = ''
        Captcha_done = ''
        while Captcha_done != 'q':
            print('Open a new tabe and get past the Captcha.  Enter ''q'' to quit, anything else to continue.')
            Captcha_done = input('Captcha done?')
            if Captcha_done == 'q':
                print('quitting...')
                ret = 'quit'
            else:
                ret = self.get_tab_hdl_by_title(title_of_tab)
                if ret == 'not found':
                    print('tab not found')
        
        return ret




def main():
    print('selenium_overlord start')
    so = selenium_overlord()
    so.init_conn('cr')

    so.da_driver.get('https://ifconfig.co/')
    print('drv_stat: ' + so.s_stat)
    print(so.get_tab_count())
    so.open_new_tab('https://www.whatismyip.com/')
    print(so.get_tab_count())
    sleep(5)
    so.close_tab_by_number(0)
    a = ''
    while a != 'q':
        # for so_tab in so.da_driver.window_handles:
        #     so.da_driver.switch_to.window(so_tab)
        #     print(so.da_driver.title)
        #     if str(so.da_driver.title).find('Field Nation') > 0:
        #         print('found FN: ' + so_tab)

        print(so.get_tab_hdl_by_title('Log in to Field Nation'))
        sleep(2)

        print(so.get_tab_count())
        a = input()
    so.da_driver.quit()


if __name__ == "__main__":
    main()
