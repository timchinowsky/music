import pyautogui as py import time

you'll need to adjust the x,y coordinates
based on you screen size. This is a mac
configuration.
x,y coordinates. py.displayMousePosition()
def launch_spotify(): py.hotkey('command', 'space')#'windows' py.typewrite('spotify') py.press('enter') time.sleep(10) py.hotkey('command', 'space') py.typewrite('spotify') py.click(39,512)#x,y coordinates for playlist

def play(): py.click(518,294)#play for i in range(30): time.sleep(30) py.click(690,747)#nextsong

launch_spotify() play()