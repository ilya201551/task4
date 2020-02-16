class DBQueries:
    @staticmethod
    def create_db_query():
        return 'CREATE DATABASE result'

    @staticmethod
    def delete_db_query():
        return 'DROP DATABASE result'

    @staticmethod
    def create_tables_query():
        return ['''CREATE TABLE Rooms (id INTEGER NOT NULL,
                                       name VARCHAR(30) NOT NULL,
                                       PRIMARY KEY(id))''',
                '''CREATE TABLE Students (id INTEGER NOT NULL,
                                          name VARCHAR(30) NOT NULL,
                                          birthday DATETIME,
                                          room INTEGER NOT NULL,
                                          sex CHAR(1) NOT NULL,
                                          PRIMARY KEY(id),
                                          FOREIGN KEY(room) REFERENCES Rooms(id) ON DELETE CASCADE)''',
                ]

    @staticmethod
    def drop_tables():
        return ['DROP TABLE Students',
                'DROP TABLE Rooms',
                ]

    @staticmethod
    def rooms_inserting():
        return 'INSERT INTO Rooms(id, name) VALUES(%s, %s)'

    @staticmethod
    def students_inserting():
        return 'INSERT INTO Students(id, name, birthday, room, sex) VALUES(%s, %s, %s, %s, %s)'

    @staticmethod
    def selecting_from_db():
        queries = {'rooms_and_students_quantity': '''SELECT Rooms.id as room_id,
                                                            Rooms.name as room_name,
                                                            COUNT(Students.id) as quantity 
                                                     FROM Rooms JOIN Students ON Rooms.id = Students.room
                                                     GROUP BY Rooms.id''',

                   'top5_rooms_with_min_avg_age': '''SELECT Rooms.id as room_id,
                                                            Rooms.name as room_name,
                                                            CAST(AVG(TIMESTAMPDIFF(YEAR,Students.birthday,NOW())) as float) as avg_age
                                                     FROM Rooms JOIN Students ON Rooms.id = Students.room
                                                     GROUP BY Rooms.id
                                                     ORDER BY avg_age
                                                     LIMIT 5''',

                   'top5_rooms_with_max_age_diff': '''SELECT Rooms.id as room_id,
                                                      Rooms.name as room_name,
                                                      TIMESTAMPDIFF(YEAR,MIN(Students.birthday),MAX(Students.birthday))
                                                                    as age_diff
                                                      FROM Rooms
                                                      JOIN Students ON Rooms.id = Students.room
                                                      GROUP BY Rooms.id
                                                      ORDER BY age_diff DESC
                                                      LIMIT 5''',

                   'rooms_with_M_and_F_sex': '''SELECT Rooms.id as room_id,
                                                       Rooms.name as room_name
                                                       FROM Rooms JOIN Students ON Rooms.id = Students.room
                                                       GROUP BY Rooms.id
                                                       HAVING COUNT(DISTINCT Students.sex) > 1''',
                   }
        return queries
