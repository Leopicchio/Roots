import sys

# NOTE!!! There was a problem finding the pyqtgraph library, so I had to run this code:
# sys.path.append("C:/Users/leo/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0/LocalCache/local-packages/Python38/Scripts");



from PySide2.QtGui import QIcon, QFocusEvent
from PySide2.QtCore import QSize, Qt, QTimer, QRunnable, QThreadPool
from PySide2.QtCore import QObject, Signal, Slot, QEvent
from PySide2.QtWidgets import QSizePolicy, QSpacerItem, QApplication, QMainWindow, QPushButton
from PySide2.QtWidgets import QVBoxLayout, QHBoxLayout, QToolBar, QStatusBar, QAction, QProgressDialog, QLabel
from PySide2.QtWidgets import QLineEdit, QDialog, QDialogButtonBox, QComboBox, QFrame, QMessageBox
from PySide2.QtWidgets import QMenu, QFileDialog

import os
import shutil
import socket
import database_gestion as database
import styles
import strings

import numpy
import pyqtgraph
from pyqtgraph import PlotWidget, plot

import pyqtgraph.examples
import classifier




## ------------------------------------------- ROOTSAPP ----------------------------------------
# this is the main window class, where most of the logic is and which defines the window graphical interface.

class RootsApp(QMainWindow):
    standard_deviation_threshold = 0.1                      # when I receive a measurement from the sensor I check if its standard deviation; if it's too low it means the sensor is not working
    temporary_database_filename = "temporary.db"            # the current session is stored in a temporary database. When the user saves, it is copied at the desired location
    def __init__(self):
        super().__init__();
        self.setWindowTitle("Roots")
        self.setFixedWidth(1200)
        self.resize(1200, 1200)
        self.threadpool = QThreadPool();
        self.object_list = list()
        self.is_training_on = False
        self.interaction_under_training = None
        self.n_measurements_collected = 0
        self.n_measurements_to_collect = 3
        self.sensor_not_responding = True
        self.sensor_not_responding_timeout = 2000        # milliseconds
        self.database_connection = self.create_temporary_database()
        self.active_object = None
        self.number_of_objects_added = 0
        self.sensor_start_freq = 250000
        self.sensor_end_freq = 3000000

    # creates the plot
        self.plotWidget = pyqtgraph.PlotWidget(title = "Sensor Response")
        self.plotWidget.setFixedHeight(300)
        self.plotWidget.getAxis("bottom").setLabel("Excitation frequency", "Hz")
        self.plotWidget.getAxis("left").setLabel("Volts", "V")
        self.dataPlot = self.plotWidget.plot()

    # timer used to see if the sensor is responding
        self.timer = QTimer()
        self.timer.setInterval(self.sensor_not_responding_timeout)
        self.timer.timeout.connect(self.timer_timeout)
        self.timer_timeout()

    # defines the actions in the file menu with button actions
        iconExit = QIcon("icons/icon_exit.png")
        btnActionExit = QAction(iconExit, "Exit", self)
        btnActionExit.setStatusTip("Click to terminate the program")
        btnActionExit.triggered.connect(self.exit)

        iconSave = QIcon("icons/icon_save.ico")
        buttonActionSave = QAction(iconSave, "Save current set of objects", self)
        # buttonActionSave.setStatusTip("Click to perform action 2")
        buttonActionSave.triggered.connect(self.save)

        iconOpen = QIcon("icons/icon_load.png")
        buttonActionOpen = QAction(iconOpen, "Load set of objects", self)
        buttonActionOpen.triggered.connect(self.open)

    # toolbar
        toolBar = QToolBar("Toolbar")
        toolBar.addAction(buttonActionSave)
        toolBar.addAction(buttonActionOpen)
        toolBar.setIconSize(QSize(64, 64))
        toolBar.setStyleSheet(styles.toolbar)
        self.addToolBar(toolBar)

    # menu
        menuBar = self.menuBar()
        menuBar.setStyleSheet(styles.menuBar)
        menuFile = menuBar.addMenu("File")
        menuOptions = menuBar.addMenu("Options")
        menuView = menuBar.addMenu("View")
        menuConnect = menuBar.addMenu("Connect")
        menuFile.addAction(buttonActionSave)
        menuFile.addAction(buttonActionOpen)
        menuFile.addAction(btnActionExit)

    # status bar
        self.setStatusBar(QStatusBar(self))

    # creates the "My Objects" label
        labelMyObjects = QLabel("My Objects")
        labelMyObjects.setFixedHeight(100)
        labelMyObjects.setAlignment(Qt.AlignCenter)
        labelMyObjects.setStyleSheet(styles.labelMyObjects)

    # button "add object"
        icon_plus = QIcon("icons/icon_add.png")
        self.btn_create_object = QPushButton("Add Object")
        self.btn_create_object.setCheckable(False)
        self.btn_create_object.setIcon(icon_plus)
        self.btn_create_object.setFixedHeight(80)
        self.btn_create_object.setStyleSheet(styles.addObjectButton)
        self.btn_create_object.clicked.connect(self.create_object)

    # defines the layout of the "My Objects" section
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setContentsMargins(0,0,0,0)
        self.verticalLayout.addWidget(labelMyObjects)
        self.verticalLayout.addWidget(self.btn_create_object)
        self.spacer = QSpacerItem(0,2000, QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.addSpacerItem(self.spacer)  #adds spacer

    # defines the ComboBox which holds the names of the objects
        self.comboBox = QComboBox()
        self.comboBox.addItem("- no object selected")
        self.comboBox.currentIndexChanged.connect(self.comboBox_index_changed)
        self.comboBox.setFixedSize(300, 40)
        self.comboBox.setStyleSheet(styles.comboBox)
        self.update_comboBox()

    # defines the label "Selected Object" (above the comboBox)
        self.labelComboBox = QLabel()
        self.labelComboBox.setText("Selected Object:")
        self.labelComboBox.setStyleSheet(styles.labelComboBox)
        self.labelComboBox.adjustSize()

    # vertical layout for the combobox and its label
        self.VLayoutComboBox = QVBoxLayout()
        self.VLayoutComboBox.addWidget(self.labelComboBox)
        self.VLayoutComboBox.addWidget(self.comboBox)

    # label with the output text (the big one on the right)
        self.labelClassification = QLabel()
        self.labelClassification.setText("No interaction detected")
        self.labelClassification.setFixedHeight(80)
        self.labelClassification.setStyleSheet(styles.labelClassification)
        self.labelClassification.adjustSize()

        HLayoutComboBox = QHBoxLayout()
        HLayoutComboBox.addLayout(self.VLayoutComboBox)
        HLayoutComboBox.addSpacerItem(QSpacerItem(1000,0, QSizePolicy.Expanding, QSizePolicy.Expanding));  #adds spacer
        HLayoutComboBox.addWidget(self.labelClassification)

    # creates a frame that contains the combobox and the labels
        frame = QFrame()
        frame.setStyleSheet(styles.frame)
        frame.setLayout(HLayoutComboBox)

    # sets the window layout with the elements created before
        self.windowLayout = QVBoxLayout()
        self.windowLayout.addWidget(self.plotWidget)
        self.windowLayout.addWidget(frame)
        self.windowLayout.addLayout(self.verticalLayout)

    # puts everything into a frame and displays it on the window
        self.mainWindowFrame = QFrame()
        self.mainWindowFrame.setLayout(self.windowLayout)
        self.mainWindowFrame.setStyleSheet(styles.mainWindowFrame)
        self.setCentralWidget(self.mainWindowFrame)

        self.create_object()        # creates one object at the beginning



# -----------------------------------------------------------------------------------------------------------
# Shows a welcome message
    def show_welcome_msg(self):
        welcome_msg = QMessageBox()
        welcome_msg.setText("Welcome to the Roots application!")
        welcome_msg.setIcon(QMessageBox.Information)
        welcome_msg.setInformativeText(strings.welcome_text)
        welcome_msg.setWindowTitle("Welcome")
        welcome_msg.exec_()


# -----------------------------------------------------------------------------------------------------------
# When the user changes the object in the combobox, updates the active object
    def comboBox_index_changed(self, index):
        object_name = self.comboBox.currentText()
        for object in self.object_list:
            if object.name == object_name:
                self.set_active_object(object)
                print("DEBUG: selected object changed. Object name: {0}".format(object.name))
                return

# -----------------------------------------------------------------------------------------------------------
# This function allows to save the current objects on a file
    def save(self):
        current_path = os.getcwd()
        directory_path = current_path + "/Saved_Workspaces"

        if not os.path.exists(directory_path):
            os.mkdir(directory_path)

        file_path = None
        [file_path, file_extension] = QFileDialog.getSaveFileName(self,"Roots", directory_path, "Roots database (*.db)")
        if file_path is None:
            return

        temp_database_path = current_path + "/" + RootsApp.temporary_database_filename
        shutil.copyfile(temp_database_path, file_path)      # copies the temporary database to save the current workspace
        return



# -----------------------------------------------------------------------------------------------------------
# this function creates a clean database where all the data of this session will be temporarily stored
    def create_temporary_database(self):
        current_path = os.getcwd()
        file_path = current_path + "/" + RootsApp.temporary_database_filename

        if os.path.exists(file_path):   # if the database is already there it deletes it to reset it
            os.remove(file_path)
            print("DEBUG: removing database. (in 'RootsApp.create_temporary_database()'")

        database_connection = database.create_connection(RootsApp.temporary_database_filename)  # creates the temporary database
        database.create_tables(database_connection)                                             # initializes the database
        database.reset_db(database_connection)                                                  # resets the database (not needed but it doesn't cost anything to put it)

        return database_connection


# -----------------------------------------------------------------------------------------------------------
# This function allows to load previously created objects from a file
    def open(self):
        current_path = os.getcwd()
        saved_files_directory = current_path + "/Saved_Workspaces"

        [file_path, file_extension] = QFileDialog.getOpenFileName(self,"Roots", saved_files_directory, "Roots database (*.db)");
        if file_path == '':
            return

        for object in self.object_list.copy():     # deletes all the objects
            print("DEBUG: deleting object {0} (in 'open()')".format(object.name))
            self.delete_object(object)

        temp_database_path = current_path + "/" + RootsApp.temporary_database_filename
        self.database_connection.close()
        os.remove(temp_database_path)
        shutil.copyfile(file_path, temp_database_path)      # replaces the temporary database with the file to open
        self.database_connection = database.create_connection(temp_database_path)

        object_tuples = database.get_all_objects(self.database_connection)
        for object_tuple in object_tuples:
            object_ID, object_name = object_tuple
            location_IDs = database.get_locations_id_for_object(self.database_connection, object_ID)
            formatted_location_IDs = []
            for location_ID in location_IDs:
                formatted_location_IDs.append(location_ID[0])

            print("DEBUG: loading object {0} with location IDs {1}. (in 'RootsApp.open()')".format(object_name, formatted_location_IDs))
            self.add_object(object_name, object_ID, formatted_location_IDs)
            self.train_classifiers()
        return


# -----------------------------------------------------------------------------------------------------------
# This function updates the ComboBox whenever objects are created, destroyed or the active object has changed
    def update_comboBox(self):
        print("DEBUG: repainting ComboBox. (in 'RootsApp.update_comboBox()'")
        self.comboBox.clear()
        self.comboBox.addItem("none")
        for object in self.object_list:
            self.comboBox.addItem(object.name)
        self.comboBox.adjustSize()


# -----------------------------------------------------------------------------------------------------------
# This is a timer which is restarted every time a measurement is received. If it elapses it means that the sesnor is not connected
    def timer_timeout(self):
        print("DEBUG: timer timeout. (in 'RootsApp.timer_timeout()'")
        self.sensor_not_responding = True
        self.statusBar().showMessage(strings.sensor_disconnected)
        self.statusBar().setStyleSheet(styles.statusBarError)
        self.plotWidget.setTitle("Sensor not connected")

# -----------------------------------------------------------------------------------------------------------
# This function creates a new object in the database and then calls the "add_object" function, which adds the newly created object to the application
    def create_object(self):
        new_object_name = "Object {0}".format(self.number_of_objects_added + 1)
        [new_object_ID, location_IDs] = database.create_object(self.database_connection, new_object_name)
        self.add_object(new_object_name, new_object_ID, location_IDs)


# -----------------------------------------------------------------------------------------------------------
# This function deletes an object from the database, and from the application object list. It alsos destroys the object
    def delete_object(self, object):
        print("DEBUG: deleting object {0}. (in 'RootsApp.delete_object()')".format(object.ID))
        database.delete_object(self.database_connection, object.ID)
        self.object_list.remove(object)
        self.verticalLayout.removeItem(object.layout)
        self.update_comboBox()
        object.delete()


# -----------------------------------------------------------------------------------------------------------
# This function adds an object to the current application. Note that if you want to create an object ex-novo you should call "create_object". This function is useful when loading existing objects from a file
    def add_object(self, name, object_ID, location_IDs):
        self.number_of_objects_added += 1
        new_object = Object(name, object_ID, location_IDs, self)
        self.object_list.append(new_object)

        for ID in location_IDs:                                         # initializes the measurements with 0 if the measurement is empty
            #print("DEBUG: initializing location ID {0}".format(ID))
            measurements = database.get_measurements_for_location(self.database_connection, ID)

            print("DEBUG: location {0} of object {1} is trained: {2}. (in 'RootsApp.add_object()')".format(ID, new_object.name, database.is_location_trained(self.database_connection, ID)))
            if len(measurements) == 0:
                database.save_points(self.database_connection, [0], ID)
                database.set_location_trained(self.database_connection, ID, "FALSE")
            elif database.is_location_trained(self.database_connection, ID) == "TRUE":
                new_object.get_interaction_by_ID(ID).setCalibrated(True)

        # inserts the newly created object before the "Add Object" button
        index = self.verticalLayout.indexOf(self.btn_create_object)
        self.verticalLayout.insertLayout(index, new_object.layout)
        self.update_comboBox()
        print("DEBUG: object {0} added. (in 'RootsApp.add_object()')".format(new_object.name))
        return



# -----------------------------------------------------------------------------------------------------------
# This function takes as input the measurement data and formats it to plot it on the graph
    def update_graph(self, data):
        frequency_step = (self.sensor_end_freq - self.sensor_start_freq) / len(data)
        x_axis = numpy.arange(self.sensor_start_freq, self.sensor_end_freq, frequency_step)
        formatted_data = numpy.transpose(numpy.asarray([x_axis, data]))
        self.dataPlot.setData(formatted_data)


# -----------------------------------------------------------------------------------------------------------
# This function starts the UDP server that receives the measurements
    def run_UDP_server(self, UDP_IP, UDP_PORT):
        self.UDPServer = UDPServer(UDP_IP, UDP_PORT)
        self.UDPServer.signals.measurementReceived.connect(self.process_measurement)
        self.threadpool.start(self.UDPServer)


# -----------------------------------------------------------------------------------------------------------
# This function changes some global variables to tell the application to save the incoming measurements into the database. The measurements belong to the interaction passed as argument
    def start_collecting_measurements(self, interaction):
        if self.sensor_not_responding:
            print("DEBUG: warning! Can't start calibration, the sensor is not responding! (in 'RootsApp.start_collecting_measurements()')")
            error_msg = QMessageBox()
            error_msg.setText("Can't start calibration!")
            error_msg.setIcon(QMessageBox.Critical)
            error_msg.setInformativeText('The sensor is not responding, make sure it is connected')
            error_msg.setWindowTitle("Error")
            error_msg.exec_()
        else:
            print("starting to collect measurements into the database at location ID {0} (in 'RootsApp.start_collecting_measurements()')".format(interaction.ID));
            self.is_training_on = True
            self.interaction_under_training = interaction
            database.delete_measurements_from_location(self.database_connection, interaction.ID)   # resets the location measurements

            self.progress_dialog = QProgressDialog("Calibrating", "Abort", 0, self.n_measurements_to_collect, self)
            self.progress_dialog.setWindowModality(Qt.WindowModal)
            self.progress_dialog.setWindowTitle("Calibration")
            self.progress_dialog.setFixedSize(400, 200)
            self.progress_dialog.setValue(0)
            self.progress_dialog.exec_()



# -----------------------------------------------------------------------------------------------------------
# This function is called by the UDP thread every time that a measurement is received. It does the following:
#   1. Plots the incoming measurement
#   2. IF training mode IS on:
#           Predicts the interaction (tries to guess where the user is touching)
#      ELSE:
#           Saves the measurement and retrains the classifier with the new data
    def process_measurement(self, received_data):
        self.sensor_not_responding = False
        self.plotWidget.setTitle("Sensor response")
        self.timer.start()                                          # starts the timer that checks if we are receiving data from the sensor

        measurement = received_data.split(' ')                      # get rid of separator
        measurement = [float(i) for i in measurement]               # convert strings to float
        self.update_graph(measurement)
        self.predict_interaction(measurement)

        # checks the standard deviation of the received data to see if the sensor is working well
        if (numpy.std(measurement) < self.standard_deviation_threshold):
            self.statusBar().showMessage(strings.sensor_not_working)
            self.statusBar().setStyleSheet(styles.statusBarError)
        else:
            self.statusBar().setStyleSheet(styles.statusBar)

        if self.is_training_on:
            print("saving measurement {0} into database at location_ID {1}. (in 'RootsApp.process_measurement()')".format(self.n_measurements_collected + 1, self.interaction_under_training.ID))
            database.save_points(self.database_connection, measurement, self.interaction_under_training.ID)
            self.n_measurements_collected += 1
            self.progress_dialog.setValue(self.n_measurements_collected)
            if (self.n_measurements_collected >= self.n_measurements_to_collect):
                self.is_training_on = False
                self.n_measurements_collected = 0
                print("DEBUG: {0} measurements were saved at location_ID {1}. (in 'RootsApp.process_measurement()')".format(self.n_measurements_to_collect, self.interaction_under_training.ID))
                self.train_classifiers()
                self.interaction_under_training.setCalibrated(True)     # this makes the button "Calibrate" change coulour


# -----------------------------------------------------------------------------------------------------------
# This function retrains the classifiers using all the measurements present in the database and assigns to each object its classifier
    def train_classifiers(self):
        #[objects_ID, classifiers]
        classifiers = classifier.get_classifiers(self.database_connection)
        print("DEBUG: the following classifiers were created: {0}. (in 'RootsApp.train_classifiers')".format(classifiers))
        for object in self.object_list:
            for index, tuple in enumerate(classifiers):
                object_ID, classif = tuple;  # extracts the object ID and the classifier from the tuple
                if object_ID == object.ID:
                    object.classifier = classif
                    del classifiers[index]


# -----------------------------------------------------------------------------------------------------------
# This function changes the current active object (the software tries to guess where the user is touching using the calibration data from the active object)
    def set_active_object(self, active_object):
        self.active_object = active_object

        for obj in self.object_list:
            if obj == active_object:
                active_object.set_highlighted(True)
            else:
                obj.set_highlighted(False)

        index = self.comboBox.findText(self.active_object.name)     # updates the index of the ComboBox
        self.comboBox.setCurrentIndex(index)


# -----------------------------------------------------------------------------------------------------------
# This function changes the name of an object. It updates the database AND the application data structure.
    def rename_object(self, object, new_name):
        print("DEBUG: changing name of object '{0}' (in 'RootsApp.rename_object')".format(object.name))
        object.set_name(new_name)
        database.rename_object(self.database_connection, object.ID, new_name)
        self.update_comboBox()



# -----------------------------------------------------------------------------------------------------------
# This function uses the classifier of the active object to guess where the user is touching, based on the incoming measurement
    def predict_interaction(self, measurement):
        if (len(self.object_list) <= 0):
            self.labelClassification.setText("No objects available")
            self.statusBar().showMessage(strings.no_objects)
            return
        if self.active_object is None:
            self.labelClassification.setText("No object selected")
            self.statusBar().showMessage(strings.no_object_selected)
            return
        if self.active_object.classifier is None:
            self.labelClassification.setText("The object is not calibrated")
            self.statusBar().showMessage(strings.object_not_calibrated)
            return
        else:
            predicted_interaction_id = self.active_object.classifier(measurement)
            interaction = self.active_object.get_interaction_by_ID(predicted_interaction_id)
            self.labelClassification.setText(interaction.name)
            self.statusBar().showMessage("")
            #print("DEBUG: predicted interaction ID: ", interaction.ID)



# -----------------------------------------------------------------------------------------------------------
# This is a system event that gets called whenever the user tries to close the application. It calls the "exit()"
# function (just below) to open a dialog to make sure the user really wants to quit.
    def closeEvent(self, event):
        if not self.exit():
            event.ignore()


# -----------------------------------------------------------------------------------------------------------
# This function gets called when the user cliks on the "Exit" button in the "File" menu or when it tries to close the window (indirectly)
# Here we open a dialog to make sure the user really wants to quit.
    def exit(self):
        dialogWindow = DialogExit()
        answer = dialogWindow.exec_()
        if (answer == True):
            self.UDPServer.stop()
            self.close()
        return answer














############################### UDPServerThread Class ###################################

# this class is used to create a thread which receives the messages sent by the ESP trhough an UDP socket
class UDPServer(QRunnable):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        UDP_IP = args[0]
        UDP_PORT = args[1]

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
        self.sock.bind((UDP_IP, UDP_PORT))
        self.sock.settimeout(0.5)
        self.signals = UDPServerSignals()      # this line creates the Signals used to communicate between the thread and the main window
        self.is_running = True
        self.msg_start_received = False
        self.received_data = ""

# -----------------------------------------------------------------------------------------------------------
# Stops the thread
    def stop(self):
        print("DEBUG: Stopping UDP server thread (in 'UDPServer.stop()')")
        self.is_running = False


# -----------------------------------------------------------------------------------------------------------
# Here is the code that runs inside the thread
    @Slot()
    def run(self):
        while True:
            try:
                if (self.is_running == False):
                    print("DEBUG: raising UDP server stopped exception. (in 'UDPServer.run()')")
                    raise UDPServerStoppedException

                data, addr = self.sock.recvfrom(1024) # buffer size is 1024 bytes
                data = data.decode()
                #print("Received datapoint: {0}".format(data))

                if data == "s":
                    self.msg_start_received = True
                elif data == "e":
                    self.signals.measurementReceived.emit(self.received_data)  # the "measurementReceived" signal of the thread is connected to the "processMeasurement()" function of the application
                else:
                    self.received_data = data

            except UDPServerStoppedException:
                print("DEBUG: UDP server stopped. (in 'UDPServer.run()')")
                return
            except socket.timeout:
                print ("DEBUG: Socket timed out. (in 'UDPServer.run()')")





############################### UDPServerSignals Class ###################################

class UDPServerSignals(QObject):
    measurementReceived = Signal(dict)


############################### UDPServerStoppedException Class ###################################
class UDPServerStoppedException(Exception):
    pass






############################### DialogExit Class ###################################
# This class defines the dialog that opens whenever a user tries to exit the application. It simply asks if he/she is really sure.
class DialogExit(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exit?")

        QBtn = QDialogButtonBox.Yes | QDialogButtonBox.No
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.layout = QVBoxLayout()
        message = QLabel("Are you sure you want to exit?")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)







############################### Object Class ###################################
# This is the data structure that holds all information useful for the graphical interface of the object (data is stored in the database).
# Note that this class defines and manages the graphical elements (buttons, labels etc) of each object.
class Object():
    number_of_objects = 0;
    def __init__(self, name, ID, interaction_IDs, parent_application):
        Object.number_of_objects += 1
        self.highlighted = False
        self.parent_application = parent_application
        self.name = name
        self.ID = ID
        self.max_number_of_interactions = 4
        self.interaction = [None]*self.max_number_of_interactions
        self.classifier = None

        for index in range(0,self.max_number_of_interactions):
            self.interaction[index] = Interaction("Interaction {0}".format(index+1), interaction_IDs[index], parent_application)

        self.label = EditableLabel(self.name, self)      # passes also a reference to the parent object
        self.btn_delete = QPushButton()
        self.layout = QHBoxLayout()
        self.icon_delete = QIcon("icons/delete_icon.jpg")

        self.label.setFixedSize(300, 100)
        self.label.setReadOnly(True)
        self.label.setFrame(False)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet(styles.objectNameLabel)

        # defines the style of the buttons
        self.btn_delete = QPushButton()
        self.btn_delete.setFixedSize(100, 100)
        self.btn_delete.setIcon(self.icon_delete)
        self.btn_delete.setStyleSheet(styles.calibrateButton)
        self.btn_delete.clicked.connect(lambda: self.parent_application.delete_object(self))

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.btn_delete)
        self.layout.addWidget(self.label)
        for interaction in self.interaction:
            self.layout.addWidget(interaction.button)
        self.layout.addSpacerItem(QSpacerItem(0,0, QSizePolicy.Expanding, QSizePolicy.Expanding))    # adds a white spacer on the right
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.setSpacing(0)

