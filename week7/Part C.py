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


