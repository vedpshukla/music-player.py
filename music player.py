from pygame import mixer
mixer.init() #start the mixer
mixer.music.load("song.mp3") #load the song
mixer.music.set_volume(0.7) #set the volume
mixer.music.play()
while True:
    print("press 'p' to pause 'r' to resume")
    print("press 'e' to exit the program")
    query=input(">>>")

    if query=='p':
        mixer.music.pause() #Pause music
    elif query=='r':
        mixer.music.unpause() #Resume Music
    elif query=='e':
        mixer.music.stop() #Stop the mixer
        break
