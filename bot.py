import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set up hidden (headless) Chrome browser
chrome_options = Options()
chrome_options.add_argument("--headless")  # Runs without a visual window
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=chrome_options)

try:
    # Your target AFK rewards website
    target_url = "https://altare.gg" 
    
    print(f"Opening website: {target_url}")
    driver.get(target_url)
    
    # Wait 5 seconds for the page elements to fully load
    driver.implicitly_wait(5)
    
    # Check if the page loaded successfully
    print(f"Success! Page title is: {driver.title}")

finally:
    # Safeguard to close the browser session cleanly
    driver.quit()
