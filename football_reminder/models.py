from football_reminder import db

class Match(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    teams = db.Column(db.String(250), unique=True, nullable=False)
    host = db.Column(db.String(50), nullable=False)
    guest = db.Column(db.String(50), nullable=False)
    day = db.Column(db.String(100), nullable=False)
    match_datetime_start = db.Column(db.DateTime, nullable=False)
    match_datetime_end = db.Column(db.DateTime, nullable=False)
    channel = db.Column(db.String(150), nullable=False)
    league = db.Column(db.String(100), nullable=False)
    time = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return self.teams



