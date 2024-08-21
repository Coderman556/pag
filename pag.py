import pyautogui as pag
import timeit as ti
import time as t

try:
    i = 0
    start = ti.default_timer()
    while True:
        # pag.move(0,50)
        # pag.move(0,-50)
        pag.click()
        t.sleep(60)
        i+=1
        print(f"moved! {i} times")

except KeyboardInterrupt:
    print(f"stopped due to manual cancellation.")

finally:
    stop = ti.default_timer()
    print(f"Program has been up for {stop - start}")