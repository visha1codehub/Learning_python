from datetime import datetime
import time


while True:
    now1 = datetime.now().time() 
    print(now1,end="\r")
    time.sleep(1)


