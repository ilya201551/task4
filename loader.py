import json
from abc import abstractmethod, ABC


class Loader(ABC):
    @staticmethod
    @abstractmethod
    def load(file_path: str):
        pass


class JsonLoader(Loader):
    @staticmethod
    def load(file_path: str):
        with open(file_path, 'r') as read_file:
            json_list = json.load(read_file)
        return json_list
