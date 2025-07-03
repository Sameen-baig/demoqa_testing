from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Text Box
def selenium_textbox():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://demoqa.com/text-box")
    time.sleep(2)

    driver.find_element(By.ID, "userName").send_keys("John")
    driver.find_element(By.ID, "userEmail").send_keys("john@example.com")
    driver.find_element(By.ID, "currentAddress").send_keys("123 Demo Street")
    driver.find_element(By.ID, "permanentAddress").send_keys("456 Permanent Avenue")

    time.sleep(1)
    driver.find_element(By.ID, "submit").click()

    output_name = driver.find_element(By.ID, "name").text
    output_email = driver.find_element(By.ID, "email").text
    print("Text Box Output:")
    print(output_name)
    print(output_email)

    time.sleep(2)
    driver.quit()

#Checkbox
def checkbox_example(driver):
    driver.get("https://demoqa.com/checkbox")
    time.sleep(2)

    # Expand all
    driver.find_element(By.CSS_SELECTOR, ".rct-option-expand-all").click()
    time.sleep(1)

    for node in ["desktop", "documents", "downloads"]:
        checkbox = driver.find_element(By.XPATH, f"//label[@for='tree-node-{node}']")
        driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)
        time.sleep(0.5)
        driver.execute_script("arguments[0].click();", checkbox)

    result = driver.find_element(By.ID, "result").text
    print("Checkbox Result")
    print(result)

# Radio Button
def radio_button_example(driver):
    driver.get("https://demoqa.com/radio-button")
    time.sleep(2)

    yes_radio = driver.find_element(By.XPATH, "//label[@for='yesRadio']")
    yes_radio.click()
    result = driver.find_element(By.CLASS_NAME, "text-success").text
    print("Radio Button Result:", result)

# Web Tables
def web_tables_example(driver):
    driver.get("https://demoqa.com/webtables")
    time.sleep(2)

    driver.find_element(By.ID, "addNewRecordButton").click()
    time.sleep(1)

    driver.find_element(By.ID, "firstName").send_keys("Alice")
    driver.find_element(By.ID, "lastName").send_keys("Smith")
    driver.find_element(By.ID, "userEmail").send_keys("alice@example.com")
    driver.find_element(By.ID, "age").send_keys("30")
    driver.find_element(By.ID, "salary").send_keys("5000")
    driver.find_element(By.ID, "department").send_keys("QA")
    driver.find_element(By.ID, "submit").click()
    time.sleep(1)

    print("Web Table Rows:")
    rows = driver.find_elements(By.CLASS_NAME, "rt-tr-group")
    for row in rows:
        print(row.text)

# Buttons
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def buttons_example(driver):
    driver.get("https://demoqa.com/buttons")
    time.sleep(2)

    actions = webdriver.ActionChains(driver)

    # Double Click
    double_click_btn = driver.find_element(By.ID, "doubleClickBtn")
    actions.double_click(double_click_btn).perform()

    wait = WebDriverWait(driver, 5)
    double_result = wait.until(EC.visibility_of_element_located((By.ID, "doubleClickMessage"))).text
    print("Double Click Message:", double_result)

    right_click_btn = driver.find_element(By.ID, "rightClickBtn")
    actions.context_click(right_click_btn).perform()
    right_result = wait.until(EC.visibility_of_element_located((By.ID, "rightClickMessage"))).text
    print("Right Click Message:", right_result)

    buttons = driver.find_elements(By.TAG_NAME, "button")
    for btn in buttons:
        if btn.text.strip() == "Click Me":
            btn.click()
            break

    dynamic_result = wait.until(EC.visibility_of_element_located((By.ID, "dynamicClickMessage"))).text
    print("Dynamic Click Message:", dynamic_result)

#Links
def links_example(driver):
    driver.get("https://demoqa.com/links")
    time.sleep(2)

    # Click on Home link and go back
    home_link = driver.find_element(By.ID, "simpleLink")
    home_link.click()
    time.sleep(2)

    # Switch to new tab
    driver.switch_to.window(driver.window_handles[1])
    print("Navigated to:", driver.current_url)
    driver.close()

    driver.switch_to.window(driver.window_handles[0])