# changes the name of the object (actually not very useful)
    def set_name(self, new_name):
        self.name = new_name
        self.label.setText(new_name)

# Returns an object of type "Interaction" with the corresponding ID
    def get_interaction_by_ID(self, interaction_ID):
        for interaction in self.interaction:
            if interaction_ID == interaction.ID:
                return interaction

# It changes the color of the object. Useful to show that this is the active object.
    def set_highlighted(self, value):
        if value is False:
            self.highlighted = False
            self.label.setStyleSheet(styles.objectNameLabel)
            self.btn_delete.setStyleSheet(styles.calibrateButton)
            for interaction in self.interaction:
                if interaction.calibrated:
                    interaction.button.setStyleSheet(styles.calibrateButton_calibrated)
                else:
                    interaction.button.setStyleSheet(styles.calibrateButton)
        elif value is True:
            self.highlighted = True
            self.label.setStyleSheet(styles.objectNameLabel_highlighted)
            self.btn_delete.setStyleSheet(styles.calibrateButton_highlighted)
            for interaction in self.interaction:
                if interaction.calibrated:
                    interaction.button.setStyleSheet(styles.calibrateButton_calibrated_highlighted)
                else:
                    interaction.button.setStyleSheet(styles.calibrateButton_highlighted)
        else:
            return


