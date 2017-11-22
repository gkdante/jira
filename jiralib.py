import getpass
from jira import JIRA

def issuesWithComponent(jiraconnection,component,project):

	issuesfound = jiraconnection.search_issues('component = '+component+' AND project = '+project)
	print issuesfound

	return issuesfound


def replaceComponent(jiraconnection, issueId, old, new):

	issue = jiraconnection.issue(issueId)
	
	currentcomponents = []

	for component in issue.fields.components:
		if component.name == old:
			currentcomponents.append({'name' : new })
			#print('added')
		else:
			currentcomponents.append({'name' : component.name})
			#print('skipped')

	issue.update(fields={"components": currentcomponents})
			
	#print(issue.fields.components)
	return issue.fields.components


def connect():

#	user = 'fcampuzano'

	user = raw_input('Username: ')
	secret = getpass.getpass('Password: ')

	options = {'server': 'https://sharkbyte.atlassian.net'}

	jira = JIRA(options,basic_auth=(user, secret))
	
	return jira

def getProjects(jiraconnection, generateFile):


	projectslist = jiraconnection.projects()
	print(projectslist)

	if (generateFile == True):
		file = open('projectslist.csv',"w")
		file.write(str(projectslist))
		file.close()


	return projectslist

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
