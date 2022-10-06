from flask import Flask
import sqlite3
import json
from flask import Flask, request
from flask import jsonify
from twiiter import twint_scrapper
from model import sentence_prediction

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__, static_folder='static')

# API
@app.route('/v0/api/twitter', methods=['GET', 'POST'])
def twitter():
    if request.method == 'POST':
        data = request.get_json()
        conn = get_db_connection()
        hashtags = list(data['hashtags'])
        batch = conn.execute('SELECT MAX(batch) FROM twitter').fetchone()[0]
        batch_new = batch + 1
        data_scrapped = twint_scrapper(hashtags, project_id=batch_new)
        for tweet in data_scrapped:
            posts = conn.execute("INSERT INTO twitter (batch,conversation_id, date_created,username,name,place,tweet,language,mentions,urls,photos,replies_count,retweets_count,likes_count,hashtags,link,thumbnail) VALUES (?,?, ?,?, ?,?, ?,?, ?,?, ?,?, ?,?, ?,?, ?)",
                                 (batch_new, tweet['conversation_id'], tweet['created_at'], tweet['username'], str(tweet['name']), str(tweet['place']), str(tweet['tweet']), tweet['language'], str(tweet['mentions']), str(tweet['urls']), str(tweet['photos']), tweet['replies_count'], tweet['retweets_count'], tweet['likes_count'], str(tweet['hashtags']), str(tweet['link']), str(tweet['thumbnail']))).fetchall()
            conn.commit()
        conn.close()
        return jsonify({'data': {'twitterData': data_scrapped, 'hashtags': hashtags, 'batch':batch_new}})
    elif request.method == "GET":
        return jsonify("Error GET Not Configured")


@app.route('/v0/api/predict/<int:id>', methods=['GET', 'POST'])
def predict(id):
    if request.method == 'GET':
        batch_to_fetch = id
        conn = get_db_connection()
        data = conn.execute('SELECT * FROM twitter WHERE batch = ?', (batch_to_fetch,)).fetchall()
        conn.close()
        out = []
        for row in data:
            tweet = dict(row)
            pred = sentence_prediction(tweet['tweet'])
            if pred >= 0.85:
                tweet['prediction'] = 1
            else:
                tweet['prediction'] = 0
            out.append(tweet)
        return jsonify({'data': {'twitterData': out}})
    elif request.method == "GET":
        return jsonify("Error GET Not Configured")


if __name__ == '__main__':
    app.run(debug=True, port=5000)
