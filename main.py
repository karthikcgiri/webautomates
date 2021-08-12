"""Main file to run the both the scripts with specified time delay"""
import time
import login_naukri
import gulf_login_naukri

for i in range(1, 1000):
    try:
        login_naukri.naukri_login_india()
    except Exception as err:
        print("Naukri INDIA Login Error :", err)
    print("Naukri INDIA profile updated %d times" % i)
    time.sleep(300)
    try:
        gulf_login_naukri.naukri_login_gulf()
    except Exception as err:
        print("Naukri Gulf Login Error :", err)
    print("Naukri GULF profile updated %d times" % i)
    time.sleep(300)
