import pygame, time

# Set up the audio output - only once!
# 2-channel (stereo), 16-bit signed integer value output at 44khz
pygame.mixer.init(frequency=44100, channels=2, size=-16)

# Load piano samples
noteC5 = pygame.mixer.Sound( "piano_samples/C5.wav" )
noteD5 = pygame.mixer.Sound( "piano_samples/D5.wav" )

# Play samples
noteC5.play()
noteD5.play()

# Keep the program active until the notes are complete
time.sleep(2)
