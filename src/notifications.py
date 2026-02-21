import dearpygui.dearpygui as dpg
from notifypy import Notify
from utils.sys_utils import get_file_path

from config import WORK_TIME, REST_TIME

def timer_notify(user_data: str):
    work_preset = dpg.get_value("work_time_presets")
    rest_preset = dpg.get_value("rest_time_presets")
    work_duration = WORK_TIME[work_preset] // 60
    rest_duration = REST_TIME[rest_preset] // 60
    notification = Notify()
    if user_data == "start":
        notification.title='Pomodoro'
        notification.icon=get_file_path("icon.ico") 
        notification.message=f'Время работать! {work_duration} минут до перерыва'
        notification.application_name='Pomodoro'
        notification.send(block=False)
    else:
        notification.title='Pomodoro'
        notification.icon=get_file_path("icon.ico")
        notification.message=f'Время отдыхать! {rest_duration} минут перерыва'
        notification.application_name='Pomodoro'
        notification.send(block=False)
