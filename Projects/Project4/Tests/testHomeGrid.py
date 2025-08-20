from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://cymbal-shops.retail.cymbal.dev/")
print("✅ Opened homepage")

wait = WebDriverWait(driver, 10)

# Updated selector: selects product links inside the product grid
products = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "main a[href^='/product/']")))

if products and len(products) > 0:
    print(f"✅ Found {len(products)} product(s) — PASS")
else:
    print("❌ No products found — FAIL")

driver.quit()