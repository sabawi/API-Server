from flask import request

from app import app


@app.route('/authenticate', methods=['POST'])
def authenticate():
    content = request.get_json()
    authentication = 'Failed'
    if content['userid'] == 'myusername' and content['password'] == 'password123':
        authentication = 'Success'

    print(authentication)
    return '\n' + authentication + '\n'
