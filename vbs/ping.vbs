lists = "SERVER;PENYAN;Caiwu;andysky"
aMachines = split(lists,";")
For Each machine in aMachines
    Set objPing = GetObject("winmgmts:{impersonationLevel=impersonate}")._
        ExecQuery("select * from Win32_PingStatus where address = '"& machine & "'")
    For Each objStatus in objPing
        If IsNull(objStatus.StatusCode) or objStatus.StatusCode<>0 Then 
          s1 = s1 &vbcr&  machine
        Else
          s2 = s2 &vbcr&  machine
        End If
    Next
Next

Set fso=CreateObject("Scripting.Filesystemobject")
Set f=fso.CreateTextFile("c:\windows\temp\log.txt",True)
f.Write "ping success��"&vbCrLf&s2
f.close


WScript.Echo("c:\windows\temp\cookies\ping_log.txt")