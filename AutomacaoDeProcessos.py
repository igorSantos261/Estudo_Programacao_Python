import pyautogui
import time



#pyautogui.KEYBOARD_KEYS


pyautogui.alert("Codigo de Automação Inicializado")
pyautogui.PAUSE = 0.5
# Abrir o google no meu Computador
pyautogui.press("winleft")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(1)
pyautogui.write("https://drive.google.com/drive/my-drive")
pyautogui.press("enter")

#Entrar na minha área de Trabalho
pyautogui.hotkey("winleft", "d")
