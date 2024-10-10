import undetected_chromedriver as uc

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time
# buat driver

driver = uc.Chrome()

# buka url

driver.get('https://dashboard-shoecraft.vercel.app')

# time delay biar web keload sempurna dlu

WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".text-center.text-2xl.font-medium.mb-10")))

isLogin = False if driver.find_element(By.CSS_SELECTOR, ".text-center.text-2xl.font-medium.mb-10").text == "Login" else True



admin_account = {
   "email" : "email harap rubah disini",
   "password" : "password harap rubah disini"
}




if not isLogin :
   inputEmailElement=driver.find_element(By.NAME, "email")
   inputEmailElement.send_keys(admin_account["email"])

   inputPasswordElement=driver.find_element(By.NAME,"password")
   inputPasswordElement.send_keys(admin_account['password'])

   # Tunggu sampai tombol login terlihat dan bisa diklik, kemudian klik
   buttonLoginElement = WebDriverWait(driver, 10).until(
     EC.element_to_be_clickable((By.TAG_NAME, "button"))
     )
   buttonLoginElement.click()

   time.sleep(5)

   try :
      alert = WebDriverWait(driver,10).until(EC.alert_is_present())
      alert.accept()
      print("alert di klik enter")
      time.sleep(5)

   except :
      print("Tidak ada alert yang muncul")


time.sleep(3)

isOnDashboardPage = True if driver.find_element(By.TAG_NAME,"h2").text == "All Data" else False

rows = driver.find_elements(By.CSS_SELECTOR,"table.min-w-full tbody tr")
products = []
time.sleep(3)

if isOnDashboardPage :
    # proses scraping
   for row in rows:
      thumbnail_img = row.find_element(By.CSS_SELECTOR, "td img").get_attribute("src")
      name = row.find_element(By.CSS_SELECTOR, "td h3").text
      price = row.find_element(By.CSS_SELECTOR, "td p").text

      product = {
         'thumbnail_img' : thumbnail_img,
         'name' : name,
         'price' : price
      }

      products.append(product)

with open('scraping_data.json','w') as f:
   json.dump(products,f,indent=4)

print("scraping success")


print(isLogin)
