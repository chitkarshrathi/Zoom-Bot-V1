from selenium import webdriver
import time
import keyboard
import pyautogui
from pynput.keyboard import Key, Controller

Keyboard = Controller

#Add the address of the chromedriver inside the 2 commas. eg - "C:\\chromedriver.exe"
driver = webdriver.Chrome("")

driver.get("https://zoom.us")

link = driver.find_element_by_link_text("JOIN A MEETING")
link.click()

time.sleep(5)

#Please put in Meeting ID inside the 2 upper commas. eg - "11 digit meeting ID"
keyboard.write("")

pyautogui.press("enter")

time.sleep(5)

pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(10)

#Please put in the meeting password inside the 2 upper commas. eg - "pass123"
keyboard.write("")

time.sleep(3)

pyautogui.press("enter")

#You can change the time after you want to log out of the meeting by typing in the number of seconds in bracket below. Default is of 1 hour (3600 seconds)
time.sleep(3600)

pyautogui.hotkey("alt", "f4")
pyautogui.press("tab")
pyautogui.press("enter")

quit()

