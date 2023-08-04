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

Searching: create a filter -> convert to sql query

Search bar? -> text search through everything
vs Filter each option

## Decisions

### Stack

Python3 - Flask application
Database - SQLite

### Database

SQL vs NoSQL

Configurable form - NoSQL OR SQL with JSON 'Other' column

Elasticsearch

| Database      | Pros                                                                                  | Cons                                                                   |
|---------------|---------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| SQL           | - SQL filter and queries<br/>- Separate tables                                        | - Not great for text search<br/> - Requires structured schema and data |
| NoSQL         | - Good for unstructured data (Others field)<br/> - Scalability for access and queries | - No data schema                                                       |
| Elasticsearch | - Text search                                                                         | - Expensive                                                            | 

#### Schema

Patients table:

- First Name (Required)
- Middle Name
- Last Name (Required)
- Date of Birth (Required)
- Status (Inquiry, Onboarding, Active, Churned) (Enum)
- Address (there may be multiple for a given patient)
- Other: Additional text/number fields that can be arbitrarily created by the provider (think: a configurable form)
- Contact?

Users table:

- Email (Primary Key)
- Password

### Considerations

User interface - consider using React instead
Scalability of database:

- Will a single table be sufficient in the future?
- Do fields need to be split into various table? (one-to-one or potentially one-to-many mappings)
- Availability of data