#!/usr/bin/env python
# coding: utf-8


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.edge.service import Service


import os
import wget
import time
import pprint
import os
from decouple import config


# # Message to Send





service = Service(os.path.join("edgedriver","msedgedriver.exe"),verbose = True)
driver = webdriver.Edge(service = service)
driver.get("https://www.instagram.com")


# In[88]:

your_username = ' '  #your instagram username here.
your_password = ' '  #your instagram password here for login.

username = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
username.clear()
password.clear()
time.sleep(2)
username.send_keys(your_username)
time.sleep(2)
password.send_keys(your_password)
time.sleep(4)
try:
    login =  WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
except:
    print("Couldn't login....")
    os._exit()
try:
    now_now =  WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(text(), 'Not Now')]"))).click()
    now_now2 =  WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(text(), 'Not Now')]"))).click()
except:
    pass


# In[89]:


driver.get(f'https://www.instagram.com/{your_username}/')
time.sleep(4)
follower = driver.find_element(By.XPATH,"//a[contains(@href, '/followers')]/div/span")
followers = driver.find_element(By.XPATH,"//a[contains(@href, '/followers')]")
followers.click()

time.sleep(1)

# get followers count
followers_count= int(follower.text)
print("\n\nTotal Followers: {} \n\n".format(followers_count))
last_count = -1
list_of_followers = []
list_of_followers_uname = []
while True:
        
        driver.execute_script('''
                var fDialog = document.querySelector('._aano');
                fDialog.scrollTop = fDialog.scrollHeight
            ''')
        time.sleep(2)
        list_of_followers_uname = driver.find_elements(By.XPATH,'//span[@class="_aacl _aaco _aacw _adda _aacx _aad7 _aade"]/div')

        
        
        list_of_followers_count = len(list_of_followers_uname)
        
        # print("\n Count " + str(list_of_followers_count) + "\n")

#         print("Current Length is at {}".format(list_of_followers_count))
        
        if list_of_followers_count == followers_count or list_of_followers_count == last_count:
            break
        last_count = len(list_of_followers_uname)

for i in list_of_followers_uname:
    list_of_followers.append(i.text)


# print(list_of_followers)

# print("\n\n\n\n")

last_count = -1
driver.get(f'https://www.instagram.com/{your_username}/')
time.sleep(4)
follower = driver.find_element(By.XPATH,"//a[contains(@href, '/following')]/div/span")
followers = driver.find_element(By.XPATH,"//a[contains(@href, '/following')]")
followers.click()

time.sleep(3)

# get followers count
followers_count= int(follower.text)
print("\n\nTotal Following: {} \n\n".format(followers_count))
list_of_following = []
while True:
        driver.execute_script('''
                var fDialog = document.querySelector('._aano');
                fDialog.scrollTop = fDialog.scrollHeight
            ''')
        time.sleep(1)
        list_of_following = driver.find_elements(By.XPATH,'//span[@class="_aacl _aaco _aacw _adda _aacx _aad7 _aade"]/div')
        
        count = len(list_of_following)
        
        if count == followers_count or count == last_count:
            break
        last_count = len(list_of_following)
        print(str(last_count) + "\n\n\n")

following_list = []

for j in list_of_following:
    following_list.append(j.text)

for i in list_of_followers:
    if i in following_list:
        user = i
        driver.get(f'https://www.instagram.com/{user}')
        time.sleep(4)
        try:
            msg_button = driver.find_element(By.XPATH,'//button[@type="button"]')
            msg_button.click()
        except e as Exception:
            print("\n Error " + str(e) + "\n")
            continue
        time.sleep(4)
        try:
            message_box = driver.find_element(By.XPATH,"//textarea[contains(@placeholder,'Message...')]")
        except:
            time.sleep(2)
            message_box = driver.find_element(By.XPATH,"//textarea[contains(@placeholder,'Message...')]")
        time.sleep(2)
        message_box.clear()
        message = " " # message_to_send here
        message_box.send_keys(message)
        message_box.send_keys(Keys.ENTER)
        time.sleep(0.5)
        print(f'\n\nMessage successfully sent to {user}\n\n')
    else:
        continue
print("Done!!!!")
driver.close()
driver.quit()