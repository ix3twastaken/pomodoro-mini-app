import os

import dearpygui.dearpygui as dpg
from notifypy import Notify

from config import WORK_TIME, REST_TIME

def timer_notify(user_data: str):
    work_preset = dpg.get_value("work_time_presets")
    rest_preset = dpg.get_value("rest_time_presets")
    work_duration = WORK_TIME[work_preset] // 60
    rest_duration = REST_TIME[rest_preset] // 60
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
        notification.message=f'Время отдыхать! {rest_duration} минут перерыва'
        notification.application_name='Pomodoro'
        notification.send(block=False)
