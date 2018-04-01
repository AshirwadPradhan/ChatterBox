from flask import Flask, render_template, jsonify, request
import pusher
from cred import app_id, key, secret, cluster

app = Flask(__name__)


pusher_client = pusher.Pusher(
  app_id=app_id,
  key=key,
  secret=secret,
  cluster=cluster,
  ssl=True

)

@app.route('/')
def index():
   # pusher_client.trigger('my-channel', 'my-event', {'message': 'hello world'})
    return render_template('index.html')

@app.route('/message', methods=['POST'])
def message():

    try:
        username = request.form.get('username')
        message = request.form.get('message')

        pusher_client.trigger('chat-channel', 'chat-event', {'username': username ,'message': message})
        
        return jsonify({'result':'success'})
    except:
        return jsonify({'result':'failure'})

    return 


if __name__=='__main__':
    app.run(debug=True)