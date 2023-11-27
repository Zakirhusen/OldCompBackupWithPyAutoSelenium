from selenium import webdriver
import os
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# C:\Users\Indian Driving Schoo\AppData\Local\Google\Chrome\User Data
options = webdriver.ChromeOptions()
options.add_argument('user-data-dir=C:\\Users\\Indian Driving Schoo\\AppData\\Local\\Google\\Chrome\\User Data\\Default')
driver=webdriver.Chrome(executable_path="chromedriver.exe",chrome_options=options)
driver.get("https://web.whatsapp.com/")
driver.maximize_window()
driver.implicitly_wait(10) # seconds
print("first wait for 10 sec")
# time.sleep(70)
print("second wait for 60 sec")
# wait = WebDriverWait(driver, 60)
# wait.until(EC.visibility_of_element_located(targetElem))
# while True:
#     print("inside while")
#     try:        
        # time.sleep(20)
        # check for new message notification
# targetElem=driver.find_element(By.CSS_SELECTOR,'div[role="gridcell"]:has(span[title="ubi"])+div span[aria-label="Unread"]')
# noOfNewMsg=int(targetElem.text)
# if noOfNewMsg:
# print("inside if")

# click on user to read messages
time.sleep(13)
driver.find_element(By.XPATH,"//*[@title='ubi']").click()

# number of unread messages
# noOfUnreadMsg=int(((driver.find_element(By.XPATH,"//*[@aria-live='polite']").text).split())[0])

# time.sleep(10)
# driver.find_element(By.XPATH,"//div[@id='main']//span[@data-icon='menu']").click()
# driver.find_element(By.XPATH,"//*[@id='app']/div/span[4]/div/ul/div/div/li[3]/div").click()
# time.sleep(2)
# driver.find_element(By.XPATH,"//*[@id='main']/div[2]/div/div[2]/div[3]/div[8]/div/div/span/div/div").click()
# time.sleep(2)
# click for forward
# driver.find_element(By.XPATH,"//span[@data-icon='forward']").click()
# time.sleep(2)
# find and select user to send
# driver.find_element(By.XPATH,"//*[@id='app']/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/div/div[1]/p").send_keys("Shafiulla",Keys.ENTER)
# Clicking sending
# driver.find_element(By.XPATH,"//span[@data-icon='send']").click()
# all messages in frame
parentElem=driver.find_element(By.XPATH,"//div[@data-tab='8']")
print("parent ",parentElem)
# print("parent type",type(parentElem))
# print("parent number",len(parentElem))
# allChilds=parentElem.find_elements(By.XPATH,"//div[@role='row']")

#click here opn menu 
driver.find_element(By.XPATH,"//div[@id='main']//span[@data-icon='menu']").click()
# click here to select messages
driver.find_element(By.XPATH,"//*[@id='app']/div/span[4]/div/ul/div/div/li[3]/div").click()
time.sleep(2)
# all incoming messages
allChilds=parentElem.find_elements(By.CSS_SELECTOR,"div[role='row']:has(div[tabindex='-1']):has(div.message-in)")
# div#app div[data-tab="8"] div[role="row"]:has(div[tabindex="-1"]):has(div.message-in) input

print("childs",(allChilds))
print("childs number",len(allChilds))
# click here to select checkbox
allChilds[-1].find_element(By.CSS_SELECTOR,"input+div").click()
            # print("no of divs in frame",allChilds.size())
            # for item in range(noOfUnreadMsg):
                
            
# print("nof messages",noOfNewMsg)
# time.sleep(10)
    # except:
        # time.sleep(10)
  
# .click()
# driver.find_element(By.ID,'loginForm')
# //*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p
# div[role="gridcell"]:has(span[title="Shakir Veerapur"])+div
# div[role="gridcell"]:has(span[title="+91 98443 03335"])+div span[aria-label="Unread"]
# slect messages div[aria-label="Select messages"]


#  //*[@id="main"]/div[2]/div/div[2]/div[3]/div[19]
#  //*[@id="main"]/div[2]/div/div[2]/div[3]/div[16]
#//*[@id="main"]/div[2]/div/div[2]/div[3]/div[10]/div/div/span/div/div
#//*[@id="main"]/div[2]/div/div[2]/div[3]/div[19]/div/div/span/div/div