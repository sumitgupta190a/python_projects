# # pip install pywhatkit
# import pywhatkit
# pywhatkit.sendwhatmsg('+917024036191', 'hello draupati this msg is not by me this msg is send by python', 22, 11)


# pip install pyautogui
import pyautogui
import time
time.sleep(5)
count = 0
while count <= 10:
    pyautogui.typewrite('hello dwaupati ' + str(count))
    pyautogui.press("enter")
    count = count + 1

    