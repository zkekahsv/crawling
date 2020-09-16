import urllib.request
import bs4


url = "https://www.naver.com/"
html = urllib.request.urlopen(url)

bsObj = bs4.BeautifulSoup(html, "html.parser")

# print(html.read())
# print(bsObj)

top_right = bsObj.find("div", {"class":"service_area"})

print(top_right)