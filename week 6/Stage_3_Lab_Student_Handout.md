# Assignment 2- Case Study Stage 3 Lab Activities SmartCare Domain Modelling 

AI OFF -> AI ON -> COMPARE -> VERIFY | 1 hour 

## **A - Requirements Review** 

Highlight nouns, verbs and business rules in SmartCare v0.2. 

Nouns kept as candidate concepts: patient, practitioner, appointment, status, date and time, time slot, identifier, name, contact details, appointment history, clinic. 

Verbs as candidate behavior: create, search, modify, book, reject, cancel, record, display, order, store, retrieve. 

Business rules: 

- BR-1: no two active appointments may exist for the same practitioner at the same date and time (FR-06, NFR-01). 

- BR-2: a booking is rejected unless every required value is supplied (FR-07). 

- BR-3: cancelling an appointment sets its status to cancelled and never deletes the record (FR-09, US-04). 

- BR-4: every appointment carries a status (FR-08). 

- BR-5: an update changes the existing record instead of creating a second copy (FR-03). 

- BR-6: patient, practitioner and appointment data survives the program closing (FR-12, US-05). 

- BR-7: a rejection is reported to the user as a message, never as an unhandled Python error (NFR-02, NFR-05). 

## **B - Candidate Classes** 

Record candidate concepts, supporting requirements, state and behaviour. 

|Concepts|Supporting<br>requirements|State|Behaviour|
|---|---|---|---|
|Patient|FR-01, FR-02,<br>FR-03, FR-11, US-01|patient_id, name,<br>date_of_birth,<br>phone|update_details(),<br>matches(), history()|
|Practitioner|FR-04, FR-06,<br>FR-10,US-06|practitioner_id,<br>name,role|is_busy(),<br>schedule_for()|
|Appointment|FR-05, FR-06,<br>FR-07, FR-08, FR-09|appointment_id,<br>patient,<br>practitioner,|cancel(), is_active()|



|||date_time,status||
|---|---|---|---|
|Clinic|FR-02, FR-06,<br>FR-10, FR-11, FR-12|patient, practitioner<br>and appointment<br>registers|register_patient(),<br>fnd_patient(),<br>book_appointment(),<br>save(),load()|
|Name|FR-01,FR-04|String|none|
|Status|FR-08, FR-09|one of Booked,<br>Cancelled,<br>Completed|none|
|Cancellation|FR-09|none of its own|V|



## **C - CRC Cards** 

Create CRC cards for Patient, Practitioner and Appointment. 

### **Patient** 

|Responsibilities|Collaborators|
|---|---|
|Supplies its appointment history, including cancelled|Appointment|
|Report if it matches a search term, by name or<br>|None|
|identifer||



### **Practitioner** 

|Responsibilities|Collaborators|
|---|---|
|Report whether there is an active appointment at a|Appointment|
|given date and time||
|Supplies appointments for a chosen day|Appointment|



### **Appointment** 

|Responsibilities|Collaborators|
|---|---|
|Refuse to create when a value is missing|None|
|Know the patient, practitioner, date and time it<br>belongs to|Patient, practitioner|



## **D - UML Model** 

Draw classes, attributes, operations, associations and multiplicities. 



<!-- Start of picture text -->
’ ee<br>ee Patient<br>; - - Appointment<br>oname :adSet == patient_idname: String: String = appointment_id : String AppointmentStatus-<br>+ register_patient(patient) ee .. oef_birth :“Date -. oaeimeime :qeDateTit Booked<br>+ register_practitioner(practitioner) ey as AppointmentStatus . — — stots — > Cancelled<br>+ find_patient(search_term) : Patient ‘ datelst Booked ‘Completed<br>+ book_appointment(patient, cari ~ .<br>practitioner, date_time) : Appointment + matches(search farm) : + cancel<br>: rn2 Boolean + is_active() ; Boolean<br>+ history() : Appointment<br>registers:<br>Practitioner<br>= practitioner_id :<br>String<br>= name : String<br>= role: String pu svi<br>+ is_busy(date_time) :<br>Boolean<br>+ schedule_foridate) :<br>Appointment<br><!-- End of picture text -->

- FR-10: Display appointments for a practitioner. 

### **3. Appointment** 

### **Supported by** 

- FR-05: Create appointment bookings. 

- FR-06: Prevent double bookings. 

- FR-08: Record appointment status. 

- FR-09: Cancel appointments while retaining history. 

- FR-10: Display practitioner appointments. 

- FR-11: Display patient appointment history. 

## **F - Compare and Decide** 

Record at least one accepted, modified and rejected AI suggestion. 

Accept all of these classes, as these are already included in my responses. Co-pilot essentially just restated the most basic answers. 

## **G - Python Skeletons** 

Create simple Patient, Practitioner and Appointment class skeletons. 

