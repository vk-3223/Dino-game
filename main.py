from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from PIL import Image,ImageGrab
import pyautogui

url = "https://elgoog.im/t-rex/"
chrome_driver_path = r"CHROME_DRIVER_PATH"
header ={
    "Accept-Language":"en-US,en;q=0.9,hi;q=0.8",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
}

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url=url)
start = driver.find_element_by_xpath('/html/body')
time.sleep(2)



def click(key):
    pyautogui.keyDown(key)
    return

def isCollision(data):

    for i in range(530,560):
        for j in range(80, 127):
            if data[i, j] < 171:
                start = driver.find_element_by_xpath('/html/body')
                start.send_keys(Keys.DOWN)
                return

    for i in range(530, 625):
        for j in range(135, 160):
            if data[i, j] < 95:
                start.send_keys(Keys.UP)
                return
    return

if __name__ == "__main__":
    
    start.send_keys(Keys.SPACE)
    time.sleep(5)
    click('up') 
    
    while True:
        image = ImageGrab.grab().convert('L')  
        data = image.load()
        isCollision(data)