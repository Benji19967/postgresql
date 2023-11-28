# Installation

https://wiki.postgresql.org/wiki/Homebrew

- `brew install postgresql@15`
- `brew services start postgresql`
- `brew services restart postgresql` if `start` does not work
- `psql <db name>`: `psql postgres` or `psql birthdays`

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

