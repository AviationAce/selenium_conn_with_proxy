# TO DO
# build and import FireFox, Chrome and Chromium libs that return a driver object going thru my proxy

import FireFox_conn
import GenericUtils as GU

def main():
    print('main start')
    ff_conn = FireFox_conn.ff_WebDriver()
    ff_driver = ff_conn.driver
    ff_driver.get('https://www.expressvpn.com/what-is-my-ip')
    GU.GenericUtils.SleepFor(10, 'will quit after pause')
    ff_driver.quit()

if __name__ == "__main__":
    main()
