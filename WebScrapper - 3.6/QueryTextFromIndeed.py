from bs4 import BeautifulSoup # For HTML parsing
from urllib2 import urlopen # Website connections

#Start Scrapping maneouver

final_site = 'https://www.indeed.com/jobs?q=google&l=United+States&jt=internship'
print "Starting Script..."
html = urlopen(final_site).read()
print "Page Read..."
soup = BeautifulSoup(html,"lxml")
print "Page Retrieved..Going in to find the element.."
num_jobs_area = soup.find('div',attrs={'id': 'searchCount'})
no = num_jobs_area.text.strip()
print no

#get individual job postings
print "Getting individual job postings.."
indv_jobs = soup.findAll('h2',attrs={'class': 'jobtitle'})
for jobs in indv_jobs:
    print jobs.a['title']

int(no_of_pages)+1
