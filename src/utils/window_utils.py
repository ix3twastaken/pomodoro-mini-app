def get_monitor_size():
    import tkinter as tk
    
    root = tk.Tk()
    monitor_width = root.winfo_screenwidth()
    monitor_height = root.winfo_screenheight()
    root.destroy()
    
    return monitor_width, monitor_height
 
def calculate_default_window_pos(
        width: int,
        height: int
):
    monitor_width, monitor_height = get_monitor_size()
    
    monitor_width_center = monitor_width//2
    monitor_height_center = monitor_height//2
    
    window_center_width = width//2
    window_center_height = height//2
    
    x_pos = monitor_width_center-window_center_width
    y_pos = monitor_height_center-window_center_height
    
    return x_pos, y_pos
