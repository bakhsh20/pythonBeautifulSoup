#import beautifulsoup and request here
import requests
from bs4 import BeautifulSoup

#function to get job list from url 'https://www.monster.com/jobs/search?q={role}&where={location}'
def getJobList(role,location):
    # TODO: Change back to user input link
    url = 'https://www.talent.com/jobs?k=Software+Engineer&l=Raleigh%2C+NC&radius=40'
    # Complete the missing part of this function here

    # Params for user input
    params = {
        'q' : role,
        'where': location
    }

    response = requests.request("GET", url, params=params)
    
    doc = BeautifulSoup(response.text, 'lxml')

    jobTitle = doc.find_all('a', {'class' : 'card__job-link gojob'})
    city = doc.find('div', class_ = 'card__job-location').text
    # description = doc.find_all('p', class_ = 'card__job-snippet').text
    
    print(doc.prettify())
    print(response.status_code)
    for jobs in jobTitle:
      print(jobs.text)
    # print(city)
    # print(description)

#save data in JSON file
def saveDataInJSON(jobDetails):
    #Complete the missing part of this function here
    print("Saving data to JSON")

#main function
def main():
    # Write a code here to get job location and role from user e.g. role = input())
    role = input("Enter role you want to search\n")
    location = input("Enter location you want to search\n")
    print("The role you searched is " + "'" + role + "'" + " and the location you searched is " + "'" + location + "'.")

    getJobList(role,location)

if __name__ == '__main__':
    main()