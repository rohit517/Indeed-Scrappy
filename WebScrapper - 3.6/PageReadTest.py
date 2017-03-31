from bs4 import BeautifulSoup # For HTML parsing
from urllib2 import urlopen # Website connections

final_site = 'https://www.indeed.com/jobs?q=google&l=United+States&jt=internship'
html = urlopen(final_site).read()
soup = BeautifulSoup(html,"lxml")
print soup.prettify()
