from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
     players = ["adele","shakira", "shawn"]
     return render_template (
     	"index.html", 
     	players=players , 
     	no_players = True)


if __name__ == '__main__':
   app.run(debug = True)