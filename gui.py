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
                tag="start",
                callback=handle_start,
                width=100,
                height=50
            )
            dpg.add_button(
                label="Stop",
                tag="stop",
                callback=handle_stop,
                width=100,
                height=50,
                show=False
            )

def handle_start():
    dpg.hide_item("start")
    dpg.show_item("stop")
    dpg.configure_item("presets", enabled=False)
    timer.start_timer()

def handle_stop():
    dpg.hide_item("stop")
    dpg.show_item("start")
    timer.stop_timer()
    dpg.configure_item("presets", enabled=True)
    dpg.set_value("time", "00:00")