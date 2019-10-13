from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from time import sleep
import sys
import urllib.request as urllib2

while(True):
    try:        
        options = Options()
        options.add_argument('--headless')
            
        driver = webdriver.Firefox(options=options)
        driver.get("https://client.ebox.ca/?lng=fr_FR")

        driver.find_element_by_id("usrname").send_keys("ENTER_CLIENT_ID")
        driver.find_element_by_id("pwd").send_keys("ENTER_PASSWORD_HERE")

        driver.find_element_by_id("btnLogin").click()
        sleep(1)
        driver.get("https://client.ebox.ca/myusage")
        elem = driver.find_element_by_class_name("text_summary3")
        consommation_text = elem.text.replace('G','').replace('o','')
        used = consommation_text.split()[0]
        maximum = consommation_text.split()[2]
        percent = float(used)/float(maximum)
        print(used)
        print(maximum)
        print(percent*100)

        # Thingspeak
        myAPI = 'ENTER_THINGSPEAK_API_KEY' 
        baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI 
        conn = urllib2.urlopen(baseURL + '&field1=%s&field2=%s' % (used, percent*100))
        sleep(100)
    except:
        pass
