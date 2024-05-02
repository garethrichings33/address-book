from Contact import Contact


class ContactList:
    def __init__(self):
        self._contact_list = {}

    def add_contact(self, first_name, last_name, house_number,
                    street, town, postcode, phone_number, email, contact_id):
        try:
            contact = Contact(first_name, last_name, house_number,
                              street, town, postcode, phone_number, email, contact_id)
        except TypeError:
            raise

        self._contact_list[contact_id] = contact

    def delete_contact(self, contact_id):
        self._contact_list.pop(contact_id, None)

    def edit_contact(self, contact_id, first_name, last_name, house_number,
                     street, town, postcode, phone_number, email_address, new_contact_id):
        if not contact_id in self._contact_list:
            return

        contact = self._contact_list.pop(contact_id)

        try:
            self.add_contact(first_name, last_name, house_number,
                             street, town, postcode, phone_number, email_address, new_contact_id)
        except TypeError:
            self._contact_list[contact_id] = contact

    def get_contact(self, contact_id):
        if contact_id in self._contact_list:
            return self._contact_list[contact_id]

    def get_all_contacts(self):
        return dict(sorted(self._contact_list.items()))
