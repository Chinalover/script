@echo off
for /f   %%i in (netview1.txt) do (
  echo %%i
  echo %%i >> ping.txt
  ping  %%i^ -n -1 >> ping1.txt

 
)