# Assignment 2-Case Study Stage 4 Lab Activities Implementing the SmartCare Domain Layer 

DESIGN FIRST -> AI PAIR PROGRAMMING -> REVIEW -> VERIFY | 1hour 

## **A - Revisit Approved UML** 

Confirm responsibilities, attributes and relationships before coding. 

|**Class**|**Attributes**|**Operations**|**Relationships**|
|---|---|---|---|
|Patient|patient_id, name,<br>date_of_birth, phone|update_details(),<br>matches(), history(),<br>add_appointment()|1 to 0..* Appointment (attends)|
|Practitioner|practitioner_id,<br>name, specialty|is_busy(), schedule_for(),<br>add_appointment()|1 to 0..* Appointment (delivers)|
|Appointment|appointment_id,<br>patient, practitioner,<br>date_time, status|cancel(), complete(),<br>is_active()|references exactly 1 Patient<br>and 1 Practitioner|
|AppointmentStatus|Booked, Cancelled,<br>Completed|none|type of Appointment.status|



## **B - Implement Patient: AI OFF** 

# Domain exceptions 

class SmartCareError(Exception): 

"""Base class error""" 

class ValidationError(SmartCareError): 

"""A required value was missing""" 

class StatusTransitionError(SmartCareError): 

"""A status change the rules do not allow""" 

class DoubleBookingError(SmartCareError): 

"""The practitioner is already booked here """ 

Patient Itself; class Patient: 

"""patient records.""" 

def __init__(self, patient_id: str, name: str, date_of_birth: date, 

phone: str) -> None: self.patient_id: str = _require_text(patient_id, "Patient identifier") self.name: str = _require_text(name, "Patient name") if not isinstance(date_of_birth, date): raise ValidationError("Date of birth is required and must be a date.") self.date_of_birth: date = date_of_birth 

self.phone: str = _require_text(phone, "Phone number") self.appointments: List["Appointment"] = [] 

def update_details(self, name: Optional[str] = None, 

phone: Optional[str] = None) -> None: 

if name is not None: 

self.name = _require_text(name, "Patient name") if phone is not None: 

self.phone = _require_text(phone, "Phone number") 

def matches(self, search_term: str) -> bool: 

term = _require_text(search_term, "Search term").lower() return term in self.name.lower() or term == self.patient_id.lower() 

def add_appointment(self, appointment: "Appointment") -> None: 

if appointment not in self.appointments: 

self.appointments.append(appointment) 

def history(self) -> List["Appointment"]: 

return sorted(self.appointments, key=lambda a: a.date_time) 

def __str__(self) -> str: 

return f"{self.name} ({self.patient_id})" 

## **C - Implement Practitioner: AI OFF** 

Implement Practitioner with identifier, name and specialty; no database logic. 

class Practitioner: 

"""A practitioner""" 

def __init__(self, practitioner_id: str, name: str, specialty: str) -> None: 

self.practitioner_id: str = _require_text(practitioner_id, 

"Practitioner identifier") 

self.name: str = _require_text(name, "Practitioner name") 

self.specialty: str = _require_text(specialty, "Specialty") 

self.appointments: List["Appointment"] = [] 

def add_appointment(self, appointment: "Appointment") -> None: 

"""Maintain the association end. Called by the Appointment constructor.""" 

if appointment not in self.appointments: self.appointments.append(appointment) 

def is_busy(self, date_time: datetime) -> bool: 

"""FR-06, NFR-01. True when an active appointment holds this slot. 

A cancelled appointment does not hold the slot, which is what makes the 

third acceptance criterion in v0.2 work. """ 

if not isinstance(date_time, datetime): 

raise ValidationError("A date and time is required to check availability.") 

return any(a.is_active() and a.date_time == date_time 

for a in self.appointments) 

def schedule_for(self, day: date) -> List["Appointment"]: 

"""FR-10, US-06. This practitioner's appointments for one day, in order. 

Cancelled appointments are included, because FR-09 keeps the record and the practitioner benefits from seeing that a slot was given up. 

""" 

if not isinstance(day, date): 

raise ValidationError("A date is required to build a schedule.") 

on_day = [a for a in self.appointments if a.date_time.date() == day] 

return sorted(on_day, key=lambda a: a.date_time) 

def __str__(self) -> str: 

return f"{self.name}, {self.specialty} ({self.practitioner_id})" 

## **D - Implement Appointment: AI ON** 

Give AI the approved Appointment UML, business rules and explicit constraints. Ask it to implement only Appointment and agreed enum/exception. 

```
from dataclasses import dataclass
```

```
from datetime import datetime, timedelta
from enum import Enum
```

```
from typing import Optional
```

```
class AppointmentStatus(Enum):
    SCHEDULED = "scheduled"
    CANCELLED = "cancelled"
    COMPLETED = "completed"
    NO_SHOW = "no_show"
```

