import os
from plyer import notification
from config import PRESETS
import dearpygui.dearpygui as dpg

def timer_notify(user_data: str):
    preset = dpg.get_value("presets")
    work_duration = PRESETS[preset][0] // 60
    chill_duration = PRESETS[preset][1] // 60
    
    if user_data == "start":
        notification.notify(
            title='Pomodoro',
            app_icon=os.path.join(os.path.dirname(__file__), "tomato.ico"), #This icon was designed using resources from Flaticon.com.
            message=f'Время работать! {work_duration} минут до перерыва',
            app_name='Pomodoro Timer'
        )
    else:
        notification.notify(
            title='Pomodoro',
            app_icon=os.path.join(os.path.dirname(__file__), "tomato.ico"), #This icon was designed using resources from Flaticon.com.
            message=f'Время отдыхать! {chill_duration} минут перерыва',
            app_name='Pomodoro Timer'
        )