# Installation

https://wiki.postgresql.org/wiki/Homebrew

- `brew install postgresql@15`
- `brew services start postgresql`
- `brew services restart postgresql` if `start` does not work
- `psql <db name>`: `psql postgres` or `psql birthdays`

# Resources

- SQL Cookbook by Anthony Molinaro

# Errors

## Cannot start DB

```
psql: error: connection to server on socket "/tmp/.s.PGSQL.5432" failed: No such file or directory
        Is the server running locally and accepting connections on that socket?
```
```bash
rm /opt/homebrew/var/postgresql@15/postmaster.pid
brew services restart postgresql@15
```

# Commands

https://tomcam.github.io/postgres/#using-psql

## Creating a new database

`createdb <db name>`

## `psql`

`psql <db name>` to start

- `\q`: quitting
- `\h`: getting help
  - `\h <command>`
  - `\h ALTER TABLE`

- `\l`: list databases
- `\l+`: list databases with size, tablespace and description
- `\x on/off`: toggle on or off expanded display
- `\c <name of database>`: connect to a database
- `\dt`: display all relations (tables) in database
- `\d <name of table>` or `\d+ <name of table>`: display columns (field names) of a table
- `\du` or `\du <user>`: display user roles
- `\timing on/off`: turn timing on or off

## SQL

### SQL vs Pandas

- Pulling a lot of data to handle it with Pandas requires a lot of memory,
network bandwidth, ... .
- It's better to filter out data early (use SQL to filter at DB level)
- SQL can be more intuitive (the API to do joins in Pandas can unintuitive)

### Create a table

```SQL
create table if not exists birthday (
  id              SERIAL,
  first_name      VARCHAR(100) NOT NULL, 
  last_name       VARCHAR(100) NOT NULL,
  birthday        DATE NOT NULL
);
```

### Insert into a table

```SQL
INSERT INTO birthday VALUES(DEFAULT, 'John', 'Doe', '1993-11-19');
```

### Delete from a table

```SQL
DELETE FROM birthday WHERE first_name = 'John';
```

### Delete all rows from a table

```SQL
DELETE FROM birthday;
```

### Select all rows from a table

```SQL
SELECT * FROM birthday;
```

### Count number of rows in a table

```SQL
SELECT COUNT(*) FROM birthday;
```

### Select all rows from a table where a column is not null

```SQL
SELECT price_display from listing WHERE price_display IS NOT NULL;
```

### Select all unique values (distinct) in a column

```SQL
SELECT DISTINCT price_display_type from listing;
```

### Select max from a column (there are other ways)

```SQL
SELECT * from listing WHERE price_display IS NOT NULL ORDER BY price_display DESC LIMIT 1;
```

### Concatenate strings from different columns

- Postgres specific

```SQL
SELECT city||' at latitude '||latitude AS msg FROM listing;
```

### Use conditional logic (if/else)

```SQL
SELECT price_display,
    CASE 
        WHEN price_display < 1000 THEN 'CHEAP'
        WHEN price_display > 3000 THEN 'EXPENSIVE'
        ELSE 'REGULAR' 
    END AS price_category
from listing;
```

### Select rows at random

```SQL
SELECT id, city, slug from listing ORDER BY random() LIMIT 1;
```

### Transform NULL values into real values

```SQL
SELECT COALESCE(price_display, -9999) from listing;
```

### Search for patterns (in strings)

- Select all slugs that contain the substring zurich

```SQL
SELECT slug FROM listing WHERE slug LIKE '%zurich%'
```

- Select all the cities that start with the letter "g" or "G"

```SQL
SELECT city FROM listing WHERE city LIKE 'g%' or city LIKE 'G%'
```

### Sort by substrings

- Sort cities by their last 2 characters
- `substr(str, start_position inclusive)` 1-indexed

```SQL
SELECT city FROM listing ORDER by substr(city, length(city)-1);
```

- ... and get only unique values

```SQL
SELECT city FROM listing GROUP BY city ORDER by substr(city, length(city)-1);
```

### Sort mixed alphanumeric data

```SQL
CREATE VIEW v 
AS SELECT city||' '||floor AS data 
FROM listing WHERE floor IS NOT NULL;
```

```SQL
SELECT * FROM v;
                 data                  
---------------------------------------
 St. Margrethen SG 10
 St. Gallen 0
 Zürich 5
 Pully 4
 Echallens 4
 Lausanne 0
 Vouvry 0
 Neuchâtel 0
 Founex 2
 Perrefitte 2
 Trimbach 1
```

- Sort by chars

```SQL
SELECT data FROM v 
ORDER BY REPLACE(TRANSLATE(data, '0123456789', '##########'), '#', '');
```

- Sort by numbers

```SQL
SELECT data FROM v 
ORDER BY REPLACE(data, 
REPLACE(TRANSLATE(data, '0123456789', '##########'), '#', ''), '');
```

- Get chars only

```SQL
SELECT data, 
REPLACE(TRANSLATE(data, '0123456789', '##########'), '#', '') chars 
FROM v;

                 data                  |                chars                 
---------------------------------------+--------------------------------------
 St. Margrethen SG 1                   | St. Margrethen SG 
 St. Gallen 0                          | St. Gallen 
 Zürich 5                              | Zürich 
 Pully 4                               | Pully 
 Echallens 4                           | Echallens 
 Lausanne 0                            | Lausanne 
 Vouvry 0                              | Vouvry 
 Neuchâtel 0                           | Neuchâtel 
 Founex 2                              | Founex 
 Perrefitte 2                          | Perrefitte
```

- Get numbers only
```SQL
SELECT data, 
REPLACE(data, 
REPLACE(TRANSLATE(data, '0123456789', '##########'), '#', ''), '') nums
FROM v;

                 data                  |      nums       
---------------------------------------+-----------------
 St. Margrethen SG 1                   | 1
 St. Gallen 0                          | 0
 Zürich 5                              | 5
 Pully 4                               | 4
 Echallens 4                           | 4
 Lausanne 0                            | 0
 Vouvry 0                              | 0
 Neuchâtel 0                           | 0
 Founex 2                              | 2
 Perrefitte 2                          | 2
```

```SQL
DROP VIEW v;
```
