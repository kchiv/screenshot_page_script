import os
import time
from selenium import webdriver


current_date = time.strftime('%d-%m-%Y')
os.makedirs(current_date)


br = webdriver.PhantomJS()
br.set_window_size(1024, 768)

urllist = [
'https://www.lifelock.com',
'https://www.lifelock.com/how-it-works/what-is-identity-theft/',
'https://www.lifelock.com/how-it-works/overview/',
'https://www.lifelock.com/how-it-works/lifelock-experience/',
'https://www.lifelock.com/how-it-works/lifelock-mobile-app/',
'https://www.lifelock.com/products/',
'https://www.lifelock.com/store',
'https://www.lifelock.com/products/lifelock-standard/',
'https://www.lifelock.com/products/lifelock-advantage/',
'https://www.lifelock.com/products/lifelock-ultimate-plus/',
'https://www.lifelock.com/products/lifelock-junior/',
'https://www.lifelock.com/reviews/',
'https://www.lifelock.com/reviews/lifelock-standard/',
'https://www.lifelock.com/reviews/lifelock-advantage/',
'https://www.lifelock.com/reviews/lifelock-ultimate-plus/',
'https://www.lifelock.com/education/'
]

for listitem in urllist:
    br.get(listitem)
    remove_domain = listitem[24:]
    file_name = remove_domain.replace('/','')
    screenshot_file = file_name + '_screenshot.png'
    br.save_screenshot('/Users/kyle.chivers/Desktop/python_scripts/screenshot_script/' + current_date + '/' + screenshot_file)

br.quit()