# Deletes the object and all the graphical elements inside it.
    def delete(self):
        Object.number_of_objects -= 1

        self.btn_delete.deleteLater()
        self.label.deleteLater();
        for interaction in self.interaction:
            interaction.button.deleteLater()
        self.layout.deleteLater()

        del self;




############################### Interaction Class ###################################
# I chose to create a class to represent an Interaction because it would make it easier to expand the number of possible interactions per object.
# This class basically contains a button  "Calibrate interaction" and some useful information about the interaction (calibrated or not etc)
class Interaction():
    def __init__(self, name, ID, parent_application):
        self.parent_application = parent_application
        self.name = name
        self.ID = ID            # every interaction with the object has an ID assigned to access it in the database
        self.calibrated = False
        self.button = QPushButton("Calibrate\n {0}".format(name))
        self.button.setFixedSize(200, 100)
        self.button.setStyleSheet(styles.calibrateButton)
        self.button.clicked.connect(lambda: self.parent_application.start_collecting_measurements(self))

    def setCalibrated(self, value):
        if value is True:
            self.calibrated = True
            self.button.setStyleSheet(styles.calibrateButton_calibrated)
        elif value is False:
            self.calibrated = False
        else:
            print("DEBUG: incorrect argument, expected 'bool' instead")



############################### EditableLabel Class ###################################
# I created this class to extend the functionality of the QLineEdit widget (to be able to process doubleClick and other events)
class EditableLabel(QLineEdit):
    def __init__(self, name, parent_object):
        QLineEdit.__init__(self, name)
        self.parent_object = parent_object

    def mouseDoubleClickEvent(self, event):
        self.setReadOnly(False)
        self.selectAll()

    def mousePressEvent(self, event):
        if event.button() is Qt.LeftButton:
            self.parent_object.parent_application.set_active_object(self.parent_object)
        QLineEdit.mousePressEvent(self, event)

    def focusOutEvent(self, event):
        QLineEdit.focusOutEvent(self, event)
        self.setReadOnly(True)
        self.parent_object.parent_application.rename_object(self.parent_object, self.text())


    def keyPressEvent(self, event):
        QLineEdit.keyPressEvent(self, event);
        if (event.key() == Qt.Key_Return):
            self.focusOutEvent(QFocusEvent( QEvent.FocusOut, Qt.MouseFocusReason))

