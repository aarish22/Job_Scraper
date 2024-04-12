import requests
from bs4 import BeautifulSoup
import time

skills = input("Enter the skills you are failiar to(in comma seprated way): ")
skills = skills.split(",")

def job_posts():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=India').text
    #print(html_text)

    soup = BeautifulSoup(html_text , 'lxml')

    jobs = soup.find_all("li" , class_ = "clearfix job-bx wht-shd-bx")
    for job in jobs:
        date_posted = job .find("span" , class_ = "sim-posted").text
        skills_needed = job.find("span" , class_ = "srp-skills").text.replace(' ','').strip().split(",")
        if 'few' in date_posted and set(skills) & set(skills_needed):
            company_name = job.find("h3" , class_ = "joblist-comp-name").text.lstrip()
            job_link = job.header.h2.a['href']
            print(
            f''' 
Company Name : {company_name}
Skills Needed : {skills_needed}
Job_Link : {job_link}
            ''')       
        
if __name__ == "__main__":
        while True:
            job_posts()
            print("Please Wait")
            time.sleep(2)  ## will get a new result at every 2 second interval

        
    