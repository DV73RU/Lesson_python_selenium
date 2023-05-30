

from selenium.webdriver.common.by import By

def add_card(driver, xpath):
    try:
        element = driver_g.find_element(By.XPATH, xpath)
    except:
        element = None
    return element
