from selenium import webdriver
import time
import socket
import json

with open("/home/karthik/webautomates/user-info.json") as f:
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

url = "https://www.naukri.com/mnjuser/profile?id=&altresid"


for i in range(1,1000):
    try:
        for user in user_info:
	        #print(user)
            # create a new Chrome session
            driver = webdriver.Firefox()
            driver.implicitly_wait(30)
            driver.maximize_window()

            # navigate to the application home page
            driver.get(url)
            time.sleep(10)
            #get the username textbox
            login_field = driver.find_element_by_id("usernameField")
            # login_field = driver.find_element_by_name("usernameField")
            login_field.clear()

            #enter username
            login_field.send_keys(user_info[user]['Email'])
            login_field.send_keys(u'\ue007') #unicode for enter key
            time.sleep(10)

            #get the password textbox
            password_field = driver.find_element_by_id("passwordField")
            password_field.clear()

            #enter password
            password_field.send_keys(user_info[user]['PWD'])
            password_field.send_keys(u'\ue007') #unicode for enter key
            time.sleep(40)

            #navigate to gmail
            # driver.find_element_by_css_selector("a.btn.btn-block.btn-large.white-text").click()
            # driver.find_element_by_id("Karthik Giri").click()
            # time.sleep(5)
            resume = driver.find_element_by_id("attachCV")
            resume.send_keys(user_info[user]['resume'])
            # resume.send_keys(u'\ue007')
            time.sleep(10)
            driver.quit()
            time.sleep(300)
        print("resume uploaded and closed the browser Count = ",i)
    except:

        if is_connected():
            driver.quit()
            continue
        else:
            driver.quit()
            time.sleep(1800)