#Broken_links_and_images
def broken_links_and_images(driver):
    driver.get("https://demoqa.com/broken")
    time.sleep(2)

    # Check if image is broken
    image = driver.find_element(By.XPATH, "(//img)[2]")  # Second image is broken
    image_src = image.get_attribute("src")
    response = requests.get(image_src)
    print("Broken Image Status Code:", response.status_code)

    # Check if link is broken
    link = driver.find_element(By.LINK_TEXT, "Click Here for Broken Link")
    url = link.get_attribute("href")
    res = requests.get(url)
    print("Broken Link Status Code:", res.status_code)

#upload_and_download
def upload_and_download(driver):
    driver.get("https://demoqa.com/upload-download")
    time.sleep(2)

    download_button = driver.find_element(By.ID, "downloadButton")
    download_button.click()
    print("Download button clicked")

    upload_input = driver.find_element(By.ID, "uploadFile")
    upload_path = os.path.abspath("sample.txt")  # Ensure this file exists
    with open("sample.txt", "w") as f:
        f.write("This is a test upload file.")

    upload_input.send_keys(upload_path)
    time.sleep(2)

    uploaded_text = driver.find_element(By.ID, "uploadedFilePath").text
    print("Uploaded File Path:", uploaded_text)

#Dynamic_properties
def dynamic_properties(driver):
    driver.get("https://demoqa.com/dynamic-properties")

    wait = WebDriverWait(driver, 10)

    enable_button = wait.until(EC.element_to_be_clickable((By.ID, "enableAfter")))
    print("Enable Button is now clickable")

    color_button = driver.find_element(By.ID, "colorChange")
    original_class = color_button.get_attribute("class")
    time.sleep(6)  # Allow time for color to change
    new_class = color_button.get_attribute("class")

    print("Color changed:", original_class != new_class)

    visible_button = wait.until(EC.visibility_of_element_located((By.ID, "visibleAfter")))
    print("Visible Button is now shown:", visible_button.is_displayed())

#Practice_forms
def practice_form(driver):
    driver.get("https://demoqa.com/automation-practice-form")
    time.sleep(2)

    driver.find_element(By.ID, "firstName").send_keys("ABC")
    driver.find_element(By.ID, "lastName").send_keys("XYZ")
    driver.find_element(By.ID, "userEmail").send_keys("abc123@example.com")
    driver.find_element(By.XPATH, "//label[@for='gender-radio-1']").click()
    driver.find_element(By.ID, "userNumber").send_keys("03123456789")

    submit_button = driver.find_element(By.ID, "submit")
    driver.execute_script("arguments[0].scrollIntoView();", submit_button)
    driver.find_element(By.ID, "dateOfBirthInput").click()
    driver.find_element(By.CLASS_NAME, "react-datepicker__day--015").click()
    driver.find_element(By.ID, "subjectsInput").send_keys("Maths")
    driver.find_element(By.ID, "subjectsInput").send_keys("\n")
    driver.find_element(By.XPATH, "//label[@for='hobbies-checkbox-1']").click()
    picture_path = os.path.abspath("sample.txt")
    driver.find_element(By.ID, "uploadPicture").send_keys(picture_path)
    driver.find_element(By.ID, "currentAddress").send_keys("Tokyo, Japan")
    driver.find_element(By.ID, "submit").click()
    modal_title = driver.find_element(By.ID, "example-modal-sizes-title-lg").text
    print("Form Submitted: ", modal_title)
    driver.find_element(By.ID, "closeLargeModal").click()


# Main
def main():
    driver = webdriver.Chrome()
    driver.maximize_window()

    links_example(driver)
    broken_links_and_images(driver)
    upload_and_download(driver)
    dynamic_properties(driver)
    practice_form(driver)

    driver.quit()

if __name__ == "__main__":
    main()
