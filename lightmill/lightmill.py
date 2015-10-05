"""
Reads a Crookes Radiometer's (light-mill's) spin rate to detect quantitatively how much light is hitting it.
"""

import os

import cv2
from matplotlib import pyplot as plt
import scipy.fftpack
import numpy

def measureIntensities(videoFileName, pointOfInterest):
    """
    Find the intensity of a point of interest for each frame
    """
    video = cv2.VideoCapture(videoFileName)
    intensities = []
    while video.isOpened():
        _returnCode, frame = video.read()
        if frame is None:
            break
        pixelValues = frame[pointOfInterest]
        intensities.append(pixelValues.sum())
    video.release()
    return intensities

def performFrequencyAnalysis(intensities, frameRateHz):
    """
    Analyze the time-domain signal and do an FFT to figure out which frequencies are present
    """
    frequencyDomain = abs(scipy.fft(intensities))
    frequencies = scipy.fftpack.fftfreq(len(intensities), 1.0 / frameRateHz)
    return frequencyDomain, frequencies

def plotTimeAndFrequencyDomains(intensities, frequencyDomain, frequencies, fName=None):
    sampleTimes = numpy.linspace(0, len(intensities) / frameRateHz, len(intensities))
    plt.figure()
    plt.subplot(211)
    plt.plot(sampleTimes, intensities)
    plt.title('Intensity vs. time of {}'.format(videoFileName))
    plt.xlabel('Time (s)')
    plt.ylabel('Relative intensity')

    plt.subplot(212)
    plt.plot(frequencies[0:len(intensities) / 2], 20 * scipy.log10(frequencyDomain[0:len(intensities) / 2]))
    plt.title('Frequency analysis for {}'.format(videoFileName))
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Power (dB)')
    plt.tight_layout()
    if fName is None:
        plt.show()
    else:
        plt.savefig(fName)

if __name__ == '__main__':
    # define inputs as (filename, point of interest, framesPerSecond)
    # This assumes there's a folder (or link) called ../videos full of the video files.
    LOW_INTENISITY_30FPS = ('low intensity 30fps.MOV', (240, 772), 30.0)
    HIGH_INTENSITY_30FPS = ('high intensity 30fps.MOV', (156, 728), 30.0)
    MEDIUM_INTENSITY_120FPS = ('medium intensity 120fps.AVI', (153, 352), 120.0)
    HIGH_INTENSITY_120FPS = ('high intensity 120fps.AVI', (150, 350), 120.0)
    HIGH_INTENSITY_240FPS = ('high intensity 240fps.AVI', (82, 180), 240.0)
    allFiles = [LOW_INTENISITY_30FPS, HIGH_INTENSITY_30FPS, MEDIUM_INTENSITY_120FPS,
                HIGH_INTENSITY_120FPS, HIGH_INTENSITY_240FPS]

    # analyze all cases.
    for videoFileName, pointOfInterest, frameRateHz in allFiles:
        videoPath = os.path.join('..', 'videos', videoFileName)
        intensities = measureIntensities(videoPath, pointOfInterest)
        frequencyDomain, frequencies = performFrequencyAnalysis(intensities, frameRateHz)
        plotFileName = videoFileName.split('.')[0] + '.png'
        plotPath = os.path.join('..', 'videos', plotFileName)
        plotTimeAndFrequencyDomains(intensities, frequencyDomain, frequencies, fName=plotPath)
