import os
import time
import undetected_selenium as uc

options = uc.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920,1080")

# Launch the anti-detect cloud browser
driver = uc.Chrome(options=options)

try:
    target_url = "https://altare.gg"
    
    # 1. Visit domain first so the browser accepts cookies
    print("Navigating to home domain...")
    driver.get("https://altare.gg")
    time.sleep(5)
    
    # 2. Get your secret keys
    altare_session = os.environ.get("ALTARE_SESSION")
    cf_clearance = os.environ.get("CF_CLEARANCE")
    
    # 3. Inject Cloudflare cookie bypass
    if cf_clearance:
        driver.add_cookie({
            "name": "cf_clearance",
            "value": cf_clearance,
            "domain": ".altare.gg",
            "path": "/"
        })
        print("Cloudflare verification cookie injected.")

    # 4. Inject your login session cookie
    if altare_session:
        driver.add_cookie({
            "name": "altare_session",
            "value": altare_session,
            "domain": ".altare.gg",
            "path": "/"
        })
        print("Login session cookie injected.")

    # 5. Open your rewards page fully bypassed
    print(f"Opening rewards page: {target_url}")
    driver.get(target_url)
    
    # Keep the tab active on the page for 30 seconds so it registers you as AFK
    time.sleep(30)
    
    print(f"Current location verified as: {driver.current_url}")
    print(f"Page title confirmation: {driver.title}")

finally:
    driver.quit()
