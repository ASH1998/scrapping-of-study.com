from down_contents import *
import bs4
import urllib.request
import time
import re

summary = []
course_type = []
credits = []
no_of_lessons = []
total_views = []
avg_lesson_length = []

print("Starting summary collection...")
start = time.time()
j = 1
for i in range(len(linkss)):
    src = urllib.request.urlopen(linkss[i]).read()
    soup = bs4.BeautifulSoup(src,'lxml')
    text = '''<div class="courseSummary" data-cname="course_summary" data-tabinsert="COURSE SUMMARY" test-id="course_summary">'''
    soup_text = str(soup)
    souped_text = soup.text
    splitted_text = soup_text.split(text)
    splitted_text = splitted_text[1]
    summary.append(splitted_text.split('</h3>')[1].replace('\n', '').split('.  ')[0])
    
    lessons = souped_text.split("Available Lessons: ")[1][:4]
    no_of_lessons.append(lessons)

    a = re.findall(r'\d+(?:[\d,.]*\d)', souped_text)
    for i in range(len(a)):
        if ',' in a[i]:
            a[i] = a[i][:].replace(',', '')
            if int(a[i])>20000:
                if not int(a[i]) == 55000:
                    total_views.append(a[i])


    try:
        course = souped_text.split("Course type:\n            \n                \n                ")[1][:11]
    except Exception:
        course = 'nil'
    course_type.append(course)
    
    try:
        lesson_length = souped_text.split("Average Lesson Length:\n            \n                ")[1][:7]
    except Exception:
        lesson_length = 'nil'
    avg_lesson_length.append(lesson_length)

    try:
        credit = souped_text.split("Eligible for Credit: ")[1][:4]
    except Exception:
        credit = 'No'
    credits.append(credit)
    
    j+=1

    print("iter : ", j , "complete...")

print("All things collected...time taken : ", time.time()-start, " secs")