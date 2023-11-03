import winreg as reg

reg.CreateKey()
key = reg.CreateKey(reg.HKEY_CURRENT_USER, 'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System')
reg.SetValueEx(key, 'DisableRegistryTools', 0, reg.REG_DWORD, 1)
reg.CloseKey(key)