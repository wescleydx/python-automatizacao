import pyautogui
import time

def proc_third():
    print ('Teste')
    pyautogui.click(x= 516, y= 879)
    time.sleep(5)
    pyautogui.click(x= 98, y= 381)
    time.sleep(5)
    pyautogui.click(x= 319, y= 131)
    time.sleep(5)
    pyautogui.doubleClick(x= 409, y=125)
    time.sleep(5)
    pyautogui.doubleClick(x= 178, y= 384)
    pyautogui.keyDown('ctrl')
    pyautogui.press('c')
    pyautogui.keyUp('ctrl')
    pyautogui.click(x= 564, y= 877)
    time.sleep(5)
    pyautogui.click(x= 375, y= 36)
    time.sleep(5)
    pyautogui.click(x= 379, y= 119)
    time.sleep(5)
    pyautogui.click(x= 523, y= 225)
    time.sleep(5)
    pyautogui.doubleClick(x= 330, y= 202)
    time.sleep(5)
    pyautogui.press('f9')
    time.sleep(5)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.click(x= 570, y= 202)
    pyautogui.keyDown('ctrl')
    pyautogui.press('v')
    pyautogui.keyUp('ctrl')
    pyautogui.click(x= 1031, y= 248)
    pyautogui.click(x= 993, y= 629) #Se tiver em branco, terá que cancelar, caso continue, ele fará a linha seguinte
    pyautogui.click(x= 881, y= 519)