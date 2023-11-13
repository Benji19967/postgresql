import psycopg2

if __name__ == "__main__":
    conn = psycopg2.connect("dbname=birthdays user=benjaminlabrecque")

    cur = conn.cursor()

    cur.execute("SELECT * FROM birthday;")
    row = cur.fetchone()
    all_rows = cur.fetchall()  # fetches only remaining rows
    print(row)
    print(all_rows)

    cur.close()