# this defines the menu that opens up when the user right clicks on the name of an object
    def contextMenuEvent(self, event):
        print("Label tries to open menu")
        menu = QMenu()
        menu.addAction("Rename")
        menu.actions()[0].triggered.connect(self.mouseDoubleClickEvent)
        menu.addAction("Set as current object")
        menu.actions()[1].triggered.connect(lambda: self.parent_object.parent_application.set_active_object(self.parent_object))
        menu.addAction("Delete")
        menu.actions()[2].triggered.connect(self.parent_object.remove)
        menu.exec_(event.globalPos())
        del menu






############################### MAIN ##########################################
# Here we create the main window, we start the UDP server thread and we show the welcome message

if __name__ == "__main__":

    hostname = socket.gethostname()     # gets the IP address of the host computer
    IP_address = socket.gethostbyname(hostname)

    UDP_IP = IP_address     # this is the IP address of the host computer and it MUST be given to the ESP8266 in order to establish a communication
    UDP_PORT = 5005         # this is a predefined number that we chose and that MUST be the same as the one in the code of the ESP8266

    app = QApplication(sys.argv)

    window = RootsApp()
    window.show()
    window.run_UDP_server(UDP_IP, UDP_PORT)    # creates the UDP server thread
    window.show_welcome_msg()

    sys.exit(app.exec_())
