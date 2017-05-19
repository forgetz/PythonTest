import autopy
import time

time.sleep(3)
savescreen = autopy.bitmap.capture_screen().save("screen.png")
alertmsg = autopy.alert.alert("save screenshot completed!", "autopy")