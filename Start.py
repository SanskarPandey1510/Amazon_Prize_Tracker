# Importing Required modules
from bs4 import BeautifulSoup
import requests

link="https://appbrewery.github.io/instant_pot/"

# ?getting html response
response=requests.get(link)
response=response.text
soup=BeautifulSoup(response,"html.parser")
x=soup.select_one("span.a-price-whole").text
y=soup.select_one("span.a-price-fraction").text
v=0
i=0
while i<len(x) and x[i]!='.':
    v=v*10+int(x[i])
    i+=1
x=v
y=int(y)
z=x+y/100
print(z,type(z))

# User-Agent:
# Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:136.0) Gecko/20100101 Firefox/136.0
header={
 "User-Agent":
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:136.0) Gecko/20100101 Firefox/136.0",
"Accept-Language":
"en-US,en;q=0.5",
}