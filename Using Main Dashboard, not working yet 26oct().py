import requests
from bs4 import BeautifulSoup

Tutorial = "https://www.dataquest.io/blog/web-scraping-tutorial-python/"


page = requests.get("https://www.sunnyportal.com/Templates/PublicPage.aspx?page=1169a2ff-8f51-4ea9-ba72-316009593c62")
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())

print([type(item) for item in list(soup.children)])
html = list(soup.children)[8]
print(list(html.children))