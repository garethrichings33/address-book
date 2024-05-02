from MainWindow import Ui_MainWindow
from AddContactWindow import Ui_AddContactWindow
from ViewContactWindow import Ui_ViewContactWindow
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMessageBox
from ContactList import ContactList
import sys

if __name__ == "__main__":

    class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
        def __init__(self):
            super().__init__()
            self.setupUi(self)
            self._contact_list = ContactList()

            self.addContactButton.pressed.connect(self.add_contact)
            self.deleteContactButton.pressed.connect(lambda:
                                                     self.confirm_delete_contact(self.contactList.currentItem().text()))
            self.viewContactButton.pressed.connect(lambda:
                                                   self.view_contact(self.contactList.currentItem().text()))

            self.contactList.itemPressed.connect(self.activate_delete_contact)
            self.contactList.itemPressed.connect(self.activate_view_contact)

        def add_contact(self):
            self.add_contact_window = AddContactWindow(
                self, self._contact_list)
            self.setEnabled(False)
            self.add_contact_window.show()

        def activate_delete_contact(self):
            self.deleteContactButton.setEnabled(True)

        def confirm_delete_contact(self, contact_id):
            dialog = QMessageBox(self)
            dialog.setWindowTitle("Delete?")
            dialog.setIcon(QMessageBox.Question)
            dialog.setText("Really delete contact " + contact_id + "?")
            dialog.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            button = dialog.exec()
            if button == QMessageBox.Ok:
                self.delete_contact(contact_id)
            elif button == QMessageBox.Cancel:
                self.deleteContactButton.setDown(False)

        def delete_contact(self, contact):
            self._contact_list.delete_contact(contact)
            self.deleteContactButton.setEnabled(False)
            self.viewContactButton.setEnabled(False)
            self.refresh_list()

        def activate_view_contact(self):
            self.viewContactButton.setEnabled(True)

        def view_contact(self, contact_id):
            self.view_contact_window = ViewContactWindow(
                self, self._contact_list, contact_id)
            self.setEnabled(False)
            self.view_contact_window.show()

        def refresh_list(self):
            self.contactList.clear()
            for contact in self._contact_list.get_all_contacts():
                self.contactList.addItem(contact)

    class ViewContactWindow(QtWidgets.QMainWindow, Ui_ViewContactWindow):
        def __init__(self, main_window, contact_list, contact_id):
            super().__init__()
            self.setupUi(self)

            self.main_window = main_window
            self.contact_list = contact_list
            self.contact_id = contact_id

            self.extract_contact_details()
            self.populate_forms()

            self.contact_saved = True
            self.contact_altered = False

            self.connect_forms()
            self.connect_buttons()

        def extract_contact_details(self):
            contact = self.contact_list.get_contact(self.contact_id)
            self.first_name = contact.first_name
            self.last_name = contact.last_name
            self.house = contact.house_number
            self.street = contact.street
            self.town = contact.town
            self.postcode = contact.postcode
            self.phone = contact.phone_number
            self.email = contact.email_address

        def populate_forms(self):
            contact = self.contact_list.get_contact(self.contact_id)
            self.firstNameEdit.setText(contact.first_name)
            self.lastNameEdit.setText(contact.last_name)
            self.houseEdit.setText(contact.house_number)
            self.streetEdit.setText(contact.street)
            self.townEdit.setText(contact.town)
            self.postcodeEdit.setText(contact.postcode)
            self.phoneEdit.setText(contact.phone_number)
            self.emailEdit.setText(contact.email_address)
            self.contactIdEdit.setText(contact.contact_id)

        def makeEditable(self):
            self.firstNameEdit.setEnabled(True)
            self.lastNameEdit.setEnabled(True)
            self.houseEdit.setEnabled(True)
            self.streetEdit.setEnabled(True)
            self.townEdit.setEnabled(True)
            self.postcodeEdit.setEnabled(True)
            self.phoneEdit.setEnabled(True)
            self.emailEdit.setEnabled(True)
            self.contactIdEdit.setEnabled(True)

            self.editContactButton.setEnabled(False)

        def makeUnEditable(self):
            self.firstNameEdit.setEnabled(False)
            self.lastNameEdit.setEnabled(False)
            self.houseEdit.setEnabled(False)
            self.streetEdit.setEnabled(False)
            self.townEdit.setEnabled(False)
            self.postcodeEdit.setEnabled(False)
            self.phoneEdit.setEnabled(False)
            self.emailEdit.setEnabled(False)
            self.contactIdEdit.setEnabled(False)

            self.editContactButton.setEnabled(True)

        def connect_forms(self):
            self.firstNameEdit.textChanged.connect(self.contact_edited)
            self.firstNameEdit.textChanged.connect(self.update_first_name)

            self.lastNameEdit.textChanged.connect(self.contact_edited)
            self.lastNameEdit.textChanged.connect(self.update_last_name)

            self.houseEdit.textChanged.connect(self.contact_edited)
            self.houseEdit.textChanged.connect(self.update_house)

            self.streetEdit.textChanged.connect(self.contact_edited)
            self.streetEdit.textChanged.connect(self.update_street)

            self.townEdit.textChanged.connect(self.contact_edited)
            self.townEdit.textChanged.connect(self.update_town)

            self.postcodeEdit.textChanged.connect(self.contact_edited)
            self.postcodeEdit.textChanged.connect(self.update_postcode)

            self.phoneEdit.textChanged.connect(self.contact_edited)
            self.phoneEdit.textChanged.connect(self.update_phone)

            self.emailEdit.textChanged.connect(self.contact_edited)
            self.emailEdit.textChanged.connect(self.update_email)

            self.contactIdEdit.textChanged.connect(self.contact_edited)
            self.contactIdEdit.textChanged.connect(self.update_contact_id)

        def connect_buttons(self):
            self.editContactButton.pressed.connect(self.makeEditable)
            self.saveContactButton.pressed.connect(self.save_contact)
            self.closeButton.pressed.connect(self.close_contact)

        def update_first_name(self, text):
            self.first_name = text

        def update_last_name(self, text):
            self.last_name = text

        def update_house(self, text):
            self.house = text

        def update_street(self, text):
            self.street = text

        def update_town(self, text):
            self.town = text

        def update_postcode(self, text):
            self.postcode = text

        def update_phone(self, text):
            self.phone = text

        def update_email(self, text):
            self.email = text

        def update_contact_id(self, text):
            self.contact_id = text

        def first_name_contact_id(self, text):
            self.contactIdEdit.setText(text)

        def contact_edited(self):
            self.contact_altered = True
            self.contact_saved = False
            self.editContactButton.setEnabled(False)
            self.saveContactButton.setEnabled(True)

        def save_contact(self):
            if self.contact_id:
                try:
                    self.contact_list.add_contact(self.first_name, self.last_name, self.house,
                                                  self.street, self.town, self.postcode, self.phone,
                                                  self.email, self.contact_id)
                    self.contact_saved = True
                    self.contact_altered = False
                    self.saveContactButton.setEnabled(False)
                    self.makeUnEditable()
                except TypeError as ex:
                    self.save_contact_error(ex)

            self.saveContactButton.setDown(False)

        def save_contact_error(self, ex):
            dialog = QtWidgets.QMessageBox()
            dialog.setWindowTitle("Error Saving Contact")
            dialog.setText(str(ex))
            dialog.exec()

        def close_contact(self):
            print(self.contact_altered, self.contact_saved)
            if self.contact_altered and not self.contact_saved:
                self.contact_not_saved_warning()
            else:
                self.close()
                self.main_window.setEnabled(True)

        def contact_not_saved_warning(self):
            dialog = QMessageBox(self)
            dialog.setWindowTitle("Contact Not Saved")
            dialog.setIcon(QMessageBox.Question)
            dialog.setText("Really close contact without saving?")
            dialog.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            button = dialog.exec()
            if button == QMessageBox.Ok:
                self.close()
                self.main_window.setEnabled(True)
            elif button == QMessageBox.Cancel:
                self.closeButton.setDown(False)

    class AddContactWindow(QtWidgets.QMainWindow, Ui_AddContactWindow):
        def __init__(self, main_window, contact_list):
            super().__init__()
            self.setupUi(self)

            self.main_window = main_window
            self.contact_list = contact_list

            self.init_variables()
            self.empty_form()

            self.connect_forms()
            self.connect_first_name_id()
            self.connect_buttons()

        def connect_forms(self):
            self.firstNameEdit.textChanged.connect(self.contact_edited)
            self.firstNameEdit.textChanged.connect(self.update_first_name)

            self.lastNameEdit.textChanged.connect(self.contact_edited)
            self.lastNameEdit.textChanged.connect(self.update_last_name)

            self.houseEdit.textChanged.connect(self.contact_edited)
            self.houseEdit.textChanged.connect(self.update_house)

            self.streetEdit.textChanged.connect(self.contact_edited)
            self.streetEdit.textChanged.connect(self.update_street)

            self.townEdit.textChanged.connect(self.contact_edited)
            self.townEdit.textChanged.connect(self.update_town)

            self.postcodeEdit.textChanged.connect(self.contact_edited)
            self.postcodeEdit.textChanged.connect(self.update_postcode)

            self.phoneEdit.textChanged.connect(self.contact_edited)
            self.phoneEdit.textChanged.connect(self.update_phone)

            self.emailEdit.textChanged.connect(self.contact_edited)
            self.emailEdit.textChanged.connect(self.update_email)

            self.contactIdEdit.textChanged.connect(self.contact_edited)
            self.contactIdEdit.textChanged.connect(self.update_contact_id)

        def connect_first_name_id(self):
            self.firstNameEdit.textChanged.connect(self.first_name_contact_id)

        def connect_buttons(self):
            self.addContactButton.pressed.connect(self.save_new_contact)

        def empty_form(self):
            self.firstNameEdit.clear()
            self.lastNameEdit.clear()
            self.houseEdit.clear()
            self.streetEdit.clear()
            self.townEdit.clear()
            self.postcodeEdit.clear()
            self.phoneEdit.clear()
            self.emailEdit.clear()
            self.contactIdEdit.clear()

        def init_variables(self):
            self.first_name = ""
            self.last_name = ""
            self.house = ""
            self.street = ""
            self.town = ""
            self.postcode = ""
            self.phone = ""
            self.email = ""
            self.contact_id = ""

        def contact_edited(self):
            self.addContactButton.setEnabled(True)

        def update_first_name(self, text):
            self.first_name = text

        def update_last_name(self, text):
            self.last_name = text

        def update_house(self, text):
            self.house = text

        def update_street(self, text):
            self.street = text

        def update_town(self, text):
            self.town = text

        def update_postcode(self, text):
            self.postcode = text

        def update_phone(self, text):
            self.phone = text

        def update_email(self, text):
            self.email = text

        def update_contact_id(self, text):
            self.contact_id = text

        def first_name_contact_id(self, text):
            self.contactIdEdit.setText(text)

        def save_new_contact(self):
            if self.contact_id:
                try:
                    self.contact_list.add_contact(self.first_name, self.last_name, self.house,
                                                  self.street, self.town, self.postcode, self.phone,
                                                  self.email, self.contact_id)
                except TypeError as ex:
                    self.add_contact_error(ex)

                self.close()
                self.main_window.refresh_list()
                self.main_window.setEnabled(True)
            else:
                self.no_contact_id_message()

        def add_contact_error(self, ex):
            dialog = QtWidgets.QMessageBox()
            dialog.setWindowTitle("Error Adding Contact")
            dialog.setText(str(ex))
            dialog.exec()
            self.addContactButton.setDown(False)

        def no_contact_id_message(self):
            dialog = QMessageBox(self)
            dialog.setWindowTitle("No Contact ID")
            dialog.setText("Please add a contact ID")
            dialog.exec()
            self.addContactButton.setDown(False)

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
