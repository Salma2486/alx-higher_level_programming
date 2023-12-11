#!/usr/bin/python3
""" we5t wy5e  yw4rwy 454"""
import json
import csv


class Base:
    """ro yjeori6y woriy6 twry """

    __nb_objects = 0

    def __init__(self, id=None):
        """rts ihyker oypkwry """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ rthwr hthw r"""
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """be56w4b5y6by56neb5v  e55e y55"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """ eyrohij reioj wry"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ tyd eyrh eyty"""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            dummy_instance = cls()

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """ehrt eytyh yr"""
        filename = "{}.json".format(cls.__name__)

        try:
            with open(filename, mode='r') as file:
                json_str = file.read()
                dicts = cls.from_json_string(json_str)
                instances = [cls.create(**dictionary) for dictionary in dicts]
                return instances
        except FileNotFoundError:
            return []
