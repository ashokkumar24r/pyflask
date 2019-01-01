import sys
# import pdb; pdb.set_trace()
try:
    from flask import Flask
except ModuleNotFoundError:
    print("Not able to find flask")

else:
    print("Flask successfully installed")

app = Flask(__name__)

@app.route('/')
def index():
    return "Hi Ashok{}"

@app.route('/<name>')
def Name(name):
    return "{}" .format(name[10])

if __name__ == '__main__':
    app.run(debug=True)
