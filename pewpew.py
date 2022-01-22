"""
pewpew: selenium spraying script for all them crazy m0nkeys
"""
import argparse,os,sys,random,time
from argparse import RawTextHelpFormatter
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


def create_driver(proxyaddr, user, password, resolution):
        
    capability = webdriver.DesiredCapabilities.CHROME
    capability['proxy'] = {
        "httpProxy": proxyaddr,
        "ftpProxy": proxyaddr,
        "sslProxy": proxyaddr,
        "proxyType": "manual"
    }

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument('ignore-certificate-errors')
    chrome_options.add_argument("--window-size="+resolution)
    PATH = "C:\Users\bubbles\pathto\chromedriver.exe"
    chrome_driver = webdriver.Chrome(executable_path=PATH,options=chrome_options,desired_capabilities=capability)
    return chrome_driver


def waitforit(scale=1):
    sleepnumoffset = random.random()
    offset = sleepnumoffset + scale
    time.sleep(offset)


































































































