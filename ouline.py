#import beautifulsoup and request here
import requests

url = "https://www.indeed.com/jobs?q=Software Developer&l=Charlotte"

payload={}
headers = {
  'Cookie': 'CTK=1g95jo3ttghpg800; __cf_bm=jj8rAx0vP1FapIQGa4zXdd8t9AiNW3_tbGUXONiyhZE-1659119603-0-AY9Fnr+c+0IZPCv1UPE91Yyy2FBhX0ZHUP2J7D39NgyVZpLF2xclijQMBBVzPWOmGRWVgcyyzdmZ7YhH51XiirM=; _cfuvid=Hclq0XDBWx6T9IdLK3qK8tCpJLiP5G6DWqPr3Irw00g-1659119603850-0-604800000; INDEED_CSRF_TOKEN=Y5wcaiTFatj3VWlGQMsAvWFshL2zhL69; JSESSIONID=FD42A4B2BF8169AF5EF182C3FCDA2F42; PREF="TM=1659119603654:L=Charlotte"; RQ="q=Software+Developer&l=Charlotte&ts=1659119603681"; UD="LA=1659119603:CV=1659119603:TS=1659119603:SG=3a462e59ad44d1c33c6a4faeb9544bf8"; ctkgen=1; indeed_rcc=""; jaSerpCount=1'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

def displayJobDetails():
    print("Display job details")

#function to get job list from url 'https://www.indeed.com/jobs?q={role}&l={location}'
def getJobList(role,location):
    url = 'https://www.indeed.com/jobs?q={role}&l={location}'
    # Complete the missing part of this function here 

#save data in JSON file
def saveDataInJSON(jobDetails):
    #Complete the missing part of this function here
    print("Saving data to JSON")

#main function
def main():
    # Write a code here to get job location and role from user e.g. role = input()
    print("Enter role you want to search")
    role = input()
    location = input("Enter location you want to search\n")
    # Complete the missing part of this function here
    print("My role is: " + "'" + role + "'" + ' ' + "my location is " + "'" + location + "'")
    
if __name__ == '__main__':
    main()
