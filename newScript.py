import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os

# Initialize the Firefox WebDriver
driver = webdriver.Firefox()

idJobs = [
    "70edaf5e-0195-4874-620e-e2535fb8db08",
    "0dc165ab-c6c9-4057-92c5-c6c7f9c4db08",
    "b13dc961-5d5a-4f41-0dc0-d4b0c9bddb08",
    "c9a537c0-ccba-4321-77c1-0240f2afdb08",
    "27e692a0-4fc1-41ba-146e-0b04eeb2db08",
    "af0518b9-1b34-47e0-ff69-cc6f6faadb08",
    "a55e84fc-54e7-4f1e-56ae-cab9a1a9db08",
    "f865ebc0-b86a-4ec7-3f92-7a4da2a9db08",
    "bcd3c67f-495a-4da9-620c-e888caa8db08",
    "01b30b92-9405-4aff-688c-88162999db08",
    "ccaa5e63-c97e-4a76-adcf-ea67039ddb08",
    "77fd44d1-e2d6-4660-d91c-cfbbf08edb08",
    "73943d85-11db-4767-5866-455bea7bdb08",
    "16b0d8bd-0c4d-4521-9b0a-c6b9207dd908",
    "d450bf20-9008-42b1-e0ad-dd29fb76da08",
    "368741d7-30b8-480c-9b7c-b1cde59fda08",
    "baba512b-9759-4fbe-3e96-72b58c6dd908",
    "50130ea6-815c-4b6e-8bc7-aa9b0110148a",
    "5684e520-f617-4c41-b9d2-ab1000fbc318",
]


def click_element_with_id_and_fill_form(element_id, file_path):
    try:
        # Navigate to the URL
        driver.get("https://jobs.crelate.com/portal/prediktive")

        # Wait for the element to load and click it
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "cr-jobs-container"))
        )
        element_to_click = driver.find_element(By.ID, element_id)
        element_to_click.click()

        # Wait for the apply button and click it
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".cr-portal-button.cr-apply-default.cr-h4")
            )
        ).click()

        # Fill out the form fields
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "firstName"))
        ).send_keys("Alvaro")

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "lastName"))
        ).send_keys("Llano")

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "email"))
        ).send_keys("alvarollano04@gmail.com")

        # Interact with the star rating
        star_rating_container = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "cr-star-rating-container"))
        )
        stars = star_rating_container.find_elements(
            By.CSS_SELECTOR, "input[type='radio'][value='5']"
        )
        if stars:
            stars[-1].click()  # Click the last star (highest rating)

        # Fill out the additional input field
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "e49c4230-526b-4288-842e-a95a0030e2d6"))
        ).send_keys("I just find it on the internet")

        # Find the file upload element and send the file path
        file_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "file-uploadResume"))
        )
        file_input.send_keys(file_path)

        # Click the submit button
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "submitButton"))
        )
        submit_button.click()
        print("Submit button clicked.")

    except TimeoutException:
        print("The operation timed out.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
# Make sure to use the absolute path to the file you want to upload
file_to_upload = os.path.abspath("AlvaroBLlano Resume.pdf")

# The main URL
main_url = "https://jobs.crelate.com/portal/prediktive/"

# Iterate through idJobs
for idJob in idJobs:
    # Click the element and fill the form
    click_element_with_id_and_fill_form(idJob, file_to_upload)
    print(idJob)
    time.sleep(5)
    # After filling the form, you can navigate back to the main page using driver.get(main_url) again
    driver.get(main_url)
    time.sleep(5)

driver.quit()
