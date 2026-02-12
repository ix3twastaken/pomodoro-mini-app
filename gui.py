import dearpygui.dearpygui as dpg

import timer
from config import WORK_TIME, REST_TIME
from utils.sys_utils import get_file_path

def setup_default_font():
    with dpg.font_registry():
        with dpg.font(file=get_file_path("Eitai.otf", __file__), 
                      size=18, 
                      default_font=True
                      ) as font_id:
            dpg.bind_font(font_id)
    

def setup_theme():
    with dpg.theme() as global_theme:
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 10)
            dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 1)    
    dpg.bind_theme(global_theme)
    
def setup_gui():
    with dpg.window(tag="Window"):
        with dpg.group():
            dpg.add_text(default_value="Work time")
            dpg.add_listbox(
                tag="work_time_presets",
                items=list(WORK_TIME.keys()),
                default_value="25",
                width=45
            )
            dpg.add_text(default_value="Rest time")
            dpg.add_listbox(
                tag="rest_time_presets",
                items=list(REST_TIME.keys()),
                default_value="5",
                width=45
            )

        with dpg.group():
            dpg.add_text(default_value="Time")
            dpg.add_text(default_value="00:00", 
                         tag="time"
                        )       

        with dpg.group():
            dpg.add_button(
                label="Start",
                tag="start_btn",
                callback=handle_start,
                width=100,
                height=50
            )
            dpg.add_button(
                label="Stop",
                tag="stop_btn",
                callback=handle_stop,
                width=100,
                height=50,
                show=False
            )          
            
def listbox_toggle(
        listbox_tag: str, 
        flag: bool
):
    dpg.configure_item(listbox_tag, enabled=flag)          

def replace_button(
        btn_to_replace_tag: str,
        btn_to_insert_tag: str      
):
    dpg.hide_item(btn_to_replace_tag)
    dpg.show_item(btn_to_insert_tag)

def handle_start():
    replace_button("start_btn", "stop_btn")
    listbox_toggle("work_time_presets", False)
    listbox_toggle("rest_time_presets", False)
    timer.start_timer()

def handle_stop():
    replace_button("stop_btn", "start_btn")
    timer.stop_timer()
    listbox_toggle("work_time_presets", True)
    listbox_toggle("rest_time_presets", True)
    dpg.set_value("time", "00:00")