#!/usr/bin/python3
"""This module defines the BaseModel Class"""


from datetime import datetime
from uuid import uuid4
import models


class BaseModel():
    """This is the BaseModel class"""
    def __init__(self, *args, **kwargs):
        """
        Initialize the object with a random uuid
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))

                else:
                    self.__setattr__(key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def to_dict(self):
        """
        Returns a dict containing values of self.__dict__
        """
        result = dict(self.__dict__)
        result['created_at'] = self.created_at.isoformat()
        result['updated_at'] = self.updated_at.isoformat()
        result['__class__'] = self.__class__.__name__
        return result

    def save(self):
        """
        Updates the public instance attribute updated_at to now
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def __repr__(self):
        """
        Returns a string representation in the form
        [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
