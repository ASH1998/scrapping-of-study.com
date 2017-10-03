'''
# !! downloading images------------------------------
import urllib.request
import os
name = 'gp'
link = "/cimages/course-image/life-span-developmental-psychology_118941_small.jpg"
resource = urllib.request.urlopen("https://study.com" + link)
os.mkdir('images')
output = open("images//"+name +".jpg","wb")
output.write(resource.read())
output.close()
'''
'''
#!! downloading course names-------------------------
import bs4
import urllib.request
src = urllib.request.urlopen('http://study.com/academy/course/index.html').read()
soup = bs4.BeautifulSoup(src, 'lxml')
names  = []
for divs in soup.find_all(attrs={'class': 'titleTwo'}):
    names.append(divs.text)

print(len(names))

'''
"""
# !!! downloading summaries
src = urllib.request.urlopen('http://study.com/academy/course/high-school-biology-homework-help.html').read()
soup = bs4.BeautifulSoup(src,'lxml')

text = '''<div class="courseSummary" data-cname="course_summary" data-tabinsert="COURSE SUMMARY" test-id="course_summary">'''
soup_text = str(soup)
splitted_text = soup_text.split(text)
splitted_text = splitted_text[1]
print(splitted_text.split('</h3>')[1].replace('\n', '').split('.  ')[0])
"""
'''
# !!! downloading course lesson numbers
import urllib.request
import bs4
src = urllib.request.urlopen('http://study.com/academy/course/principles-of-management-course.html').read()
soup = bs4.BeautifulSoup(src,'lxml')
plain_text = soup.text
no_of_lessons = plain_text.split("Available Lessons: ")[1][:4]
print(no_of_lessons)
'''
'''
# !!! downloading course number of views
import urllib.request
import bs4
import re
src = urllib.request.urlopen('http://study.com/academy/course/introduction-to-biology.html').read()
soup = bs4.BeautifulSoup(src,'lxml')
b = []
plain_text = soup.text
a = re.findall(r'\d+(?:[\d,.]*\d)', plain_text)
for i in range(len(a)-1):
    if ',' in a[i]:
        a[i] = a[i][:].replace(',', '')
        if int(a[i])>20000:
            if not int(a[i]) == 55000:
                b.append(a[i])
print(b)

'''
# finding course type and avg lesson length and credit
import urllib.request
import bs4
src = urllib.request.urlopen('http://study.com/academy/course/ged-science-tutoring-solution.html').read()
soup = bs4.BeautifulSoup(src,'lxml')
plain_text = soup.text
#course = plain_text.split("Course type:\n            \n                \n                ")[1][:11]
#print(course)
#lesson_length = plain_text.split("Average Lesson Length:\n            \n                ")[1][:7]
credit = plain_text.split("Eligible for Credit: ")[1][:4]
print(credit)