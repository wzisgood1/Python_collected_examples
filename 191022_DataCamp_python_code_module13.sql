-- ********** ********** ********** ********** ********** **********
-- Chap1: First database
-- ********** ********** ********** **********
-- https://campus.datacamp.com/courses/introduction-to-relational-databases-in-sql/your-first-database?ex=3
-- ********** ********** 
-- Query the right table in information_schema
SELECT table_name 
FROM information_schema.tables
-- Specify the correct table_schema value
WHERE table_schema = 'public';

-- ********** ********** 
-- Query the right table in information_schema to get columns
SELECT column_name, data_type 
FROM information_schema.columns 
WHERE table_name = 'university_professors' AND table_schema = 'public';

-- ********** ********** ********** **********
-- https://campus.datacamp.com/courses/introduction-to-relational-databases-in-sql/your-first-database?ex=5
-- ********** **********
-- Create a table for the professors entity type
CREATE TABLE professors (
 firstname text,
 lastname text
);
-- Print the contents of this table
SELECT * 
FROM professors

-- ********** **********
-- Create a table for the universities entity type
create table universities (
    university_shortname text,
    university text,
    university_city text
);
-- Print the contents of this table
SELECT * 
FROM universities

-- ********** ********** ********** **********
-- https://campus.datacamp.com/courses/introduction-to-relational-databases-in-sql/your-first-database?ex=6
-- ********** **********
-- Add the university_shortname column
ALTER TABLE professors
ADD COLUMN university_shortname text;
-- Print the contents of this table
SELECT * 
FROM professors

-- ********** ********** ********** **********
-- https://campus.datacamp.com/courses/introduction-to-relational-databases-in-sql/your-first-database?ex=8
-- ********** **********
-- Rename the organisation column
ALTER TABLE affiliations
RENAME COLUMN organisation TO organization;

-- Delete the university_shortname column
ALTER TABLE affiliations
DROP COLUMN university_shortname;

-- ********** ********** ********** **********
-- https://campus.datacamp.com/courses/introduction-to-relational-databases-in-sql/your-first-database?ex=9
-- ********** **********
-- Insert unique professors into the new table
INSERT INTO professors 
SELECT DISTINCT firstname, lastname, university_shortname 
FROM university_professors;
-- Doublecheck the contents of professors
SELECT * 
FROM professors;

-- ********** **********
-- Insert unique affiliations into the new table
INSERT INTO affiliations 
SELECT DISTINCT firstname, lastname, function, organization 
FROM university_professors;
-- Doublecheck the contents of affiliations
SELECT * 
FROM affiliations;

-- ********** ********** ********** **********
-- https://campus.datacamp.com/courses/introduction-to-relational-databases-in-sql/your-first-database?ex=10
-- ********** **********
-- Delete the university_professors table
DROP TABLE university_professors;

-- ********** ********** ********** ********** ********** **********
-- Chap2: Enforce data consistency with attribute constraints
-- ********** ********** ********** **********
-- https://campus.datacamp.com/courses/introduction-to-relational-databases-in-sql/enforce-data-consistency-with-attribute-constraints?ex=3
-- ********** **********
CREATE TABLE transactions (
 transaction_date date, 
 amount integer,
 fee text
);

-- Let us add a record to the table
INSERT INTO transactions (transaction_date, amount, fee) 
VALUES ('2018-09-24', 5454, '30');
-- Doublecheck the contents
SELECT *
FROM transactions;

-- ********** ********** ********** **********
-- https://campus.datacamp.com/courses/introduction-to-relational-databases-in-sql/enforce-data-consistency-with-attribute-constraints?ex=4
-- ********** **********
-- Calculate the net amount as amount + fee
SELECT transaction_date, amount + CAST(fee AS integer) AS net_amount 
FROM transactions;

-- ********** ********** ********** **********
-- https://campus.datacamp.com/courses/introduction-to-relational-databases-in-sql/enforce-data-consistency-with-attribute-constraints?ex=6
-- ********** **********
-- Select the university_shortname column
SELECT DISTINCT university_shortname
FROM professors;

-- Specify the correct fixed-length character type
ALTER TABLE professors
ALTER COLUMN university_shortname
TYPE char(3);

-- Change the type of firstname
ALTER TABLE professors
ALTER COLUMN firstname
TYPE varchar(64);

-- ********** ********** ********** **********
-- https://campus.datacamp.com/courses/introduction-to-relational-databases-in-sql/enforce-data-consistency-with-attribute-constraints?ex=7
-- ********** **********
-- Convert the values in firstname to a max. of 16 characters
ALTER TABLE professors 
ALTER COLUMN firstname 
TYPE varchar(16)
USING SUBSTRING(firstname FROM 1 FOR 16);
select firstname
from professors

