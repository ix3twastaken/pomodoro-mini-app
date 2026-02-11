import time
import threading
from config import WORK_TIME, REST_TIME
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
                duration = get_preset("rest_time_presets")
                timer(duration)
            else:
                timer_loop = True
                timer_notify("start")
                duration = get_preset("work_time_presets")
                timer(duration)
            break

        time.sleep(0.1)

def get_preset(listbox_tag: str) -> int:
    listbox_value = dpg.get_value(listbox_tag)
    if listbox_tag == "work_time_presets":
        return WORK_TIME[listbox_value]
    elif listbox_tag == "rest_time_presets":
        return REST_TIME[listbox_value]

def start_timer():
    global timer_stop, timer_loop
    timer_stop = False
    timer_loop = True
    duration = get_preset("work_time_presets")
    current_thread = threading.Thread(target=timer, 
                                      args=(duration,),
                                      daemon=True
                                      )
    current_thread.start()
    timer_notify("start")

def stop_timer():
    global timer_stop
    timer_stop = True