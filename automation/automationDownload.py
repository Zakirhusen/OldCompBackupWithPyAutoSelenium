from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome(executable_path="chromedriver.exe")
driver.maximize_window()
driver.get("https://sts.karnataka.gov.in/SATS/main.htm?actionCode=showLoginPage#")
driver.find_element(By.ID,"userName").send_keys("SHIGGAONBRC")
driver.find_element(By.ID,"xxZTT9p2wQ").send_keys("Moon@123")
captcha=driver.find_element(By.ID,"randomfield").text

# to get captcha value
print(captcha)
driver.find_element(By.ID,"txtcode").send_keys(captcha)

# click on login button
driver.find_element(By.ID,"xmlLogin").click()

# click on dashboard
driver.find_element(By.XPATH,"//*[@id='cssmenu']/li[1]/a").click()

# click to show all clusters
select = Select(driver.find_element(By.NAME,'allchilds_length'))
select.select_by_value("-1")

# click on cluster
driver.find_element(By.XPATH,"//*[@id='allchilds']/tbody/tr[2]/td[1]").click()

for i in range(17):
    print(i)
    if i>9:
        select = Select(driver.find_element(By.NAME, 'allchilds_length'))
        select.select_by_value("-1")

    # click on school 
    driver.find_element(By.CSS_SELECTOR,f"#allchilds > tbody > tr:nth-child({i+1}) > td.sorting_1").click()
    
    # click to open download page
    driver.find_element(By.CSS_SELECTOR,'#searchschool > tbody > tr:last-child > td:nth-child(4) > a').click()
    handles=driver.window_handles
    driver.switch_to.window(driver.window_handles[1])
    if(i==6):
        driver.close()
    else:
        driver.find_element(By.XPATH,"//*[@id='maincontent']/table[2]/tbody/tr/td/a[2]/b").click()
        driver.close()
    driver.switch_to.window(driver.window_handles[0])
    driver.find_element(By.XPATH,"//*[@id='frmSearchStudent']/table[1]/tbody/tr/td/table/tbody/tr/td[1]/a").click()
    

