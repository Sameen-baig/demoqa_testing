from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Browser Windows
def browser_windows(driver):
    driver.get("https://demoqa.com/browser-windows")
    time.sleep(2)

    # Tab Button
    driver.find_element(By.ID, "tabButton").click()
    driver.switch_to.window(driver.window_handles[1])
    print("New Tab Text:", driver.find_element(By.ID, "sampleHeading").text)
    driver.close()

    driver.switch_to.window(driver.window_handles[0])

    # Window Button - Fix click interception
    window_button = driver.find_element(By.ID, "windowButton")
    driver.execute_script("arguments[0].scrollIntoView(true);", window_button)
    driver.execute_script("arguments[0].click();", window_button)

    driver.switch_to.window(driver.window_handles[1])
    print("New Window Text:", driver.find_element(By.ID, "sampleHeading").text)
    driver.close()

    driver.switch_to.window(driver.window_handles[0])

# Alerts
def alerts_example(driver):
    driver.get("https://demoqa.com/alerts")
    time.sleep(2)

    # Simple alert
    driver.find_element(By.ID, "alertButton").click()
    alert = driver.switch_to.alert
    print("Alert Text:", alert.text)
    alert.accept()

    # Timed alert (fixed with JS click to avoid ad overlap)
    timer_button = driver.find_element(By.ID, "timerAlertButton")
    driver.execute_script("arguments[0].scrollIntoView(true);", timer_button)
    driver.execute_script("arguments[0].click();", timer_button)
    time.sleep(6)
    alert = driver.switch_to.alert
    print("Timer Alert Text:", alert.text)
    alert.accept()

    # Confirm alert
    driver.find_element(By.ID, "confirmButton").click()
    alert = driver.switch_to.alert
    alert.dismiss()
    print("Confirm Result:", driver.find_element(By.ID, "confirmResult").text)

    # Prompt alert
    driver.find_element(By.ID, "promtButton").click()
    alert = driver.switch_to.alert
    alert.send_keys("Samee")
    alert.accept()
    print("Prompt Result:", driver.find_element(By.ID, "promptResult").text)

# Frames
def frames_example(driver):
    driver.get("https://demoqa.com/frames")
    time.sleep(2)

    driver.switch_to.frame("frame1")
    print("Frame 1 Text:", driver.find_element(By.ID, "sampleHeading").text)
    driver.switch_to.default_content()

    driver.switch_to.frame("frame2")
    print("Frame 2 Text:", driver.find_element(By.ID, "sampleHeading").text)
    driver.switch_to.default_content()

# Nested Frames
def nested_frames_example(driver):
    driver.get("https://demoqa.com/nestedframes")
    time.sleep(2)

    # Switch to parent frame
    driver.switch_to.frame(driver.find_element(By.ID, "frame1"))
    parent_text = driver.find_element(By.TAG_NAME, "body").text
    print("Parent Frame Text:", parent_text)

    # Switch to child frame inside parent
    child_iframe = driver.find_element(By.TAG_NAME, "iframe")
    driver.switch_to.frame(child_iframe)
    child_text = driver.find_element(By.TAG_NAME, "p").text
    print("Child Frame Text:", child_text)

    driver.switch_to.default_content()  # back to main page

#Modal_dialogs
def modal_dialogs(driver):
    driver.get("https://demoqa.com/modal-dialogs")
    time.sleep(2)

    driver.find_element(By.ID, "showSmallModal").click()   
    time.sleep(1)
    print("Small Modal Title:", driver.find_element(By.ID, "example-modal-sizes-title-sm").text) #small modal title
    driver.find_element(By.ID, "closeSmallModal").click() 

    driver.find_element(By.ID, "showLargeModal").click()
    time.sleep(1)
    print("Large Modal Title:", driver.find_element(By.ID, "example-modal-sizes-title-lg").text) #large modal title
    driver.find_element(By.ID, "closeLargeModal").click()

#Accordian
def accordian_example(driver):
    driver.get("https://demoqa.com/accordian")
    time.sleep(2)

    driver.find_element(By.ID, "section1Heading").click()
    time.sleep(1)
    #print("Accordian Content:", driver.find_element(By.ID, "collapseOne").text)
    driver.find_element(By.ID, "section2Heading").click()
    time.sleep(1)
    driver.find_element(By.ID, "section3Heading").click()
    time.sleep(1)

def auto_complete(driver):
    driver.get("https://demoqa.com/auto-complete")
    time.sleep(2)

    input_box = driver.find_element(By.ID, "autoCompleteMultipleInput")
    input_box.send_keys("Re")
    time.sleep(1)
    input_box.send_keys(Keys.DOWN)
    input_box.send_keys(Keys.ENTER)

    input_box.send_keys("Gr")
    time.sleep(1)
    input_box.send_keys(Keys.DOWN)
    input_box.send_keys(Keys.ENTER)
    print("Auto Complete Input Done")

