from football_reminder import db
from football_reminder.models import Match
import datetime

ended_games = db.session.query(Match).filter(
    Match.match_datetime_end < datetime.datetime.now()
).all()

for item in ended_games:
    db.session.delete(item)
db.session.commit()



