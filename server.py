from flask import Flask, json

api = Flask(__name__)

@api.route('/', methods=['GET'])
def get_companies():
  return 'hi'

if __name__ == '__main__':
    api.run()