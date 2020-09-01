#import some module or packages first
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common import exceptions
from selenium.webdriver.common.keys import Keys
import csv


total_page=int(input("Type the number of page you want")) # like how much search-results page do you want (ex:1,2,3,4...n)
keywords=input('What do you want to search in Google?: ')

filename=input() #name the csv file


options = Options()
options.add_argument("--no-sandbox")
options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"# it locates chrome exe
driver=webdriver.Chrome(options=options,executable_path='C:\\Users\\<username_of_pc>\\Downloads\\chromedriver_win32\\chromedriver')#it locates chromedriver exe

driver.get("https://www.google.com/")
sleep(3)

search_query = driver.find_element_by_name('q') #search box finding
search_query.send_keys(keywords)
sleep(0.5)

search_query.send_keys(Keys.RETURN) # sending what do you want to search in search box of google
print("Wait for a while!!!")
sleep(3)

search_results=[] #this data structer will collect all the search result
result_link=[]
for i in range(total_page):
	next_button=driver.find_element_by_xpath('//*[@id="pnnext"]').click()
	search_results_mini = driver.find_elements_by_xpath('//*[@id="rso"]/div/div/div[1]/a') #finding the link of search result
	result_link_mini=[url.get_attribute('href') for url in search_results_mini] #getting the link
	result_link.extend(result_link_mini)
	search_results_mini = [url.text for url in search_results_mini]
	search_results.extend(search_results_mini)

	sleep(0.5)

driver.quit()


print("Writing all information.Don't close this file now!")



with open(filemname+".csv","w",encoding="utf-8",newline="") as f: #creating csv file
	writer=csv.DictWriter(f,["Page No","Name","URL"])
	writer.writeheader()
	a=1
	length=len(result_link)
  
	for i in range(1,length+1):
		link=result_link[i-1]
		li=search_results[i-1].split("\n")
		text=li[0]
		if i%10==0:
			a+=1
		writer.writerow({"Page No":a,"Name":text,"URL":link})
    
    
print("DONE!") # completed.
