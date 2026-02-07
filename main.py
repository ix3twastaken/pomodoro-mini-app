import dearpygui.dearpygui as dpg
from plyer import notification
import time, threading

timer_stop = False
PRESETS = {"25|5": (1500, 300), "30|10": (1800, 600), "45|15": (2700, 900)}

def main():
    dpg.create_context()
    dpg.create_viewport(title = 'Pomodoro', 
                        max_width = 200,
                        max_height = 250,
                        min_width = 200, 
                        min_height = 250)
    
    
    with dpg.window(tag="Window"):
        with dpg.group():
            dpg.add_text(default_value="Presets:")
            dpg.add_listbox(tag = "presets",
                            items = ["25|5", "30|10", "45|15"],
                            default_value = "25|5",
                            user_data = ["25", "30,", "45"],
                            width = 45)
        
        with dpg.group() as Timer:
            dpg.add_text(default_value = "Time:", before="start")
            dpg.add_text(default_value = "00:00", tag = "time")
            
        with dpg.group() as StartStopButtons:
            dpg.add_button(label = "Start",
                           tag = "start", 
                           callback = button_callback, 
                           user_data = "start", 
                           width = 100, 
                           height = 50)
            
            dpg.add_button(label = "Stop", 
                           tag = "stop",
                           callback = button_callback, 
                           user_data = "stop", 
                           width = 100, 
                           height = 50,
                           show = False)
    
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("Window", True)  
    dpg.start_dearpygui()
    dpg.destroy_context()

def timer(seconds):
    end_time = round(time.time()) + seconds 
    while not timer_stop:
        current_time = round(time.time())
        remaining_time = end_time - current_time
        mins = remaining_time // 60
        secs = remaining_time % 60
         
        dpg.set_value(item = "time", value = f"{mins}.{secs}")
        if remaining_time == 0:
            timer_notify("stop")
            break
            
        dpg.render_dearpygui_frame()
    
def stop_timer():
    global timer_stop
    timer_stop = True
    
def start_timer():
    global timer_stop
    timer_stop = False
    preset = dpg.get_value("presets")
    duration = PRESETS[preset][0]
    current_thread = threading.Thread(target=timer, args=(duration,))
    current_thread.daemon = True
    current_thread.start()
    timer_notify("start")

def swap_start_and_stop_btns(user_data):
    '''
    Swaps "Start" button to "Stop" button and vice versa
    '''
    if user_data == "start":
        dpg.hide_item(user_data)
        dpg.show_item("stop")
        
        start_timer()
    elif user_data == "stop":
        dpg.hide_item(user_data)
        dpg.show_item("start")
        stop_timer()
        dpg.set_value(item="time", value="00:00")
        
def timer_notify(user_data: str):
    preset = dpg.get_value("presets")
    work_duration = (PRESETS[preset][0]) // 60
    chill_duration = (PRESETS[preset][1]) // 60
    if user_data == "start":
        notification.notify(
        title='🍅 Pomodoro',
        message=f'Время работать! {work_duration} минут до перерыва',
        app_name='Pomodoro Timer',     
        # app_icon='test.ico',           
        timeout=2)                      
    else:
        notification.notify(
        title='🍅 Pomodoro',
        message=f'Время отдыхать! {chill_duration} минут перерыва',
        app_name='Pomodoro Timer',
        # app_icon='test.ico',
        timeout=2)
             
def button_callback(sender, app_data, user_data):
    swap_start_and_stop_btns(user_data)


if __name__ == "__main__":
    main()