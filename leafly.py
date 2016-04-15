from bs4 import BeautifulSoup
import requests
import random

# Open and read the template file
fo = open("template_scrape.html", "r")
html_template = fo.read();
fo.close()

# get the webpage
r=requests.get("http://www.collective-evolution.com/2012/12/05/how-hemp-became-illegal-the-marijuana-link/")

# get the HTML source from that page
html_doc = r.text

# turn the source into a bs4 "soup" object
soup = BeautifulSoup(html_doc,"html.parser")

history_section = soup.find("div", class_="post-single-body clearfix margin-t20")
history_paragraph = history_section.find_all("p")

history_words1 = history_paragraph[11].get_text()
history_words2 = history_paragraph[12].get_text()
history_words3 = history_paragraph[13].get_text()

history_output1 = BeautifulSoup(history_words1).prettify (formatter='html')
history_output2 = BeautifulSoup(history_words2).prettify (formatter='html')
history_output3 = BeautifulSoup(history_words3).prettify (formatter='html')

print(history_output1, history_output2, history_output3)

	
# history_output = BeautifulSoup(history_words).prettify (formatter='html')

r=requests.get("https://www.leafly.com/news/headlines/hemp-vs-cotton-3-reasons-why-cotton-is-not-king")

# get the HTML source from that page
html_doc = r.text

# turn the source into a bs4 "soup" object
soup = BeautifulSoup(html_doc,"html.parser")

# narrow down to the div on the page that contains our content
leafly_section = soup.find("div", class_="news__article-body")
leafly_paragraph = leafly_section.find_all("p")

leafly_words1 = leafly_paragraph[5].get_text()
leafly_words2 = leafly_paragraph[10].get_text()
leafly_words3 = leafly_paragraph[11].get_text()

leafly_output1 = BeautifulSoup(leafly_words1).prettify (formatter='html')
leafly_output2 = BeautifulSoup(leafly_words2).prettify (formatter='html')
leafly_output3 = BeautifulSoup(leafly_words3).prettify (formatter='html')

r=requests.get("https://www.leafly.com/news/cannabis-101/whats-the-deal-with-these-high-cbd-strains")

# get the HTML source from that page
html_doc = r.text

# turn the source into a bs4 "soup" object
soup = BeautifulSoup(html_doc,"html.parser")

# narrow down to the div on the page that contains our content
cbd_section = soup.find("div", class_="news__article-body")
cbd_paragraph = cbd_section.find_all("p")

cbd_words1 = cbd_paragraph[2].get_text()
cbd_words2 = cbd_paragraph[4].get_text()
cbd_words3 = cbd_paragraph[5].get_text()

cbd_output1 = BeautifulSoup(cbd_words1).prettify (formatter='html')
cbd_output2 = BeautifulSoup(cbd_words2).prettify (formatter='html')
cbd_output3 = BeautifulSoup(cbd_words3).prettify (formatter='html')


# create the complete HTML page to display in a certain order.
html_file = html_template.format(history_output1, history_output2, history_output3, leafly_output1, leafly_output2, leafly_output3, cbd_output1, cbd_output2, cbd_output3)

# write out the html file
fo = open("sentence_scrape.html", "w")
fo.write( html_file );
fo.close()