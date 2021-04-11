#
# get and archive the number of pages from my printer in a csv file
#

#try with selenium
# from selenium import webdriver
# driver = webdriver.PhantomJS()
# driver.get('https://HP093A74/#hId-pgDevInfo')
# p_element = driver.find_element_by_id(id_='intro-text')
# print(p_element.text)
# pages = driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/div[2]/form/div[1]/div[4]/div/table/tbody/tr[6]/td[2]')
# print ("pages: ", pages)



# try with dryscrape
import dryscrape
import bs4 as bs

dryscrape.start_xvfb()
sess = dryscrape.Session()
sess.visit('https://HP093A74/#hId-pgDevInfo')
source = sess.body()
print ("Source:", source)
print ()
# soup = bs.BeautifulSoup(source,'lxml')
soup = bs.BeautifulSoup(source,'lxml')
print ("Soup:", soup)
print ()
# test = soup.find('p', class_='jstest')
# print(test.text)
test = soup.find('div.pgm-overall-container')
print(test)

# try with PyQt4
# import sys
# from PyQt4.QtGui import QApplication
# from PyQt4.QtCore import QUrl
# from PyQt4.QtWebKit import QWebPage
# import bs4 as bs
# import urllib

# class Client(QWebPage):

    # def __init__(self, url):
        # self.app = QApplication(sys.argv)
        # QWebPage.__init__(self)
        # self.loadFinished.connect(self.on_page_load)
        # self.mainFrame().load(QUrl(url))
        # self.app.exec_()
        
    # def on_page_load(self):
        # self.app.quit()
        
# url = 'https://192.168.124.32/#hId-pgDevInfo'
# client_response = Client(url)
# source = client_response.mainFrame().toHtml()
# soup = bs.BeautifulSoup(source, 'lxml')
# js_test = soup.find('p', class_='jstest')
# print(js_test.text)
