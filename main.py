from PIL import ImageGrab
import pytesseract
import time
import tkinter as tk, ctypes
import pyperclip

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
def show_notification():
    """Slides in the notification from the right."""
    global x_pos
    if x_pos > screen_width - window_width - 10:
        x_pos -= 10
        root.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")
        root.after(3, show_notification)
    else:
        root.after(2000, hide_notification)  # Stay for 2 sec before hiding

def hide_notification():
    """Slides out the notification to the right."""
    global x_pos
    if x_pos < screen_width:
        x_pos += 10
        root.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")
        root.after(3, hide_notification)
    else:
        root.destroy()

def capture_screenshot():
    print("Here is your text","--------------------","\n")
    screenshot = ImageGrab.grabclipboard()
    text_data = pytesseract.image_to_string(screenshot)
    pyperclip.copy(text_data)
    print(text_data, "\n")
    global root
    root = tk.Tk()
    root.overrideredirect(True) 
    root.configure(bg="#030303")
    global screen_width , screen_height, window_width, window_height, x_pos, y_pos
    screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight()
    window_width, window_height = 400, 50

    x_pos, y_pos = screen_width, screen_height - 150
    ctypes.windll.dwmapi.DwmSetWindowAttribute(ctypes.windll.user32.GetParent(root.winfo_id()), 33, ctypes.byref(ctypes.c_int(20)), 4)
    root.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")
    tk.Label(root ,background="#030303",foreground="white", justify="center",text="Text Copied To Clipboard",font=("Arial", 15)).place(relx=0.5, rely=0.5, anchor="center")
    show_notification()
    root.mainloop()

def main_loop():
    capture_screenshot()
    while True:
        if ImageGrab.grabclipboard() is not None:
            capture_screenshot()
        time.sleep(2)

# Run the program
if __name__ == "__main__":
    main_loop()