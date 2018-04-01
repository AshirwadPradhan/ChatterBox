from flask import Flask, render_template, jsonify, request
import pusher

app = Flask(__name__)


pusher_client = pusher.Pusher(
  app_id='501662',
  key='ce7ac0ad03e1aa221465',
  secret='722e4809517e7599891f',
  cluster='ap2',
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