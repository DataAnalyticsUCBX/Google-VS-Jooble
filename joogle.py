import http.client
import json
import requests
import pandas as pd

key = "5e885af9-75bb-4d99-b61b-29451e56addb"
# host = 'us.jooble.org'
host = f"https://us.jooble.org/api/{key}"
headers = {"Content-type": "application/x-www-form-urlencoded"}
request = '{ "keywords": "python", "location": "Dallas", "page": "2"}'
resultsPerPage = 20
response = requests.post(host,headers=headers,data=request)
# print(f"Link: {response.url}")
response = response.json()
# print(response)
totalcount = response["totalCount"]
totalPages = totalcount/resultsPerPage

title = []
location = []
snippet = []
salary = []
source = []
jobtype = []
link = []
company = []
updated = []
jobid = []

print(round(totalPages,0))

def toappend(tit,loc,sni,sal,sou,jobt,lin,com,upd,jobi):
    title.append(tit)
    location.append(loc)
    snippet.append(sni)
    salary.append(sal)
    source.append(sou)
    jobtype.append(jobt)
    link.append(lin)
    company.append(com)
    updated.append(upd)
    jobid.append(jobi)



def jobparser(data):
    # print(data)
    def tryandcatch(item):
        try:
            output = data[item]
            print(output)
            return output
        except:
            output = "Missing"
            print(output)
            return output
    title = tryandcatch("title")
    location = tryandcatch("location")
    snippet = tryandcatch("snippet")
    salary = tryandcatch("salary")
    source = tryandcatch("source")
    jobtype = tryandcatch("type")
    link = tryandcatch("link")
    company = tryandcatch("company")
    updated = tryandcatch("updated")
    jobid = tryandcatch("id")
    datatoappend = [title,location,snippet,salary,source,jobtype,link,company,updated,jobid]
    toappend(*datatoappend)

    
    # print(f"Found title: {title}")

print(f"Total Counts found: {totalcount}")
jobs = response["jobs"]
# print(jobs)
for job in jobs:
        jobparser(job)
        

frame = [title,location,snippet,salary,source,jobtype,link,company,updated,jobid]
frameofdata = pd.DataFrame(frame)
print(frameofdata)


 
        # print()

    # print(f"Job: {title}, Located at {location} with the company {company}")








# connection = http.client.HTTPConnection(host)
# #request headers
#json query
# connection.request('POST','/api/' + key, body, headers)
# response = connection.getresponse()
# print(response.geturl.read())
# print(response.status, response.reason)
# print(response.read())
# reponse = 
# jobs = response["jobs"][0]["title"]
# print(type(response))
# print(jobs)
