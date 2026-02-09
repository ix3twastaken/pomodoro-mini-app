def get_monitor_size():
    import tkinter as tk
    
    root = tk.Tk()
    monitor_width = root.winfo_screenwidth()
    monitor_height = root.winfo_screenheight()
    root.destroy()
    
    return monitor_width, monitor_height
 
def calculate_default_window_pos(
        width: int = 250,
        height: int = 250
):
    monitor_width, monitor_height = get_monitor_size()
    
    MONITOR_WIDTH_CENTER = monitor_width//2
    MONITOR_HEIGHT_CENTER = monitor_height//2
    
    window_center_width = width//2
    window_center_height = height//2
    
    x_pos = MONITOR_WIDTH_CENTER-window_center_width
    y_pos = MONITOR_HEIGHT_CENTER-window_center_height
    
    return x_pos, y_pos
