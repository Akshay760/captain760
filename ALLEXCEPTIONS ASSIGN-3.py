#!/usr/bin/env python
# coding: utf-8

# In[33]:


#1..no such element exception
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

from selenium.common.exceptions import NoSuchElementException


# In[39]:


driver = webdriver.Chrome(r"chromedriver.exe")
driver.get("https://www.google.com/")
time.sleep(5)
element = driver.find_element("Hoo-Haa-hOO")
element.text


# In[ ]:


try:
    element = driver.find_element("Hoo-Haa-hOO")
    print(element.text)
except NoSuchElementException as e:
    print("Exception Raised: ", e)
    element = driver.find_element(By.XPATH,'//a[@class="gb_p"]')
    print(element.text)
    


# In[ ]:


driver.close()


# In[40]:


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# In[41]:


driver = webdriver.Chrome(r"chromedriver.exe")
driver.get("https://www.snapdeal.com/")
delay=10
WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'searchTextSpan')))
element = driver.find_element(By.XPATH,"//span[@class='searchTextSpan']")
element


# In[42]:


driver.close()


# In[43]:


#2..staleelementreferenceexception


# In[44]:


from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


# In[45]:


driver =  webdriver.Chrome(r"chromedriver.exe")
driver.get("https://www.snapdeal.com/")
try:
    element = driver.find_element(By.XPATH,"//span[@class='searchTextSpan']")
    print(element)
except StaleElementReferenceException as e:
    print ("Exception Raise: ",e)
    print ("Refresh the page!!")
    driver.get("https://www.snapdeal.com/")
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'searchTextSpan')))
    element = driver.find_element(By.XPATH,"//span[@class='searchTextSpan']")
    print(element)


# In[46]:


driver.close()


# In[47]:


#3...elementnotinteractableexception


# In[48]:


from selenium.common.exceptions import ElementNotInteractableException


# In[49]:


driver = webdriver.Chrome(r"chromedriver.exe")
driver.get("https://www.amazon.in/")
time.sleep(5)
try:
    element=driver.find_element(By.XPATH,"//i[@class='a-icon a-icon-previous-rounded']/span")
    element.click()
except ElementNotInteractableException as e:
    print ("Exception Raised: ", e)
    element = driver.find_element(By.XPATH,'//a[@class="a-carousel-goto-nextpage"]')
    driver.get(element.get_attribute('href'))
    


# In[50]:


from selenium.common.exceptions import SessionNotCreatedException
#sessionnotcreatedexceptions


# In[52]:


try:
    driver = webdriver.Chrome(r"chromedriver")
    driver.get('https://www.google.com/')
except SessionNotCreatedException as e:
    print("Exception Raised: ", e)
    driver = webdriver.Chrome(r"chromedrivr.exe")
    driver.get('https://www.google.com/')                        


# In[53]:


driver.close()


# In[54]:


#timeout exceptions


# In[55]:


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


# In[56]:


driver = webdriver.Chrome(r"chromedriver.exe")
delay=5
try:
    driver.get("https://www.amazon.in/")
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'a-section a-spacing-mini')))
    print(element)
except TimeoutException as e:
    print("Exception Raised: ", e)
    


# In[57]:


driver.close()


# In[58]:


#opening crome in icognito mode


# In[59]:


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--incognito')


# In[60]:


driver = webdriver.Chrome(r"chromedriver.exe")


# In[61]:


driver.get('https://www.google.com/')


# In[62]:


driver.close()


# In[ ]:





# In[ ]:





# In[63]:


#web scraping exceptioms handaling


# In[71]:


import selenium
import pandas as pd
import time
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
import requests
import re
from selenium.webdriver.common.by import By
import time


# In[72]:


driver = webdriver.Chrome(r"chromedriver.exe")


# In[73]:


driver.get('https://www.naukri.com/')


# In[80]:


search_field_designation=driver.find_element(By.CLASS_NAME,"suggestor-input ")
search_field_designation.send_keys("data scientist")

search_field_location=driver.find_element(By.XPATH,'/html/body/div[1]/div[6]/div/div/div[5]/div/div/div/input')
search_field_location.send_keys("Bangalore")

search_button=driver.find_element( By.XPATH,"/html/body/div[1]/div[6]/div/div/div[6]")
search_button.click()


time.sleep(4)


# In[69]:


job_opening_url = []
start=0
end=1
for page in range(start,end):
    url=driver.find_elements(By.XPATH,'//a[@class= "title ellipsis"]')
    for i in url:
        job_opening_url.append(i.get_attribute('href'))
    next_button=driver.find_elements(By.XPATH,"/html/body/div[1]/div[3]/div[2]/section[2]/div[3]/div/a[2]/span")    


# In[70]:


len(job_opening_url)


# In[1]:


job_opening_url


# In[2]:


JD=[]

for i in job_opening_url[0:10]:
    driver.get(i)
    time.sleep(5)
    try:
        description = driver.find_element(By.XPATH,'/html/body/div[1]/main/div[2]/div[2]/section[2]/div[1]')
        JD.append(description.text)
    except NoSuchElementException :
        JD.append('Not present')


# In[ ]:


JD

