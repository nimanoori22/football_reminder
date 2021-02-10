from sqlalchemy.orm import defer
from football_reminder import db

def getFromdb(model, column):
    query = db.session.query(model)
    query = query.options(defer(column))
    mylist = query.all()

    return ([getattr(obj, column) for obj in mylist])

def teams_separator(teams):
    return [item.strip() for item in teams.split('-')]