from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def main(event, context):
    search_query = "Nelson Court, Nottingham"
    gl = "IN"
    driver = webdriver.Chrome()
    driver.get(f"https://www.google.com/search?q={search_query}&gl={gl}")
    time.sleep(5)
    div_with_data_ta_slot = driver.find_elements(By.XPATH, "//div[@data-ta-slot]")
    data={}
    ctr=0
    for div in div_with_data_ta_slot:
        ctr+=1
        print(div.text)
        data[ctr]=div.text
    driver.close();
    driver.quit();

    response = {
        "statusCode": 200,
        "body": data
    }

    return response
main({}, {})