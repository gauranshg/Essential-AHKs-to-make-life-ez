F6::
send,^c
filepath:=Clipboard
if filepath contains \
{

SplitPath, filepath , , Dir, ext, original_Name
;msgbox %original_Name% %Dir%
if InStr(original_Name, "_")
 {
Gui, Destroy
Gui, Add, Edit, w135 vsuffix
Gui, Add, button, default w135 gEnter, Enter
Gui, Show
 }


else
{
msgbox,16,OOPS!! Error!!, file name should be in this format number_name.extension example: 24_working.xls
IfMsgBox, Ok
ExitApp
    Return 
}


}

else
{
msgbox,16,OOPS!! Error!!, file name should be in this format number_name.extension example: 24_working.xls
IfMsgBox, Ok
ExitApp
    Return 
}

return

Enter:
Gui, submit, hide

{
pos_us:= InStr(original_Name, "_")
current_no:=SubStr(original_Name, 1 , pos_us-1)
;msgbox %current_no%
new_no := current_no + 1
;msgbox %new_no%
real_name:=SubStr(original_Name, pos_us , StrLen(original_Name))
;msgbox %real_name%
new_name := new_no . real_name
;msgbox %new_name%
if (suffix = "")
{
outpath := Dir . "\" . new_name . "." . ext
}
else if (suffix <> "")
outpath := Dir . "\" . new_name . "_" . suffix . "." . ext
;msgbox %outpath%
filecopy, %filepath%, %outpath%
Gui, Destroy
}

ExitApp





