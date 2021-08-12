"""Script to run the gulf naukri login"""

from selenium import webdriver
import time
import socket
import json
import os

path = os.getcwd()
with open(path + "/user-info-gulf.json") as f:
    user_info = json.load(f)


def is_connected():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False

def naukri_login_gulf():
    url = "https://www.naukrigulf.com/ni/nilogin/user/login"
    try:
        driver = webdriver.Firefox(executable_path='/home/karthikgiri/git-webautomates/webautomates/geckodriver')
    except Exception as err:
        print("Unable to launch the browser with error", err)
    if driver:
        try:
            for user in user_info:
                # create a new Chrome session
                driver.implicitly_wait(30)
                driver.maximize_window()

                # navigate to the application home page
                driver.get(url)
                time.sleep(5)
                # get the username textbox
                login_field = driver.find_element_by_id("loginPageLoginEmail")
                # enter username
                login_field.send_keys(user_info[user]['Email'])
                # time.sleep(5)
                # get the password textbox
                password_field = driver.find_element_by_id("loginPassword")
                # enter password
                password_field.send_keys(user_info[user]['PWD'])
                # time.sleep(5)
                # navigate to gmail
                driver.find_element_by_id("loginPageLoginSubmit").click()
                driver.find_element_by_css_selector("a.ng-btn.blue.cc-list-btn").click()
                time.sleep(10)
                ########################################################
                resume = driver.find_element_by_id("resumeSection")
                resume.send_keys(user_info[user]['resume'])
                time.sleep(5)
                # resume.send_keys(u'\ue007')
                driver.quit()
        except:
            if is_connected():
                driver.quit()
            else:
                driver.quit()
                time.sleep(1800)
