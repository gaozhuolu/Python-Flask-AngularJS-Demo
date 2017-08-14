from selenium import webdriver

options = webdriver.ChromeOptions()
options.binary_location = '/usr/bin/google-chrome'
options.add_argument('headless')
options.add_argument('window-size=1200x600')
driver = webdriver.Chrome(chrome_options=options)

driver.get('https://facebook.com')
driver.implicitly_wait(10)

#email = driver.find_element_by_css_selector('input[type=email]')
#password = driver.find_element_by_css_selector('input[type=password]')
#login = driver.find_element_by_css_selector('input[value="Log In"]')

#email.send_keys('evan@intoli.com')
#password.send_keys('hunter2')

driver.get_screenshot_as_file('main-page.png')

driver.quit()
