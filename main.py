import os
import dearpygui.dearpygui as dpg
from config import icon_path
from gui import setup_gui

def main():
    dpg.create_context()
    dpg.create_viewport(
        title='Pomodoro',
        max_width=200,
        max_height=250,
        min_width=200,
        min_height=250,
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