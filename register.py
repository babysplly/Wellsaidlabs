import itertools
import threading
import os,time,sys
from asyncore import write
from importlib import import_module
from lib2to3.pgen2.driver import Driver
from lib2to3.pgen2.token import NAME
from re import A, search
from unicodedata import name
from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


#style
banner = """\u001b[1m \u001b[1;31m 
    AUTO     _ __              _ __     __ 
 _  REGISTER/ / /__ ___ _(_)__/ / /__ _/ /  ___  
| |/|/ / -_) / (_-</ _ `/ / _  / / _ `/ _ \(_-<_ 
|__,__/\__/_/_/___/\_,_/_/\_,_/_/\_,_/_.__/___(_)   \u001b[0m \u001b[1m                 
                                   Author: Splly \u001b[0m"""
print(banner)

#text
warning = """\u001b[34m
*don't type your real email and password, use other password
 also u can use temp mail, here: https://temp-mail.org/ \u001b[0m\033[1m
______________________________________________________________\u001b[0m
"""
print(warning)

#start 
eminpt=input ("Email    :")


#animation
done = False
#here is the animation
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break    
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\r\033[92mPassword :W3K#eadVB4Y!!fT')

t = threading.Thread(target=animate)
t.start()

#long process here


driver = webdriver.Firefox()
driver.get ("https://wellsaidlabs.com/")

search = driver.find_element(By.XPATH, "/html/body/div[3]/section[1]/div/div[1]/div/section/div/div/div/div[1]/div/div/a")
search.click()

fn = driver.find_element(By.NAME, "firstName")
fn.send_keys("firstName")

ln= driver.find_element(By.NAME, "lastName")
ln.send_keys("lastname")

eml= driver.find_element(By.NAME, "email")
eml.send_keys(eminpt)

cn= driver.find_element(By.NAME, "companyName")
cn.send_keys("companyName")

pw= driver.find_element(By.NAME, "password")
pw.send_keys("W3K#eadVB4Y!!fT")

smt= driver.find_element(By.XPATH, "//*[@id='signup-form']/button")
smt.click()

#animation end here
done = True  
time.sleep (3)
driver.quit()
  
