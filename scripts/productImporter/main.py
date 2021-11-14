import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
standard_delay = 20  # seconds
max_processing_time = 10000  # seconds
admin_main_site = "https://localhost/admin-dev/"
admin_password = "rootroot"
admin_email = "adm.chmielecki@gmail.com"


def prepare_options():
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('ignore-certificate-errors')
    options.binary_location = chrome_path
    return options


def login():
    email = driver.find_element(By.ID, "email")
    email.clear()
    email.send_keys(admin_email)
    pas = driver.find_element(By.ID, "passwd")
    pas.clear()
    pas.send_keys(admin_password)
    pas.send_keys(Keys.RETURN)


def assert_window_loaded():
    driver.maximize_window()
    driver.set_window_rect(width=1920, height=1080)
    driver.get(admin_main_site)
    assert "lampyiswiatlo" in driver.title


def go_to_import_screen():
    WebDriverWait(driver, standard_delay).until(EC.presence_of_element_located((By.ID, "subtab-AdminImport")))
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight",
                          driver.find_element(By.ID, "nav-sidebar"))
    driver.find_elements(By.CSS_SELECTOR, ".material-icons.mi-settings_applications")[0].click()
    WebDriverWait(driver, standard_delay).until(EC.presence_of_element_located((By.LINK_TEXT, 'Importuj')))
    driver.find_element(By.LINK_TEXT, 'Importuj').click()
    WebDriverWait(driver, standard_delay).until(EC.presence_of_element_located((By.LINK_TEXT, 'Importuj')))
    assert "Importuj" in driver.title


def import_xlsx(path):
    Select(driver.find_element(By.ID, 'entity')).select_by_value("1")
    file_upload = driver.find_element(By.ID, "file")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", file_upload)
    file_upload.send_keys(path)

    delete_categories = driver.find_element(By.CSS_SELECTOR, "[for='truncate_1']")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", delete_categories)
    delete_categories.click()

    force_ids = driver.find_element(By.CSS_SELECTOR, "[for='forceIDs_1']")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", force_ids)
    force_ids.click()

    submit_button = driver.find_element(By.NAME, "submitImportFile")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", submit_button)
    submit_button.click()
    driver.switch_to.alert.accept()

    WebDriverWait(driver, standard_delay).until(EC.presence_of_element_located((By.ID, "import")))
    driver.find_element(By.ID, "import").click()

    WebDriverWait(driver, max_processing_time).until(EC.element_to_be_clickable((By.ID, "import_close_button")))
    driver.find_element(By.ID, "import_close_button").click()


def index_products():
    driver.get(admin_main_site)
    driver.get(admin_main_site)
    WebDriverWait(driver, standard_delay).until(EC.presence_of_element_located((By.ID, "subtab-ShopParameters")))
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight",
                          driver.find_element(By.ID, "nav-sidebar"))
    driver.find_elements(By.CSS_SELECTOR, ".material-icons.mi-settings")[0].click()
    WebDriverWait(driver, standard_delay).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Szukaj')))
    driver.find_element(By.LINK_TEXT, 'Szukaj').click()
    WebDriverWait(driver, standard_delay).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Przebuduj cały indeks')))
    driver.find_element(By.LINK_TEXT, "Przebuduj cały indeks").click()
    WebDriverWait(driver, max_processing_time).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".alert.alert-success")))


driver_path = os.path.join(os.path.dirname(__file__), './chromedriver.exe')
driver = webdriver.Chrome(chrome_options=prepare_options(), executable_path=driver_path)
assert_window_loaded()
login()
go_to_import_screen()
import_xlsx(os.path.join(os.path.dirname(__file__), 'test.xlsx'))
index_products()
driver.close()
print("import done")