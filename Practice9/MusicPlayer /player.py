import pygame
import os

class MusicPlayer:
    def __init__(self, music_folder):
        # Проверяем, существует ли папка, чтобы не было ошибок
        if not os.path.exists(music_folder):
            os.makedirs(music_folder)
            
        self.playlist = [os.path.join(music_folder, f) for f in os.listdir(music_folder) if f.endswith(('.mp3', '.wav'))]
        self.current_index = 0
        self.is_paused = False
        pygame.mixer.init()

    def play(self):
        if self.playlist:
            if self.is_paused:
                pygame.mixer.music.unpause()
                self.is_paused = False
            else:
                pygame.mixer.music.load(self.playlist[self.current_index])
                pygame.mixer.music.play()

    def pause(self):
        pygame.mixer.music.pause()
        self.is_paused = True

    def stop(self):
        pygame.mixer.music.stop()
        self.is_paused = False

    def next_track(self):
        if self.playlist:
            self.current_index = (self.current_index + 1) % len(self.playlist)
            self.is_paused = False
            self.play()

    def prev_track(self):
        if self.playlist:
            self.current_index = (self.current_index - 1) % len(self.playlist)
            self.is_paused = False
            self.play()

    def get_current_track_name(self):
        if not self.playlist:
            return "No tracks found"
        return os.path.basename(self.playlist[self.current_index])