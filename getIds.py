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
