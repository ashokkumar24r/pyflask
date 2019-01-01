from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def index():
    name="Ashok kumar"
    lists=name.split()
    return render_template('bootstrapMethodsRT.html',name=name,lists=lists)

if __name__ == '__main__':
    app.run(debug="True")
