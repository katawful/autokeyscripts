import time
winPref="Preferences"
winRef="Choose Reference"
winMain="TES Construction Set *"
window.activate(winPref, switchDesktop=False, matchClass=False)
if window.wait_for_focus(winPref, timeOut=0.5):
    time.sleep(0.1)
    mouse.click_relative(200, 170, 1)
    time.sleep(0.1)
    window.activate(winRef, switchDesktop=False, matchClass=False)
    mouse.click_relative(200, 30 ,1)
    exit()
else:
    window.activate(winMain, switchDesktop=False, matchClass=False)
    time.sleep(0.1)
    mouse.click_relative(80, 30, 1)
    mouse.click_relative(80, 30, 1)
    time.sleep(0.1)
    window.activate(winPref, switchDesktop=False, matchClass=False)
    time.sleep(0.1)
    mouse.click_relative(200, 170, 1)
    time.sleep(0.1)
    window.activate(winMain, switchDesktop=False, matchClass=False)
    mouse.click_relative(200, 30, 1)
    exit()