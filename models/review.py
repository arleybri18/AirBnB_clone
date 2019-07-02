#!/usr/bin/python3
from models.base_model import BaseModel


class City(BaseModel):
    """ Class review for create reviewes of application
    place_id: string - empty string: it will be the Place.id
    user_id: string - empty string: it will be the User.id
    text: string - empty string
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """ init method call method of the super class """
        """instantiates a new user"""
        super().__init__(self, *args, **kwargs)
