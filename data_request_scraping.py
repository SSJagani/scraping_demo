# GoglePlay Store App Data Scraping using requests and BeautifulSoup
# Write Excell file using xlwt

import requests,os
from bs4 import BeautifulSoup
import xlwt 
from xlwt import Workbook 

wb = Workbook() 
sheet1 = wb.add_sheet('Sheet 1')


url = 'https://play.google.com/store/apps/collection/cluster?clp=0g4jCiEKG3RvcHNlbGxpbmdfZnJlZV9BUFBMSUNBVElPThAHGAM%3D:S:ANO1ljKs-KA&gsr=CibSDiMKIQobdG9wc2VsbGluZ19mcmVlX0FQUExJQ0FUSU9OEAcYAw%3D%3D:S:ANO1ljL40zU&hl=enj'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

# ---------- Write Header in Sheet START ----------
sheet1.write(0, 0, 'Application name') 
sheet1.write(0, 1, 'Devloper name') 
sheet1.write(0, 2, 'Rating') 
# ---------- Write Header in Sheet END ----------
n=1
for wrapper,com,rate in zip(soup.find_all('div', {"class":"WsMG1c nnK0zc"}),soup.find_all('div', {"class":"KoLSrc"}),soup.find_all('div', {"class":"pf5lIe"})):
	app_name=wrapper.text
	Devloper_name=com.text
	for rat in rate:
		 rating = rat.attrs["aria-label"]

	# ---------- Write Data in Sheet START ----------
	sheet1.write(n, 0, app_name) 
	sheet1.write(n, 1, Devloper_name) 
	sheet1.write(n, 2, rating) 
	# ---------- Write Data in Sheet END ----------
	n=n+1


# ---------- Store Excel File in same Folder ----------
wb.save('data_request.xls') 