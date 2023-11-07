import time
from selenium import webdriver
from bs4 import BeautifulSoup

# Set up the Selenium WebDriver
driver = webdriver.Firefox()

# URL of the page to scrape
url = "https://jobs.crelate.com/portal/prediktive"

# Navigate to the page
driver.get(url)

# Give the page some time to load JavaScript content
time.sleep(5)  # Adjust the sleep time as necessary

# Once the page is loaded, grab the HTML source
html = driver.page_source
driver.quit()

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Find the container with all the job listings
jobs_container = soup.find(class_="cr-jobs-container")

# Extract all element IDs within the jobs container
# Assuming that the IDs are stored in the 'id' attribute of each job listing element
job_ids = [job.get("id") for job in jobs_container.find_all(True, id=True)]

# Now, write the IDs to a text file in an array format
with open("job_ids.txt", "w") as file:
    file.write(str(job_ids))

print("Job IDs have been written to job_ids.txt")


idJobs = [
    "8d31f1af-a907-42f5-70aa-68c0adc9db08",
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
