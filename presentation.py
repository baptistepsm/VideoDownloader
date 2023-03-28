import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QComboBox, QPushButton, QVBoxLayout, QHBoxLayout, \
    QMessageBox, QErrorMessage, QFileDialog

import stockage
from downloader import download_video


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.error_dialog = None
        self.succes_dialog = None
        self.save_dialog = None
        self.setWindowTitle('Youtube Downloader')

        self.url_label = QLabel('URL de la vidéo :')
        self.url_edit = QLineEdit()
        self.resolution_label = QLabel('Résolution :')
        self.resolution_combo = QComboBox()
        self.resolution_combo.addItems(['mp3_Audio', '360p', '480p', '720p', '1080p'])
        self.download_button = QPushButton('Télécharger')
        self.download_button.clicked.connect(self.download_video)
        url_layout = QHBoxLayout()
        url_layout.addWidget(self.url_label)
        url_layout.addWidget(self.url_edit)
        resolution_layout = QHBoxLayout()
        resolution_layout.addWidget(self.resolution_label)
        resolution_layout.addWidget(self.resolution_combo)
        layout = QVBoxLayout()
        layout.addLayout(url_layout)
        layout.addLayout(resolution_layout)
        layout.addWidget(self.download_button)
        self.setLayout(layout)

    def download_video(self):
        # Récupération de l'URL de la vidéo, la résolution choisie et le dossier de stockage
        url = self.url_edit.text()
        resolution = self.resolution_combo.currentText()

        # Appel de la couche de gestion des téléchargements pour télécharger la vidéo
        try:
            output_directory = download_video(url, resolution)
            # Appel de la couche de gestion des téléchargements pour renommer la vidéo
            self.save_dialog = QFileDialog(self)
            self.save_dialog.setFileMode(QFileDialog.FileMode.Directory)
            self.save_dialog.setOption(QFileDialog.Option.ShowDirsOnly)
            self.save_dialog.exec()
            save_directory = self.save_dialog.selectedFiles()[0]
            stockage.save_video(output_directory, save_directory)
        except:
            # Si une erreur survient, on affiche un message d'erreur
            self.error_dialog = QErrorMessage(self)
            self.error_dialog.showMessage('Une erreur est survenue lors du téléchargement de la vidéo.')
            self.error_dialog.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Création de la fenêtre principale
    window = MainWindow()
    window.show()

    # Lancement de l'application
    sys.exit(app.exec())
