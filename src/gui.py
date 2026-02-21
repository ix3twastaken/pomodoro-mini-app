import dearpygui.dearpygui as dpg
import os
import timer
from themes import create_theme_imgui_dark, create_theme_imgui_light
from config import *
from utils.sys_utils import get_file_path

font_path = get_file_path("assets\\Eitai.otf")
print(font_path)

def theme_callback(sender, app_data, user_data):
    if user_data == "light":
        dpg.bind_theme(create_theme_imgui_light())
    else:
        dpg.bind_theme(create_theme_imgui_dark())

def setup_default_font():
    with dpg.font_registry():
        with dpg.font(file=font_path, size=18, default_font=True) as default_font:
            pass
        dpg.bind_font(default_font)

def setup_default_theme():
    dpg.bind_theme(create_theme_imgui_dark())
    
def setup_gui():
    with dpg.window(tag="Window"):
        with dpg.menu_bar(tag="menu_bar"):
            with dpg.menu(label="Themes", tag="themes_menu"):
                dpg.add_menu_item(label="Dark", callback=theme_callback, user_data="dark")
                dpg.add_menu_item(label="Light", callback=theme_callback, user_data="light")
        
        with dpg.group(tag="time_block", horizontal=False):
            dpg.add_separator()
            dpg.add_spacer(height=10)   
            dpg.add_text(default_value="Time", 
                         tag="time_label",
                         indent=132
                         )
            dpg.add_text(default_value="00:00", 
                         tag="time",
                         indent=128
                         )
            dpg.add_spacer(height=10)   
            dpg.add_separator()
            dpg.add_spacer(height=10)
        
        with dpg.table(tag="presets_table", header_row=False, borders_outerH=False, borders_outerV=False, borders_innerH=False, borders_innerV=False):
            dpg.add_table_column(tag="col_1")
            dpg.add_table_column(tag="col_2")

            with dpg.table_row(tag="row_1"):
                with dpg.group(tag="work_time_listbox"):
                    dpg.add_text(default_value="Work time",
                                 indent=24)
                    dpg.add_listbox(
                        tag="work_time_presets",
                        items=list(WORK_TIME.keys()),
                        default_value="25",
                        width=152
                    )
                with dpg.group(tag="rest_time_listbox"):
                    dpg.add_text(default_value="Rest time",
                                 indent=24)
                    dpg.add_listbox(
                    tag="rest_time_presets",
                    items=list(REST_TIME.keys()),
                    default_value="5",
                    width=152,
                    indent=4
                    )
                    
        dpg.add_spacer(height=10)   
        dpg.add_separator()
        dpg.add_spacer(height=10)
        
        with dpg.group(tag="start_stop_btns", horizontal=True):
            dpg.add_button(
                label="Start",
                tag="start_btn",
                callback=handle_start,
                width=318,
                height=50
            )
            dpg.add_button(
                label="Stop",
                tag="stop_btn",
                callback=handle_stop,
                width=318,
                height=50,
                show=False
            )
 
    setup_default_font() 
    setup_default_theme()
            
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