#!/usr/bin/python3
"""
Module: base.py
Creates the Base Class
"""
import json
import csv


class Base:
    """
    Base Class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts a dictionary or string to json"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save list of objects to a json file"""
        json_string = "[]"
        if list_objs is not None and len(list_objs) > 0:
            to_save = []
            for obj in list_objs:
                to_save.append(cls.to_dictionary(obj))
            json_string = Base.to_json_string(to_save)

        file_name = "{}.json".format(cls.__name__)
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Converts json to string"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates a new instance based on a class and a dictionary"""
        if cls.__name__ == 'Rectangle':
            new_instance = cls(1, 1)
        elif cls.__name__ == 'Square':
            new_instance = cls(1)
        cls.update(new_instance, **dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """Creates instances based on a list of instances from json file"""
        try:
            list_instances = []
            with open(cls.__name__ + '.json', 'r', encoding='utf-8') as f:
                json_string = f.read()
                list_attributes = Base.from_json_string(json_string)
            for dictionary in list_attributes:
                list_instances.append(cls.create(**dictionary))
            return list_instances
        except:
            return list_instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save list of objects to a csv file"""
        with open(cls.__name__ + '.csv', 'w', encoding='utf-8') as file:
            if cls.__name__ == 'Rectangle':
                headers = ['id', 'width', 'height', 'x', 'y']

                r_writer = csv.DictWriter(file, fieldnames=headers)

                r_writer.writeheader()
                rec_dictionary = {}
                for rec in list_objs:
                    rec_dictionary['id'] = rec.id
                    rec_dictionary['width'] = rec.width
                    rec_dictionary['height'] = rec.height
                    rec_dictionary['x'] = rec.x
                    rec_dictionary['y'] = rec.y
                    r_writer.writerow(rec_dictionary)

            if cls.__name__ == 'Square':
                headers = ['id', 'size', 'x', 'y']
                s_writer = csv.DictWriter(file, fieldnames=headers)
                s_writer.writeheader()
                squ_dictionary = {}
                for squ in list_objs:
                    squ_dictionary['id'] = squ.id
                    squ_dictionary['size'] = squ.size
                    squ_dictionary['x'] = squ.x
                    squ_dictionary['y'] = squ.y
                    s_writer.writerow(squ_dictionary)

    @classmethod
    def load_from_file_csv(cls):
        """Creates instances based on a list of instances from csv file"""
        try:
            with open(cls.__name__ + '.csv', 'w', encoding='utf-8') as file:
                csv_reader = csv.DictReader(file)
                line_count = 0
                list_objects = []
                for row in csv_reader:
                    dictionary = {}
                    if line_count > 0:
                        dictionary['id'] = row['id']
                        dictionary['x'] = row['x']
                        dictionary['y'] = row['y']
                        if cls.__name__ == 'Rectangle':
                            dictionary['width'] = row['width']
                            dictionary['height'] = row['height']
                        elif cls.__name__ == 'Square':
                            dictionary['size'] = row['size']
                        list_objects.append(cls.create(**dictionary))
                        line_count += 1
            return list_objects
        except:
            return []
