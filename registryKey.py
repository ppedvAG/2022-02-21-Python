import winreg
# https://docs.python.org/3/library/winreg.html#module-winreg
# https://www.blog.pythonlibrary.org/2010/03/20/pythons-_winreg-editing-the-windows-registry/
keyVal = r"SOFTWARE\Microsoft\Cryptography\Protect\Providers\df9d8cd0-1501-11d1-8c7a-00c04fc297eb"
try:
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, keyVal, reserved=0, access=winreg.KEY_ALL_ACCESS)
except:
    key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, keyVal)
winreg.SetValueEx(key, "ProtectionPolicy", 0, winreg.REG_DWORD, 1)
winreg.DeleteValue(key, "ProtectionPolicy")
winreg.CloseKey(key)
key.Close()

