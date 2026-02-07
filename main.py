import dearpygui.dearpygui as dpg
from plyer import notification

PRESETS = {"25|5": (1500, 300), "30|10": (1800, 600), "45|15": (3300, 900)}

def main():
    dpg.create_context()
    dpg.create_viewport(title = 'Pomodoro', 
                        max_width = 200,
                        max_height = 200,
                        min_width = 200, 
                        min_height = 200)
    
    with dpg.window(tag="Primary Window"):
        with dpg.group():
            dpg.add_text(default_value="Presets:")
            dpg.add_listbox(tag = "presets",
                            items = ["25|5", "30|10", "45|15"],
                            default_value = "25|5",
                            callback = on_listbox_change,
                            width = 45)
        
        with dpg.group():
            dpg.add_text(default_value = "Time:", before="start")
            dpg.add_text(default_value = "00:00")

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
    dpg.set_primary_window("Primary Window", True)
    dpg.start_dearpygui()
    dpg.destroy_context()

def on_listbox_change(sender, app_data):
    print(f"listbox selected: {app_data}")


def swap_start_and_stop_btns(user_data):
    '''
    Swaps "Start" button to "Stop" button and vice versa
    '''
    if user_data == "stop":
        dpg.hide_item(item = user_data)
        dpg.show_item(item = "start")
    elif user_data == "start":
        dpg.hide_item(item = user_data)
        dpg.show_item(item = "stop")
        timer_start_or_stop_notify(user_data)
        
def timer_start_or_stop_notify(user_data):
    if user_data == "start":
        notification.notify(
        title='🍅 Pomodoro',
        message='Время работать! 25 минут до перерыва',
        app_name='Pomodoro Timer',     
        app_icon='D:/Programming/Files/pomodoro-mini-app/test.ico',           
        timeout=2)                      
    else:
        notification.notify(
        title='🍅 Pomodoro',
        message='Время отдыхать! 5 минут перерыва',
        app_name='Pomodoro Timer',
        app_icon='D:/Programming/Files/pomodoro-mini-app/test.ico',
        timeout=2)
             
def button_callback(sender, app_data, user_data):
    swap_start_and_stop_btns(user_data)


if __name__ == "__main__":
    main()