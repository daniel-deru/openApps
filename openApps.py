from os import error
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QWidget, QRadioButton, QCheckBox, QMessageBox
import re, json, os.path as file


class Ui_OpenApps(QWidget):
    def setupUi(self, OpenApps):
        OpenApps.setObjectName("OpenApps")
        OpenApps.resize(1000, 800)

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(OpenApps)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.website_vertical_layout = QtWidgets.QVBoxLayout()
        self.website_vertical_layout.setObjectName("website_vertical_layout")

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.insert_website_button = QtWidgets.QPushButton(OpenApps)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.insert_website_button.sizePolicy().hasHeightForWidth())

        self.insert_website_button.setSizePolicy(sizePolicy)
        self.insert_website_button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.insert_website_button.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";")
        self.insert_website_button.setObjectName("insert_website_button")

        self.horizontalLayout.addWidget(self.insert_website_button)

        self.remove_website_button = QtWidgets.QPushButton(OpenApps)
        self.remove_website_button.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";")
        self.remove_website_button.setObjectName("remove_website_button")

        self.horizontalLayout.addWidget(self.remove_website_button)

        self.run_website_button = QtWidgets.QPushButton(OpenApps)
        self.run_website_button.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";")
        self.run_website_button.setObjectName("run_website_button")

        self.horizontalLayout.addWidget(self.run_website_button)

        self.website_vertical_layout.addLayout(self.horizontalLayout)

        self.select_website_gridlayout = QtWidgets.QGridLayout()
        self.select_website_gridlayout.setObjectName("select_website_gridlayout")

        self.website_vertical_layout.addLayout(self.select_website_gridlayout)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        self.website_vertical_layout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.website_vertical_layout)

        self.desktop_vertical_layout = QtWidgets.QVBoxLayout()
        self.desktop_vertical_layout.setObjectName("desktop_vertical_layout")

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.insert_desktop_button = QtWidgets.QPushButton(OpenApps)
        self.insert_desktop_button.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";")
        self.insert_desktop_button.setObjectName("insert_desktop_button")
        self.insert_desktop_button.clicked.connect(self.open_explorer_desktop)

        self.horizontalLayout_4.addWidget(self.insert_desktop_button)

        self.remove_desktop_button = QtWidgets.QPushButton(OpenApps)
        self.remove_desktop_button.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";")
        self.remove_desktop_button.setObjectName("remove_desktop_button")

        self.horizontalLayout_4.addWidget(self.remove_desktop_button)

        self.run_desktop_button = QtWidgets.QPushButton(OpenApps)
        self.run_desktop_button.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";")
        self.run_desktop_button.setObjectName("run_desktop_button")

        self.horizontalLayout_4.addWidget(self.run_desktop_button)

        self.desktop_vertical_layout.addLayout(self.horizontalLayout_4)

        self.verticalLayout_2.addLayout(self.desktop_vertical_layout)
        self.select_desktop_gridlayout = QtWidgets.QGridLayout()
        self.select_desktop_gridlayout.setObjectName("select_desktop_gridlayout")
        self.verticalLayout_2.addLayout(self.select_desktop_gridlayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.run_all_button = QtWidgets.QPushButton(OpenApps)
        self.run_all_button.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";")
        self.run_all_button.setObjectName("run_all_button")
        self.horizontalLayout_3.addWidget(self.run_all_button)

        self.save_button = QtWidgets.QPushButton(OpenApps)
        self.save_button.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";")
        self.save_button.setObjectName("save_button")
        self.horizontalLayout_3.addWidget(self.save_button)

        self.run_on_start_radio = QtWidgets.QRadioButton(OpenApps)
        self.run_on_start_radio.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";")
        self.run_on_start_radio.setObjectName("run_on_start_radio")
        self.horizontalLayout_3.addWidget(self.run_on_start_radio)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.retranslateUi(OpenApps)
        QtCore.QMetaObject.connectSlotsByName(OpenApps)
        self.update()
        self.update_checked()


    def retranslateUi(self, OpenApps):
        _translate = QtCore.QCoreApplication.translate
        OpenApps.setWindowTitle(_translate("OpenApps", "Form"))
        self.insert_website_button.setText(_translate("OpenApps", "Insert Website"))
        self.remove_website_button.setText(_translate("OpenApps", "Remove Website"))
        self.run_website_button.setText(_translate("OpenApps", "Run"))
        self.insert_desktop_button.setText(_translate("OpenApps", "Insert Desktop App"))
        self.remove_desktop_button.setText(_translate("OpenApps", "Remove Desktop App"))
        self.run_desktop_button.setText(_translate("OpenApps", "Run"))
        self.run_all_button.setText(_translate("OpenApps", "Run All"))
        self.save_button.setText(_translate("OpenApps", "Save"))
        self.run_on_start_radio.setText(_translate("OpenApps", "Run On Start Up"))

    def load_json(self):
        data_template = {
            'desktop': [],
            'desktop_is_checked': [],
            'website': [],
            'website_is_checked': []
        }
        if file.isfile("data.json"):
            if file.getsize("data.json") == 0:
                try:
                    with open("data.json", "w") as json_file:
                        json.dump(data_template, json_file)
                except IOError as error:
                    print(error)

            # IMPORTANT this will be used later to load data into application note self.data is globally accessible
            else:
                try:
                    with open("data.json", "r") as json_file:
                        self.data = json.load(json_file)
                        # print(self.data)     
                except IOError:
                    print("there was an error")
        elif not file.isfile("data.json"):
            with open("data.json", "w") as json_file:
                json.dump(data_template, json_file)

    def open_explorer_desktop(self):
        self.path = QFileDialog.getOpenFileName(self, "Open a file", "", "Executables (*.exe)")
        # app = re.search("(?<=/)(\w*)(?=\.exe)", self.path[0]).group()
        self.add_desktop()

    def add_desktop(self):
        try:
            with open("data.json", "r") as json_file:
                app = self.path[0]
                data = json.load(json_file)

                if app in data["desktop"]:
                    message = QMessageBox()
                    message.setWindowTitle("There was an error")
                    message.setIcon(QMessageBox.Warning)
                    message.setText(f"the program {self.app_name} is already in your list")
                    message.exec()

                elif app not in data["desktop"]:
                    data["desktop"].append(app)
                    data["desktop_is_checked"].append(True)
                    try:
                        with open("data.json", "w") as json_file:
                            json.dump(data, json_file, indent=2)

                    except IOError as error:
                        print(f"there was an error on line 158: {error}")
        except IOError as error:
            print(f"there was an error in the add_data method: {error}")
        finally:
            with open("data.json", "r") as json_file:
                data = json.load(json_file)
            self.update()

    def show_desktop_apps(self):
        try:
            with open("data.json", "r") as json_file:
                data = json.load(json_file)
        except IOError as error:
            print(f"there was an error in the show_desktop_apps method on line 180: {error}")
        apps = data["desktop"]
        is_checked = data["desktop_is_checked"]

        # these vars control the positioning of the checkboxes 
        # the checkboxes are not allocated with the loop for simplicity performance reasons
        rows = 0
        columns = 0

        no_of_columns = 3

        for i in range(0, len(apps)):
            # this if check creates a new row
            if (columns % no_of_columns) == 0:
                rows += 1
                columns = 0
            self.app_name = re.search("(?<=/)(\w*)(?=\.exe)", apps[i]).group()
            self.checkbox = QCheckBox(self.app_name)
            self.checkbox.setChecked(is_checked[i])
            self.checkbox.stateChanged.connect(self.update_checked)
            columns += 1
            self.select_desktop_gridlayout.addWidget(self.checkbox, rows, columns)

    def update(self):
        self.load_json()
        self.show_desktop_apps()


    def update_checked(self):
        # print(self.checkbox.isChecked())
        # print(self.checkbox.text())

        items = self.findChildren(QWidget)
        print(items)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    OpenApps = QtWidgets.QWidget()
    ui = Ui_OpenApps()
    ui.setupUi(OpenApps)
    OpenApps.show()
    sys.exit(app.exec_())
