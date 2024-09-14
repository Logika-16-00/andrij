from PyQt5.QtWidgets import QApplication

App = QApplication([])

App.setStyleSheet("""
    QPushButton {  
        background-color: lightgreen; 
        color:black ;
        font-size: 16px;
        border-radius: 10px;
        padding: 10px 20px;
    }
    QPushButton:hover {
        background-color: lightgreen; 
        color:black;
    }
    QSpinBox, QListWidget{
        padding: 5px;
        font-size: 14px;
        border-radius: 10px;
        padding: 10px 20px;
    }

    QRadioButton {
        font-size: 14px;
        padding: 5px;
        margin-top: 10px;
    }

    QLabel {
        font-size: 16px;
        font-weight: bold;
    }

    QGroupBox {
        font-size: 18px;
        border: 2px solid #4CAF50; /* Green border */
        border-radius: 10px;
    }
    
    QListWidget{
        padding: 5px;
        font-size: 16px;
        font-weight: bold;
        border-radius: 5px;
        padding: 10px 10px;
        border: 2px solid #4CAF50;
        background-color: grey;
        color:black;
    }
    
    
""")