from selenium import webdriver
import time
import socket
from selenium.webdriver.common.keys import Keys


def is_connected():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False

for i in range(1,2):
        # try:
        # create a new Chrome session
        driver = webdriver.Firefox(executable_path='/home/karthikgiri/git-webautomates/webautomates/geckodriver')
        driver.implicitly_wait(30)
        driver.maximize_window()

        # navigate to the application home page
        driver.get("https://www.monsterindia.com/rio/login")

        #get the username textbox
        login_field = driver.find_element_by_id("signInName")
        # login_field = driver.find_element_by_name("usernameField")
        login_field.clear()

        #enter username
        login_field.send_keys("karthikcgiri@hotmail.com")
        login_field.send_keys(u'\ue007') #unicode for enter key
        time.sleep(2)

        #get the password textbox
        password_field = driver.find_element_by_id("password")
        password_field.clear()

        #enter password
        password_field.send_keys("kaushik")
        password_field.send_keys(u'\ue007') #unicode for enter key
        time.sleep(5)
        driver.find_element_by_css_selector("a.line-btn.btn-update-profile.w100.text-center").click()
        time.sleep(5)
        resu = driver.find_element_by_css_selector("i.mqfi-upload").click()
        resume = driver.find_element_by_id("resume")
        # resume.send_keys(u'\ue007')
        resume.send_keys("/home/karthikgiri/git-webautomates/webautomates/Karthik-June-2021CV.docx")
        time.sleep(5)
        ok = driver.find_element_by_class_name("div.form-control.fixed-button mb0").click()
        # driver.find_element_by_class_name("div.col-md-12.text-right").click()
        # driver.find_element_by_css_selector("button.btn.wt-100.pt10.pb10.no-radius").click()
        print("111111111111111111111111111111111")
        # driver.execute_script("arguments[0].scrollIntoView();", element)
#         # resume.send_keys("/home/kartik/Downloads/Resume.docx")
#         # resume.send_keys(u'\ue007')
#         print("111111111111111111111111111111111")
#         time.sleep(10)
#         driver.quit()
#         time.sleep(300)
#         print("resume uploaded and closed the browser Count ="),i
'''
    except:

        if is_connected():
            driver.quit()
            continue
        else:
            driver.quit()
            time.sleep(1800)
'''

