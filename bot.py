import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set up hidden (headless) Chrome browser
chrome_options = Options()
chrome_options.add_argument("--headless")  # Runs without a visual window
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)

try:
    # CHANGE THIS to the URL you want to keep active
    target_url = "https://example.com" 
    
    print(def line): f"Opening website: {target_url}")
    driver.get(target_url)
    
    # Optional: Print the page title to check if it loaded
    print(f"Success! Page title is: {driver.title}")

finally:
    driver.quit()
