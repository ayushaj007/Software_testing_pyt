import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_registration_success(browser):
    registration_url = 'http://127.0.0.1:5000/register'
    browser.get(registration_url)

    # Find the form elements and interact with them
    username_field = browser.find_element(By.ID, 'username')
    email_field = browser.find_element(By.ID, 'email')
    password_field = browser.find_element(By.ID, 'password')
    password_retype_field = browser.find_element(By.ID, 'password_retype')
    submit_button = browser.find_element(By.CSS_SELECTOR, 'input[type="submit"]')

    # Fill in the form fields
    username_field.send_keys('testuser')
    email_field.send_keys('test@gmail.com') 
    password_field.send_keys('testpassword')
    password_retype_field.send_keys('testpassword')

    # Submit the form
    submit_button.click()

    # Add assertions to check for success messages or bugs
    success_message = "Registration Successful"
    error_message = "Email format is incorrect"  # Update this with the expected error message

    if success_message in browser.page_source:
        # Test passed
        print("Test Passed: Registration was successful.")
    elif error_message in browser.page_source:
        # Bug identified
        print("Bug Identified: Email format is incorrect.")
    else:
        # Unexpected behavior
        print("Unexpected Behavior: Something went wrong during registration.")

    # Optionally, capture screenshots for the test report
    browser.save_screenshot("registration.png")

def test_login_success(browser):
    # Navigate to the login page
    login_url = 'http://127.0.0.1:5000/login'
    browser.get(login_url)

    # Find the form elements and interact with them
    username_field = browser.find_element(By.ID, 'username')
    password_field = browser.find_element(By.ID, 'password')
    submit_button = browser.find_element(By.CSS_SELECTOR, 'input[type="submit"]')

    # Fill in the form fields
    username_field.send_keys('testuser')
    password_field.send_keys('testpassword')

    # Submit the form
    submit_button.click()

    # Add assertions to check for successful login or bugs
    success_message = "Welcome, testuser!"
    error_message = "Login failed. Invalid username or password"

    if success_message in browser.page_source:
        # Test passed
        print("Test Passed: Login was successful.")
        
        # Navigate to the user profile page
        profile_url = 'http://127.0.0.1:5000/profile'
        browser.get(profile_url)

        # Optionally, capture screenshot for the user profile
        browser.save_screenshot("profile.png")
        
    elif error_message in browser.page_source:
        # Bug identified
        print("Bug Identified: Login failed with invalid credentials.")
    else:
        # Unexpected behavior
        print("Unexpected Behavior: Something went wrong during login.")

    # Optionally, capture screenshot for the login page
    browser.save_screenshot("login.png")
