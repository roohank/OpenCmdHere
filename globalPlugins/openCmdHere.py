import globalPluginHandler
from scriptHandler import script
import ui
import threading
import ctypes
import winUser
import comtypes.client
from comtypes import CoInitialize, CoUninitialize
import urllib.parse

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

    @script(
        description="Open Command Prompt as Administrator in the current Explorer folder",
        gesture="kb:NVDA+control+windows+c"
    )
    def script_openCmdHere(self, gesture):
        ui.message("Opening Command Prompt...")
        threading.Thread(target=self._openElevatedCmd).start()

    def _openElevatedCmd(self):
        try:
            target_path = self._getActiveExplorerPath()
            
            # اگر مسیری پیدا نشد، از مسیر پیش‌فرض استفاده کن
            if not target_path:
                target_path = r"C:\Windows\System32"
            
            # باز کردن CMD با دسترسی ادمین و تغییر مسیر به پوشه هدف
            result = ctypes.windll.shell32.ShellExecuteW(
                None,           # parent window
                "runas",        # operation (درخواست دسترسی ادمین)
                "cmd.exe",      # file to execute
                f'/k cd /d "{target_path}"',  # parameters
                None,           # working directory
                1               # show window (SW_SHOWNORMAL)
            )
            
            if result <= 32:
                ui.message("Failed to open Command Prompt as Administrator.")
                
        except Exception as e:
            ui.message(f"Error: {str(e)}")

    def _getActiveExplorerPath(self):
        """گرفتن مسیر پوشه فعلی از پنجره فعال Explorer با استفاده از COM"""
        try:
            # گرفتن هندل پنجره فعال
            hwnd = winUser.getForegroundWindow()
            if not hwnd:
                return None
            
            # مقداردهی اولیه COM در این ترد
            CoInitialize()
            try:
                # ساخت شیء Shell.Application
                shell = comtypes.client.CreateObject("Shell.Application")
                
                # پیمایش بین همه پنجره‌های باز Explorer
                for window in shell.Windows():
                    try:
                        # مقایسه هندل پنجره
                        if window.HWND == hwnd:
                            # گرفتن مسیر از LocationURL
                            location_url = window.LocationURL
                            if location_url and location_url.startswith("file:///"):
                                # حذف پیشوند file:/// و دیکد کردن
                                path = urllib.parse.unquote(location_url[8:])
                                return path
                    except Exception:
                        continue
                        
            finally:
                CoUninitialize()
                
        except Exception:
            pass
        
        return None