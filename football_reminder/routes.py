from flask import jsonify
from football_reminder import app
from football_reminder.models import Match

@app.route('/', methods=['GET'])
def get_matches():
    match_list = []
    all_matches = Match.query.all()
    for match in all_matches:
        mydict = {}
        mydict['name'] = match.teams
        mydict['host'] = match.host
        mydict['guest'] = match.guest
        mydict['day'] = match.day
        mydict['channel'] = match.channel
        mydict['league'] = match.league
        mydict['time'] = match.time
        match_list.append(mydict)
    response = jsonify(match_list)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response