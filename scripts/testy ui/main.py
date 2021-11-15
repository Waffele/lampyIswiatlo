from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random

driver = webdriver.Chrome('./chromedriver.exe')
loginEmail = 'maciejmaciej2@exmaple.com'

def add_to_cart():
    driver.find_element(By.XPATH,"/html/body/main/section/div/div/section/div[1]/div[2]/div[2]/div[2]/form/div[2]/div/div[2]/button").click()
    time.sleep(1)

def continue_shopping():
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[2]/div/div/button").click()

def category_1():   #lampy wiszace
    driver.find_element(By.XPATH, "/html/body/main/header/div[2]/div/div[1]/div[2]/div[1]/ul/li[1]/a").click()

def category_2():
    xpath = "/html/body/main/header/div[2]/div/div[1]/div[2]/div[1]/ul/li[2]/a"
    driver.find_element(By.XPATH, xpath).click()

def category_3():
    xpath = "/html/body/main/header/div[2]/div/div[1]/div[2]/div[1]/ul/li[3]/a"
    driver.find_element(By.XPATH, xpath).click()

def category_4():
    xpath = "/html/body/main/header/div[2]/div/div[1]/div[2]/div[1]/ul/li[4]/a"
    driver.find_element(By.XPATH, xpath).click()

def get_into_lamp(id):
    xpath = "/html/body/main/section/div/div[2]/section/section/div[3]/div/div[1]/div[" + str(id) + "]/article/div/a"
    driver.find_element(By.XPATH, xpath).click()

def click_quantity_more(x):
    for _ in range(x-1):
        driver.find_element(By.XPATH, "/html/body/main/section/div/div/section/div[1]/div[2]/div[2]/div[2]/form/div[2]/div/div[1]/div/span[3]/button[1]/i").click()

def go_to_page(id):
    currenturl = driver.current_url
    currenturl += "?page=" + str(id)
    driver.get(currenturl)
    time.sleep(1)

def go_to_cart():
    xpath = "/html/body/main/header/nav/div/div/div[1]/div[2]/div[2]/div/div/a"
    driver.find_element(By.XPATH, xpath).click()

def delete_from_cart():
    xpath = "/html/body/main/section/div/div/section/div/div[1]/div/div[2]/ul/li/div/div[3]/div/div[3]/div/a"
    driver.find_element(By.XPATH, xpath).click()

def go_to_login_page():
    xpath = "/html/body/main/header/nav/div/div/div[1]/div[2]/div[1]/div/a"
    driver.find_element(By.XPATH, xpath).click()

def register():
    xpath = "/html/body/main/section/div/div/section/section/div/a"
    driver.find_element(By.XPATH, xpath).click()

    #plec
    driver.find_element(By.XPATH, "/html/body/main/section/div/div/section/section/section/form/section/div[1]/div[1]/label[1]/span/input").click()

    firstname = driver.find_element(By.NAME, "firstname")
    firstname.clear()
    firstname.send_keys("Maciej")

    surname = driver.find_element(By.NAME, "lastname")
    surname.clear()
    surname.send_keys("Kowalski")

    email = driver.find_element(By.NAME, "email")
    email.clear()
    email.send_keys(loginEmail)

    password = driver.find_element(By.NAME, "password")
    password.clear()
    password.send_keys("123456789")

    birthday = driver.find_element(By.NAME, "birthday")
    birthday.clear()
    birthday.send_keys("1999-10-10")

    #przetwarzanie danych
    driver.find_element(By.XPATH,"/html/body/main/section/div/div/section/section/section/form/section/div[8]/div[1]/span/label/input").click()

    #akceptowanie warunkow
    driver.find_element(By.XPATH, "/html/body/main/section/div/div/section/section/section/form/section/div[10]/div[1]/span/label/input").click()

    #zapisz
    driver.find_element(By.XPATH,"/html/body/main/section/div/div/section/section/section/form/footer/button").click()


def login():
    go_to_login_page()

    email = driver.find_element(By.NAME, "email")
    email.clear()
    email.send_keys(email)

    password = driver.find_element(By.NAME, "password")
    password.clear()
    password.send_keys("123456789")

    driver.find_element(By.XPATH, "/html/body/main/section/div/div/section/section/section/form/footer/button").click()

def finish_order():
    xpath = "/html/body/main/section/div/div/section/div/div[2]/div[1]/div[2]/div/a"
    driver.find_element(By.XPATH, xpath).click()
    time.sleep(1)

    adress = driver.find_element(By.NAME, "address1")
    adress.clear()
    adress.send_keys("Amundsena 20")

    postcode = driver.find_element(By.NAME, "postcode")
    postcode.clear()
    postcode.send_keys("69-420")

    city = driver.find_element(By.NAME, "city")
    city.clear()
    city.send_keys("Gdansk")

    time.sleep(2)

    driver.find_element(By.XPATH, "/html/body/section/div/section/div/div[1]/section[2]/div/div/form/div/div/footer/button").click()
    time.sleep(1)

    #choose dhl
    driver.find_element(By.XPATH,"/html/body/section/div/section/div/div[1]/section[3]/div/div[2]/form/div/div[1]/div[1]/div/span/input").click()
    time.sleep(1)

    #go dalej
    driver.find_element(By.XPATH,"/html/body/section/div/section/div/div[1]/section[3]/div/div[2]/form/button").click()
    time.sleep(1)

    #choose cash on delivery
    driver.find_element(By.XPATH,"/html/body/section/div/section/div/div[1]/section[4]/div/div[2]/div[4]/div/span/input").click()
    time.sleep(1)

    #check zgoda na warunki świadczenia usług
    driver.find_element(By.XPATH, "/html/body/section/div/section/div/div[1]/section[4]/div/form/ul/li/div[1]/span/input").click()
    time.sleep(1)

    #Złóż zamówienie
    driver.find_element(By.XPATH,"/html/body/section/div/section/div/div[1]/section[4]/div/div[3]/div[1]/button").click()

    time.sleep(5)

def go_to_summary():
    driver.find_element(By.XPATH,"/html/body/main/header/nav/div/div/div[1]/div[2]/div[1]/div/a[2]/span").click()
    time.sleep(1)

    driver.find_element(By.XPATH, "/html/body/main/section/div/div/section/section/div/div/a[3]").click()


def add_product(category, page):
    if category == 0:
        category_1()
    elif category == 1:
        category_2()
    elif category == 2:
        category_3()
    else:
        category_4()

    if page != 1:
        go_to_page(page)

    id = random.randint(1, 12)
    get_into_lamp(id)

    quantity = random.randint(1,15)
    click_quantity_more(quantity)
    add_to_cart()
    continue_shopping()



if __name__ == '__main__':
    driver.get("https://localhost/")
    driver.find_element(By.ID, "details-button").click()
    driver.find_element(By.ID, "proceed-link").click()

    add_product(0, 1)
    add_product(0, 2)
    add_product(0, 3)
    add_product(1, 1)
    add_product(1, 2)
    add_product(1, 3)
    add_product(2, 1)
    add_product(2, 2)
    add_product(3, 1)
    add_product(4, 2)

    go_to_cart()
    time.sleep(5)

    delete_from_cart()
    time.sleep(2)

    go_to_login_page()
    register()

    go_to_cart()
    finish_order()

    go_to_summary()





