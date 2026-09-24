# Assignment 2 – Case Study Stage 4 Tutorial Activities Object-Oriented Design Decisions 

Week 7 | 60 minutes 

## **Activity 1 - Encapsulation Review** 

|Class|Protected state / invariant<br>i|Public operations|
|---|---|---|
|Patient|The input fields are validated when<br>made and cant be left empty, a<br>change of details doesn’t make a<br>new file but rewrites the original<br>i|update_details(name, phone)<br>matches(search_term)<br>add_appointment(appointment)<br>history()|
|Practitioner|The input fields are validated when<br>made and cant be left empty, The<br>practitioner's own appointment<br>list is the only source of truth for<br>availability,|add_appointment(appointment)<br>is_busy(date_time)<br>schedule_for(day)|
|Appointment|The status is on a readonly<br>property and can only be changed<br>when change_status writes to it.<br>Inputs are checked at creation and<br>wont let double appointments be<br>booked.|status (read only)<br>cancel()<br>complete()<br>is_active()|



## **Activity 2 - Composition or Inheritance?** 

Appointment and Patient -> □ Composition/association  Reason: An appointment isn’t a kind of patient, it refers to one. : the appointment is shared with a practitioner and has to survive as a record after cancellation and as said in stage 3: one patient to zero or more appointments, each appointment to exactly one patient and practitioner 

Appointment and Practitioner -> □ Composition/association  : Exact same reasoning. An appointment isn’t a kind of practitioner, it refers to one. : the appointment is shared with a practitioner and has to survive as a record after cancellation and as said in stage 3: one patient to zero or more appointments, each appointment to exactly one patient and practitioner 

Doctor and Practitioner (hypothetical) -> □ Inheritance  Reason: As they are essentially just the same thing and anything expecting a practitioner could be handed a doctor. 

Clinic and Appointment -> □ Composition/association  :  If one existed the relationship would be composition: the appointment register would own the lifecycle of the records it holds, and no appointment would exist outside it. 

## **Activity 3 - Responsibility Allocation** 

Who decides whether SCHEDULED can become CANCELLED? 

For the title changes in the code, only the appointment itself can decide that after being changed externally. 

Who validates a patient name? 

Patient, in its constructor and in update_details(). This is validated in the ValidationError with field named in the message. 

Should Appointment execute SQL? Why? 

No, firstly its out of scope for this project, Second, it makes the class impossible to test without a live database. 

Should the UI decide whether a status transition is legal? 

No, The appointment class should only enforce the rules and not let UI decide so that they always apply regardless of the interface. 

## **Activity 4 - AI Code Critique** 

AI generates an Appointment class with public status mutation, SQL inside cancel(), a NotificationManager dependency and inheritance from PatientRecord. Identify at least five design problems and corrections. 

Problem 1. Public status mutation 

This is a design fault because any code anywhere can write into any value to status, including one the enum doesn’t contain. **Correction:** Make the attribute private behind a read only. 

### Problem 2. SQL inside cancel() 

The class now knows whats a database is but cancelling can fail for storage reasons unrelated to appointments. Changes in the database could mean editing domain logic and the class cannot be tested with a connectiojn. **Solution:** make it so cancel() changes status and nothing else 

Problem 3.  NotificationManager dependency 

This is a problem since theres no requirement for it mentioned, there is no need to implement reminders of messes  therefore this feature has been invented. The solution for this is to just leave it for now and question the client to see if they would like this implementation. 

### Problem 4. One method doing three jobs 

The problem here is that cancel() changes state, writes to a database and sends a message. That is three reasons for one method to change. Solution to this is create one responsibility per method, Status change stays in the domain; storage and messaging. 

### Problem 5. No domain Error Type 

With SQL and notification and a service notice inside. Failures happens as database errors or bare exceptions. 

## **Exit question** 

Why can code be object-oriented syntactically but still have poor object-oriented design? 

Using keywords are the easy part, writing class, def and base in brackets makes the code “object-oriented” in form, but design is abou where the data and the rules about that said data end up. For example, the appointment class, it uses the correct python syntax, defines methods and would run however it is still not a great design. This is because of the fact that the status rules are enforced by whoever remembers them. 

