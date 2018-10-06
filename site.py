from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
   return "Hello welcome to my site"

@app.route('/Genre')
   return "List of genres"

@app.route('/Genre/FPS')
   return "List of First Person Shooters"

@app.route('/Genre/Platformer')
   return "List of Platformers"

@app.route('/Genre/Strategy')
   return "List of Strategy games"

@app.route('/Genre/RPG')
   return "List of RPGs"

if __name__ == "__main__":
   app.run(host='0.0.0.0', debug=True)
