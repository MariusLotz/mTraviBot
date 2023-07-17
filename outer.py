from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
def main():
    # Configure Selenium options
    options = Options()
    options.headless = True  # Run the browser in headless mode (without UI)

    # Set path to chromedriver executable
    chromedriver_path = '/home/user/Coding/chromedriver'

    # Initialize the Chrome driver
    driver = webdriver.Chrome(service=Service(chromedriver_path), options=options)

    try:
        # Seite aufrufen
        driver.get("https://ts2.x1.international.travian.com/logout")

        # Warten, bis das Benutzername-Feld sichtbar ist
        username_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "username"))
        
        # Benutzernamen eingeben
        username_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//tr[@class="account"]//input[@class="text"]'))
        )
        username_field.send_keys(USER_NAME)

        # Passwort eingeben
        username_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//tr[@class="pass"]//input[@class="text"]'))
        )
        username_field.send_keys(PASSWORD)

        # Warten, bis der Login-Button klickbar ist
        login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@id="button64a1c43bdfaf3"]'))
        )

        # Login-Button klicken
        login_button.click()

        # 20 Sekunden warten
        WebDriverWait(driver, 20)

    finally:
        # Quit the driver
        driver.quit()

if __name__ == "__main__":
    main()
