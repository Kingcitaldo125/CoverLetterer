# AUTHOR: PAUL ARELT
# See the LICENSE file for information on applying the legalese

import random
import re

def readTemplate(tempNumber):
	templateText = ""
	templateSections = []
	
	if tempNumber == 1:
		with open("tOneSections.txt","r") as f:
			templateSections = [x.strip() for x in f.readlines()]
		with open("templateOne.txt","r") as f:
			templateText = f.read()
	else:
		with open("tTwoSections.txt","r") as f:
			templateSections = [x.strip() for x in f.readlines()]
		with open("templateTwo.txt","r") as f:
			templateText = f.read()
	
	return [templateText,templateSections]
	
def buildCLetter(section, sectionTxt, txt):
	regex = r'\[' + re.escape(str(section)) + r'\]'

	m = re.sub(regex, sectionTxt, txt)
	
	return m


def mymain(role, company, requirements, templateNumber, name):
	values = "works hard, pays close attention to detail and works well with others"
	career_profile = "I also have experience working with C++(Qt 5 and STL), Python, and Java programming languages"
	seller = "I am a hard worker with a passion for coding. I believe that I can be a strong asset to "+company+" because of my strong knowledge in the languages described"
	languages = "C++, Python, and Java"

	templateList = readTemplate(templateNumber)
	totalText = ""
	for data in templateList:
		txt = templateList[0]
		totalText = txt
		sections = templateList[1]
		for s in sections:
			if s == "[role]":
				totalText = buildCLetter("role", role, totalText)
			elif s == "[company]":
				totalText = buildCLetter("company", company, totalText)
			elif s == "[career_profile]":
				totalText = buildCLetter("career_profile", career_profile, totalText)
			elif s == "[requirements]":
				totalText = buildCLetter("requirements", requirements, totalText)
			elif s == "[languages]":
				totalText = buildCLetter("languages", languages, totalText)
			elif s == "[seller]":
				totalText = buildCLetter("seller", seller, totalText)
			elif s == "[values]":
				totalText = buildCLetter("values", values, totalText)
			elif s == "[name]":
				totalText = buildCLetter("name", name, totalText)

	with open("out.txt","w") as f:
		f.write(str(totalText))
		f.write("\n")

	return totalText

if __name__ == "__main__":
	name = str(input('Enter your name\n'))
	role = str(input('Enter the Role\n'))
	company = str(input('Enter the Company name\n'))
	requirements = str(input('Enter the job requirements as they appear\n'))

	templateNumber = random.randrange(1, 3)

	# For testing
	#templateNumber = 2

	print("Template Number:", templateNumber)
	print(mymain(role, company, requirements, templateNumber, name))
