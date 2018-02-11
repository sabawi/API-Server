from flask import request
from app import app


@app.route('/authenticate', methods=['POST'])
def authenticate():
    # Test this API with curl:
    # curl -d '{"userid":"myusername", "password":"password123"}' -H "Content-Type: application/json" -X  POST http://localhost:8080/authenticate
    content = request.get_json()
    authentication = 'Failed'
    if content['userid'] == 'myusername' and content['password'] == 'password123':
        authentication = 'Success'

    print(authentication)
    return '\n' + authentication + '\n'
