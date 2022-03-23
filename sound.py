from pydub import AudioSegment
import pydub.playback 

class Sound:
    def __init__(self, file_name, pitch=0) -> None:
        self.song = AudioSegment.from_wav(file_name)
        self.pitch = pitch

    def pitch_up(self):
        pass

    def play(self):
        pydub.playback.play(self.song)

    