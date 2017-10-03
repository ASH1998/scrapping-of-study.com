import bs4
import threading
import urllib.request
import os
import time

MASTER_URL = 'http://study.com/academy/course/index.html'
IMAGE_DIR_NAME = 'images'

src = urllib.request.urlopen(MASTER_URL).read()
soup = bs4.BeautifulSoup(src, 'lxml')
if not os.path.isdir(IMAGE_DIR_NAME):
    os.makedirs(IMAGE_DIR_NAME)

a = []
for imgs in soup.findAll('img'):
    a.append(str(imgs.get('src')))

image_links = []

for i in range(len(a)):
    if '/cimages/cou' in a[i]:
        image_links.append(a[i])

del(a)

titles = []
for course_names in soup.find_all(attrs={'class':'titleTwo'}):
    titles.append(course_names.text)
titles.pop(len(titles)-1)
dict_link_titles = dict(zip(image_links, titles))

start = time.time()

print("Downloading course images in dir : ", IMAGE_DIR_NAME)

for keys,_ in dict_link_titles.items():
    dict_link_titles[keys] = dict_link_titles[keys].replace(':', '')

for link, name in dict_link_titles.items():
    resource = urllib.request.urlopen("https://study.com"+link)
    output = open("images//"+name+".jpg","wb")
    output.write(resource.read())
    output.close()

print("Downloading complete, time taken = ", time.time()- start)
