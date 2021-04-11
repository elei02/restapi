from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

users = { 
   'users_list' :
   [
      { 
         'id' : 'xyz789',
         'name' : 'Charlie',
         'job': 'Janitor',
      },
      {
         'id' : 'abc123', 
         'name': 'Mac',
         'job': 'Bouncer',
      },
      {
         'id' : 'ppp222', 
         'name': 'Mac',
         'job': 'Professor',
      }, 
      {
         'id' : 'yat999', 
         'name': 'Dee',
         'job': 'Aspring actress',
      },
      {
         'id' : 'zap555', 
         'name': 'Dennis',
         'job': 'Bartender',
      }
   ]
}

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/users', methods=['GET', 'POST'])
def get_users():
   if request.method == 'GET':
      search_username = request.args.get('name')
      search_job = request.args.get('job')
      
      if search_username and not search_job:
         subdict = {'users_list' : []}
         for user in users['users_list']:
            if user['name'] == search_username:
               subdict['users_list'].append(user)
         return subdict
      elif search_username and search_job:
         subdict = {'users_list' :[]}
         for user in users['users_list']:
            if user['name'] == search_username and user['job'] == search_job:
               subdict['users_list'].append(user)
         return subdict
      return users
   elif request.method == 'POST':
      userToAdd = request.get_json()
      userToAdd['id'] = randomID(userToAdd['name']);
      users['users_list'].append(userToAdd)
      resp = jsonify(userToAdd)
      #resp.status_code = 200 #optionally, you can always set a response code. 
      # 200 is the default code for a normal response
      resp.status_code = 201
      return resp

@app.route('/users/<id>', methods = ['GET','DELETE'])
def get_user(id):
   if request.method == 'GET':
      if id :
         for user in users['users_list']:
           if user['id'] == id:
              return user
         return ({})
      return users
   elif request.method == 'DELETE':
      response = jsonify(success=True)
      response.status_code = 404
      for user in users['users_list']:
         if id==user['id'] :
            users['users_list'].remove(user)
            response.status_code = 204
            return response
      response = jsonify(success=False)
      return response

def randomID(fname):
   a = ''
   for character in fname:
      a = a + chr(((ord(character)*7)%74)+48)
   return a
