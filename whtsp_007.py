import pyautogui as spam
import time

limit = input("Enter no. of messages")
msg = input("Message you want to send")

i = 0

time.sleep(5)

while i<int(limit):

    spam.typewrite(msg)
    spam.press("Enter")

    i+=1
