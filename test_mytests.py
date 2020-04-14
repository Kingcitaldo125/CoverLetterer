import main

def test_templateone():
	role = "Software Engineer"
	company = "Ball"
	requirements = "C,C++,Python"
	templateNumber = 1
	
	totalText = main.mymain(role, company, requirements, templateNumber)
	totalText = "".join(totalText.split("\n"))
	
	mytesttxt = "Dear Hiring Manager,\
\
I am writing in response to your recently advertised position for a Software Engineer.\
I am very interested in this opportunity with Ball and believe that my qualifications,\
education and professional experience would make me a strong candidate for the position.\
I am a software engineer who works hard, pays close attention to detail and works well with others.\
I have experience working with C++(Qt 5 and STL), Java, Python, HTML, Javascript, CSS.\
Enclosed is my resume that more fully details my background and work experience, and how they relate to your position.\
As you can see, I have worked with your C,C++,Python requirements in the past, and I enjoy working with those requirements.\
I firmly believe that I can be a valuable asset to your team.\
I welcome the opportunity to speak with you about this position and how my experience could help Ball achieve its goals.\
\
Thank you in advance for your consideration.\
\
Kind regards,\
\
Paul Arelt"

	assert totalText == mytesttxt


def test_templatetwo():
	role = "Software Engineer"
	company = "Ball"
	requirements = "C,C++,Python"
	templateNumber = 2
	
	totalText = main.mymain(role, company, requirements, templateNumber)
	totalText = "".join(totalText.split("\n"))
	
	mytesttxt = "Dear Hiring Manager,\
\
I am writing to express my interest in the recently advertised Software Engineer role.\
I believe I could bring valuable skills and experience to Ball that would make me an ideal fit for this position.\
I have 3 years of experience as a software engineer/developer, and in this time I have helped deploy applications in C++,\
 wrote a web applet in Javascript, helped improve a backend database system using PostgreSQL and C++, and much more.\
I believe that I am an ample fit for the Software Engineer position here at Ball, because I have closely worked with\
languages such as C++, Java, Javascript, Python, HTML and CSS in the past.\
I am a hard worker with a passion for coding. I believe that I can be a strong asset to Ball because of my strong knowledge in the languages described.\
Thank you for taking the time to consider my application, and I look forward to hearing from you.\
\
Yours sincerely,\
\
Paul Arelt"

	assert totalText == mytesttxt


def test_templatethree():
	role = "Software Engineer"
	company = "Ball"
	requirements = "C,C++,Python"
	templateNumber = 3
	
	totalText = main.mymain(role, company, requirements, templateNumber)
	totalText = "".join(totalText.split("\n"))
	
	mytesttxt = "Dear Hiring Manager,\
\
I am writing to express my interest in the recently advertised Software Engineer role.\
I believe I could bring valuable skills and experience to Ball that would make me an ideal fit for this position.\
I have 3 years of experience as a software engineer/developer, and in this time I have helped deploy applications in C++,\
 wrote a web applet in Javascript, helped improve a backend database system using PostgreSQL and C++, and much more.\
I believe that I am an ample fit for the Software Engineer position here at Ball, because I have closely worked with\
languages such as C++, Java, Javascript, Python, HTML and CSS in the past.\
I am a hard worker with a passion for coding. I believe that I can be a strong asset to Ball because of my strong knowledge in the languages described.\
Thank you for taking the time to consider my application, and I look forward to hearing from you.\
\
Yours sincerely,\
\
Paul Arelt"

	assert totalText == mytesttxt
