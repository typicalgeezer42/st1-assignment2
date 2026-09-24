from datetime import date, datetime
from enum import Enum
from typing import List, Optional


# Domain exceptions 
class SmartCareError(Exception):
    """base class error."""


class ValidationError(SmartCareError):
    """A required value was missing or the wrong type"""


class StatusTransitionError(SmartCareError):
    """A status change the rules do not allo"""


class DoubleBookingError(SmartCareError):
    """The practitioner is already booked at that time"""


#statuses
class AppointmentStatus(Enum):
    BOOKED = "Booked"
    CANCELLED = "Cancelled"
    COMPLETED = "Completed"

    def __str__(self) -> str:
        return self.value

def _require_text(value: str, field_name: str) -> str:
    """Return the value trimmed, or raise ValidationError if it is blank."""
    if not isinstance(value, str) or not value.strip():
        raise ValidationError(f"{field_name} is required and cannot be blank.")
    return value.strip()
#patient class
class Patient:
    def __init__(self, patient_id: str, name: str, date_of_birth: date,
                 phone: str) -> None:
        self.patient_id = _require_text(patient_id, "Patient identifier")
        self.name = _require_text(name, "Patient name")
        if not isinstance(date_of_birth, date):
            raise ValidationError("Date of birth is required.")
        self.date_of_birth = date_of_birth
        self.phone = _require_text(phone, "Phone number")
        self.appointments: List["Appointment"] = []

    def update_details(self, name: Optional[str] = None,
                       phone: Optional[str] = None) -> None:
        """Change this record."""
        if name is not None:
            self.name = _require_text(name, "Patient name")
        if phone is not None:
            self.phone = _require_text(phone, "Phone number")

    def matches(self, search_term: str) -> bool:
        term = _require_text(search_term, "Search term").lower()
        return term in self.name.lower() or term == self.patient_id.lower()

    def add_appointment(self, appointment: "Appointment") -> None:
        """Called by the Appointment constructor."""
        if appointment not in self.appointments:
            self.appointments.append(appointment)

    def history(self) -> List["Appointment"]:
        """Every appointment"""
        return sorted(self.appointments, key=lambda a: a.date_time)

    def __str__(self) -> str:
        return f"{self.name} ({self.patient_id})"

#practitioner clas
class Practitioner:
    """A practitioner and their own schedule."""

    def __init__(self, practitioner_id: str, name: str, specialty: str) -> None:
        self.practitioner_id = _require_text(practitioner_id, "Practitioner identifier")
        self.name = _require_text(name, "Practitioner name")
        self.specialty = _require_text(specialty, "Specialty")
        self.appointments: List["Appointment"] = []

    def add_appointment(self, appointment: "Appointment") -> None:
        """Called by the Appointment constructor."""
        if appointment not in self.appointments:
            self.appointments.append(appointment)

    def is_busy(self, date_time: datetime) -> bool:
        """appoitnment already holds this slot"""
        return any(a.is_active() and a.date_time == date_time
                   for a in self.appointments)

    def schedule_for(self, day: date) -> List["Appointment"]:
        """appontment list"""
        on_day = [a for a in self.appointments if a.date_time.date() == day]
        return sorted(on_day, key=lambda a: a.date_time)

    def __str__(self) -> str:
        return f"{self.name}, {self.specialty} ({self.practitioner_id})"


class Appointment:
    _ALLOWED_TRANSITIONS = {
        AppointmentStatus.BOOKED: (AppointmentStatus.CANCELLED,
                                   AppointmentStatus.COMPLETED),
        AppointmentStatus.CANCELLED: (),
        AppointmentStatus.COMPLETED: (),
    }

    def __init__(self, appointment_id: str, patient: Patient,
                 practitioner: Practitioner, date_time: datetime) -> None:
        self.appointment_id = _require_text(appointment_id, "Appointment identifier")
        if not isinstance(patient, Patient):
            raise ValidationError("A patient is required to book an appointment.")
        if not isinstance(practitioner, Practitioner):
            raise ValidationError("A practitioner is required to book an appointment.")
        if not isinstance(date_time, datetime):
            raise ValidationError("A date and time is required to book an appointment.")
        if practitioner.is_busy(date_time):
            raise DoubleBookingError(
                f"{practitioner.name} already has an appointment at "
                f"{date_time:%d/%m/%Y %H:%M}. The booking was not created.")
        self.patient = patient
        self.practitioner = practitioner
        self.date_time = date_time
        self._status = AppointmentStatus.BOOKED
        patient.add_appointment(self)
        practitioner.add_appointment(self)

    @property
    def status(self) -> AppointmentStatus:
        """readonly unless changed by only below"""
        return self._status

    def _change_status(self, new_status: AppointmentStatus) -> None:
        """Allow only the transitions in the table above."""
        if new_status not in Appointment._ALLOWED_TRANSITIONS[self._status]:
            raise StatusTransitionError(
                f"Appointment {self.appointment_id} is already {self._status} "
                f"and cannot be changed to {new_status}.")
        self._status = new_status

    def cancel(self) -> None:
        """Set the status to cancelled"""
        self._change_status(AppointmentStatus.CANCELLED)

    def complete(self) -> None:
        """Mark an attended appointment as completed."""
        self._change_status(AppointmentStatus.COMPLETED)

    def is_active(self) -> bool:
        """True while this appointment still holds its slot."""
        return self._status is AppointmentStatus.BOOKED

    def __str__(self) -> str:
        return (f"{self.appointment_id}: {self.patient.name} with "
                f"{self.practitioner.name} at "
                f"{self.date_time:%d/%m/%Y %H:%M} [{self._status}]")
