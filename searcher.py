import BeautifulSoup
import urllib2

URL_Choice=raw_input("Enter 1 for http://reddit.com/r/programming\nEnter 2 for https://news.ycombinator.com/\n")
if( URL_Choice == "1"):
	req = urllib2.Request('http://reddit.com/r/programming')
elif( URL_Choice == "2" ):
	req = urllib2.Request('https://news.ycombinator.com/')
else:
	print "Invalid choice"
page = urllib2.urlopen(req)
pager = page.read()
soup = BeautifulSoup.BeautifulSoup(pager)
if( URL_Choice == "1"):
	links = soup.findAll('a',{'class':'title may-blank '}, href = True)
elif( URL_Choice == "2" ):
	links = BeautifulSoup(str(soup.findAll('td',{'class':'title'}))).findAll('a', href = True)
term = raw_input(" Enter the search term\n")
for link in links:
    words = link.text.split()
    for item in words:
        if term == item:
            url = link['href']
            page_new = urllib2.urlopen(url)
            pager_new = page_new.read()
            soup_new = BeautifulSoup.BeautifulSoup(pager_new)
            print soup_new.html.head.title.text
            break
