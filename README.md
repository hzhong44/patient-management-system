# Notes
Patient Management Dashboard

## Requirements
### Views
- Form for adding patients
- Patient dashboard and search
- Individual patient card (?)

- Viewing data
- Filtering data
- Search data (equality)

Bonus:
- A nice to have would be authentication using email & password and/or OAuth
- Login page
- Account creation
- 

### Database
Searching with SQL 
vs. searching in memory with Python

## Decisions
### Stack
Python3 - Flask application
Database - SQLite

### Database
SQL vs NoSQL

Configurable form - NoSQL OR SQL with JSON 'Other' column

#### Schema
Required fields
Patients table:
- First Name
- Middle Name
- Last Name
- Date of Birth
- Status (Inquiry, Onboarding, Active, Churned) (Enum)
- Address (there may be multiple for a given patient)
- Other: Additional text/number fields that can be arbitrarily created by the provider (think: a configurable form)
- Contact?

Users table:
- Email
- Password

### Considerations
User interface - consider using React instead
Scalability of database:
- Will a single table be sufficient in the future?
- Do fields need to be split into various table? (one-to-one or potentially one-to-many mappings)
- Availability of data