import Tkinter
import tkSnack

# set the volume of the sound system"""
def setVolume(volume=50):
    if volume > 100:
        volume = 100
    elif volume < 0:
        volume = 0
    tkSnack.audio.play_gain(volume)

# """play a note of freq (hertz) for duration (seconds)"""
def playNote(freq, duration):
    snd = tkSnack.Sound()
    filt = tkSnack.Filter('generator', freq, 30000, 0.0, 'sine', int(11500*duration))
    snd.stop()
    snd.play(filter=filt, blocking=1)

# """stop the sound the hard way"""
def soundStop():
    try:
        root = root.destroy()
        filt = None
    except:
        pass
       
root = Tkinter.Tk()

# have to initialize the sound system, required!!
tkSnack.initializeSnack(root)
# set the volume of the sound system (0 to 100%)
setVolume(50)
# play a note of requency 440 hertz (A4) for a duration of 2 seconds
playNote(440, 2)
# optional
soundStop()

root.withdraw()
