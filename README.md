# Lightmill: Reading a Crookes Radiometer with a camera #

This is a program that can analyze a video of a Crookes radiometer (aka a light-mill) and tell you
how fast it is spinning. The spin rate should be proportional to the amount of radiation
that is hitting the radiometer. This allows you to read out a radiometer without using
a stroboscope. 

Writeup with example results is here: http://partofthething.com/thoughts/?p=777

## Requirements ##

* numpy
* scipy
* OpenCV


### Example of reading out a radiometer ###
```python

import lightmill

intensities = measureIntensities('high intensity 120fps.AVI', pointOfInterest = (240, 772))
frequencyDomain, frequencies = performFrequencyAnalysis(intensities, frameRateHz = 120.0)
plotTimeAndFrequencyDomains(intensities, frequencyDomain, frequencies)
```

This gives a plot of intensity vs. time and a frequency domain plot. 
    