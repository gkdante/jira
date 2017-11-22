from jira import JIRA
import re
import getpass
import json
import requests

user = raw_input('Username: ')
secret = getpass.getpass('Password: ')



def connect():

	options = {'server': 'https://sharkbyte.atlassian.net'}

	jira = JIRA(options,basic_auth=(user, secret))
	
	return jira


def getComponents(jiraconnection,targetProject, generateFile):


	#projects = jira.projects()
	#print(projects)
	
	myproject = jiraconnection.project(targetProject)
	print(('Project: {0}').format(myproject))
	print('Project lead: {0}'.format(myproject.lead.displayName))
	comps = jiraconnection.project_components(myproject)

	if (generateFile == True):
		file = open('components.csv',"w")
	
	mycomponents = {}

	for c in comps:

		componentid = c.id
		myurl = 'https://sharkbyte.atlassian.net/rest/api/2/component/'+componentid+'/relatedIssueCounts'
		r=requests.get(myurl, auth=(user, secret ))
		s = json.loads(r.content)
		count=s['issueCount']
		
		mycomponents[c.name] = count
 
		#print(c.name," ",c.id," ",count)
		
		if (generateFile == True):
			file.write(c.name+','+str(count)+'\n')

	if (generateFile == True):	
		file.close()

	return(mycomponents)




myjira = connect()

sbscomponents= getComponents(myjira,'SWEET', False)

for i in sbscomponents:
	print (i,sbscomponents[i])



