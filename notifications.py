import os
from notifypy import Notify
from config import PRESETS
import dearpygui.dearpygui as dpg

def timer_notify(user_data: str):
    preset = dpg.get_value("presets")
    work_duration = PRESETS[preset][0] // 60
    chill_duration = PRESETS[preset][1] // 60
    notification = Notify()
    if user_data == "start":
        notification.title='Pomodoro'
        notification.icon=os.path.join(os.path.dirname(__file__), "icon.ico") #This icon was designed using resources from Flaticon.com.
        notification.message=f'Время работать! {work_duration} минут до перерыва'
        notification.application_name='Pomodoro'
        notification.send(block=False)
    else:
        notification.title='Pomodoro'
        notification.icon=os.path.join(os.path.dirname(__file__), "icon.ico") #This icon was designed using resources from Flaticon.com.
        notification.message=f'Время отдыхать! {chill_duration} минут перерыва'
        notification.application_name='Pomodoro'
        notification.send(block=False)
