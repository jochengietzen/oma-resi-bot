"""
This module provides some models for messaging purposes
"""
# pylint: disable=too-few-public-methods,unused-private-member
from typing import List, Optional

from oma_resi_bot.models.base_pydantic import BaseModel, Field


class User(BaseModel):
    """
    simple user model
    """

    id: str


class Chat(BaseModel):
    """
    simple chat model
    """

    id: str
    type: str


class Message(BaseModel):
    """
    simple message model
    """

    sender: User
    chat: Chat
    text: Optional[str] = None
    photo: List[str] = Field(default_factory=list)

    __message_dict: dict = {"sender": "from"}
