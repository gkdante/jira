import re
import json
import requests
import jiralib 

myjira = jiralib.connect()

#To find issues that have a component
#jiralib.issuesWithComponent(myjira,'BO','SBS')

#JQL get all issues (no limit of 50)

allissues = jiralib.jqlAllIssues(myjira,'project = SBS and component = BackOffice')
#print (allissues)

#To replace a component on an issue
#jiralib.replaceComponent(myjira,'QB-1','BackOffice','BO')


#sbsprojects = jiralib.getProjects(myjira,True)

#sbscomponents= jiralib.getComponents(myjira,'QB', True)

#for i in sbscomponents:
#	print (i,sbscomponents[i])



