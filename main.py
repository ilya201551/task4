import argparse
from connector import DBConnector
from queries import DBQueries
from loader import JsonLoader
from saver import JsonSaver, XmlSaver


def parsing_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('students_path', type=str, help='Path to the students file.')
    parser.add_argument('rooms_path', type=str, help='Path to the rooms file.')
    parser.add_argument('format_', type=str, help='Source file format(json/xml).')
    args = parser.parse_args()
    return args


def main():
    args = parsing_args()
    savers = {
        'json': JsonSaver(),
        'xml': XmlSaver(),
    }
    if args.format_.lower() not in savers.keys():
        raise ValueError('Invalid format.')

    db = DBConnector()
    db.create_tables()
    db.rooms_inserting(JsonLoader.load(args.rooms_path))
    db.students_inserting(JsonLoader.load(args.students_path))
    db.commit()

    for query_name, query in DBQueries.selecting_from_db().items():
        savers[args.format_.lower()].save(db.selecting_data(query), query_name)

    db.drop_tables()


main()
