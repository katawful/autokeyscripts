import time
winTitle="Object Window"
winClass="tesconstructionset.exe.Wine"
window.activate(winTitle, switchDesktop=False, matchClass=False)
time.sleep(0.1)
mouse.click_relative(80, 20, 1)