def date_picker(driver):
    driver.get("https://demoqa.com/date-picker")
    time.sleep(2)

    date_input = driver.find_element(By.ID, "datePickerMonthYearInput")
    date_input.clear()
    date_input.send_keys("06/28/2025")
    date_input.send_keys(Keys.ENTER)

    date_time_input = driver.find_element(By.ID, "dateAndTimePickerInput")
    date_time_input.clear()
    date_time_input.send_keys("June 28, 2025 3:30 PM")
    date_time_input.send_keys(Keys.ENTER)

    print("Date Picker Updated")

def slider_example(driver):
    driver.get("https://demoqa.com/slider")
    time.sleep(2)

    slider = driver.find_element(By.CLASS_NAME, "range-slider")
    driver.execute_script("arguments[0].value = 80;", slider)
    driver.execute_script("arguments[0].dispatchEvent(new Event('change'))", slider)

    print("Slider Value:", driver.find_element(By.ID, "sliderValue").get_attribute("value"))

def progress_bar(driver):
    driver.get("https://demoqa.com/progress-bar")
    time.sleep(2)

    start_button = driver.find_element(By.ID, "startStopButton")
    start_button.click()
    time.sleep(5)
    driver.find_element(By.ID, "startStopButton").click()
    
    progress = driver.find_element(By.CLASS_NAME, "progress-bar").text
    print("Progress Bar Status:", progress)

def tabs_example(driver):
    driver.get("https://demoqa.com/tabs")
    time.sleep(2)

    driver.find_element(By.ID, "demo-tab-what").click()
    time.sleep(1)
    print("Tab - What:", driver.find_element(By.ID, "demo-tabpane-what").text[:50])

    driver.find_element(By.ID, "demo-tab-origin").click()
    time.sleep(1)
    print("Tab - Origin:", driver.find_element(By.ID, "demo-tabpane-origin").text[:50])

    driver.find_element(By.ID, "demo-tab-use").click()
    time.sleep(1)
    print("Tab - Use:", driver.find_element(By.ID, "demo-tabpane-use").text[:50])

def tool_tips(driver):
    driver.get("https://demoqa.com/tool-tips")
    time.sleep(2)

    # Locate the button and hover
    button = driver.find_element(By.ID, "toolTipButton")
    ActionChains(driver).move_to_element(button).perform()

    # Wait for tooltip to appear
    wait = WebDriverWait(driver, 10)
    tooltip = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "tooltip-inner")))
    
    print("Tooltip on Button:", tooltip.text)

def menu_example(driver):
    driver.get("https://demoqa.com/menu")
    time.sleep(2)

    # Scroll to make menu visible
    menu = driver.find_element(By.ID, "nav")
    driver.execute_script("arguments[0].scrollIntoView(true);", menu)

    # Hover over menu items
    main_item = driver.find_element(By.XPATH, "//a[text()='Main Item 2']")
    ActionChains(driver).move_to_element(main_item).perform()
    time.sleep(1)

    sub_item = driver.find_element(By.XPATH, "//a[text()='SUB SUB LIST »']")
    ActionChains(driver).move_to_element(sub_item).perform()
    time.sleep(1)

    sub_sub_item = driver.find_element(By.XPATH, "//a[text()='Sub Sub Item 2']")
    ActionChains(driver).move_to_element(sub_sub_item).perform()
    time.sleep(1)

    print("Menu Interaction Completed")


def select_menu(driver):
    driver.get("https://demoqa.com/select-menu")
    time.sleep(2)

    # Select value
    driver.find_element(By.ID, "react-select-2-input").send_keys("Group 1, option 1", Keys.ENTER)
    # Select one
    driver.find_element(By.ID, "react-select-3-input").send_keys("Dr.", Keys.ENTER)

    # Old style select menu
    select = driver.find_element(By.ID, "oldSelectMenu")
    select.send_keys("Purple")

    print("Select Menu Selections Completed")

# Main Function
def new():
    driver = webdriver.Chrome()
    driver.maximize_window()

    #browser_windows(driver)
    #alerts_example(driver)
    #frames_example(driver)
    #nested_frames_example(driver)
    #modal_dialogs(driver)
    #accordian_example(driver)
    #auto_complete(driver)
    ##date_picker(driver)
    ##slider_example(driver)
    #progress_bar(driver)
    #tabs_example(driver)
    ##tool_tips(driver)
    menu_example(driver)
    ##select_menu(driver)

    driver.quit()

if __name__ == "__main__":
    new()
