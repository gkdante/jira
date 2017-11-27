import re
import json
import requests
import jiralib 

myjira = jiralib.connect()

#To find issues that have a component
#jiralib.issuesWithComponent(myjira,'BO','SBS')

#JQL get all issues (no limit of 50)

oldissue = 'Gates'
newissue = 'Gate'

allissues = jiralib.jqlAllIssues(myjira,str('project = SBS and component ='+oldissue))

for issue in allissues:
#	print('Issue: '+issue.key)
#	print('Old components: '+str(issue.fields.components))
#	print('New components: ')
	jiralib.replaceComponent(myjira,issue.key,oldissue,newissue,False)


#print (allissues)

#To replace a component on an issue
#jiralib.replaceComponent(myjira,'QB-1','BackOffice','BO')


#sbsprojects = jiralib.getProjects(myjira,True)

#sbscomponents= jiralib.getComponents(myjira,'QB', True)

#for i in sbscomponents:
#	print (i,sbscomponents[i])



