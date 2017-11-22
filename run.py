import re
import json
import requests
import jiralib 

myjira = jiralib.connect()

#To find issues that have a component
jiralib.issuesWithComponent(myjira,'BO','SBS')

#To replace a component on an issue
#jiralib.replaceComponent(myjira,'QB-1','BackOffice','BO')


#sbsprojects = jiralib.getProjects(myjira,True)

#sbscomponents= jiralib.getComponents(myjira,'QB', True)

#for i in sbscomponents:
#	print (i,sbscomponents[i])



