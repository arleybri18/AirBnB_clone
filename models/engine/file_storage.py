#!/usr/bin/python3
""" Class FileStorage """
from os.path import exists
from json import dump, load, dumps


class FileStorage:
    """ Create private class variables """
    __file_path = "objects.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key
        <obj class name>.id """
        class_name = obj.__class__.__name__
        iden = obj.id
        cl_id = class_name + "." + iden
        FileStorage.__objects[cl_id] = obj

    def save(self):
        """ serializes __objects to the JSON file
        (path: __file_path) """
        dict_to_json = {}
        for key, value in FileStorage.__objects.items():
            if type(value) is dict:
                dict_to_json[key] = value
            else:
                dict_to_json[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding='utf-8') as fil:
            dump(dict_to_json, fil)

    def reload(self):
        """ deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists )
        otherwise, do nothing. If the file doesnt exist,
        no exception should be raised) """
        if (exists(FileStorage.__file_path)):
            with open(FileStorage.__file_path, "r") as fil:
                FileStorage.__objects = load(fil)