```
@dataclass
class Appointment:
    appointment_id: str
    patient: "Patient"
    practitioner: "Practitioner"
    date_time: datetime
    duration_minutes: int = 30
    notes: Optional[str] = None
    status: AppointmentStatus = AppointmentStatus.SCHEDULED
    def set_status(self, new_status: AppointmentStatus) -> None:
        self.status = new_status
    def cancel(self) -> bool:
        if self.status == AppointmentStatus.CANCELLED:
            return False
        self.status = AppointmentStatus.CANCELLED
        return True
    def reschedule(self, new_date_time: datetime) -> None:
        if new_date_time < datetime.now():
            raise ValueError("Cannot reschedule to the past")
        self.date_time = new_date_time
    def end_time(self) -> datetime:
        return self.date_time + timedelta(minutes=self.duration_minutes)
    def to_dict(self) -> dict:
        return {
            "appointment_id": self.appointment_id,
            "patient": self.patient.name,
            "practitioner": self.practitioner.name,
            "date_time": self.date_time.isoformat(),
            "status": self.status.value,
        }
```

## **E - Review Generated Code** 

Check model consistency, unsupported features, public state mutation, unnecessary inheritance, invented dependencies and error handling. 

|**Checkpoint**|**What the generated code did**|**Decision and action**|
|---|---|---|
|Model<br>consistency|Status values came back as SCHEDULED,<br>CANCELLED, COMPLETED and<br>NO_SHOW. Compared to original names.|Disregard it, use original names.|
|Unsupported<br>features|duration_minutes with a default of 30,<br>end_time(), a notes attribute and<br>reschedule().|Out of scope, remove it, was never<br>mentioned in the original or in the scope<br>list.|
|Unnecessary|None found. The class inherits from object|No actions|



|inheritance|||
|---|---|---|
|Invented<br>dependencies|No external packages, but timedelta was<br>imported purely to serve the invented<br>duration|No need for it, remove.|
|Error handling|cancel() returned False when the<br>appointment was already cancelled|Replace with proper error message.|
|Missing rules|Nothing in the generated class enforced<br>FR-06, and nothing filled the two<br>association ends. Both had been left to a<br>caller that does not exist.|If this code were to be used, would need to<br>fix asap|



## **F - Manual Behaviour Checks** 

Create valid objects, test invalid input, cancel a scheduled appointment and attempt an illegal repeated transition. 

Smartcare 0.4 

- 1: create patient, pass. 

2. create practitioner: pass 

3. book appointment: pass 

4. blank name rejected: pass 

5. non date and time rejected: pass 

6. patient name string rejected in place of a patient: pass 

7. prac reports slot as taken : pass 

8. a different slot is free: pass 

9. cancelled slot is free: pass 

10. record is kept, not deleted after cencellation: pass 

11. free slot can be rebooked: pass 

## **G - Refactor** 

Remove unnecessary code and make implementation simpler and design-consistent. 

Changes from the ai code: 

- Removed duration_minutes, end_time(), notes, to_dict() and reschedule(). 

- Removed @dataclass, so identity is not silently redefined 

- Renamed SCHEDULED to BOOKED and deleted NO_SHOW 

- Replaced ValueError and the False with ValidationError and StatusTransitionError, both under SmartCareError. 

- Added doubling booking error 

- Added complete() 

- Added type checks in the constructor, so passing a patient's name where a Patient belongs is rejected 

## **H - AI Engineering Log** 

Record prompt, generated contribution, decisions and verification evidence. 

Prompt: 

Act as a Python pair programmer. Implement only the Appointment class from the approved SmartCare UML. Use type hints and an AppointmentStatus enum. Cancelled appointments remain as objects. Do not add database, UI, notification or service classes. Protect status transitions and explain any decision not directly visible in the UML. 

Generated contribution from part D: 

```
from dataclasses import dataclass
from datetime import datetime, timedelta
from enum import Enum
from typing import Optional
```

```
class AppointmentStatus(Enum):
    SCHEDULED = "scheduled"
    CANCELLED = "cancelled"
    COMPLETED = "completed"
    NO_SHOW = "no_show"
```

```
@dataclass
class Appointment:
    appointment_id: str
    patient: "Patient"
    practitioner: "Practitioner"
    date_time: datetime
    duration_minutes: int = 30
    notes: Optional[str] = None
    status: AppointmentStatus = AppointmentStatus.SCHEDULED
    def set_status(self, new_status: AppointmentStatus) -> None:
        self.status = new_status
    def cancel(self) -> bool:
        if self.status == AppointmentStatus.CANCELLED:
            return False
        self.status = AppointmentStatus.CANCELLED
        return True
    def reschedule(self, new_date_time: datetime) -> None:
        if new_date_time < datetime.now():
            raise ValueError("Cannot reschedule to the past")
        self.date_time = new_date_time
    def end_time(self) -> datetime:
        return self.date_time + timedelta(minutes=self.duration_minutes)
    def to_dict(self) -> dict:
        return {
            "appointment_id": self.appointment_id,
```

```
            "patient": self.patient.name,
            "practitioner": self.practitioner.name,
            "date_time": self.date_time.isoformat(),
            "status": self.status.value,
        }
```

Verification evidence: 

See manual checks.py 

## **Reflection** 

Which AI-generated part did you modify or reject? Why? How did the approved design constrain the AI? 

See reflection.md 

