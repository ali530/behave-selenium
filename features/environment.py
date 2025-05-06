from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import logging


def before_scenario(context, scenario):
    if 'ui' in scenario.tags:
        options = Options()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")


        # Creating temp folders for the container 
        safe_name = scenario.name.replace(" ", "_").replace("/", "_")
        user_data_dir = f"/tmp/chrome_profile_{os.getpid()}_{safe_name}"
        os.makedirs(user_data_dir, exist_ok=True)
        options.add_argument(f"--user-data-dir={user_data_dir}")

        context.driver = webdriver.Chrome(options=options)

        # Open SDAIA website
        context.driver.get("https://sdaia.gov.sa/en/default.aspx")

        # Accept cookies if popup appears, otherwise ignore it
        try:
            WebDriverWait(context.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@data-sm-button-text='Approve']"))
            ).click()
        except:
            pass 

def after_scenario(context, scenario):
    # Taking screenshots if the scenario failed 
    if hasattr(context, 'driver'):
        if scenario.status == "failed":
            screenshots_dir = "screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)
            screenshot_path = os.path.join(screenshots_dir, f"{scenario.name}.png")
            context.driver.save_screenshot(screenshot_path)
            print(f"Scenario failed. Screenshot saved to: {screenshot_path}")
        context.driver.quit()

    
logging.basicConfig(
    # Format the logs 
    level=logging.INFO,
    format="[%(levelname)s] %(message)s",
)
