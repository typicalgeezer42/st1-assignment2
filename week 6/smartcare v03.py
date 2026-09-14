# SmartCare v0.3 

class Patient:

    def __init__(self, patient_id, name, date_of_birth, phone):
        self.patient_id = patient_id
        self.name = name
        self.date_of_birth = date_of_birth
        self.phone = phone
        self.appointments = []

    def update_details(self, name=None, phone=None): #to change the record instead of creating duplicates
        pass    

    def matches(self, search_term):
        pass    

    def history(self): #the history of appointments
        pass    


class Practitioner:

    def __init__(self, practitioner_id, name, role):
        self.practitioner_id = practitioner_id
        self.name = name
        self.role = role
        self.appointments = []

    def is_busy(self, date_time): #only true if already booked
        pass

    def schedule_for(self, date): #shows the appintements
        pass


class Appointment:

    BOOKED = "Booked"
    CANCELLED = "Cancelled"
    COMPLETED = "Completed"

    def __init__(self, appointment_id, patient, practitioner, date_time):
        self.appointment_id = appointment_id
        self.patient = patient
        self.practitioner = practitioner
        self.date_time = date_time
        self.status = Appointment.BOOKED

    def cancel(self): #sets to cancelled
        pass

    def is_active(self): #true until cancelled or completed
        pass


class Clinic:

    def __init__(self, name):
        self.name = name
        self.patients = []
        self.practitioners = []
        self.appointments = []

    def register_patient(self, patient):
        pass

    def register_practitioner(self, practitioner):
        pass

    def find_patient(self, search_term):
        pass

    def book_appointment(self, patient, practitioner, date_time):
        pass

    def save(self):
        pass

    def load(self):
        pass