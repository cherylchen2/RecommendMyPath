import time
import callRadar

while True:
    await time.sleep(50000)
    callRadar.callRadar()
