import os
from mutagen.mp3 import MP3

class HandleTracksQuality:

    def __init__(self, folder_path):
        self.folder_path = folder_path

    def remove_low_quality_tracks(self, target_bitrate):
        for filename in os.listdir(self.folder_path):
            file_path = os.path.join(self.folder_path, filename)
            encoded_path = file_path.encode("utf-8").decode("utf-8")
            if os.path.isfile(encoded_path):
                try:
                    audio = MP3(encoded_path)
                    bitrate = audio.info.bitrate // 1000
                    os.remove(encoded_path)
                    print(f"BITRATE {bitrate} de {filename}")
                except Exception as e:
                    print(f"Erreur lors de la vérification de {filename}: {str(e)}")

# Exemple d'utilisation
folder_path = r'/your/path/tofile/'
bitrate_target = 320  # 320 Kbps

handler = HandleTracksQuality(folder_path)
handler.remove_low_quality_tracks(bitrate_target)
