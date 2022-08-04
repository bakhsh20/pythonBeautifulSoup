#import beautifulsoup and request here
from pyparsing import str_type
import requests
from bs4 import BeautifulSoup
import json

#function to get job list from url 'https://www.monster.com/jobs/search?q={role}&where={location}'
def getJobList(role,location):
    # Params for user input
    params = {
        'k' : role,
        'l': location
    }

    url = 'https://www.talent.com/jobs?'

    # Get request from url using params
    response = requests.request("GET", url, params=params)
    
    # Create BeautifulSoup object, pass request object
    doc = BeautifulSoup(response.text, 'lxml')

    # Response, get a response from specified url
    # Doc object from beautiful soup that parses html 
    response = requests.request("GET", url, params=params)
    doc = BeautifulSoup(response.text, 'html.parser')
    
    # Get all jobTitles, locations, descriptions
    jobTitle = doc.find_all('a', {'class' : 'card__job-link gojob'})
    location = doc.find_all('div', {'class' : 'card__job-location'})
    description = doc.find_all('p', {'class' : 'card__job-snippet'})
    companyName = doc.find_all('div', {'class' : 'card__job-empname-label'})

    # Empty list for jobs 
    jobList = []

    # For loop using all job details
    for j, l, d, c in zip(jobTitle, location, description, companyName):
        jobDetails = {'Title' : j.text, 'Company' : c.text, 'Description' : d.text, 'Location' : l.text}
        jobList.append(jobDetails)

    # Return list
    return jobList
    


#save data in JSON file
def saveDataInJSON(jobDetails):
    #Complete the missing part of this function here
    print("Saving data to JSON")
    
    # Writing to json file
    jobDetails_json = open('jobDetails.json', 'w')
    json.dump(jobDetails, jobDetails_json)
    

#main function
def main():
    # Get user input. Make function calls. 
    role = input("Enter role you want to search\n")
    location = input("Enter location you want to search\n")
    print("The role you searched is " + "'" + role + "'" + " and the location you searched is " + "'" + location + "'.")
    print("=============================================================================================================")
    jobDetails = getJobList(role,location)
    for j in jobDetails:
        print(j)
        print("==============================")
    print("*\n")
    print("*\n")
    print("*\n")
    print("*\n")
    saveDataInJSON(jobDetails)

if __name__ == '__main__':
    main()