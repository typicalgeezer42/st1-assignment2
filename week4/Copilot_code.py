# Store appointments in a list
appointments = []

# Function to book an appointment
def book_appointment(patient_name, practitioner_name, appointment_time):
    # Simple validation
    if not patient_name:
        print("Patient name cannot be empty.")
        return

    # Store appointment details in a dictionary
    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }

    # Add the appointment to the list
    appointments.append(appointment)

# Function to display all appointments
def display_appointments():
    for appointment in appointments:
        print(
            f"Patient: {appointment['patient']}, "
            f"Practitioner: {appointment['practitioner']}, "
            f"Time: {appointment['time']}"
        )

# Example usage
book_appointment("Alice Smith", "Dr. John Doe", "2024-07-20 10:00 AM")
book_appointment("Bob Johnson", "Dr. Jane Roe", "2024-07-20 11:30 AM")

display_appointments()