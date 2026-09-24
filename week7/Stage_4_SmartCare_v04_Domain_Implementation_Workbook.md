# SmartCare v0.4 - Domain Implementation Workbook 

Week 7 student resource 

## **1. UML-to-Code Trace** 

|UML element|Python element|Implemented?|Notes|
|---|---|---|---|
|Paitent Class|class Patient|yes|Four attributes, 3<br>operations|
|Patient attributes:|attributes set in __init__,<br>typed str,str,date,str|yes||
|Patient operatiosn|Methods of the same<br>names|yes|History gives a sorted<br>copy so the caller cant<br>change the record by<br>editingthe list|
|Practitioner class|class practitioner|yes|role became specialty on<br>the Stage 4 brief.|
|Practitioner operations:|Methods of the same<br>names|yes|is_busy() tests is_active()<br>rather than existence, so<br>a cancelled appointment<br>releases its slot.|
|Appointment class|class appointment|yes|Holds the patient and<br>practitioner as objects,<br>not copies of names|
|Appointment operations|Methods of same names|yes||
|Enum appointment<br>status|class<br>AppointmentStatus(Enum)|yes||
|Association Patient 1 to<br>0..* Appointment|Patient.appointments list<br>and Appointment.patient<br>reference|Yes||
|Association Practitioner<br>1 to 0..* Appointment|Patient.appointments list<br>and Appointment.patient<br>reference|yes||



## **2. Domain Invariants** 

|Class|Invariant / rule|Howprotected|
|---|---|---|
|paitent|Inputs like name, dob etc.. cant be<br>left blank|_require_text() raises<br>ValidationError in __init__, and<br>date_of_birth is type checked<br>against date|
|Patient|Change of details updates the<br>record and doesn’t create a new<br>one.|update_details() writes to self and<br>returns nothing. No method<br>anywhere returns a new Patient|
|practitioner|Inputs like name, dob etc.. cant be<br>left blank|Same as patient|
|Practitioner|No two appointment booked at<br>same time.|is_busy() is consulted by<br>Appointment.__init__,which|



|||raises DoubleBookingError before<br>anystate is written|
|---|---|---|
|appointment|Status is always one of the three<br>enumeration values|Set once in __init__ and typed as<br>appointment status|
|appointment|Status moves only from Booked to|_ALLOWED_TRANSITIONS is|
||Cancelled or Completed|consulted by _change_status(),|



## **3. Composition / Inheritance Decisions** 

|Relationship|Decision|Rationale|
|---|---|---|
|Patient to appointment|Association by reference|An appointment is not a kind of<br>patient and not a part of one. It is<br>shared with apractitioner|
|Practitioner to Appointment|Association by reference|Same as previous, it isn’t a kind of<br>practitioner and not part of one, it<br>is shared withpatient.|
|Appointment to<br>AppointmentStatus|Attribute by enumeration|The status doesn’t have any<br>behaviour or identity only a value<br>type.|
|A container class over all three|Rejected|When looking at the work on<br>canvas it mentioned that there<br>was only 3, and also checked with<br>peers to see what I did in v0.3 was<br>wrongbyme usingit.|
|Exception hierarchy|Inheritance used deliberately|The errors all inherit from<br>smartcareerror, which inherits<br>from excepted.|



## **4. AI Pair-Programming Record** 

|AI contribution|Conforms?|Decision|Reason|Verification|
|---|---|---|---|---|
|Appointmentstatus<br>values|partly|modified|Names don’t match<br>the original, so<br>change them.|i<br>See lab handout|
|cancel() returning<br>False when the<br>appointment was<br>alreadycancelled|No|rejected|Need a rejection<br>message not a<br>silent false.|See lab handout|
|No doubling<br>booking check|no|rejected|The software has it<br>in the requirements<br>to have this. This<br>was just something<br>ai missed evidently|See lab handout|
|ValueError raised<br>for invalid input|no|modified|Requirements need<br>one domain rather<br>than a built in error|See lab handout|
|duration_minutes<br>with a default of 30,<br>end_time(), a notes<br>attribute and<br>reschedule().|No|rejected|Out of scope, , was<br>never mentioned in<br>the original or in the<br>scope list.|See lab handout|



## **5. Updated UML** 

Insert updated UML only if implementation revealed a justified design change. Explain every change. 



<!-- Start of picture text -->
Patient<br>= patientid<br>name : String: Sting = appointmentid: String AppointmentStatus<br>= date_of_birh :Date = date.time : DateTime 7<br>= phonphon e :: String — = status: ~ betaa teen<br>phone)<br>+ matches(search.term) + cancel)<br>Boolean | + Is_activel): Boolean<br>+ history0 : Appointment |<br>= practitioner.idPracttioner |<br>String | Exe<br>name : String envers —<br>= role: Sting L—__| SmanCareéror 4g<br>Boolean+ 1s_busy{date.time) oT<br>+ schedule.for(date)<br>Appointment<br>Exception Exception Exception<br>ValidationError StatusTransitionsror DoubleBookingError<br><!-- End of picture text -->

