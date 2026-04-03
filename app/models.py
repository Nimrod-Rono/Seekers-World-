from mongoengine import Document, StringField, IntField, ListField, ReferenceField, DateTimeField


class User(Document):
    username = StringField(required=True, unique=True)
    email = StringField(required=True, unique=True)
    password = StringField(required=True)
    created_at = DateTimeField()


class Game(Document):
    title = StringField(required=True)
    description = StringField()
    release_date = DateTimeField()
    created_by = ReferenceField(User)
    created_at = DateTimeField()


class Stream(Document):
    game = ReferenceField(Game)
    user = ReferenceField(User)
    start_time = DateTimeField()
    end_time = DateTimeField()
    created_at = DateTimeField()


class Highlight(Document):
    stream = ReferenceField(Stream)
    description = StringField()
    timestamp = DateTimeField()
    created_at = DateTimeField()


class GameTable(Document):
    game = ReferenceField(Game)
    players = ListField(ReferenceField(User))
    created_at = DateTimeField()