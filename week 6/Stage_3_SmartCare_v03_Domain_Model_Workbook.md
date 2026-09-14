# SmartCare v0.3 - Domain Model Workbook 

### Week 6 student resource 

## **Requirement-to-Concept Trace** 

|Requirement|Concept|State/behaviour|Decision|
|---|---|---|---|
|FR-01|Patient|State: patient_id, name,<br>date_of_birth, phone.|Class|
|FR-02|Patient, Clinic|Behaviour:<br>Patient.matches(search_term);<br>Clinic.fnd_patient(search_term).|No search class|
|Fr-03|Patient|Behaviour:<br>update_details(name, phone).|Class|
|Fr-4|Practitioner|State: practitioner_id, name,<br>role.|Class|
|Fr-5|Appointment|State: appointment_id, patient,<br>practitioner,date_time,status|Class|
|Fr-6|Practitioner,<br>Appointment|Behaviour:<br>Practitioner.is_busy(date_time),<br>called by<br>Clinic.book_appointment()<br>before an Appointment is<br>created.|Unsure|
|Fr-7|Appointment|Behaviour: validation of every<br>required value at creation.|Rule allocated to<br>appointment|
|Fr-8, fr-9|Appointmentstatus|State: one of Booked, Cancelled,<br>Completed. Behaviour:<br>Appointment.cancel(),<br>Appointment.is_active().|Not a class|
|Fr-10, fr-11|Practitioner, Patient|Behaviour:<br>Practitioner.schedule_for(date);<br>Patient.history().|No class|
|Fr-12|Clinic|State: the patient, practitioner<br>and appointment registers.<br>Behaviour: save(),load().|unsure|



## **CRC Cards** 

### **Patient** 

|Responsibilities|Collaborators|
|---|---|
|Supplies its appointment history, including cancelled|Appointment|
|Report if it matches a search term, by name or<br>|None|
|identifer||



### **Practitioner** 

|Responsibilities|Collaborators|
|---|---|





<!-- Start of picture text -->
Clinic (SRR S 008 82 eePatient<br>int Appointment<br>+ name : Strin 9 -- namepatient_id: String: String - appointmentid : String AppointmentStatusi<br>+ register_patient(patient) e131 -. prenedate_of_birth- Stic : Date ~; “tetas.date_time : DateTime Booked<br>+ register_practitioner(practitioner) 9 attends: A onantsuaie _ — —— —status- — > Cancelled<br>+ find_patient(search_term) : Patient aoe ee - Completed<br>+ book_appointment(patient, a ~ ‘<br>practitioner,save! date_time) :Appointment aeiet ealaemecitiensed~ + cancel()<br>+, an Boolean + is_active() :Boolean<br>+ history() : Appointment<br>registers<br>Practitioner<br>- practitioner_id :<br>String<br>- name : String<br>~ role : String elivers<br>+ is_busy(date_time) :<br>Boolean<br>+ schedule_for(date) :<br>Appointment<br><!-- End of picture text -->

Following the case study, four classes were selected however clinic can be considered optional. Patient, practitioner and appointment were chosen by seeing it applied against 2 questions: Does it hold state that persists beyond a single operation and does it have behaviour of its own? Overall they pass and on top of this are named in my requirements. 

Clinic is added for 2 reasons, FR-06 cant be checked from inside a single appoint because the clas is only visible across a set of appoints and FR-12 needs one object that owns everything. For responsibilities, they are allocated to the object that holds the data needed to answer it. E.g. availability is on practitioner because only that specific prac’s appointments matter, status and cancellation sit on appointment, search mathcning sits on patient while the match is on client. 

Lastly the relationships follow pretty much the same evidence. For patient to appointment it’s a binary association, every appointment will be linked with atleast one patient, one patient to zero or more appointments. Its not composition since appointment is not part of patient, its shared with practitioner. 

## **AI Design Review Record** 

|AI suggestion|Evidence|Decision|Reason|Model change|
|---|---|---|---|---|
|PatientManager|None cited|rejected|state and the rules<br>already belong to<br>Patient and the<br>collection already<br>belongs to Clinic.|None|
|PractitionerManager|none cited|Rejected<br>|Same aspatient|None|
|AppointmentManager|Partially|Modifed|The need is real but<br>three managers are<br>not.|Clinic added as the<br>fourth class|
|ClinicController<br>|None|Rejected|There is no second<br>boundary to<br>control.|None|
|Notifcationmanager|None|Rejected|Remains<br>provisional|None|
|ScheduleEngine|none|Rejected|An engine implies<br>allocation or<br>optimisation, which<br>is out of scope.|none|



