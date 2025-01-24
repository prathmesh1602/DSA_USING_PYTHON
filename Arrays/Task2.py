from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

# LinkedIn login function
def linkedin_login(driver, username, password):
    driver.get("https://www.linkedin.com/login")
    time.sleep(2)
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(3)

# Function to scrape profiles
def scrape_profiles(driver, search_url):
    driver.get(search_url)
    time.sleep(5)

    profiles_data = []

    # Loop through profiles on the page
    profiles = driver.find_elements(By.CSS_SELECTOR, ".entity-result__content")
    for profile in profiles:
        try:
            name = profile.find_element(By.CSS_SELECTOR, ".entity-result__title-text a span").text
            job_title = profile.find_element(By.CSS_SELECTOR, ".entity-result__primary-subtitle").text
            company = profile.find_element(By.CSS_SELECTOR, ".entity-result__secondary-subtitle").text
            profiles_data.append({
                "Name": name,
                "Job Title": job_title,
                "Company": company,
            })
        except Exception as e:
            print(f"Error extracting data: {e}")
    
    return profiles_data

# Main script
def main():
    # Configure Selenium WebDriver
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    service = Service("path_to_chromedriver")  # Replace with your chromedriver path
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Login credentials
    username = "your_email@example.com"  # Replace with your LinkedIn email
    password = "your_password"           # Replace with your LinkedIn password

    try:
        # Login to LinkedIn
        linkedin_login(driver, username, password)

        # Search URL for IIT graduates (replace with your specific search)
        search_url = "https://www.linkedin.com/search/results/people/?keywords=IIT&origin=SWITCH_SEARCH_VERTICAL"

        # Scrape profiles
        profiles_data = scrape_profiles(driver, search_url)

        # Save to CSV
        if profiles_data:
            df = pd.DataFrame(profiles_data)
            df.to_csv("linkedin_profiles.csv", index=False)
            print("Scraped data saved to linkedin_profiles.csv")
        else:
            print("No profiles found.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
