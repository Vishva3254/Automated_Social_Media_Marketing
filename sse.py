from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

def perplexity_search(query):

    driver = webdriver.Chrome()
    driver.minimize_window()
    
       
    query_row = []
    sse = "Perplexity"
    query_row.append(sse)
    driver.get("https://www.perplexity.ai/")
    
    search_box = driver.find_element(By.TAG_NAME, "textarea")
    search_box.send_keys(query)
    search_box.send_keys(Keys.ENTER)
    time.sleep(15)
    
    try:
        result_div = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.break-words"))
        )
        
        ans = result_div.text
        print("DONE")
        print(ans)
        return ans
        
        
    except Exception as e:
        print("Error:", e)

    finally:
        driver.quit()

user = input("Specify the platform name/names : ")
query = f"What are the top trending topics on {user} right now? Please provide a summary of the content related to each trend, including relevant links and images.And note that I wwant all the content in python list format."
perplexity_search(query)