# coding: utf-8
import os
import selenium
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import codecs
from pyvirtualdisplay import Display

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
chrome_path = os.path.join(dname, "chromedriver")

os.system("pkill chrome")
# driver = webdriver.Chrome(chrome_path) 
display = Display(visible=0, size=(800, 600))
display.start()
# driver = webdriver.Chrome(chrome_path)
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_path = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(chrome_path, chrome_options=chrome_options)
driver.maximize_window()


delay = 10
keyword = "nltk"
url = "https://yandex.com/"


file_web = codecs.open("web.txt", "w", "utf8")
file_img = codecs.open("img.txt", "w", "utf8")
file_video = codecs.open("video.txt", "w", "utf8")


driver.get(url)

search_form = WebDriverWait(driver, delay).until(
						EC.presence_of_element_located((By.ID, "text"))
			  )

search_form.send_keys(keyword)


submit_btn = driver.find_element_by_xpath('//button[@type="submit"]')
submit_btn.click()

title_css = "a.link organic__url link_cropped_no i-bem".replace(" ", ".")
dscrpt_css = "div.text-container typo typo_text_m typo_line_m organic__text".replace(" ", ".")

for i in range(10):

	while True:
		try:
			titles = driver.find_elements_by_css_selector(title_css)
			if len(titles) == 10: break

		except Exception as e:
			continue


	prev_title = titles[0].text
	dscrpts = driver.find_elements_by_css_selector(dscrpt_css)

	for title, dscrpt in zip(titles, dscrpts):

		link = title.get_attribute("href")
		title = title.text
		dscrpt = dscrpt.text.replace("\n", " ")

		print(title)
		print(link)
		print(dscrpt)
		print('\n')

		file_web.write("\n".join([title, link, dscrpt]) + "\n\n\n")

	next_btn = driver.find_element_by_css_selector("a.link link_ajax_yes pager__item pager__item_kind_next i-bem".replace(" ", "."))
	try:
		next_btn.click()
	except Exception as e:
		pass

	while True:
		try:
			if prev_title != driver.find_element_by_css_selector(title_css).text: break

		except Exception as e:
			continue

file_web.close()

print("-------------------------------------------------------------")

driver.quit()
driver = webdriver.Chrome(chrome_path, chrome_options=chrome_options)
driver.maximize_window()
image_url = "https://yandex.com/images/search?text=" + keyword
driver.get(image_url)

# image_links = driver.find_elements_by_css_selector("div.serp-item__preview")
print()

prev_title = ""
prev_dscrpt = ""

for i in range(100):

	image_links = driver.find_elements_by_css_selector("div.serp-item__preview")
	image_srcs = driver.find_elements_by_css_selector("img.serp-item__thumb")
	# print(len(image_links))
	# image_link = driver.find_element_by_class_name("serp-item_pos_%d" % i)
	# image_link = WebDriverWait(driver, delay).until(
		#		EC.presence_of_element_located((By.CLASS_NAME, "serp-item_pos_%d" % i))
		#)

	driver.execute_script('document.querySelector(".tabs-navigation__content").style.display="none";')
	driver.execute_script('document.querySelector("#advanced-search-placeholder").style.display="none";')

	image_link = image_links[i]
	# print(image_link.location["y"])
	driver.execute_script("window.scrollTo(0, %d)" % (int(image_link.location["y"]) - 150))
	image_src = image_srcs[i]
	#print(len(image_links))
	print(i)
	
	"""
	try:
		image_link.click()
	except:
		pass
	
	"""
	
	while True:
		try:
			image_link.click()
			# image_link.send_keys(selenium.webdriver.common.keys.Keys.SPACE)

			# driver.execute_script("arguments[0].click()", image_link)

			# print("done")
			# time.sleep(1)
			break
		except Exception as e:
			time.sleep(0.1)
			# print(e)			
			continue

	
	while True:
		title_link = WebDriverWait(driver, delay).until(
				EC.presence_of_element_located((By.CSS_SELECTOR, "a.snippet2__title".replace(" ", ".")))
		)

		dscrpt = driver.find_element_by_css_selector("div.snippet2__text").text.replace("\n", " ")
		# print(title_link.text)
		# print(prev_dscrpt)
		# print(dscrpt)
		if title_link.text != "" and title_link.text != prev_title:
			if dscrpt != "" and dscrpt != prev_dscrpt: break

	title = title_link.text
	prev_title = title
	prev_dscrpt = dscrpt
	link = driver.find_element_by_css_selector("a.snippet2__link").get_attribute("href")

	print(title)
	print(image_src.get_attribute("src"))
	print(dscrpt)
	print('\n')

	file_img.write("\n".join([title, image_src.get_attribute("src"), dscrpt]) + "\n\n\n")
	
	
	close_btn = driver.find_element_by_xpath('//a[@aria-label="Close"]')
	close_btn.click()
	# driver.execute_script("arguments[0].scrollIntoView();", image_link)


	# time.sleep(0.5)

	# if i == 100 - 1: break

file_img.close()

print("-------------------------------------------------------------")
driver.quit()
driver = webdriver.Chrome(chrome_path, chrome_options=chrome_options)
driver.maximize_window()
video_url = "https://yandex.com/video/search?text=" + keyword
driver.get(video_url)

more_btn_css = "button.button2 button2_size_l button2_theme_action more__button i-bem button2_js_inited".replace(" ", ".")

for i in range(10):

	# _ = WebDriverWait(driver, delay).until(
	# 		EC.presence_of_element_located((By.CSS_SELECTOR, "h2.serp-item__title"))
	# )

	while True:
		try:
			titles = driver.find_elements_by_css_selector("h2.serp-item__title")
			if len(titles) == 20*(i+1): break

		except Exception as e:
			continue

	links = driver.find_elements_by_css_selector("a.link link_theme_normal serp-url__link i-bem".replace(" ", "."))
	dscrpts = driver.find_elements_by_css_selector("div.serp-item__text")

	for j, title, link, dscrpt in zip(range(20), titles, links, dscrpts):
		# cnt += 1
		idx = 20*i + j
		print(idx)
		title = titles[idx].text
		link = links[idx].get_attribute("onmousedown")
		link = link.split("href\":\"")[1]
		link = link.split("\"},this")[0]
		dscrpt = dscrpts[idx].text.replace("\n", " ")

		print(title)
		print(link)
		print(dscrpt)
		print('\n')

		
		file_video.write("\n".join([title, link, dscrpt]) + "\n\n\n")

		if j == 20 - 1:
			driver.execute_script("arguments[0].scrollIntoView();", titles[idx])

			if i % 2 != 0:
				more_btn = WebDriverWait(driver, delay).until(
						EC.element_to_be_clickable((By.CSS_SELECTOR, more_btn_css))
				)
				more_btn.click()

file_video.close()
driver.quit()
