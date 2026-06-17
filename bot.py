import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=1920,1080")
# Makes the cloud browser mimic a regular Windows computer user agent
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

driver = webdriver.Chrome(options=chrome_options)

try:
    target_url = "https://altare.gg"
    
    # Open the home domain first so the browser allows cookie injections
    driver.get("https://altare.gg")
    time.sleep(3)
    
    # Grab the hidden security secrets from your repository settings
    altare_session = os.environ.get("ALTARE_SESSION")
    cf_clearance = os.environ.get("CF_CLEARANCE")
    
    # Inject the Cloudflare verification cookie
    if cf_clearance:
        driver.add_cookie({
            "name": "cf_clearance",
            "value": cf_clearance,
            "domain": ".altare.gg",
            "path": "/"
        })
        print("Cloudflare verification cookie injected.")

    # Inject your active login account cookie
    if altare_session:
        driver.add_cookie({
            "name": "altare_session",
            "value": altare_session,
            "domain": ".altare.gg",
            "path": "/"
        })
        print("Login session cookie injected.")

    # Open your target page fully authenticated
    print(f"Opening rewards page: {target_url}")
    driver.get(target_url)
    time.sleep(5)
    
    # Logs to verify if you successfully bypassed the login screen
    print(f"Current location verified as: {driver.current_url}")
    print(f"Page title confirmation: {driver.title}")

finally:
    # Always close the clean background session
    driver.quit()
