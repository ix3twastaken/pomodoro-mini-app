import os

import dearpygui.dearpygui as dpg

from gui import setup_gui
import utils.window_utils as window_utils
from config import DEFAULT_WINDOW_HEIGHT, DEFAULT_WINDOW_WIDTH


x, y = window_utils.calculate_default_window_pos(width=DEFAULT_WINDOW_WIDTH, height=DEFAULT_WINDOW_HEIGHT)


def main():
    dpg.create_context()
    
    with dpg.theme() as global_theme:
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 10)
            dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 1)
            dpg.add_font("RobotoSlab.ttf")
    dpg.bind_theme(global_theme)
    
    
    dpg.create_viewport(
        title='Pomodoro',
        width=DEFAULT_WINDOW_WIDTH,
        height=DEFAULT_WINDOW_HEIGHT,
        x_pos=x,
        y_pos=y,
        resizable=False,
        small_icon=os.path.join(os.path.dirname(__file__), "icon.ico") #This icon was designed using resources from Flaticon.com.
    )

    setup_gui()
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("Window", True)
    dpg.start_dearpygui()
    dpg.destroy_context()

if __name__ == "__main__":
    main() 