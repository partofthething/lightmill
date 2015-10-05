# Lightmill: Reading a Crookes Radiometer with a camera #

This is a program that can analyze a video of a Crookes Radiometer (aka a light-mill) and tell you
how fast it is spinning. The spin rate should be proportional to the amount of radiation
that is hitting the radiometer. This allows you to read out a radiometer without using
a stroboscope. 

## Requirements ##

* numpy
* scipy
* OpenCV


### Example of converting text ###
```python

from morsecodelib import text
text.text_to_code('testing text to code converSION!')
```

This prints: 
`- . ... - .. -. --.  - . -..- -  - ---  -.-. --- -.. .  -.-. ... .. --- -. -.-.--`

### Example of playing sound ###

```python
from morsecodelib import sound
morse_sound = sound.MorseSoundPlayer()
morse_sound.text_to_sound('HI THERE THIS IS A TEST')
```

    