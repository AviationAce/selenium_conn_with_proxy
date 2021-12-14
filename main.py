# TO DO
# build and import FireFox, Chrome and Chromium libs that return a driver object going thru my proxy

import sys
from typing import Generic
import FireFox_conn
# PYTHONPATH=C:\Users\ChopperDave64\OneDrive\Code\VS Code\Common_SDER_utils;C:\Users\ChopperDave64\OneDrive\Code\VS Code\selenium_conn_with_proxy;
import GenericUtils as GU

def main():
    print('main start')
    ff_conn = FireFox_conn.ff_WebDriver()
    ff_driver = ff_conn.driver
    ff_driver.get('https://www.expressvpn.com/what-is-my-ip')
    ff_driver.get('http://httpbin.org/ip')
    GU.GenericUtils.SleepFor(10, 'will quit after pause')
    ff_driver.quit()
    print(sys.path)


if __name__ == "__main__":
    main()
