import time
import threading
from config import TimeUnit, PRESETS
from notifications import timer_notify
import dearpygui.dearpygui as dpg

timer_stop = False
timer_loop = False

def timer(seconds):
    global timer_stop, timer_loop
    end_time = round(time.time()) + seconds
    while not timer_stop:
        current_time = round(time.time())
        remaining_time = end_time - current_time
        mins = remaining_time // 60
        secs = remaining_time % 60

        dpg.set_value("time", f"{mins}.{secs}")
        if remaining_time <= 0:
            if timer_loop:
                timer_loop = False
                timer_notify("stop")
                duration = get_preset(TimeUnit.CHILLTIME)
                timer(duration)
            else:
                timer_loop = True
                timer_notify("start")
                duration = get_preset(TimeUnit.WORKTIME)
                timer(duration)
            break

        time.sleep(0.1)

def get_preset(unit: TimeUnit) -> int:
    preset = dpg.get_value("presets")
    index = 0 if unit == TimeUnit.WORKTIME else 1
    return PRESETS[preset][index]

def start_timer():
    global timer_stop, timer_loop
    timer_stop = False
    timer_loop = True
    duration = get_preset(TimeUnit.WORKTIME)
    current_thread = threading.Thread(target=timer, 
                                      args=(duration,),
                                      daemon=True
                                      )
    current_thread.start()
    timer_notify("start")

def stop_timer():
    global timer_stop
    timer_stop = True