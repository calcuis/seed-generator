import sys, mnemonic, secrets
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit, QTextEdit, QLabel
from PyQt6.QtGui import QIcon

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Generator") # title
        self.setWindowIcon(QIcon("logo.ico")) # logo
        self.resize(600, 80) # width, height

        layout = QVBoxLayout()
        self.setLayout(layout)

        # widgets
        self.label = QLabel("How many words in your mnemonic? (12, 15, 18, 21 or 24)")
        self.inputField = QLineEdit()
        button = QPushButton("&Generate", clicked=self.generateSeed)
        buttonExit = QPushButton("&Exit", clicked=self.exitApp)
        self.output = QTextEdit()

        # layouts
        layout.addWidget(self.label)
        layout.addWidget(self.inputField)
        layout.addWidget(button)
        layout.addWidget(buttonExit)
        layout.addWidget(self.output)

    def generateSeed(self):
        inputText = self.inputField.text()
        if inputText=="12":byte=16
        elif inputText=="15":byte=20
        elif inputText=="18":byte=24
        elif inputText=="21":byte=28
        elif inputText=="24":byte=32
        else : quit()
        
        # define the BIP39 word list language
        language = 'english'  # You can choose a different language if desired
        # generate a random seed of 16 bytes, 20 bytes, 24 bytes, 28 bytes or 32 bytes
        seed = secrets.token_bytes(byte)
        # create a BIP39 mnemonic using the random seed and language
        mnemonic_words = mnemonic.Mnemonic(language).to_mnemonic(seed)
        # split the mnemonic into individual words
        mnemonic_word_list = " ".join(mnemonic_words.split())
        # print the mnemonic as output
        self.output.setText(mnemonic_word_list)
    
    def exitApp(self):
        quit()

app = QApplication(sys.argv)
window = MyApp()
window.show()
app.exec()
