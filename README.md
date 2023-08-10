# Notes

Patient Management Dashboard

## Requirements

### Views

- Form for adding patients
- Patient dashboard
- Search patients

Bonus:
- Login page

### Database
Store patients and users

| **Patient**                 |
|-----------------------------|
| ID (generated, primary key) |
| First Name (required)       |
| Middle Name                 |
| Last Name (required)        |
| Date of Birth (required)    |
| Status (required)           |
| Address                     |
| Other                       | 

Contact?

| **User**            |
|---------------------|
| Email (primary key) |
| Password (encrypted |

## Decisions

### Stack
Google Forms - Google Sheets


Python3 - Flask application

Database - SQLite

### Frontend
HTML - Bootstrap

### Backend
Flask - Python

Searching with SQL vs. searching in memory with Python

Text search through every field vs Search each option individually

### Database

SQL vs NoSQL vs Elasticsearch

| Database      | Pros                                                                                      | Cons                                                                   |
|---------------|-------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| SQL           | - SQL filter and queries<br/>- Separate tables                                            | - Not great for text search<br/> - Requires structured schema and data |
| NoSQL         | - Good for unstructured data (**Others** field)<br/> - Scalability for access and queries | - No data schema                                                       |
| Elasticsearch | - Text search                                                                             | - Expensive                                                            |

### Alternatives

Frontend - React
Backend - Typescript - Node.js
Database

### Improvements
1. Unit testing
2. Buggy HTML
3. Database encryption for password
4. Search - full text search through all fields and return any match?
   1. Others - JSON + add fields individually (text?)
   2. Exact match?
   3. Partial match?
5. Search box, filtering
6. Templates and design
7. Account creation and verification and change password
8. Changing patient details/deleting patients
9. OAuth

Scalability of database:

- Will a single table be sufficient in the future?
- Do fields need to be split into various table? (one-to-one or potentially one-to-many mappings)
- Availability of data
