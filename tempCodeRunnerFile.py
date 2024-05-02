        def __init__(self):
            super().__init__()
            self.setupUi(self)
            self.model = AddressModel()
            self.contactList.setModel(self.model)
