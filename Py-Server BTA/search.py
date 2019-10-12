from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

#binary = FirefoxBinary('path/to/installed firefox binary')
#browser = webdriver.Firefox(firefox_binary=binary)

try:
    driver=webdriver.Firefox()
    driver.get("https://www.amazon.in/Low-Price-With-Free-Shipping/bbp?category=/mens&pf_rd_p=7ae8bb23-c2d2-4277-a4e5-a651d0266ae5&pf_rd_r=A5N025N8EZXQA5NPMN2E")
    
except Exception as e:
    print(str(e))
print("End of program")
