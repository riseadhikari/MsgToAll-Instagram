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


message = "Hi There, I am just testing my program. You can ignore this message and no-reply is expected."


service = Service("path_to_msedgedriver.exe",verbose = True)
driver = webdriver.Edge(service = service)
driver.get("https://www.instagram.com")


# In[88]:


username = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
username.clear()
password.clear()
time.sleep(2)
username.send_keys(config('USERNAME'))
time.sleep(2)
password.send_keys(config('PASSWORD'))
time.sleep(2)
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


driver.get(f'https://www.instagram.com/{config("USERNAME")}/')
follower = driver.find_element(By.XPATH,"//a[contains(@href, '/followers')]/div/span")
followers = driver.find_element(By.XPATH,"//a[contains(@href, '/followers')]")
followers.click()

time.sleep(1)

# get followers count
followers_count= int(follower.text)
print("\n\nTotal Followers: {} \n\n".format(followers_count))
last_count = -1
list_of_followers = []
while True:
        
        driver.execute_script('''
                var fDialog = document.querySelector('div[role="dialog"] .isgrP');
                fDialog.scrollTop = fDialog.scrollHeight
            ''')
        time.sleep(2)
        list_of_followers_uname = driver.find_elements(By.XPATH,'//div[@class="PZuss"]/li/div/div/div[2]/div/span/a')
        
        
        list_of_followers_count = len(list_of_followers_uname)
        
#         print("Current Length is at {}".format(list_of_followers_count))
        
        if list_of_followers_count == followers_count or list_of_followers_count == last_count:
            break
        last_count = len(list_of_followers_uname)

for i in list_of_followers_uname:
    list_of_followers.append(i.text)

last_count = -1
driver.get(f'https://www.instagram.com/{config("USERNAME")}/')
follower = driver.find_element(By.XPATH,"//a[contains(@href, '/following')]/div/span")
followers = driver.find_element(By.XPATH,"//a[contains(@href, '/following')]")
followers.click()

time.sleep(1)

# get followers count
followers_count= int(follower.text)
print("\n\nTotal Following: {} \n\n".format(followers_count))
while True:
        driver.execute_script('''
                var fDialog = document.querySelector('div[role="dialog"] .isgrP');
                fDialog.scrollTop = fDialog.scrollHeight
            ''')
        time.sleep(2)
        list_of_following = driver.find_elements(By.XPATH,'//div[@class="PZuss"]/li/div/div/div[2]/div/span/a')
        
        count = len(list_of_following)
        
        if count == followers_count or count == last_count:
            break
        last_count = len(list_of_following)

following_list = []

for j in list_of_following:
    following_list.append(j.text)

for i in list_of_followers:
    if i in following_list:
        user = i
        driver.get(f'https://www.instagram.com/{user}')
        msg_button = driver.find_element(By.XPATH,'//button[@type="button"]')
        msg_button.click()
        time.sleep(4)
        try:
            message_box = driver.find_element(By.XPATH,"//textarea[contains(@placeholder,'Message...')]")
        except:
            time.sleep(2)
            message_box = driver.find_element(By.XPATH,"//textarea[contains(@placeholder,'Message...')]")
        time.sleep(2)
        message_box.clear()
        message_box.send_keys(message)
        message_box.send_keys(Keys.ENTER)
        print(f'\n\nMessage successfully sent to {user}\n\n')
    else:
        continue
print("Done!!!!")
driver.close()
driver.quit()

