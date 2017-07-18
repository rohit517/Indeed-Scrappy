from bs4 import BeautifulSoup # For HTML parsing
from urllib.request import urlopen # Website connections
from math import ceil
import re


def main():
    #final_site = "https://www.indeed.com/jobs?q=sensor+&l=United+States"
    final_site = input('Enter URL: ')
    print ("Starting Script...v0.4")
    html = urlopen(final_site).read()
    soup = BeautifulSoup(html,"html.parser")
    num_jobs_area = soup.find('div',attrs={'id': 'searchCount'})
    no_jobs = num_jobs_area.text.strip()
    no_of_pages = noOfPages(no_jobs)
    print ("Getting individual job postings..")
    getJobTitles(no_of_pages,final_site)

def clicknext(soup):
    print ("Next function")
    badges = soup.body.find('div', attrs={'class': 'pagination'})
    for span in badges.span.find_all('span', recursive=False):
        print (span.attrs['class'])

def noOfPages(no_job):
    no_pages = ceil(getTotalJobs(no_job)/10.00)
    print ("Total Number of Pages : " + str(no_pages))
    return no_pages
 
def getTotalJobs(no):
    wordList = re.sub("[^\w]", " ",  no).split()
    if(len(wordList)==7):
        number = wordList[5] + wordList[6]
    else:
        number = wordList[5]
    print (number)
    return float(number)

def getJobTitles(no_of_pages,final_site):
    for pages in range(no_of_pages):
        print ("\nPage:" + str(pages+1) + " Starting")
        print ("----------------------------\n")
        html = urlopen(final_site).read()
        soup = BeautifulSoup(html,'html.parser')
        indv_jobs = soup.findAll('h2',attrs={'class': 'jobtitle'})
        for jobs in indv_jobs:
            print (jobs.a['title'])

        if(pages != no_of_pages-1):
            final_site = getNextPageUrl(soup)
        
        print ("\nPage:" + str(pages+1) + " Over")
        print ("----------------------------\n")

def getNextPageUrl(soup):    
    page_span = soup.find("div", class_="pagination").find("span", class_="pn")
    next_link = page_span.find_parent("a")
    next_page = "https://www.indeed.com" + next_link.get('href')
    print("\nNext Page found......")
    return next_page
    
main()

    
