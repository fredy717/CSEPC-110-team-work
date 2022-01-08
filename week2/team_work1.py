class card_identification:
    def __init__(self):
        self._month = None
        self._eye_color = None
        self._hair_color = None
        self._job_title = None
        self._phone = None
        self._email = None
        self._training = None
        self._last_name = None
        self._first_name = None
        self._id_number = 0

    def get_first_name(self):
        return self._first_name

    def set_first_name(self, first_name):
        self._first_name = first_name

    def get_last_name(self):
        return self._last_name

    def set_last_name(self, last_name):
        self._last_name = last_name

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

    def get_phone(self):
        return self._phone

    def set_phone(self, phone):
        self._phone = phone

    def get_job_title(self):
        return self._job_title

    def set_job_title(self, job_title):
        self._job_title = job_title

    def get_id_number(self):
        return self._id_number

    def set_id_number(self, id_number):
        self._id_number = id_number

    def get_hair_color(self):
        return self._email

    def set_hair_color(self, hair_color):
        self._hair_color = hair_color

    def get_eye_color(self):
        return self._eye_color

    def set_eye_color(self, eye_color):
        self._eye_color = eye_color

    def get_month(self):
        return self._month

    def set_month(self, month):
        self._month = month

    def get_training(self):
        return self._training

    def set_training(self, training):
        self._training = training

    first_name = property(get_first_name, set_first_name)
    last_name = property(get_last_name, set_last_name)
    email = property(get_email, set_email)
    phone = property(get_phone, set_phone)
    job_title = property(get_job_title, set_job_title)
    id_number = property(get_id_number, set_id_number)
    hair_color = property(get_hair_color, set_hair_color)
    eye_color = property(get_eye_color, set_eye_color)
    month = property(get_month, set_month)
    training = property(get_training, set_training)

    def show_identification_card(self):
        return '''
        The ID Card is:
        ----------------------------------------
        %s, %s
        %s
        D: %s
        
        %s
        %s
        
        Hair: %s\tEyes: %s
        Month: %s\tTraining: %s
        ----------------------------------------''' \
               % (self._first_name, self._last_name, self._email, self._phone,
                  self._job_title, self._id_number, self._hair_color,
                  self._eye_color, self._month, self._training)


def get_identification_card():
    card = card_identification()
    print("Please enter the following information:\n")
    card.first_name = input("First name: ")
    card.last_name = input("Last name: ")
    card.email = input("Email address: ")
    card.phone = input("Phone number: ")
    card.job_title = input("Job title: ")
    card.id_number = input("ID Number: ")
    card.hair_color = input("Hair color: ")
    card.eye_color = input("Eye color: ")
    card.month = input("Starting Month: ")
    card.training = input("Completed additional training? ")
    print(card.show_identification_card())


get_identification_card()
