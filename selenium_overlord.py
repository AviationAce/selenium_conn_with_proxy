try:
    import FireFox_conn
    import Chrome_conn
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
        self.b_using_crm: bool = False
        print('selenium_overlord init... done')

    def get_conn(self, s_driver_in: str):
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

            case 'crm':
                print(Fore.GREEN + '***** Init Chrome Webdriver *****')
                self.da_conn = Chrome_conn.crm_WebDriver()
                if self.da_conn.int_done == False:
                    myGU.SleepFor(
                        10, Fore.LIGHTRED_EX + 'The Chrome driver failed to init.  Waite 10 seconds and try just one more time.')
                    self.da_conn = Chrome_conn.crm_WebDriver()
        
        if self.da_conn.int_done == False:
            self.stat = 'bad-init'
        else:
            self.stat = 'init'
            self.b_stat = True
            self.da_driver = self.da_conn.driver

        return self.da_conn


def main():
    print('selenium_overlord start')
    so = selenium_overlord()
    drv, drv_stat = so.get_conn('ff')
    so.da_driver.get('https://ifconfig.co/')
    print('drv_stat: ' + drv_stat)
    print(input())
    so.da_driver.quit()

    

if __name__ == "__main__":
    main()
