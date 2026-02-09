import dearpygui.dearpygui as dpg
from config import PRESETS
import timer

def setup_gui():
    with dpg.window(tag="Window"):
        with dpg.group():
            dpg.add_text(default_value="Presets:")
            dpg.add_listbox(
                tag="presets",
                items=list(PRESETS.keys()),
                default_value="25|5",
                width=45
            )

        with dpg.group():
            dpg.add_text(default_value="Time:", before="start")
            dpg.add_text(default_value="00:00", tag="time")

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
            dpg.add_button(
                label="Pause",
                tag="pause_btn",
                callback=handle_pause,
                width=100,
                height=50
            )
            dpg.add_button(
                label="Resume",
                tag="resume_btn",
                callback=handle_resume,
                width=100,
                height=50,
                show=False
            )
            
def replace_button(
        btn_to_replace_tag: str,
        btn_to_insert_tag: str      
):
    dpg.hide_item(btn_to_replace_tag)
    dpg.show_item(btn_to_insert_tag)

def handle_start():
    replace_button("start_btn", "stop_btn")
    dpg.configure_item("presets", enabled=False)
    timer.start_timer()

def handle_stop():
    replace_button("stop_btn", "start_btn")
    timer.stop_timer()
    dpg.configure_item("presets", enabled=True)
    dpg.set_value("time", "00:00")
    
def handle_pause():
    replace_button("pause_btn", "resume_btn")
    
def handle_resume():
    replace_button("resume_btn", "pause_btn")

    