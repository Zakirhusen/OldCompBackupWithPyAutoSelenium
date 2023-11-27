from selenium import webdriver
import os
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# C:\Users\Indian Driving Schoo\AppData\Local\Google\Chrome\User Data
print("before browser start")
os.system("taskkill /im chrome.exe /f")
options = webdriver.ChromeOptions()
# option to login whatsapp when open site
options.add_argument('user-data-dir=C:\\Users\\Indian Driving Schoo\\AppData\\Local\\Google\\Chrome\\User Data\\Default')
driver=webdriver.Chrome(executable_path="chromedriver.exe",chrome_options=options)
driver.get("https://web.whatsapp.com/")
driver.maximize_window()
driver.implicitly_wait(10) # seconds
print("first wait for 10 sec")
time.sleep(10)
while True:
    print("inside while")
    try:        
        time.sleep(20)
        # check for new message notification
        targetUserElem=driver.find_element(By.CSS_SELECTOR,'div[role="gridcell"]:has(span[title="ubi"])+div span[aria-label="Unread"]')
        noOfNewMsg=int(targetUserElem.text)
        print("nof messages",noOfNewMsg)
        if noOfNewMsg:
            print("inside if")

            # click on user to read messages
            time.sleep(3)
            driver.find_element(By.XPATH,"//*[@title='ubi']").click()

            # number of unread messages
            noOfUnreadMsg=int(((driver.find_element(By.XPATH,"//*[@aria-live='polite']").text).split())[0])

            time.sleep(5)
            # click to open menu to select option 'select messages'
            driver.find_element(By.XPATH,"//div[@id='main']//span[@data-icon='menu']").click()

            # click here "select messages " option
            driver.find_element(By.XPATH,"//*[@id='app']/div/span[4]/div/ul/div/div/li[3]/div").click()
            time.sleep(1)
    
            # main div frame that have all messages
            parentElem=driver.find_element(By.XPATH,"//div[@data-tab='8']")
    
            # all incoming messages
            allChilds=parentElem.find_elements(By.CSS_SELECTOR,"div[role='row']:has(div[tabindex='-1']):has(div.message-in)")

            # click and select all unread messages in frame
            for x in range(noOfUnreadMsg):
                print("value of x",x)
                msgIndexOfUnreadMsg=int(len(allChilds)-(x+1))
                allChilds[msgIndexOfUnreadMsg].find_element(By.CSS_SELECTOR,"input+div").click()           
                time.sleep(1)

            # driver.find_element(By.XPATH,"//*[@id='main']/div[2]/div/div[2]/div[3]/div[8]/div/div/span/div/div").click()
            time.sleep(1)

            # click on forward logo
            driver.find_element(By.XPATH,"//span[@data-icon='forward']").click()
            time.sleep(1)

            # find user to  select 
            driver.find_element(By.XPATH,"//*[@id='app']/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/div/div[1]/p").send_keys("Shafiulla")

            time.sleep(1)
            # click enter to select user
            driver.find_element(By.XPATH,"//*[@id='app']/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/div/div[1]/p").send_keys(Keys.ENTER)
            time.sleep(2)

            # Click to sending
            driver.find_element(By.XPATH,"//span[@data-icon='send']").click()
            
            time.sleep(1)
            # click to open menu to select option 'close chat'
            driver.find_element(By.XPATH,"//div[@id='main']//span[@data-icon='menu']").click()

            # click here to close chat
            driver.find_element(By.XPATH,"//*[@id='app']/div/span[4]/div/ul/div/div/li[3]/div").click()
            
        time.sleep(10)
    except:
        time.sleep(10)


# to make exe file
#   pyinstaller ./main.py --onefile --noconsole --add-binary "./driver/chromedriver.exe;./driver"
