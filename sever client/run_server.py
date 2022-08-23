from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():    
    return "Hello Gaemigo Project Home Page!!"
    
@app.route('/visit/<username>')
def visited(username): 
    #return 'User %s' % username  
    return f'Hello {username}!'


@app.route('/product/<int:pid>')
def pickup(pid): 
    #return 'User %s' % username  
    return f'Pickup {pid}!'
          
          
if __name__ == '__main__':    
    app.run(debug=True, port=5000)
 