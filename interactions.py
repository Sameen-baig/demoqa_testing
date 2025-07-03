from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# draggable
def draggable_example(driver):
    driver.get("https://demoqa.com/dragabble")
    time.sleep(2)

    drag_me = driver.find_element(By.ID, "dragBox")
    print("Draggable element moved.")

    x_restricted = driver.find_element(By.ID, "restrictedX")
    print("x_axis")
    y_axis = driver.find_element(By.ID, "restrictedY")
    print("y_axis")

#droppable
def droppable_example(driver):
    driver.get("https://demoqa.com/droppable")
    time.sleep(2)

    source = driver.find_element(By.ID, "draggable")
    target = driver.find_element(By.ID, "droppable")
    webdriver.ActionChains(driver).drag_and_drop(source, target).perform()
    print("Dropped Text:", target.text)

#accept
    driver.find_element(By.ID, "droppableExample-tab-accept").click()
    time.sleep(1)

    source =  driver.find_element(By.ID, "acceptable")
    target = driver.find_element(By.ID, "droppable")
    webdriver.ActionChains(driver).drag_and_drop(source, target).perform()
    print("Dropped Text:", target.text)

#Resizeable
def resizable_example(driver):
    driver.get("https://demoqa.com/resizable")
    time.sleep(2)

    resize_handle = driver.find_element(By.CLASS_NAME, "react-resizable-handle")
    webdriver.ActionChains(driver).click_and_hold(resize_handle).move_by_offset(100, 50).release().perform()
    print("Resizable element resized.")


#selectable
def selectable_example(driver):
    driver.get("https://demoqa.com/selectable")
    time.sleep(2)

    items = driver.find_elements(By.CSS_SELECTOR, "#verticalListContainer li")
    for item in items:
        item.click()
    print("All selectable items clicked.")


#Sortable
def sortable_example(driver):
    driver.get("https://demoqa.com/sortable")
    time.sleep(2)

    item1 = driver.find_element(By.XPATH, "//div[@id='demo-tabpane-list']//div[text()='One']")
    item5 = driver.find_element(By.XPATH, "//div[@id='demo-tabpane-list']//div[text()='Five']")

    webdriver.ActionChains(driver).click_and_hold(item5).move_to_element(item1).release().perform()
    print("Sortable items rearranged.")

#login automation
def login_example(driver):
    driver.get("https://demoqa.com/login")
    time.sleep(2)

    driver.find_element(By.ID, "userName").send_keys("yourUsername")
    driver.find_element(By.ID, "password").send_keys("yourPassword")
    driver.find_element(By.ID, "login").click()
    
    time.sleep(2)
    print("Login successful:", "profile" in driver.current_url)

def book_store_example(driver):
    driver.get("https://demoqa.com/books")
    time.sleep(2)

    book_titles = driver.find_elements(By.XPATH, "//div[@class='action-buttons']//a")
    print("Available Books:")
    for book in book_titles:
        print("-", book.text)
        

    # Click on the first book to view details
    book_titles[0].click()
    time.sleep(2)
    print("Navigated to book detail page.")

def profile_example(driver):
    driver.get("https://demoqa.com/profile")
    time.sleep(2)

    # Example: Remove a book if exists
    try:
        delete_button = driver.find_element(By.XPATH, "//span[@id='delete-record-undefined']")
        delete_button.click()
        time.sleep(1)
        driver.find_element(By.ID, "closeSmallModal-ok").click()
        print("Book deleted from profile.")
    except:
        print("No book found to delete.")


def interactions():
    driver = webdriver.Chrome()
    driver.maximize_window()

    draggable_example(driver)
    droppable_example(driver)
    resizable_example(driver)
    selectable_example(driver)
    sortable_example(driver)
    login_example(driver)
    book_store_example(driver)
    profile_example(driver)



if __name__=="__main__":
    interactions()