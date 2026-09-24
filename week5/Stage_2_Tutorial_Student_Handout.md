# THIS WAS COVERTED FROM .DOCX  SO TABLES HAVE NOT CONVERTED PROPERLY, SEE THE DOCX FILE FOR THE PROPER TABLES


# Assignment 2 Case Study Stage 2 Tutorial From Problems to Requirements 

### Week 5 | 60 minutes 

## **Learning goals** 

- Analyse stakeholders. 

- Distinguish functional and non-functional requirements. 

- Recognise ambiguity and unsupported requirements. 

- Define scope. 

- Develop user stories and acceptance criteria. 

- Critique AI-generated requirements. 

## **Activity 1 - Stakeholder Map** 

|Stakeholder|Need|Potential Confict|
|---|---|---|
|Reception and<br>administration staf|One place to search<br>patients and to create,<br>change or cancel the<br>bookings. As well as this<br>they will need a way for<br>double bookings to not<br>occur and a clear<br>appointment status feature|Against management<br>as the more<br>information required to<br>be flled.|
|Practitioners (GP)|A view of their own<br>appointments and no<br>double bookings.|Against reception and<br>patients: if an urgent<br>case pops up, then<br>reception will want to<br>ft in the case which<br>could create<br>overbookng|
|Patients:|Booking that is recorded<br>correctly and a reliable<br>response from the clinic.|Against practitioners<br>convenient for the<br>patient often means<br>outside the slots for<br>practitioners has made<br>available.|
|Clinic managment|A small system that is<br>cheap to run and maintatin.|Internally confiction,<br>report and more<br>history means more<br>data and code which is<br>against small and<br>cheap|
|Maintenance workers|Code and system fles that<br>are simple to maintain and|Against everyone, each<br>stakeholder request|



|edit.|adds code that this|
|---|---|
||person keeps working|
||on|



## **Activity 2 - Functional or Non-Functional?** 

□ Functional   The system shall allow staff to cancel an appointment. 

□ Non-functional   The system should remain responsive for the course-scale dataset. 

□ Functional   The system shall retain cancelled appointments. 

□ Non-functional   Core business logic should be independently testable. 

□ Functional  The system shall search for a patient by ID. 

## **Activity 3 - Repair Ambiguous Requirements** 

The system should be easy to use. 

Problem: it’s a subjective statement, as each role has a different definition for ‘easy’   Clarification question: by easy we could decide who is the least experienced person to use the system and what task must they complete unaided? For example, can a new receptionist book a new appointment without training? 

Patient search should be fast. 

Problem: once again fast is subjective and to whose standard. Fast cannot be tested and a search function that is fast with 50 patients will have different results thatn 5000   Clarification question: What is amount of patient information will be held and what is an acceptable time for the search result. 

The system should securely manage data. 

Problem: securely bundles many thing and does not explain what security is required.   Clarification question: Who may see a record, is it encrypted, where is it stored? 

Appointments should normally be easy to cancel. 

Problem: two subject words in the statement. Easy and normal. Therefore, it is hard to tell what requirements to meet.   Clarification question: in what scenarios can a appointment be cancelled, and who is allowed to override it? 

## **Activity 4 - AI Requirements Audit** 

Classify each suggestion: Confirmed / Assumption requiring validation / Unsupported / Out of scope. 

|AI suggestion|Classifcation|Evidence / reason|
|---|---|---|
|Patients receive SMS reminders.|unsupported|SMS notifcations are not|
|||<br>mentioned anywhere in the scope,|
|||requirements,user stories,or|



|||acceptance criteria.|
|---|---|---|
|Facial recognition login.|unsupported|Authentication methods and<br>biometric login are not mentioned<br>in the requirements.|
|Receptionists create<br>appointments.|Assumption requiring validation|Receptionists are described as<br>needing to "create, change or<br>cancel bookings," which suggests<br>they create appointments, but<br>there is also a user story stating<br>patients want to book<br>appointments. The exact actor<br>responsible for booking is not fully<br>confrmed.|
|Online payment.|Out of scope|Payments are explicitly listed as<br>out of scope.|
|Practitioners view schedules.|Confrmed|A stakeholder need states<br>practitioners require "a view of<br>their own appointments," and user<br>story US-06 states practitioners<br>want to view their appointments<br>for a chosen day.|
|AI recommends treatments.|Unsupported|The document focuses on records<br>and appointment management.<br>No treatment recommendation<br>functionalityis mentioned.|
|Cancelled appointments remain in<br>history.|confrmed|FR-09 states cancelled<br>appointments should not be<br>deleted but have their status<br>changed to cancelled, and the<br>acceptance criteria state the<br>historyremains after cancellation.|



## **Exit question** 

Why is 'AI suggested it' not sufficient evidence for a requirement? 

AI being used as evidence or any practical feature should not be considered sufficient due to its large inaccuracies when it comes to generative ai. For example, AI has never spoken to clients or humans regarding the case study, so often it will lead to invention of logic or using assumptions without properly stating or reasoning them first. Because of this, issues such as inaccuracy in data/writing will occur and the made-up assumption could be indistinguishable from someone who has not properly read the case. 

