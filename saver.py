import json
from dicttoxml import dicttoxml
from xml.dom.minidom import parseString
from abc import abstractmethod, ABC


class Saver(ABC):
    @staticmethod
    @abstractmethod
    def save(values_list: list, result_name: str):
        pass


class JsonSaver:
    @staticmethod
    def save(values_list: list, result_name: str):
        with open('{}.json'.format(result_name), 'w') as write_file:
            json.dump(values_list, write_file, indent=4)


class XmlSaver:
    @staticmethod
    def save(values_list: list, result_name: str):
        xml = dicttoxml(values_list)
        pretty_xml = parseString(xml).toprettyxml()
        with open('{}.xml'.format(result_name), 'w') as write_file:
            write_file.write(pretty_xml)
