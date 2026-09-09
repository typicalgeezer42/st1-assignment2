# THIS WAS COVERTED FROM .DOCX  SO TABLES HAVE NOT CONVERTED PROPERLY, SEE THE DOCX FILE FOR THE PROPER TABLES

# SmartCare v0.2 - Requirements Specification Template 

## **1. Problem and Scope** 

The SmartCare clinic tracks and keeps all patients, practitioners, and appointment information in spreadsheets and on paper. Due to this style of information keeping, multiple accounts of the same records can be spread out across the documents, leaving to issues such as; duplicate bookings, difficulty finding patient information, inconsistent appointment status and limited appointment history. 

In scope: 

- Patient records: create searcj and update 

- Practitioner records: Create and list  Appointment bookings: rescheduling and cancellation with a recorded status  Prevention of double bookings  Display of appointments for a day and patient history 

Out of scope 

- Billing 

- Payments 

- Health insurance claims 

- Web interface 

- External system integration 

Provisional, to be confirmed: 

- Management recording 

- Multiple concurrent users using the system 

## **2. Stakeholders** 

|Stakeholder<br>|Need|Evidence<br>|
|---|---|---|
|Reception and administration staf|One place to search patients and to<br>create, change or cancel the<br>bookings. As well as this they will<br>need a way for double bookings to<br>not occur and a clear appointment<br>status feature|Stated. In the report it states staf<br>experience double bookings,<br>dificulty fnd patient information and<br>inconsistent appointment status.|
|Practitioners (GP)|A view of their own appointments<br>and no double bookings.|Partly stated; it states the<br>practitioners as a entity the system<br>must manage. The need for a<br>schedule view is implied from the<br>booking problem, not explicitly<br>stated.|
|Patients:|Booking that is recorded correctly<br>and a reliable response from the<br>clinic.|Inferred, as it states that patient<br>information gets recorded but<br>doesn’t state ifpatients can access.|



|Clinic managment|A small system that is cheap to run<br>and maintatin.<br>|Stated; it mentions and describes<br>the system that theywant.|
|---|---|---|
|Maintainence workers|Code and system fles that are<br>simple to maintain and edit.|Inferred as it states that the system<br>will be “maintainable” but nothing<br>specifc.|



## **3. Functional Requirements** 

FR-01: The system will allow a user to create a patient record containing required patient information. 

FR-02: The system will allow searching for the record database by records or identifiers, 

FR-03: The system will allow for modifying records in the database of existing information without duplicating data 

FR-04: the system will will allow a user to create a practitioner record containing required practitioner information. 

FR-05: the system will allow a user to book an appointment by selecting a time slot, patient and their information and a date and time. 

FR-06: the system will reject bookings if the booking timeslot has already been taken and will not duplicate or remove the previous bookings. 

FR-07: the system will reject bookings if all required information is not completed / filled out 

FR-08: the system will record a status for every appointment, booked, cancelled etc.. 

FR-09: the system will allow users to cancel appointments but not delete the record of it and instead set its status to cancelled 

FR-10: the system will display all appointments for a practitioner ordered by date and time. 

FR-11: the system will display appointment history for a patient 

FR-12: The system will store all information of patients, practitioner and appointment data so that it is available even after the program is closed. 

## **4. Non-Functional Requirements** 

NFR-01: Data integrity – no bookings should be occurring at the same time, can be verified through attempting double booking and looking at stored data. 

NFR-02: reliability – no input should be entered by a user that will cause an unhandled exception to code, which could end the program. 

NFR-03: validation shall be implemented and from the bookings function so that the clients request for a maintainable system is made. 

NFR-04: testability, every requirement will be verified by running the program and observing outputs 

NFR-05: useability, there should be a rejection message for each possible comibation and not show a python error to be exposed to the user 

NFR-06: performance, there should be a quick and little delay when using the system 

## **5. User Stories** 

US-01: As a Receptionist I want to search for patient records by name or identifier so that I can easily find the record without checking multiple locations of stored information. 

US-02: As a patient I want to be able to book and appointment easily and with colliding with another person so that I can attend my booking without issues. 

US-03: As a Patient I want to be able to change my booking status so that if something changes I can update or cancel my booking. 

US-04: As a Receptionist I want to be able to cancel appointments without erasing them from the system so that accurate records are kept and maintained. 

US-05: As a clinic manger I want appointment data to survive the program being close so that if something happens to the program, the data is stored and able to be read. 

US-06: As a pracitioner I want to be able to view all of my appointments for a chosen  day and time in order so that I know my schedule for the given time. 

## **6. Acceptance Criteria** 

GIVEN A paitent record exists for John Doe with his unique identifier 

WHEN the receptionist searches for his name 

THEN a record for John Doe is shown together with his identifier and no other records are shown 

GIVEN Dr john doe already holds an appointment at a date and time 

WHEN the receptionist attempts to book and appointment at that same date and time THEN an error message is displayed stating the timeslot is already taken 

GIVEN A booked appoint exists for alice smith with Dr John Doe at a date and time WHEN the receptionist choses to cancel that appointment 

THEN the appointment is cancelled and the history remains, with the time slot once again becoming available for another patient. 

## **7. Assumptions and Open Questions** 

Assumptions: 

- The system is only holding booking information not medical or clinical records, needs to be confirmed 

- Appointments occupy a single fixed slot, assumed as the appointment length isn’t mentioned 

- One member of staff uses the system at a time, assumed since there is no mention of concurrent use or a online system 

Questions: 

1. Which appointment status do you need to track? 

2. what are your booking rules? 

3. Who will use the system, which roles should be assigned what permissions? 

4. Which reports do you need, how often and what decisions will they support? 

5. what patient information needs to be stored, what privacy rules apply to it and do the existing data need to be carried over from the paper and spreadsheets. 

## **8. AI Requirements Review Record** 

|**AI Suggestion**|**Evidence?**|**Decision**|**Reason**|**Verifcation**|
|---|---|---|---|---|
|Defne required patient information<br>in FR-01<br>|Evidence-based|Accepted|A miswording from<br>my end.|<br>I reworded it to<br>include the<br>suggestion|
|Clarify supported search felds in<br>FR-02<br>|Evidence-based|Accepted|<sup>To help clarify the</sup><br>exact need|Has been<br>reworded|
|Defne valid appointment status<br>values for FR-08|Evidence-based|accepted|<sup>To show the</sup><br>requirements|Has been<br>reworded|
|Clarify whether practitioner views<br>show all appointments or daily<br>appointments only|Evidence-based|rejected|It states the<br>system shows<br>both|My writing<br>already states<br>that it shows<br>both<br>|
|Clarify whether patients directly book<br>|||Will help to clarify|Will be clarifed.|
|appointments or staf perform<br>bookings|Evidence-based|accepted|as it’s a large part<br>of the system.||



