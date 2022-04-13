from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import xlsxwriter
import time



def search_func(topic, pages, location, width, height):    
    
    options = webdriver.ChromeOptions()
    options.add_argument("window-size="+str(width)+","+str(height))
    
    #==========Uncomment this two lines if you want to use a proxy server=========#
    #PROXY = "101.255.164.146:3128"
    #options.add_argument('--proxy-server=%s' % PROXY)
    #=============================================================================#

    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option("excludeSwitches",["enable-automation"])

    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options) #chrome_options=options
    driver.get("https://scholar.google.com/")

    time.sleep(8)

    input_element = driver.find_element_by_id('gs_hdr_tsi') 
    input_element.send_keys(topic)

    time.sleep(8)

    driver.find_element_by_id('gs_hdr_tsb').click()

    counter     = 0
    titles      = []
    links_list  = [] 

    time.sleep(8)

    while(counter < int(pages)):

        page = BeautifulSoup(driver.page_source, 'lxml')
        links = page.find_all('h3', {'class': 'gs_rt'})
        
        for element in links:
            try:
                titles.append(element.text)
                links_list.append(element.find('a')['href']) 
            except:
                pass


        nexts = page.find('div', {'id': 'gs_n'}).find_all('a')
        next = nexts[counter]['href']
        counter += 1

        time.sleep(8)
        driver.get("https://scholar.google.com"+next)


    xlsfile = xlsxwriter.Workbook(location+'/google_scholar.xlsx')
    xlsheet = xlsfile.add_worksheet()
    row = 0
    col = 0

    for title, link in zip(titles, links_list):

        xlsheet.write(row, col, title)
        xlsheet.write(row, col+1, link)

        row +=1

    xlsfile.close()