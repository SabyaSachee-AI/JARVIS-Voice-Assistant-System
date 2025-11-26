import os
def play_music():
     music_dir = "F:\DS\Full-Stack-Data-Science-with-Generative-AI\JARVIS-Voice-Assistant-System\music"
     try:
         songs = os.list(music_dir)
         if songs:
              random_song = random.choice(songs)
              os.startfile(os.path.join(music_dir,random_song))
         else:
              print("no music found")

     except Exception as e:
          print("no music folder not  found")

play_music()