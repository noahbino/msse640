from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://cymbal-shops.retail.cymbal.dev/")
print("✅ Opened homepage")

# Scroll to the bottom to ensure footer loads
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)  # Allow time for lazy-loaded footer

try:
    # Check for footer presence
    footer = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "footer"))
    )
    print("✅ Footer is present")

    # Optional: Print a portion of the footer text
    print("📄 Footer text:", footer.text[:100], "...")

except Exception as e:
    print("❌ Footer not found:", e)

driver.quit()