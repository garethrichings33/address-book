class Contact:
    def __init__(self, first_name, last_name, house_number,
                 street, town, postcode, phone_number, email_address, contact_id):
        try:
            self.first_name = first_name
            self.last_name = last_name
            self.house_number = house_number
            self.street = street
            self.town = town
            self.postcode = postcode
            self.phone_number = phone_number
            self.email_address = email_address
            self.contact_id = contact_id
        except TypeError as ex:
            raise

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        if not isinstance(first_name, str):
            raise TypeError("First name must be a string")
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        if not isinstance(last_name, str):
            raise TypeError("Last name must be a string")
        self._last_name = last_name

    @property
    def house_number(self):
        return self._house_number

    @house_number.setter
    def house_number(self, house_number):
        if not isinstance(house_number, str):
            raise TypeError("House number must be a string")
        self._house_number = house_number

    @property
    def street(self):
        return self._street

    @street.setter
    def street(self, street):
        if not isinstance(street, str):
            raise TypeError("Street must be a string")
        self._street = street

    @property
    def town(self):
        return self._town

    @town.setter
    def town(self, town):
        if not isinstance(town, str):
            raise TypeError("Town must be a string")
        self._town = town

    @property
    def postcode(self):
        return self._postcode

    @postcode.setter
    def postcode(self, postcode):
        if not isinstance(postcode, str):
            raise TypeError("Postcode must be a string")
        self._postcode = postcode

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        if not isinstance(phone_number, str):
            raise TypeError("Phone number must be a string")
        phone_number = phone_number.replace(" ", "")
        if not phone_number.isdigit:
            if phone_number[0] != "+":
                raise TypeError("Phone number must only contain numbers")
        self._phone_number = phone_number

    @property
    def email_address(self):
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        if not isinstance(email_address, str):
            raise TypeError("Email address must be a string")
        if not "@" in email_address and email_address != "":
            raise TypeError("Email address must contain @")
        self._email_address = email_address

    @property
    def contact_id(self):
        return self._contact_id

    @contact_id.setter
    def contact_id(self, contact_id):
        if not isinstance(contact_id, str):
            raise TypeError("Contact ID must be a string")
        self._contact_id = contact_id
