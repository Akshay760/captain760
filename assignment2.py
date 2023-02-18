#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
import selenium
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time


# In[16]:


driver=webdriver.Chrome(r"C:\Users\USER\Downloads\chromedriver.exe")


# In[17]:


driver.get("https://www.naukri.com/")


# In[18]:


designation=driver.find_element(By.CLASS_NAME,"suggestor-input")
designation.send_keys('data analyst')


# In[19]:


location=driver.find_element(By.XPATH,"/html/body/div[1]/div[6]/div/div/div[5]/div/div/div/input")
location.send_keys('bangalore')


# In[20]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[35]:


job_title=[]
job_location=[]
company_name=[]
experience_required=[]


# In[36]:


title_tags=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in title_tags[0:10]:
    title=i.text
    job_title.append(title)


# In[37]:


#scraping location
location_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in location_tags[0:10]:
    location=i.text
    job_location.append(location)


# In[38]:


#scraping company name
company_tags=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in company_tags[0:10]:
    company=i.text
    company_name.append(company_name)


# In[39]:


#scraping experience
experience_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft expwdth"]')
for i in experience_tags[0:10]:
    exp=i.text
    experience_required.append(exp)


# In[40]:


print(len(job_title),len(job_location),len(company),len(experience_required))


# In[42]:


import pandas as pd
df=pd.DataFrame({'title':job_title,'location':job_location,'company_name':company_name,'experience':experience_required})
df


# In[ ]:




