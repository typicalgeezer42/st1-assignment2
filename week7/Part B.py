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
