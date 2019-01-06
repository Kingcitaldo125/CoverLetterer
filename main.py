# AUTHOR: PAUL ARELT

import random


def main():
    values = ['']

    hiringManager = str(input('Enter the Manager name. Write \'-\' if no manager name specified\n'))
    if hiringManager == "-":
        hiringManager = "Hiring Manager"
    role = str(input('Enter the Role\n'))
    company = str(input('Enter the Company name\n'))
    requirements = str(input('Enter the job requirements as they appear\n'))

    x = random.randrange(0, 3)
    foo = open('out.txt', 'w')
    templateNumber = 0
    languages = "C, C++, Java, Javascript, Python, HTML and CSS"

    if x == 1:
        outt = ""
        lines = []
        nlines = []
        templateNumber = 1
        fileobj = open('templateOne.txt', 'r+')
        values = "works hard, pays close attention to detail and works well with others"
        proff = "I have experience working with C, C++, Java, Python, HTML, Javascript, CSS and Swift."
        for xx in fileobj:
            lines.append(xx.split(' '))
        #print(lines)

        for l in lines:
            for ll in l:
                if ll == '[company]':
                    ll = ll.replace('[company]', company)
                if ll == '[manager]:\n':
                    ll = ll.replace('[manager]:\n', hiringManager+':\n')
                if ll == '[role]':
                    ll = ll.replace('[role]', role)
                if ll == '[values]':
                    ll = ll.replace('[values]', values)
                if ll == '[career_profile]':
                    ll = ll.replace('[career_profile]', proff)
                    ll = ll[:-2]
                if ll == '[requirements]':
                    ll = ll.replace('[requirements]', requirements)
                nlines.append([ll])

        for l in nlines:
            for ll in l:
                #print(ll)
                outt += ll
                outt += ' '

        foo.write(outt)
        foo.write("\n")

        foo.close()

    else:
        outt = ""
        lines = []
        nlines = []
        templateNumber = 2
        fileobj = open('templateTwo.txt', 'r+')
        sellr = "I am a hard worker with a passion for coding. " \
                "I believe that I can be a strong asset to "+company+" because of my strong knowledge in the languages described."
        for xx in fileobj:
            lines.append(xx.split(' '))

        for l in lines:
            for ll in l:
                if ll == '[company]':
                    ll = ll.replace('[company]', company)
                if ll == '[manager]:\n':
                    ll = ll.replace('[manager]:\n', hiringManager+':\n')
                if ll == '[role]':
                    ll = ll.replace('[role]', role)
                if ll == '[languages]':
                    ll = ll.replace('[languages]', languages)
                if ll == '[seller]':
                    ll = ll.replace('[seller]', sellr)
                    ll = ll[:-1]
                nlines.append([ll])

        for l in nlines:
            for ll in l:
                #print(ll)
                outt += ll
                outt += ' '

        foo.write(outt)
        foo.write("\n")

        foo.close()


main()
