#Reflection

**Hardest Modelling Decsion**
Definitely if Clinic should exist, from my previous weeks work, nothing really names it as a thing as a thing clinic staff work with. However it was added because two requirements cannot be satisfied without it: the object that can see more than one appointment at a time and fr-12 needs one owner for everything that is saved. So clinic was added but with as little set of responsibilities.

**Where AI over-designed**
In the suggested AI proposals, it suggested 6 classes with 5 of them being named for an action rather than a thing. Manager, controller and engine describe what code does but not what exists in the clinic. Next, the notifcationmanager and scheduleengine went furtherr and just invented the features, with no evidence or requiremnts to back it up. 

**Evidence Behind Final Choices**
Every class, attribute and method has reasoning and evidence and trace back to atleast one requirement id. For the concepts like status and Name, they were left out due to the fact  that they have no behaviour, and cancellation is an event. And anything inbetween where there wasnt enough evidence, is left as a question for the clint (from v2).