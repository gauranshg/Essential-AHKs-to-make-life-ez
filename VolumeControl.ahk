Pause::
Send {Volume_Mute}
Input volume, I L1
if volume = +
SoundSet, +10
else if volume = -
SoundSet, -10
else if volume = 0
SoundSet, 100
else if volume = m
{

}else 
{
vol:=volume*10
SoundSet, %vol%
}

;Send {Volume_Mute}
return