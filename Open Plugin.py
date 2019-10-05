import time
winTitle="TES Construction Set *"
winClass="tesconstructionset.exe.Wine"
winData="Data"
#window.wait_for_focus(winTitle, timeOut=0.2)
window.activate(winTitle, switchDesktop=False, matchClass=False)
time.sleep(0.2)
mouse.click_relative(40, 30, 1)
mouse.click_relative(40, 30, 1)
#mouse.click_relative(40, 30, 1)
#time.sleep(0.1)
window.activate(winClass, switchDesktop=False, matchClass=True)
mouse.click_absolute(-500, -400, 1)


#window.wait_for_focus(winTitle*, timeout=0.2)
#window.activate(winTitle*, switchDesktop=False, matchClass=False)
#time.sleep(0.5)
#mouse.click_relative(80, 40, 1)