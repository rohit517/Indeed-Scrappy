from bs4 import BeautifulSoup # For HTML parsing
from urllib.request import urlopen # Website connections
from math import ceil
import re


def main():
    final_site = "https://www.indeed.com/jobs?q=machine+learning&l=United+States"
    print ("Starting Script...v0.2")
    html = urlopen(final_site).read()
    soup = BeautifulSoup(html,"html.parser")
    #print (soup.prettify())
    num_jobs_area = soup.find('div',attrs={'id': 'searchCount'})
    no_jobs = num_jobs_area.text.strip()
    no_of_pages = noOfPages(no_jobs)
    print ("Getting individual job postings..")
    getJobTitles(no_of_pages,final_site)

def noOfPages(no_job):
    no_pages = ceil(getTotalJobs(no_job)/10.00)
    print (no_pages)
    return no_pages
 
def getTotalJobs(no):
    wordList = re.sub("[^\w]", " ",  no).split()
    print ("Total Jobs:" + wordList[5])
    return float(wordList[5])

def getJobTitles(no_of_pages,final_site):
    for pages in range(1,2):
        print ("")
        print ("Page:" + str(pages) + " Starting")
        print ("")
        html = urlopen(final_site).read()
        soup = BeautifulSoup(html,'html.parser')
        indv_jobs = soup.findAll('h2',attrs={'class': 'jobtitle'})
        for jobs in indv_jobs:
            print (jobs.a['title'])

        #getNextPageUrl(pages,soup)    
        print ("")
        print ("Page:" + str(pages) + " Over")
        print ("")

def getNextPageUrl(pages,soup):    
    pageDiv = soup.findAll('div', attrs={"class" : "pagination"})
    #for div in pageDiv:
     #   print div.a['href']
   # print (soup.prettify())
    
main()

    
