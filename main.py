from flask import Flask, render_template, url_for, request, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from os import path

DB_NAME="database.db"

app = Flask(__name__)
app.config["SECRET_KEY"] = "key"
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
db.init_app(app)

# NOTES: 
#   delete function
#   use another modal and onclick in order to delete
#   along with delete implement edit in same modal
#   fix scaling issues for add event button
#   idea to stick button at bottom to not interfere with spacing at the top


events = []

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(100000))
    event_date = db.Column(db.String(100000))


@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        event_name = request.form['eventName']
        event_date = request.form['eventDate']
        new_event = Event(event_name=event_name, event_date=event_date)

        db.session.add(new_event)
        db.session.commit()
        events.append({'todo': new_event.event_name, 'date': new_event.event_date})
        return redirect('/')
    else:

        return render_template('base.html', events=events)
    
@app.route('/delete', methods=['POST', 'GET'])
def delete():
    id = request.arg.get('id')


def create_database(app):
    if not path.exists('another flask project/' + DB_NAME):
        db.create_all(app=app)
        print('db created')

def db_check():
    temp = Event.query.all()
    for event in temp:
        events.append({'todo': event.event_name, 'date': event.event_date, 'id': event.id})



if __name__ == '__main__':
    db_check()
    create_database(app)
    app.run(debug=True)