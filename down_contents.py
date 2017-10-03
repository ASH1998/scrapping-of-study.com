import bs4
from selenium import webdriver

MASTER_LINK = "http://study.com/academy/course/index.html"

browser = webdriver.PhantomJS('phantomjs')
browser.get(MASTER_LINK)

#b = browser.find_element_by_xpath('//*[@class="btn btn-primary"]')

#result_links = browser.find_elements_by_link_text('View Lessons')

#soup = bs4.BeautifulSoup(browser.page_source, 'lxml')
#print(soup.text)
linkss = []
links = browser.find_elements_by_tag_name('a')
for i in links:
    try:
        #print(i.get_attribute('href'))
        if 'com/academy/course/' in i.get_attribute('href'):
            linkss.append(i.get_attribute('href'))
    except Exception:
        pass

linkss = linkss[2:-5]