-- ********** ********** ********** **********
-- https://campus.datacamp.com/courses/introduction-to-relational-databases-in-sql/enforce-data-consistency-with-attribute-constraints?ex=9
-- ********** **********
-- Disallow NULL values in firstname
ALTER TABLE professors 
ALTER COLUMN firstname SET NOT NULL;

-- Disallow NULL values in lastname
ALTER TABLE professors 
ALTER COLUMN lastname SET NOT NULL;

-- ********** ********** ********** **********
-- https://campus.datacamp.com/courses/introduction-to-relational-databases-in-sql/enforce-data-consistency-with-attribute-constraints?ex=11
-- ********** **********
-- Make universities.university_shortname unique
ALTER TABLE universities
ADD CONSTRAINT university_shortname_unq UNIQUE(university_shortname);

-- Make organizations.organization unique
ALTER TABLE organizations
ADD CONSTRAINT organization_unq UNIQUE(organization)

-- ********** ********** ********** ********** ********** **********
-- Chap3: Uniquely identify records with key constraints
-- ********** ********** ********** **********
-- https://campus.datacamp.com/courses/introduction-to-relational-databases-in-sql/uniquely-identify-records-with-key-constraints?ex=2
-- ********** **********
-- Count the number of distinct values in the university_city column
SELECT count(distinct(university_city)) 
FROM universities;

-- ********** ********** ********** **********
-- https://campus.datacamp.com/courses/introduction-to-relational-databases-in-sql/uniquely-identify-records-with-key-constraints?ex=3
-- ********** **********
SELECT COUNT(DISTINCT(firstname, lastname)) 
FROM professors;

-- ********** ********** ********** **********
-- https://campus.datacamp.com/courses/introduction-to-relational-databases-in-sql/uniquely-identify-records-with-key-constraints?ex=6
-- ********** **********
-- Rename the organization column to id
ALTER TABLE organizations
RENAME COLUMN organization TO id;
-- Make id a primary key
ALTER TABLE organizations
ADD CONSTRAINT organization_pk PRIMARY KEY (id);

-- ********** **********
-- Rename the university_shortname column to id
ALTER TABLE universities
RENAME COLUMN university_shortname TO id;
-- Make id a primary key
ALTER TABLE universities
ADD CONSTRAINT university_pk PRIMARY KEY (id);

-- ********** ********** ********** **********
-- https://campus.datacamp.com/courses/introduction-to-relational-databases-in-sql/uniquely-identify-records-with-key-constraints?ex=8
-- ********** **********
-- Add the new column to the table
ALTER TABLE professors 
ADD COLUMN id serial;
-- Make id a primary key
ALTER TABLE professors 
ADD CONSTRAINT professors_pkey PRIMARY KEY (id);
-- Have a look at the first 10 rows of professors
SELECT * FROM professors LIMIT 10;

-- ********** ********** ********** **********
-- https://campus.datacamp.com/courses/introduction-to-relational-databases-in-sql/uniquely-identify-records-with-key-constraints?ex=9
CREATE TABLE cars (
    make varchar(64) NOT NULL,
    model varchar(64) NOT NULL,
    mpg integer NOT NULL
);

-- ********** **********
-- Count the number of distinct rows with columns make, model
SELECT COUNT(DISTINCT(make, model)) 
FROM cars;
-- Add the id column
ALTER TABLE cars
ADD COLUMN id varchar(128);
-- Update id with make + model
UPDATE cars
SET id = CONCAT(make, model);
-- Make id a primary key
ALTER TABLE cars
ADD CONSTRAINT id_pk PRIMARY KEY (id);
-- Have a look at the table
SELECT * FROM cars;

-- ********** ********** ********** **********
-- https://campus.datacamp.com/courses/introduction-to-relational-databases-in-sql/uniquely-identify-records-with-key-constraints?ex=10
-- ********** **********
-- Create the table, and note that we set the ssn with type integer and as PRIMARY KEY
CREATE TABLE students (
  last_name varchar(128) NOT NULL,
  ssn integer PRIMARY KEY,
  phone_no char(12)
);
SELECT * FROM students

-- ********** ********** ********** ********** ********** **********
-- Chap4: Glue together tables with foreign keys
-- ********** ********** ********** **********
-- https://campus.datacamp.com/courses/introduction-to-relational-databases-in-sql/glue-together-tables-with-foreign-keys?ex=2
-- Rename the university_shortname column
ALTER TABLE professors
RENAME COLUMN university_shortname TO university_id;
-- Add a foreign key on professors referencing universities
ALTER TABLE professors
ADD CONSTRAINT professors_fkey FOREIGN KEY (university_id) REFERENCES universities (id);

