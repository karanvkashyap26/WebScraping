# Importing Libraries
from urllib import request
import requests
from bs4 import BeautifulSoup as BS
import pandas as pd

#The url is saved in topic_url
topics_url = 'https://github.com/topics/'
response = request.urlopen(topics_url)
#the document is parsed in doc using beautifulsoup
doc = BS(response.read(), 'html.parser')

#the topic_title_tags willfind title_tags using find_All function and from the class
topic_title_tags = doc.find_all('p',{'class':'f3 lh-condensed mb-0 mt-1 Link--primary'})

#topic_title list is will save all the names of topic found from topic_title_Tags
topic_titles = []
for tag in topic_title_tags:
    topic_titles.append(tag.text)

print(topic_titles)

#The topic desc_tags will contain the description of the topic of the github
#topic_desc_Tags will find the desc using the find_all function and class path
topic_desc_tags = doc.find_all('p',{'class':'f5 color-text-secondary mb-0 mt-1'})

topic_desc = []
for tag in topic_desc_tags:
    topic_desc.append(tag.text.strip())

print(topic_desc[:5])

#This will get the /topics/cpp end of the url link, and will save it in the topic_link_tags
topic_link_tags = doc.find_all('a', {'class': 'd-flex no-underline'})
topics_urls = []
#base_url is will be added to the topic_urls end part to make a complete link which can be traversed on a web browser
base_url = 'https://github.com'

for tag in topic_link_tags:
    topics_urls.append(base_url + tag['href'])

print(topics_urls)

#The topic dictionary will be useful for saving the data in a key pair format in csv file
topics_dict = {
'title': topic_titles,
'description': topic_desc,
'url': topics_urls
}

# pandas data frame is used to organize the data in systematic and modern fashion as compare to normal python framework
topics_df = pd.DataFrame(topics_dict)

print(topics_df)

#Code to save the data in csv file
topics_df.to_csv(r'C:\Users\Karan\Desktop\Webscraping\topics.csv', index = False ,header= True)




