from pygame import mixer

mixer.init()
mixer.music.load("music.mp3")
mixer.music.set_volumep(0.7)
mixer.music.play()

while True:
    print("P tuşuna basarak durdurun, R tuşu ile devam ettirebilirsiniz")
    print("E tuşu ile programı sonlandırabilirsiniz")
    query = input(" ")
    if query == 'p':
        mixer.music.pause()
    elif query == 'r':
        mixer.music.unpause()
    elif query == 'e':
        mixer.music.stop()
        break
    
    
    
