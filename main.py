import os
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog

class MusicPlayer(QWidget):
    def __init__(self):
        super().__init__()

        self.music_files = [] # Список файлов с музыкой
        self.current_file_index = 0 # Текущий индекс файла

        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.play_button = QPushButton("Play")
        self.play_button.clicked.connect(self.play_music)
        self.layout.addWidget(self.play_button)

        self.stop_button = QPushButton("Stop")
        self.stop_button.clicked.connect(self.stop_music)
        self.layout.addWidget(self.stop_button)

        self.next_button = QPushButton("Next")
        self.next_button.clicked.connect(self.skip_to_next)
        self.layout.addWidget(self.next_button)

        self.browse_button = QPushButton("Browse")
        self.browse_button.clicked.connect(self.browse_music_files)
        self.layout.addWidget(self.browse_button)

    def browse_music_files(self):
        directory = QFileDialog.getExistingDirectory(self, 'Select Directory', 'C:\\')
        music_files = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                _, ext = os.path.splitext(file)
                if ext.lower() in ['.mp3', '.wav', '.flac', '.aac']:
                    music_files.append(os.path.join(root, file))
        self.music_files.extend(music_files)

    def play_music(self):
        if not self.music_files:
            return
        file = self.music_files[self.current_file_index]
        self.media_player = QMediaPlayer()
        self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(file)))
        self.media_player.play()

    def stop_music(self):
        if not self.music_files:
            return
        self.media_player.stop()

    def skip_to_next(self):
        if not self.music_files:
            return
        if self.current_file_index < len(self.music_files) - 1:
            self.current_file_index += 1
        else:
            self.current_file_index = 0
        self.stop_music()
        self.play_music()

current_file_index = 0
# Это мы взяли названия файлов музыки
mode = 0

path_to_search = 'путь/к/директории'
# Проводим данную операцию 2 раза для музыки из папки релакс и папки концентрация
relaxing = ["1", "2", "3"]
concentrating = ["4", "5", "6"]
# тут идет инфа с кнопки какой режим выбрать
if mode == 0:
    print(0) # тут будет название функции для музыки с релаксом
    # начинает играть плейлист relaxing
else:
    print(1) # аналогично, но для концентрации
    # начинает играть плейлист concentrating

if __name__ == '__main__':
    app = QApplication([])
    window = MusicPlayer()
    window.setWindowTitle("Music Player")
    window.show()
    app.exec()