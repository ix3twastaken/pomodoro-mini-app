import dearpygui.dearpygui as dpg

import gui
import utils.window_utils as window_utils
from config import DEFAULT_WINDOW_HEIGHT, DEFAULT_WINDOW_WIDTH
from utils.sys_utils import get_file_path

x, y = window_utils.calculate_default_window_pos(width=DEFAULT_WINDOW_WIDTH, height=DEFAULT_WINDOW_HEIGHT)

def main():
    dpg.create_context()

    dpg.create_viewport(
        title='Pomodoro',
        width=DEFAULT_WINDOW_WIDTH,
        height=DEFAULT_WINDOW_HEIGHT,
        max_width=DEFAULT_WINDOW_WIDTH,
        max_height=DEFAULT_WINDOW_HEIGHT,
        x_pos=x,
        y_pos=y,
        resizable=False,
        small_icon=get_file_path("icon.ico", __file__) #This icon was designed using resources from Flaticon.com.
    )
    gui.setup_gui()
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("Window", True)
    dpg.start_dearpygui()
    dpg.destroy_context()

if __name__ == "__main__":
    main() 