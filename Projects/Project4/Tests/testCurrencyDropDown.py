from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://cymbal-shops.retail.cymbal.dev/")
print("✅ Opened homepage")

try:
    wait = WebDriverWait(driver, 10)

    # Wait for the dropdown <select> element
    currency_select = wait.until(
        EC.presence_of_element_located((By.NAME, "currency_code"))
    )

    # Use Select to change the currency
    select = Select(currency_select)
    select.select_by_visible_text("JPY")
    print("💱 Changed currency to JPY")

except Exception as e:
    print(f"❌ Test failed: {e}")

driver.quit()