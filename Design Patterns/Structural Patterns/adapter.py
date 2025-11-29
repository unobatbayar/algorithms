"""
Adapter Design Pattern

The Adapter pattern allows incompatible interfaces to work together by wrapping
an object with an adapter that translates calls to the wrapped object.

Use cases:
    - Integrating third-party libraries
    - Making incompatible interfaces compatible
    - Legacy code integration
"""


# Target interface (what client expects)
class MediaPlayer:
    """Target interface."""
    
    def play(self, audio_type, filename):
        """Play media file."""
        pass


# Adaptee (existing incompatible class)
class AdvancedMediaPlayer:
    """Advanced media player with different interface."""
    
    def play_vlc(self, filename):
        """Play VLC file."""
        return f"Playing VLC file: {filename}"
    
    def play_mp4(self, filename):
        """Play MP4 file."""
        return f"Playing MP4 file: {filename}"


# Adapter
class MediaAdapter(MediaPlayer):
    """Adapter that makes AdvancedMediaPlayer compatible with MediaPlayer."""
    
    def __init__(self, audio_type):
        self.advanced_player = AdvancedMediaPlayer()
        self.audio_type = audio_type
    
    def play(self, audio_type, filename):
        """Adapt the play method."""
        if audio_type == "vlc":
            return self.advanced_player.play_vlc(filename)
        elif audio_type == "mp4":
            return self.advanced_player.play_mp4(filename)


# Client
class AudioPlayer(MediaPlayer):
    """Client that uses MediaPlayer interface."""
    
    def play(self, audio_type, filename):
        if audio_type == "mp3":
            return f"Playing MP3 file: {filename}"
        elif audio_type in ["vlc", "mp4"]:
            adapter = MediaAdapter(audio_type)
            return adapter.play(audio_type, filename)
        else:
            return f"Invalid media type: {audio_type}"


# Example usage
if __name__ == "__main__":
    player = AudioPlayer()
    
    print(player.play("mp3", "song.mp3"))
    print(player.play("vlc", "movie.vlc"))
    print(player.play("mp4", "video.mp4"))
    print(player.play("avi", "clip.avi"))

