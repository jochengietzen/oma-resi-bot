class TestMessage(dict):
    def to_dict(self):
        return self


test_messages = dict(
    another_time={
        "entities": [],
        "group_chat_created": False,
        "caption_entities": [],
        "text": "another time",
        "message_id": 518,
        "photo": [],
        "new_chat_photo": [],
        "new_chat_members": [],
        "supergroup_chat_created": False,
        "delete_chat_photo": False,
        "channel_chat_created": False,
        "date": 1632746129,
        "chat": {
            "last_name": "Gietzen",
            "first_name": "Jochen",
            "id": 401524375,
            "username": "jochengietzen",
            "type": "private",
        },
        "from": {
            "is_bot": False,
            "id": 401524375,
            "last_name": "Gietzen",
            "first_name": "Jochen",
            "username": "jochengietzen",
            "language_code": "en",
        },
    }
)
