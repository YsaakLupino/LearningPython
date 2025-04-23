import screeninfo as si
import pyautogui as py
from pyautogui import ImageNotFoundException



#definindo area total das telas
monitors = si.get_monitors()

regions = []
for monitor in monitors:
    regiao = (monitor.x, monitor.y, monitor.width, monitor.height)
    regions.append(regiao)
    print(regiao)

img = py.locateOnScreen(r"C:\Users\YSAAK\Desktop\pedagogico.png", region=regions[0], confidence=0.75)
py.moveTo(img)