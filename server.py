from flask import Flask, json, request
from flask_cors import CORS;

languages = [{"id": 1, "language": "French"}, {"id": 2, "language": "English"}]

api = Flask(__name__)
CORS(api)

@api.route('/languages/get', methods=['GET'])
def get_languages():
  return json.dumps(languages)

if __name__ == '__main__':
  api.run()