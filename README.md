# CS-411-A5-Team-5
Project for CS 411 A5 Team 5

### Contact Info

Richard Buehling, rbueh@bu.edu, +16308081663

Joshua Alvarez, jhsualva@bu,edu, +19173764766

Christopher Chan, chrisdc@bu.edu, +18457296611


### Project Idea One

Idea: Polling Web Application that makes automated phone calls to a population, records, transcribes, and saves the responses in a data base for statistical analysis.

Frameworks: Django Backend, Next.js Frontend - Data Passed using the Django Rest Framework 
 
Database: mySQLite
 
APIs: Twilio API, Assembly AI API

### Project Idea Two

Idea: An app that allows restaurants to send a bill electronically to a table and then allow the table to split the check based on the items everyone ate.

APIs: Stripe API, Google Maps API

### API Documentation

```
{
user: test@email.com,
id: 2,
data: {
   [
   meeting: 1,
   transription: "Test, test, test",
   summary: "A person saying test",
   ],
   [
   meeting: 2,
   transription: "Test2, test2, test2",
   summary: "A person saying test2",
   ],
 }
}
````
