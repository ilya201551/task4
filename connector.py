import mysql.connector
from queries import DBQueries
from settings import CON_SETTINGS as CONF


class DBConnector:
    def __init__(self):
        self.connector = mysql.connector.connect(
            host=CONF['host'],
            user=CONF['user'],
            passwd=CONF['passwd'],
            database=CONF['database'],
            auth_plugin=CONF['auth_plugin'],
        )
        self.cursor = self.connector.cursor()

    def create_db(self):
        self.cursor.execute(DBQueries.create_db_query())

    def delete_db(self):
        self.cursor.execute(DBQueries.delete_db_query())

    def drop_tables(self):
        for table in DBQueries.drop_tables():
            self.cursor.execute(table)

    def create_tables(self):
        for table in DBQueries.create_tables_query():
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

    def commit(self):
        self.connector.commit()

    def selecting_data(self, query):
        self.cursor.execute(query)
        row_headers = [i[0] for i in self.cursor.description]
        results = self.cursor.fetchall()
        values_list = []
        for result in results:
            values_list.append(dict(zip(row_headers, result)))
        return values_list
