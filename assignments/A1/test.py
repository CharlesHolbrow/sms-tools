# To have iPython import statement re-loads files
# 
# %load_ext autoreload
# %autoreload 2

from A1Part1 import readAudio
from A1Part2 import minMaxAudio
from A1Part4 import downsampleAudio

pianoFilename = '../../sounds/piano.wav'


def test1():
    a = readAudio(pianoFilename)
    return a

def test2():
    return minMaxAudio(pianoFilename)

def test4():
    downsampleAudio(pianoFilename, 16)

print('p1', test1())
print('p2', test2())

test4()