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

team_league = db.Table('team_league',
    db.Column('team_id', db.Integer, db.ForeignKey('team.id'), primary_key=True),
    db.Column('league_id', db.Integer, db.ForeignKey('league.id'), primary_key=True)
)

class Team(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

class League(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    teams = db.relationship('Team', secondary=team_league, lazy='subquery', backref=db.backref('leagues', lazy=True))



