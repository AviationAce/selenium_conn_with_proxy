# TO DO
# build and import FireFox, Chrome and Chromium libs that return a driver object going thru my proxy

import sys
from typing import Generic
# sys.path.insert(1, '../Common_SDER_utils')
# sys.path.insert(1, '\\Users\\ChopperDave64\\OneDrive\\Code\\VS Code\\Common_SDER_utils\\GenericUtils.py')
import FireFox_conn
import GenericUtils as GU

def main():
    print('main start')
    ff_conn = FireFox_conn.ff_WebDriver()
    ff_driver = ff_conn.driver
    # ff_driver.get('https://www.expressvpn.com/what-is-my-ip')
    ff_driver.get('http://httpbin.org/ip')
    GU.GenericUtils.SleepFor(10, 'will quit after pause')
    ff_driver.quit()

if __name__ == "__main__":
    main()
