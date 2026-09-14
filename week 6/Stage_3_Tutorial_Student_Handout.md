# Assignment 2-Case Study Stage 3 Tutorial Activities From Requirements to Domain Models 

Week 6 | 60 minutes 

## **Candidate Concepts** 

|Candidate|Class?|Reason|
|---|---|---|
|Patient|yes|Identity shows across many<br>bookings with information such<br>as;identifer,name,dob,contact).|
|Practitioner|Yes|Identity and state are separate<br>from patient, and since the<br>requirements (fr-06) test<br>availability for practitioners, they<br>need to be an object rather than<br>just  a name stored on an<br>appointment.|
|Appointment|Yes|Has its own identity and states,<br>like booked, cancelled or<br>completed and links to both<br>patients and practitioners so<br>therefore it cant be an attribute of<br>either.|
|Name|No|Its an attribute held both by<br>patients and practitioners, no<br>identityor behavior of its own.|
|Clinic|Yes, limited|Justifed as the single container<br>that owns the patient, practitioner<br>and appointment.|
|Database|No|Implementation technology, not a<br>domain concept.|
|Cancellation|No|An event not a class.|
|Status|No|An attribute of appointment of<br>appointment drawn from fxed<br>value set. It carries no behaviour.|



## **CRC Cards** 

### **Patient** 

|Responsibilities|Collaborators|
|---|---|
|Supplies its appointment history,includingcancelled|Appointment|
|Report if it matches a search term, by name or<br>|None|
|identifer||



|**Practtoner**||
|---|---|
|Responsibilities|Collaborators|
|Report whether there is an active appointment at a<br>given date and time|Appointment|
|Supplies appointments for a chosen day|Appointment|



### **Appointment** 

|Responsibilities|Collaborators|
|---|---|
|Refuse to create when a value is missing|None|
|Know the patient, practitioner, date and time it|Patient, practitioner|
|belongs to||



## **Relationship Reasoning** 

Patient to Appointment: which relationship and why? 

It’s a binary association, every appointment will be linked with atleast one patient, one patient to zero or more appointments. Its not composition since appointment is not part of patient, its shared with practitioner. 

Practitioner to Appointment: what multiplicity? 

Zero or more, since a practitioner could hold no appointments or many of them. However the requirement fr-06 is not a multiplicity, it is a constraint on the association as no two appointments for the one practitioner should be on the same date and time. 

Should Appointment inherit from Patient? 

No, Inheriting from patient would mean that it takes on the an identifier, name, date of birth and contact details it has no use for. This would mean that any code expecting a patient could be handed an appointment instead. 

Does Clinic need to own every object? 

No as it owns the collections not the behaviour 

## **AI Model Critique** 

Critique AI proposals: PatientManager, PractitionerManager, AppointmentManager, ClinicController, NotificationManager, ScheduleEngine. 

- PatientManager and PractitionerManager: rejected as the state they hold already belong to patient and practitioner, and the collections belong to clinic. 

- AppointmentManager: Fr-06 cant be checked from a single appointment, because a clash is visible across a set. Fr-12 needs one owner for everything that is saved. The need is genuine but a third separate manager is not, so it was modified into Clinic 

- ClinicController: Rejected, describes a single clinic and puts a web interface and external integration out of scope. 

- NotificationManager. Rejected. No requirement, user story or acceptance criterion in v0.2 mentions reminders, messages or notifications, and the v0.2 stakeholder table already records patient access as inferred rather than stated. 

- Rejected. FR-10 asks for appointments displayed in date and time order, which is a sort over objects that already exist. 

