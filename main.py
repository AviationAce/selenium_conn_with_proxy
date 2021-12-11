# TO DO
# build and import FireFox, Chrome and Chromium libs that return a driver object going thru my proxy

import time
import FireFox_conn


def main():
    print('main start')
    ff_conn = FireFox_conn.ff_WebDriver()
    ff_driver = ff_conn.driver
    ff_driver.get('https://www.expressvpn.com/what-is-my-ip')
    print('sleeping...')
    time.sleep(10)
    ff_driver.quit()

if __name__ == "__main__":
    main()
