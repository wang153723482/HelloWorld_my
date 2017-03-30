@echo off   
echo 清空IE临时文件目录...  
  
del /f /s /q "%userprofile%\AppData\Local\Microsoft\Windows\Temporary Internet Files\*.*"  
  
cls  
echo.  
echo 清理IE缓存完毕，是否清理系统缓存？  
echo.  
echo 是请按任意键继续，否则请直接关闭本窗口。  
pause>nul  
  
del /f /s /q "%temp%\*.*"  
  
cls  
echo.  
echo 清除系统完成！  
echo. & pause  