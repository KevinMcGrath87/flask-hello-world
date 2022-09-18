from ast import NotIn
from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!' 
@app.route('/dojo')
def dojo():
    return('doJo!')
@app.route('/say/<string:var1>')
def say(var1):
    return(f"Hi {var1}!")
@app.route('/repeat/<int:var1>/<string:var2>')
def repeater(var1,var2):
    return(f"{var2} ")*int(var1)
@app.route('/<var1>')
def theELse(var1):
    if var1 not in ['/dojo','/repeat','/']:
        return "WHammy!"

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

