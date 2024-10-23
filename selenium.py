


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set up WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the website
driver.get("https://example.com/form")

# Find the form elements
name_field = driver.find_element(By.NAME, "name")
email_field = driver.find_element(By.NAME, "email")
submit_button = driver.find_element(By.NAME, "submit")

# Fill out the form
name_field.send_keys("John Doe")
email_field.send_keys("johndoe@example.com")

# Submit the form
submit_button.click()

# Verify the submission
try:
    confirmation_message = driver.find_element(By.ID, "confirmation")
    if confirmation_message.is_displayed():
        print("Form submitted successfully!")
    else:
        print("Form submission failed.")
except:
    print("Form submission failed.")

# Close the browser
driver.quit()
