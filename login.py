from distutils.command import config
from importlib import import_module
from importlib.machinery import BYTECODE_SUFFIXES
from lib2to3.pgen2.driver import Driver
from lib2to3.pgen2.token import NAME
from mimetypes import init
from re import A, search
from unicodedata import name
from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import os,time

#style
banner = """\u001b[1m \u001b[1;31m 
    AUTO     _ __              _ __     __ 
 _  LOGIN__ / / /__ ___ _(_)__/ / /__ _/ /  ___  
| |/|/ / -_) / (_-</ _ `/ / _  / / _ `/ _ \(_-<_ 
|__,__/\__/_/_/___/\_,_/_/\_,_/_/\_,_/_.__/___(_)   \u001b[0m \u001b[1m                 
                                   Author: Splly \u001b[0m\033[1m
__________________________________________________\u001b[0m"""
print(banner)

#text
warning = """\u001b[34m
*type your register email and password 
 then klick verif on ur email, here: https://temp-mail.org/ \u001b[0m
"""
print(warning)

#start
hasil1 = input ("Input Email :")
hasil2 = input ("Input Password :")
 

driver = webdriver.Firefox()
driver.get ("https://studio.wellsaidlabs.com/auth/sign_in?redirect_to= dashboard")

time.sleep (1)


email = driver.find_element(By.ID, "1-email")
email.send_keys(hasil1)

password = driver.find_element(By.NAME, "password")
password.send_keys(hasil2)

smt = driver.find_element(By.NAME, "submit" )
smt.click()
time.sleep(5)

driver.quit()
