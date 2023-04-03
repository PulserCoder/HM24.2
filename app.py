from flask import Flask, request, jsonify
from utils import get_file, commands

def create_application():
    app = Flask(__name__)
    return app

app = create_application()


@app.route("/perform_query", methods=["POST"])
def perform_query():
    arguments = request.args
    file_name = arguments.get('file_name')
    cmd1 = arguments.get('cmd1')
    cmd2 = arguments.get('cmd2')
    value1 = arguments.get('value1')
    value2 = arguments.get('value2')
    content = get_file(file_name)
    res1 = commands(cmd=cmd1, value1=value1, data=content)
    if cmd2 is not None:
        res1 = commands(cmd=cmd2, value1=value2, data=res1)
    return jsonify(res1)




if __name__ == '__main__':
    app.run()
