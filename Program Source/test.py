# Only used this code to learn, how to work with HWID.
# And YES i know about the typo!

import subprocess
import requests
import time
import os

hwid = str(str(subprocess.check_output('wmic csproduct get uuid')).strip().replace(r"\r", "").split(r"\n")[1].strip())
# r = requests.get("https://pastebin.com/raw/XWjYcTg1")
hwidList = []
for sHwid in requests.get("https://pastebin.com/raw/XWjYcTg1").text.split("\\n"):
    hwidList.append(str(sHwid))
    print(f"Added > {sHwid}")
print("Adding Done!")
print(f"HWID's:\n"
      f"        {hwidList}\n")

print(f"Your HWID: {hwid}\n"
      f"HWID List: {hwidList}")

if str(hwid) in hwidList:
    print("Access granted...")
    time.sleep(.1)
else:
    print("Error! HWID Not I Database!")
    print("Please contact (Your Discord Here) for help. HWID: " + hwid)
    os.system('pause >NUL')
