from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup Chrome driver
options = Options()
# options.add_argument("--headless")  # Uncomment to run headless
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(
    service=Service("/Users/noahiarrobino/Desktop/chromedriver"),
    options=options
)

try:
    wait = WebDriverWait(driver, 15)

    # 1. Open Cymbal Shops homepage
    driver.get("https://cymbal-shops.retail.cymbal.dev/")
    print("✅ Opened Cymbal Shops homepage")

    # 2. Wait for products to load
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "hot-product-card")))
    print("🛍️ Product cards loaded")

    # 3. Click the first product
    first_product = driver.find_element(By.CSS_SELECTOR, ".hot-product-card a")
    product_name = driver.find_element(By.CSS_SELECTOR, ".hot-product-card-name").text
    first_product.click()
    print(f"🔗 Clicked on product: {product_name}")

    # 4. Wait for Add to Cart button and click it
    add_to_cart = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.cymbal-button-primary"))
    )
    add_to_cart.click()
    print("🛒 Added to cart")

    time.sleep(1)  # Small buffer to let the cart update

    # 5. Navigate to cart
    driver.get("https://cymbal-shops.retail.cymbal.dev/cart")
    print("🧾 Navigated to cart")

    # 6. Read total from cart
    price_elem = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(text(), 'Total')]/following-sibling::div[1]")
        )
    )
    total_text = price_elem.text.strip()
    print(f"💰 Cart total: {total_text}")

    # 7. Screenshot the cart
    driver.save_screenshot("cymbal_cart_test.png")
    print("📸 Screenshot saved as cymbal_cart_test.png")

    # 8. Pass/fail based on presence of $
    if "$" in total_text:
        print("✅ PASS: Cart total found")
    else:
        print("❌ FAIL: Cart total missing")

finally:
    driver.quit()