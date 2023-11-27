from selenium import webdriver
import os
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://kannadasiri.karnataka.gov.in/kkg/public/")
driver.maximize_window()
# Get the list of all files and directories


path = "./syedrafeeq/dundasiCsv"
dir_list = os.listdir(path)
# filename [10].split(")")[1].split(".")[0]

print("Files and directories in '", path, "' :")
gmailNo=110
count=0
for item in dir_list:
    gmailNo+=1 
    count+=1
    print(count)
    gmail=f'brcshiggaon{gmailNo}@gmail.com'
    instName=f'{item.split(")")[1].split(".")[0]}'
    participanNo=int(f'{item.split(")")[0].split("(")[1]}')
    mobileNo=9480695259
    fileUploadPath=f"D:\Zakir\Web development\\automation\syedrafeeq\\dundasiCsv\{item}"

    # print(gmailNo,instName,participanNo) 
    # institute name

    driver.implicitly_wait(10) # seconds
    driver.find_element(By.CSS_SELECTOR,"#content > div.ppage > div:nth-child(2) > div.twoforms > div:nth-child(2) #name").send_keys(instName)

    # district name
    select = Select(driver.find_element(By.ID, 'dist2'))
    select.select_by_index(14)

    
    # gmail
    driver.find_element(By.CSS_SELECTOR,"#content > div.ppage > div:nth-child(2) > div.twoforms > div:nth-child(2) #email").send_keys(gmail)

    # participants
    driver.find_element(By.ID,"memcount").send_keys(participanNo)
    
    # mobileno
    driver.find_element(By.CSS_SELECTOR,"#content > div.ppage > div:nth-child(2) > div.twoforms > div:nth-child(2) #mobile").send_keys(mobileNo)

    # fileupload
    driver.find_element(By.NAME,"product_file").send_keys(fileUploadPath) 

    driver.implicitly_wait(10) # seconds
    driver.find_element(By.NAME,"upload").click()
    
    

# D:\Zakir\Web development\automation\syedrafeeq\bendigeriCsv"D:\Zakir\Web development\automation\syedrafeeq\bendigeriCsv"