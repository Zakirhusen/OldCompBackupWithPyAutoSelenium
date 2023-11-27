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
select = Select(driver.find_element(By.NAME, 'allchilds_length'))
select.select_by_value("-1")

# click on cluster
cluster =driver.find_element(By.XPATH,"//*[@id='allchilds']/tbody/tr[2]/td[1]")
clusterName=cluster.text
f = open(f'{clusterName}.txt', 'w+')
cluster.click()

for i in range(17):
    print(i)
    if i>9:
        select = Select(driver.find_element(By.NAME, 'allchilds_length'))
        select.select_by_value("-1")

    # click on school 
    if(i!=6):
        text=driver.find_element(By.CSS_SELECTOR,f"#allchilds > tbody > tr:nth-child({i+1}) > td.sorting_1").text
        f.write(f'"{text}",')
    
