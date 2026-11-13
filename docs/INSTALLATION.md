# Installation

https://wiki.postgresql.org/wiki/Homebrew

- `brew install postgresql@18`

## Launch the `postgresql@18` server
- `brew services start postgresql@18`
- `brew services restart postgresql` if `start` does not work

- `psql --list`: list available databases
- `psql <db name>`: `psql postgres` or `psql birthdays`

## Errors

## Cannot start DB

```
psql: error: connection to server on socket "/tmp/.s.PGSQL.5432" failed: No such file or directory
        Is the server running locally and accepting connections on that socket?
```
```bash
rm /opt/homebrew/var/postgresql@15/postmaster.pid
brew services restart postgresql@15
```