SELECT * FROM professors

-- Try to insert a new professor
INSERT INTO professors (firstname, lastname, university_id)
VALUES ('Albert', 'Einstein', 'UZH');

-- ********** ********** ********** **********
-- https://campus.datacamp.com/courses/introduction-to-relational-databases-in-sql/glue-together-tables-with-foreign-keys?ex=4
-- Select all professors working for universities in the city of Zurich
SELECT professors.lastname, universities.id, universities.university_city
FROM professors
JOIN universities
ON professors.university_id = universities.id
WHERE universities.university_city = 'Zurich';

-- ********** ********** ********** **********
-- https://campus.datacamp.com/courses/introduction-to-relational-databases-in-sql/glue-together-tables-with-foreign-keys?ex=6
-- ********** **********
-- Add a professor_id column
ALTER TABLE affiliations
ADD COLUMN professor_id integer REFERENCES professors (id);
-- Rename the organization column to organization_id
ALTER TABLE affiliations
RENAME organization TO organization_id;
-- Add a foreign key on organization_id
ALTER TABLE affiliations
ADD CONSTRAINT affiliations_organization_fkey FOREIGN KEY (organization_id) REFERENCES organizations (id);
SELECT * FROM affiliations

-- ********** ********** ********** **********
-- https://campus.datacamp.com/courses/introduction-to-relational-databases-in-sql/glue-together-tables-with-foreign-keys?ex=7
-- Update professor_id to professors.id where firstname, lastname correspond to rows in professors
UPDATE affiliations
SET professor_id = professors.id
FROM professors
WHERE affiliations.firstname = professors.firstname AND affiliations.lastname = professors.lastname;
-- Have a look at the 10 first rows of affiliations again
SELECT * FROM affiliations LIMIT 10;

-- Drop the firstname column
ALTER TABLE affiliations
DROP COLUMN firstname;
-- Drop the lastname column
ALTER TABLE affiliations
DROP COLUMN lastname;

-- ********** ********** ********** **********
-- https://campus.datacamp.com/courses/introduction-to-relational-databases-in-sql/glue-together-tables-with-foreign-keys?ex=11
-- ********** **********
-- Identify the correct constraint name
SELECT constraint_name, table_name, constraint_type
FROM information_schema.table_constraints
WHERE constraint_type = 'FOREIGN KEY';
-- Drop the right foreign key constraint
ALTER TABLE affiliations
DROP CONSTRAINT affiliations_organization_id_fkey;

-- Add a new foreign key constraint from affiliations to organizations which cascades deletion
ALTER TABLE affiliations
ADD CONSTRAINT affiliations_organization_id_fkey FOREIGN KEY (organization_id) REFERENCES organizations (id) ON DELETE CASCADE;

-- Delete an organization 
DELETE FROM organizations 
WHERE id = 'CUREM';
-- Check that no more affiliations with this organization exist
SELECT * FROM organizations
WHERE id = 'CUREM';

-- ********** ********** ********** **********
-- https://campus.datacamp.com/courses/introduction-to-relational-databases-in-sql/glue-together-tables-with-foreign-keys?ex=13
-- Count the total number of affiliations per university
SELECT COUNT(*), professors.university_id 
FROM affiliations
JOIN professors
ON affiliations.professor_id = professors.id
GROUP BY professors.university_id 
ORDER BY count DESC;

-- ********** ********** ********** **********
-- https://campus.datacamp.com/courses/introduction-to-relational-databases-in-sql/glue-together-tables-with-foreign-keys?ex=14
-- ********** **********
-- Join all tables
SELECT *
FROM affiliations
JOIN professors
ON affiliations.professor_id = professors.id
JOIN organizations
ON affiliations.organization_id = organizations.id
JOIN universities
ON professors.university_id = universities.id;

-- ********** **********
-- Group the table by organization sector, professor and university city
SELECT COUNT(*), organizations.organization_sector, 
professors.id, universities.university_city
FROM affiliations
JOIN professors
ON affiliations.professor_id = professors.id
JOIN organizations
ON affiliations.organization_id = organizations.id
JOIN universities
ON professors.university_id = universities.id
GROUP BY organizations.organization_sector, 
professors.id, universities.university_city;

-- ********** **********
-- Filter the table and sort it
SELECT COUNT(*), organizations.organization_sector, 
professors.id, universities.university_city
FROM affiliations
JOIN professors
ON affiliations.professor_id = professors.id
JOIN organizations
ON affiliations.organization_id = organizations.id
JOIN universities
ON professors.university_id = universities.id
WHERE organizations.organization_sector = 'Media & communication'
GROUP BY organizations.organization_sector, 
professors.id, universities.university_city
ORDER BY COUNT DESC;
