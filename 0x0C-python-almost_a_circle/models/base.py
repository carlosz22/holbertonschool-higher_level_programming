#!/usr/bin/python3
"""
Module: base.py
Creates the Base Class
"""
import json
import csv
import turtle


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
            if list_objs is not None and len(list_objs) > 0:
                if cls.__name__ == 'Rectangle':
                    headers = ['id', 'width', 'height', 'x', 'y']

                elif cls.__name__ == 'Square':
                    headers = ['id', 'size', 'x', 'y']

                writer = csv.DictWriter(file, fieldnames=headers)

                writer.writeheader()
                for obj in list_objs:
                    obj_dict = obj.to_dictionary()
                    writer.writerow(obj_dict)

    @classmethod
    def load_from_file_csv(cls):
        """Creates instances based on a list of instances from csv file"""
        list_instances = []
        try:
            with open(cls.__name__ + '.csv', encoding='utf-8') as file:
                reader = csv.DictReader(file, delimiter=',')
                for row in reader:
                    for key, value in row.items():
                        row[key] = int(row[key])
                    list_instances.append(cls.create(**row))
                return list_instances
        except:
            return list_instances

    @classmethod
    def draw(cls, list_rectangles, list_squares):
        """Draw the rectangles and squares using Turtle module"""
        color_list = ['coral', 'cornflowerblue', 'gold',
                      'lightseagreen', 'lightskyblue',
                      'lightgrey', 'lightcyan', 'lightcoral',
                      'mediumaquamarine']
        draw = turtle.Turtle()
        color_index = 0
        for r in list_rectangles:
            draw.up()
            draw.begin_fill()
            draw.setposition(r.x, r.y)
            draw.down()
            draw.pencolor(color_list[color_index])
            draw.fillcolor(color_list[color_index])
            for i in range(2):
                draw.down()
                draw.forward(r.width)
                draw.left(90)
                draw.forward(r.height)
                draw.left(90)
            draw.end_fill()
            color_index += 1

        for s in list_squares:
            draw.up()
            draw.begin_fill()
            draw.setposition(s.x, s.y)
            draw.down()
            draw.pencolor(color_list[color_index])
            draw.fillcolor(color_list[color_index])
            for i in range(3):
                draw.down()
                draw.forward(s.size)
                draw.left(90)
            draw.forward(s.size)
            draw.end_fill()
            draw.up()
            color_index += 1
        input()
