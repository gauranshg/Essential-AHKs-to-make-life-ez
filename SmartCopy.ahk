^+C::
Input key, I L1
Send {ctrl down}c{ctrl up}
NewVariable%key% := clipboardall
return


^+V::
Input no, I L1
clipboard := "empty"
clipboard := NewVariable%no%
Send {ctrl down}v{ctrl up}
return


^+Q::
Input no, I L1
clipboard := "empty"
clipboard := NewVariable%no%
 Send %Clipboard%
return