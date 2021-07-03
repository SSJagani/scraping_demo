# GoglePlay Store App Data Scraping using Selenium
# Write Excell file using xlwt

from selenium import webdriver
import time
import xlwt 
from xlwt import Workbook 

wb = Workbook() 
sheet1 = wb.add_sheet('Sheet 1')

chrome_path = "chromedriver.exe"

# ========== Using between comment commend for without open browser Scraping data START ==========
# options = webdriver.ChromeOptions()
# options.add_argument('--disable-gpu')
# options.add_argument('--headless')
# ========== Using between comment commend for without open browser Scraping data END ==========

driver = webdriver.Chrome(chrome_path)

# ---------- Write Header in Sheet START ----------
sheet1.write(0, 0, 'Application name') 
sheet1.write(0, 1, 'Devloper name') 
sheet1.write(0, 2, 'Rating')
# ---------- Write Header in Sheet END ----------

result = driver.get("https://play.google.com/store/apps/collection/cluster?clp=0g4jCiEKG3RvcHNlbGxpbmdfZnJlZV9BUFBMSUNBVElPThAHGAM%3D:S:ANO1ljKs-KA&gsr=CibSDiMKIQobdG9wc2VsbGluZ19mcmVlX0FQUExJQ0FUSU9OEAcYAw%3D%3D:S:ANO1ljL40zU&hl=enj")
for i in range(10):
    #scroll 300 px
    driver.execute_script('window.scrollTo(0,(window.pageYOffset+6000))')
    #waiting for the page to load
    time.sleep(3) 

    
for i in range(1,151):
	if i < 51:
		# Find text using find_element_by_xpath
		Application_Name=driver.find_element_by_xpath("//*[@id=\"fcxH9b\"]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/div["+str(i)+"]/c-wiz/div/div/div[2]/div/div/div[1]/div/div/div[1]/a/div").text
		Developer_Name=driver.find_element_by_xpath("//*[@id=\"fcxH9b\"]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/div["+str(i)+"]/c-wiz/div/div/div[2]/div/div/div[1]/div/div/div[2]/a/div").text
		Rating =driver.find_element_by_xpath("//*[@id=\"fcxH9b\"]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/div["+str(i)+"]/c-wiz/div/div/div[2]/div/div/div[2]/div/div/div/div")
		Rating_value= Rating.get_attribute("aria-label")
	else:
		Application_Name=driver.find_element_by_xpath("//*[@id=\"fcxH9b\"]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/c-wiz["+str(i)+"]/div/div/div[2]/div/div/div[1]/div/div/div[1]/a/div").text
		Developer_Name=driver.find_element_by_xpath("//*[@id=\"fcxH9b\"]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/c-wiz["+str(i)+"]/div/div/div[2]/div/div/div[1]/div/div/div[2]/a/div").text
		Rating =driver.find_element_by_xpath("//*[@id=\"fcxH9b\"]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/c-wiz["+str(i)+"]/div/div/div[2]/div/div/div[2]/div/div/div/div")
		Rating_value= Rating.get_attribute("aria-label")
	# ---------- Write Data in Sheet START ----------
	sheet1.write(i, 0, Application_Name) 
	sheet1.write(i, 1, Developer_Name) 
	sheet1.write(i, 2, Rating_value)
	# ---------- Write Data in Sheet END ----------

# ---------- Store Excel File in same Folder ----------
wb.save('data_selenium.xls')