# utils
import time
import random


class GenericUtils:
    def SleepFor(iSleepTimeIn, strRea=""):
        print("sleeping for " + str(iSleepTimeIn) + ' : ' + strRea)
        time.sleep(iSleepTimeIn)

    def SleepForRnd(rngLo=1, rngHi=60, strRea=""):
        GenericUtils.SleepFor(random.randint(rngLo, rngHi), strRea)
