from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from time import sleep
import sys
import urllib.request as urllib2

try:        
    options = Options()
    #options.add_argument('--headless')
        
    driver = webdriver.Firefox(options=options)
    driver.get("https://www.hydroquebec.com/portail/fr/group/clientele/gerer-mon-compte")
    sleep(5)
    driver.find_element_by_id("idToken1").send_keys("jeffrey.cousineau@gmail.com")
    driver.find_element_by_id("idToken2").send_keys("78523000Jc")
    driver.find_element_by_id("loginButton_0").click()
    driver.get("https://session.hydroquebec.com/portail/fr/group/clientele/gerer-mon-compte")

    sleep(15)
    
    #driver.get("https://client.ebox.ca/myusage")
    elem = driver.find_element_by_class_name("solde")
    #consommation_text = elem.text.replace('G','').replace('o','')
    #used = consommation_text.split()[0]
    #maximum = consommation_text.split()[2]
    #percent = float(used)/float(maximum)
    #print(used)
    #print(maximum)
    #print(percent*100)
    print(elem.text)

    # Thingspeak
    #myAPI = 'ENTER_THINGSPEAK_API_KEY' 
    #baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI 
    #conn = urllib2.urlopen(baseURL + '&field1=%s&field2=%s' % (used, percent*100))
    #sleep(100)
except Exception as e:
    print(e)
