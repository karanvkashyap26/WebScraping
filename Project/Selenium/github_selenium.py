from selenium import webdriver
import time
import pandas as pd

link_data = []
title = []
description = []

chromedriver_path = r"C:\Users\Karan\Desktop\Selenium\chromedriver_win32\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option("useAutomationExtension", False)
driver = webdriver.Chrome(options = options, executable_path = chromedriver_path)
driver.get("https://github.com/topics/")



while True:
    try:
        load_more = driver.find_element_by_xpath("//button[@type = 'submit']").click()
        time.sleep(2)
    except Exception as e:
        print(e)
        break
time.sleep(2)



data_2 = driver.find_elements_by_xpath("//div[@class = 'py-4 border-bottom']")
for crawl_data in data_2:
    
    link_enter = crawl_data.find_element_by_xpath(".//div[@class = 'd-sm-flex flex-auto']")
    link = link_enter.find_element_by_xpath(".//a[@class = 'd-flex no-underline']").get_attribute("href")
    link_data.append(link)
    
    title_data = crawl_data.find_element_by_xpath(".//p[@class = 'f3 lh-condensed mb-0 mt-1 Link--primary']").text
    title.append(title_data)
    
    des_data = crawl_data.find_element_by_xpath(".//p[@class = 'f5 color-text-secondary mb-0 mt-1']").text
    description.append(des_data)
    
df = {"Links":link_data, "Title": title, "Description":description}
df1 = pd.DataFrame.from_dict(df, orient='index').transpose()
df1.to_csv(r"C:\Users\Karan\Desktop\Webscraping\github_data.csv", index = False)

start = time.time()
print("Running time: ",time.time() - start)


