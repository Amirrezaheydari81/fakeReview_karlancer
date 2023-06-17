import time
import random
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
for x in range(0,6):

    print(x)
    names = [
    "ورزم",
    "تناز",
    "آریندخت",
    "دل انگیز",
    "زیار",
    "مهتاب",
    "مهناز",
    "آفرین",
    "شهین",
    "چشمه"
    ]
    projects=[
    "طراحی سایت",
    "طراحی رابط کاربری",
    "سایت وردپرس",
    "پلاگین وردپرس",
    "سئو سایت",
    "بهینه سازی سایت",
    ]
    comments=[
    "کارشون خیلی عالی و خوب بود متشکرم ازشون",
    "خیلی تمیز کار میکنن واقعا راضی بودم ازشون",
    "فوق العاده حرفه ای مخصوصا توی بحث وردپرس",
    "عالی، توضیحاتشون خیلی کامل و جامع بود",
    "خوشحالم که با این فرد کار کردم و تجربه کاری خوبی بود برام",
    ]
    random_n1 = random.randint(0, 9)
    random_n2 = random.randint(0, 6)
    random_n3 = random.randint(0, 4)

    name = names[random_n1]
    project = projects[random_n2]
    comment =comments[random_n3]

    driver = webdriver.Chrome('./chromedriver.exe')
    driver.get('https://www.karlancer.com/review/');

    input_name = driver.find_element(By.XPATH,'/html/body/app-root/div[1]/app-rate-review-public/div/div/div/div[1]/div[2]/div/div[3]/div[2]/input')
    input_project = driver.find_element(By.XPATH,"/html/body/app-root/div[1]/app-rate-review-public/div/div/div/div[1]/div[2]/div/div[3]/div[3]/input")
    input_comment = driver.find_element(By.XPATH,"/html/body/app-root/div[1]/app-rate-review-public/div/div/div/div[1]/div[2]/div/div[3]/div[4]/textarea")
    input_stars = driver.find_element(By.XPATH,"/html/body/app-root/div[1]/app-rate-review-public/div/div/div/div[1]/div[2]/div/div[3]/div[5]/div/div[2]/app-rate/div/i[5]")
    input_submit = driver.find_element(By.XPATH,"/html/body/app-root/div[1]/app-rate-review-public/div/div/div/div[1]/div[2]/div/div[3]/button")

    input_name.send_keys(name)
    time.sleep(1)
    input_project.send_keys(project)
    time.sleep(1)
    input_comment.send_keys(comment)

    ActionChains(driver).move_to_element(input_stars)
    input_stars.click()
    time.sleep(5)
    input_submit.click()
    time.sleep(2)

    driver.quit()