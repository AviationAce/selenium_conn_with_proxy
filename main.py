# TO DO
# build and import FireFox, Chrome and Chromium libs that return a driver object going thru my proxy


import FireFox_conn


def main():
    print('main start')
    ff_conn = FireFox_conn.ff_WebDriver()
    ff_driver = ff_conn.driver


if __name__ == "__main__":
    main()
