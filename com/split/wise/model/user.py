class user:
    def __init__(self, first_name, last_name, email, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone

    def get_first_name(self):
        return self.first_name

    def set_first_name(self, fname):
        self.first_name = fname

    def get_last_name(self):
        return self.last_name

    def set_last_name(self, lname):
        self.last_name = lname

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_phone_number(self):
        return self.phone

    def set_phone_number(self, phone):
        self.phone = phone
