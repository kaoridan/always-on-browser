import os
import urllib.request

try:
    # 1. Target URL
    target_url = "https://altare.gg"
    
    # 2. Extract your saved cookies from GitHub Secrets
    altare_session = os.environ.get("ALTARE_SESSION")
    cf_clearance = os.environ.get("CF_CLEARANCE")
    
    # 3. Format the data string that your PC browser normally sends
    cookie_header = f"altare_session={altare_session}; cf_clearance={cf_clearance}"
    
    # 4. Mimic a standard Windows Chrome network request header
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Cookie": cookie_header,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5"
    }
    
    print("Sending network connection ping with credentials...")
    req = urllib.request.Request(target_url, headers=headers)
    
    # 5. Open connection channel
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        print(f"Server Response Status Code: {response.getcode()}")
        
        # Verify if page loaded successfully
        if "login" in response.geturl().lower():
            print("Status: Session expired or blocked. Re-routing back to login wall.")
        else:
            print("Success! Connection established and AFK session renewed successfully.")

except Exception as e:
    print(f"An execution issue occurred: {e}")
