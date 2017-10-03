import csv
import time
from down_contents import *
from down_images import *
from collecting_data import *

start = time.time()

rows = []
#rows = zip(titles[:10], summary, course_type, credits, no_of_lessons, total_views, avg_lesson_length)
rows.append(titles[:10])
rows.append(summary)
rows.append(course_type)
rows.append(credits)
rows.append(no_of_lessons)
rows.append(total_views)
rows.append(avg_lesson_length)

rev = zip(*rows)

with open("newcsvfile.csv", 'w') as fopen:
    writer = csv.writer(fopen)
    writer.writerow(['TITLE', 'SUMMARY', 'COURSE_TYPE', 'CREDITS', 'NO_OF_LESSONS', 'TOTAL_VIEWS', 'AVG_LESSON_LENGTH'])
    writer.writerows(rev)

print("ENDING TIME TAKEN : ", time.time()-start, "secs")