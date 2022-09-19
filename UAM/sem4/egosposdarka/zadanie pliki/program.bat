@echo off
setlocal
setlocal EnableDelayedExpansion
rem store the matching file names in list
dir /b . /s 2> nul > files
rem count the match files
type files | find "" /v /c > tmp & set /p _count=<tmp 
rem get a random number between 0 and count-1
set /a _random=%random%*(%_count%)/32768
rem we can't skip 0 lines
if %_random% equ 0 (
  for /f "tokens=*" %%i in ('type files') do (
    set _randomfile=%%i
    echo !_randomfile!
    goto :eof
    )
) else (
  for /f "tokens=* skip=%_random%" %%i in ('type files') do (
    set _randomfile=%%i
    echo !_randomfile!
    goto :eof
    )
)