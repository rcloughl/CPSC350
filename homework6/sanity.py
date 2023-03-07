import mariadb
conn = mariadb.connect(user="joe", password="rjcrjc",
    host="localhost", port=5051, database="dbTour")
cur = conn.cursor()
cur.execute("select * from simple")
answer = cur.fetchone()
print(f"The answer is {answer[0]}.")
