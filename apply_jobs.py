from selenium.webdriver.firefox.service import Service
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from gemini_api import bard_flash_response
import time
import csv


driver_path = "Specify the path to the geckodriver executable"
binary = "C:\\Program Files\\Mozilla Firefox\\firefox.exe" # Specify the path to the Firefox binary
profile_path = "Specify the path to the Firefox profile"

service = Service(driver_path)

options = Options()
options.binary_location = binary

profile = FirefoxProfile(profile_path)

options.profile = profile

driver = webdriver.Firefox(service=service, options=options)

# driver.get('https://www.naukri.com/job-listings-python-backend-developer-adfolks-kochi-1-to-3-years-050624502539?src=simJobDeskACP&sid=17179253862752649&xp=9&px=1')

wait = WebDriverWait(driver, 10)

time.sleep(3)

already_applied_elements = driver.find_elements(By.ID, "already-applied")

csv_file = "jobs.csv"

status = True
maxcount=500

applied = 0  # Count of jobs applied sucessfully
failed = 0  # Count of Jobs failed

with open(csv_file, 'r') as file:
    joblink = csv.reader(file)
    for i in joblink:
        driver.get(f"https://www.naukri.com{i[0]}")
        time.sleep(3)
        status = True
        try:
            already_applied_elements = driver.find_elements(By.ID, "already-applied")
            # alert_elements = driver.find_elements(By.XPATH,
            #                                       "//div[contains(@class, 'styles_alert-message-text') and contains(text(), 'expired')]")
            # print(alert_elements)
            if already_applied_elements:
                continue


            alert_elements = driver.find_elements(By.XPATH, "//*[contains(@class, 'styles_alert-message-text__')]")

            if alert_elements:
                continue

            company_site_buttons = driver.find_elements(By.ID, "company-site-button")
            jd_container_elements = driver.find_elements(By.CLASS_NAME, "jdContainer")

            if company_site_buttons:
                continue
            elif driver.find_elements(By.CLASS_NAME, "jdContainer"):
                continue

        except:
            alert_message = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[contains(@class, 'styles_alert-message-text')]"))
            )
            if alert_message.text:
                continue

        if applied <= maxcount:
            try:
                if already_applied_elements:
                    continue
                driver.find_element(By.XPATH, "//*[text()='Apply']").click()
                # time.sleep(3)

                success_message = WebDriverWait(driver, 3).until(
                    EC.presence_of_element_located((By.XPATH,"//span[contains(@class, 'apply-message') and contains(text(), 'successfully applied')]")))
                print("Successfully applied.")
                time.sleep(3)
                if success_message:
                    continue

            except Exception as e:
                print(f"Error during initial apply attempt: {e}")
            while status:
                try:

                    radio_buttons = WebDriverWait(driver, 1).until(
                        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".ssrc__radio-btn-container"))
                    )


                    question = driver.find_element(By.XPATH, "//li[contains(@class, 'botItem')]/div/div/span").text
                    print(question)

                    options = []
                    for index, button in enumerate(radio_buttons, start=1):
                        label = button.find_element(By.CSS_SELECTOR, "label")
                        value = button.find_element(By.CSS_SELECTOR, "input").get_attribute("value")
                        options.append(f"{index}. {label.text} (Value: {value})")
                        print(options[-1])

                    options_str = "\n".join(options)
                    user_input_message = f"{question}\n{options_str}"

                    selected_option = int(bard_flash_response(user_input_message))


                    selected_button = radio_buttons[selected_option - 1].find_element(By.CSS_SELECTOR, "input")
                    driver.execute_script("arguments[0].click();", selected_button)

                    # selected_button.click()

                    save_button = wait.until(
                        EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[1]/div[3]/div/div")))
                    save_button.click()

                    success_message = WebDriverWait(driver, 3).until(
                        EC.presence_of_element_located((By.XPATH,
                                                        "//span[contains(@class, 'apply-message') and contains(text(), 'successfully applied')]")))
                    if success_message:
                        status = False

                except Exception as e:
                    print(f"Error during radio button selection or saving: {e}")
                    try:

                        chat_list = WebDriverWait(driver, 1).until(
                            EC.presence_of_element_located((By.XPATH, "//ul[contains(@id, 'chatList_')]"))
                        )


                        li_elements = chat_list.find_elements(By.TAG_NAME, "li")

                        last_question_text = None

                        if li_elements:
                            last_li_element = li_elements[-1]
                            last_question_text = last_li_element.text
                            print("Last question text:", last_question_text)
                        else:
                            print("No <li> elements found.")


                        # question_element = driver.find_element(By.XPATH, "//li[@class='botItem chatbot_ListItem']//div[@class='botMsg msg']//")
                        # question_text = question_element.text
                        # print("Question:", question_text)

                        response = bard_flash_response(last_question_text)
                        input_field = driver.find_element(By.XPATH, "//div[@class='textArea']")


                        if last_question_text == "Date of Birth":

                            dob = WebDriverWait(driver, 3).until(
                                EC.presence_of_element_located((By.XPATH, "//ul[contains(@id, 'dob__input-container')]"))
                            )
                            dob.send_keys("68767868")

                        if response:
                            input_field.send_keys(response)
                        else:
                            input_field.send_keys("None")
                            print("No response from bard_flash_response.")
                        time.sleep(1)


                        # save_button = input_field.find_element(By.XPATH, "./following-sibling::button[text()='Save']")
                        save_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[1]/div[3]/div/div")))


                        save_button.click()


                        # wait.until(EC.staleness_of(question_element))

                        apply_status_header = driver.find_elements(By.XPATH,"//div[contains(@class, 'apply-status-header') and contains(@class, 'green')]")

                        success_message = WebDriverWait(driver, 3).until(
                            EC.presence_of_element_located((By.XPATH,
                                                            "//span[contains(@class, 'apply-message') and contains(text(), 'successfully applied')]")))
                        if success_message:
                            status = False

                        if apply_status_header:
                            print("The element exists.")

                        else:
                            print("The element does not exist.")
                    except Exception as e:
                        if already_applied_elements:
                            status = False
                        elif driver.find_elements(By.XPATH,"//div[contains(@class, 'apply-status-header') and contains(@class, 'green')]"):
                            continue
                        print(f"Error during fallback procedure: {e}")
                    finally:

                        success_message_elements = driver.find_elements(By.XPATH,
                                                                        "//span[contains(@class, 'apply-message') and contains(text(), 'You have successfully applied')]")


                        if success_message_elements:
                            status = False


# Close the browser
driver.quit()
