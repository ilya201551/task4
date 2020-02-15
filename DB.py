import mysql.connector
from queries import DBQueries
from loader import JsonLoader

# cursor.execute('USE testdatabase')
# cursor.execute('''CREATE TABLE Rooms (id INTEGER NOT NULL,
#                                         name VARCHAR(30) NOT NULL,
#                                         PRIMARY KEY(id))''')
# cursor.execute("""CREATE TABLE Students (id INTEGER NOT NULL,
#                                             name VARCHAR(30) NOT NULL,
#                                             birthday DATETIME,
#                                             room INTEGER NOT NULL,
#                                             sex VARCHAR(1) NOT NULL,
#                                             PRIMARY KEY(id),
#                                             FOREIGN KEY(room) REFERENCES Rooms(id) ON DELETE CASCADE) """)

# cursor.execute('INSERT INTO rooms VALUES (1, "Room #1")')
# db.commit()


class DBConnector:
    def __init__(self):
        self.connector = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='root',
            database='result',
            auth_plugin='mysql_native_password',
        )
        self.cursor = self.connector.cursor()

    def creating_db(self):
        self.cursor.execute('CREATE DATABASE result')

    def delete_db(self):
        self.cursor.execute('DROP DATABASE result')

    def creating_tables(self):
        for table in DBQueries.creating_tables_query():
            self.cursor.execute(table)

    def rooms_inserting(self, rooms_list):
        for room in rooms_list:
            self.cursor.execute(DBQueries.rooms_inserting(), (room['id'],
                                                              room['name']))

    def students_inserting(self, students_list):
        for student in students_list:
            self.cursor.execute(DBQueries.students_inserting(), (student['id'],
                                                                 student['name'],
                                                                 student['birthday'],
                                                                 student['room'],
                                                                 student['sex']))


def main():
    db = DBConnector()
    # db.creating_tables()
    # db.rooms_inserting(JsonLoader.load('room.json'))
    # db.students_inserting(JsonLoader.load('student.json'))
    # db.connector.commit()
    db.cursor.execute('''SELECT Rooms.id as room_id, Rooms.name as room_name
                         FROM Rooms JOIN Students ON Rooms.id = Students.room
                         GROUP BY Rooms.id
                         HAVING COUNT(DISTINCT Students.sex) > 1
                         ''')
    for i in db.cursor:
        print(i)

main()










































