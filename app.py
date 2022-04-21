from flask import Flask, request, jsonify
from util.dishes import get_dishes
app = Flask(__name__)


@app.route('/colby/', methods=['GET'])
def dishes():
    HALLS_DATA = {"Dana": 1445, "Robert": 1447}
    # name = request.args.get("name", None)

    response = {"Dana": {}, "Robert": {}}
    for hall_name, hall_id in HALLS_DATA.items():
        response[hall_name] = get_dishes(hall_id)

    # # Check if the user sent a name at all
    # if not name:
    #     response["ERROR"] = "No name found. Please send a name."
    # # Check if the user entered a number
    # elif str(name).isdigit():
    #     response["ERROR"] = "The name can't be numeric. Please send a string."
    # else:
    #     response["MESSAGE"] = f"Welcome {name} to our awesome API!"

    # Return the response in json format
    return jsonify(response)


# @app.route('/post/', methods=['POST'])
# def post_something():
#     param = request.form.get('name')
#     print(param)
#     # You can add the test cases you made in the previous function, but in our case here you are just testing the POST functionality
#     if param:
#         return jsonify({
#             "Message": f"Welcome {param} to our awesome API!",
#             # Add this option to distinct the POST request
#             "METHOD": "POST"
#         })
#     else:
#         return jsonify({
#             "ERROR": "No name found. Please send a name."
#         })


@app.route('/')
def index():
    # A welcome message to test our server
    return "<h1>Welcome to our medium-greeting-api!</h1>"


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)