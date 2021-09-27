"""
Basic import model from pydantic
"""
# pylint: disable=too-few-public-methods,unused-private-member
from typing import Optional

# pylint: disable=unused-import,no-name-in-module
from pydantic import BaseModel as PyDBaseModel
from pydantic import Field  # noqa: F401


class BaseModel(PyDBaseModel):
    """
    A basic pydantic model to use in other models
    """

    __message_dict: Optional[dict] = None

    @classmethod
    def from_mesage_dict(cls, content: dict):
        """
        This method will allow you to map first-level keys of a given dictionary
        to the fitting first-level keys of your model.
        You will only need to define an attribute __message_dict in your class
        model.

        :param content: Your actual data
        :return: Your class/model
        """
        mapping: dict = cls.__getattribute__(cls, f"_{cls.__name__}__message_dict")
        if mapping is None:
            return cls(**content)

        content_ = content.copy()
        for key, val in mapping.items():
            content_[key] = content_[val]
            del content_[val]
        print(content_)
        return cls(**content_)
