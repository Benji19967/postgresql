# Installation

https://wiki.postgresql.org/wiki/Homebrew

- `brew install postgresql@15`
- `brew services start postgresql`
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

### Select all rows from a table

```SQL
SELECT * FROM birthday;
```
