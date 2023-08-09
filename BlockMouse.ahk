
$!^g::
Mouse_Blocked := true   ; assign the Boolean value "true" or "1" to this variable
BlockInput, On   ; disable MouseMove
return

; The #If directive creates context-sensitive hotkeys

#If (Mouse_Blocked) ; If this variable has the value "true" 

    ; block mouse input:
    LButton::
    RButton::
    WheelUp::
    WheelDown::
    return

    $!^g::    ; press g to re-enable MouseMove and mouse input
    BlockInput, Off
    Mouse_Blocked := false
    return


#If ; turn off context sensitivity