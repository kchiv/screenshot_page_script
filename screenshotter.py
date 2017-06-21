import os
import time
from selenium import webdriver


current_date = time.strftime('%d-%m-%Y')
os.makedirs(current_date)


br = webdriver.PhantomJS()
br.set_window_size(1024, 768)

urllist = [
'https://www.example.com',
'https://www.example.com/page-1',
'https://www.example.com/page-2'
]

for listitem in urllist:
    br.get(listitem)
    remove_domain = listitem[24:]
    file_name = remove_domain.replace('/','')
    screenshot_file = file_name + '_screenshot.png'
    br.save_screenshot('/path/to/file/' + current_date + '/' + screenshot_file)

br.quit()


