from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
import time

def main():
    try:
        # Initialize the browser
        driver = webdriver.Chrome()

        # Maximize the window
        driver.maximize_window()

        # Navigate to Google
        print("Navigating to Google...")
        driver.get("https://www.google.com")

        # Search with the keyword "Test Auto"
        print("Performing search...")
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("Test Auto")
        search_box.send_keys(Keys.RETURN)

        # Wait for a moment for the search results
        time.sleep(2)

        # Click on the "Images" tab
        try:
            images_tab = driver.find_element(By.XPATH, "//a[text()='Images']")
            images_tab.click()
            print("Clicked on the 'Images' tab.")
        except NoSuchElementException:
            print("The 'Images' tab could not be found.")
            pass

        # Wait for a moment for the images to load
        time.sleep(2)
        images = driver.find_elements(By.XPATH, "//img[contains(@src, 'http')]")
        assert len(images) > 0, "No images found on the page."
        print(f"Found {len(images)} images on the page.")

        # Take a screenshot
        driver.save_screenshot("screenshot.png")
        print("Screenshot saved successfully.")

    except ElementNotVisibleException as e:
        print("An element was not visible:", e)

    finally:
        # Close the browser
        driver.quit()
        print("Browser closed successfully.")

if __name__ == "__main__":
    main()
