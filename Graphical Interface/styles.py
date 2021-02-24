labelClassification = """
    border-style: none;
    font-weight: bold;
    font-size: 40px;
    color: white;
"""

mainWindowFrame = """
        border: 2px solid rgb(40, 40, 40);
        border-radius: 4px;
        background-color: rgb(70,70,73);
        background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                         stop: 0 rgb(70,70,70),
                                         stop: 0.8 rgb(54,54,54));
    """

labelComboBox = """
        border-style: none;
        background-color: rgba(0, 0, 0, 0);
        font-weight: bold;
        font-size: 25px;
        color: rgb(200, 200, 200);
"""


comboBox = """
        QComboBox{
            border: 2px solid rgb(40, 40, 40);
            background: rgba(0, 0, 0, 0);
            font-weight: bold;
            font-size: 30px;
            color: grey;
        }

        QComboBox:hover{
            background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                             stop: 0 rgb(90,90,90),
                                             stop: 0.8 rgb(80,80,80));
            color: rgb(200, 200, 200);;
        }
"""



frame = """
        border-style: outset;
        border-width: 2px;
        border-color: rgb(30, 30, 30);
        border-radius: 4px;
        background-color: rgb(70,70,73);
        background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                         stop: 0 rgb(40,40,40),
                                         stop: 0.8 rgb(43,43,43));
"""

objectNameLabel = """
        border-style: none;
        font-weight: bold;
        font-size:30px;
        color: rgb(200, 200, 200);
        background-color: rgba(0,0,0,0);
"""

objectNameLabel_highlighted = """
        border-style: inset;
        border-width: 3px;
        font-weight: bold;
        font-size:30px;
        background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                         stop: 0 rgb(100,100,100),
                                         stop: 0.8 rgb(110,110,110));
"""


calibrateButton = """
            QPushButton{
                background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                                 stop: 0 rgb(80,80,80),
                                                 stop: 0.8 rgb(70,70,70));
                font-weight: bold;
                font-size:20px;
                color: rgb(200, 200, 200);
                border-style: outset;
                border-color: rgb(40, 40, 40);
                border-width: 2px;
                border-radius: 5px;
            }

            QPushButton:hover{
                background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                                 stop: 0 rgb(90,90,90),
                                                 stop: 0.8 rgb(80,80,80));
            }
        """

calibrateButton_highlighted = """
            QPushButton{
                background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                                 stop: 0 rgb(110,110,110),
                                                 stop: 0.8 rgb(100,100,100));
                font-weight: bold;
                font-size:20px;
                color: rgb(200, 200, 200);
                border-style: outset;
                border-color: rgb(40, 40, 40);
                border-width: 2px;
                border-radius: 5px;
            }

            QPushButton:hover{
                background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                                 stop: 0 rgb(130,130,130),
                                                 stop: 0.8 rgb(120,120,120));
            }
        """

calibrateButton_calibrated = """
            QPushButton{
                background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                                 stop: 0 rgb(40,80,40),
                                                 stop: 0.8 rgb(35,70,35));
                font-weight: bold;
                font-size:20px;
                color: rgb(200, 200, 200);
                border-style: outset;
                border-color: rgb(40, 40, 40);
                border-width: 2px;
                border-radius: 5px;
            }

            QPushButton:hover{
                background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                                 stop: 0 rgb(45,90,45),
                                                 stop: 0.8 rgb(40,80,40));
            }
        """

calibrateButton_calibrated_highlighted = """
            QPushButton{
                background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                                 stop: 0 rgb(70,110,70),
                                                 stop: 0.8 rgb(65,100,65));
                font-weight: bold;
                font-size:20px;
                color: rgb(200, 200, 200);
                border-style: outset;
                border-color: rgb(40, 40, 40);
                border-width: 2px;
                border-radius: 5px;
            }

            QPushButton:hover{
                background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                                 stop: 0 rgb(45,90,45),
                                                 stop: 0.8 rgb(40,80,40));
            }
        """


addObjectButton = """
            QPushButton{
                background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                                 stop: 0 rgb(80,80,80),
                                                 stop: 0.8 rgb(70,70,70));
                font-weight: bold;
                font-size:20px;
                color: rgb(200, 200, 200);
                border-style: outset;
                border-color: rgb(40, 40, 40);
                border-width: 2px;
                border-radius: 5px;
            }

            QPushButton:hover{
                background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                                 stop: 0 rgb(90,90,90),
                                                 stop: 0.8 rgb(80,80,80));
            }
        """




labelMyObjects = """
        background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                         stop: 0 rgb(100,100,100),
                                         stop: 0.8 rgb(90,90,90));
        font-weight: bold;
        font-size:30px;
        color: rgb(230, 230, 230);
        border-style: solid;
        border-color: rgba(0, 0, 0, 0);
        border-width: 2px;
        border-radius: 0px;
    """



statusBar = """
        border-style: none;
        font-weight: bold;
        font-size: 20px;
        color: rgb(250, 250, 250);
        min-height: 50;

        background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                         stop: 0 rgb(100,100,100),
                                         stop: 0.8 rgb(90,90,90));
    """


statusBarError = """
        border-style: none;
        font-weight: bold;
        font-size: 20px;
        color: rgb(40, 20, 20);
        min-height: 50;

        background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                         stop: 0 rgb(200,100,100),
                                         stop: 0.8 rgb(180,90,90));
    """


toolbar = """
        QToolBar{
            border-style: none;
            font-weight: bold;
            font-size: 20px;
            color: rgb(40, 20, 20);
            min-height: 50;

            background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                             stop: 0 rgb(100,100,100),
                                             stop: 0.8 rgb(90,90,90));
        }

        QToolButton:hover{
            border-style: none;
            font-weight: bold;
            font-size: 20px;
            color: rgb(40, 20, 20);
            min-height: 50;

            background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                             stop: 0 rgb(130,130,130),
                                             stop: 0.8 rgb(120,120,120));
        }
    """

menuBar = """
        QMenuBar{
            border-style: none;
            font-weight: bold;
            font-size: 20px;
            color: rgb(200, 200, 200);
            min-height: 50;

            background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                             stop: 0 rgb(80,80,80),
                                             stop: 0.8 rgb(70,70,70));
        }

        QMenuBar:item:selected{
            border-style: none;
            font-weight: bold;
            font-size: 20px;
            color: rgb(230, 230, 230);
            min-height: 50;

            background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                             stop: 0 rgb(110,110,110),
                                             stop: 0.8 rgb(100,100,100));
        }

    """
