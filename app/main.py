from flask import Flask
 
app = Flask(__name__)
 
@app.route("/")
def home_view():
        return "<h1>Welcome to Geeks for Geeks</h1>"



'''
from explainerdashboard import ClassifierExplainer, ExplainerDashboard

explainer = ClassifierExplainer.from_file("explainer.joblib")
# you can override params during load from_config:
db = ExplainerDashboard.from_config(explainer, "dashboard.yaml", title="Awesomer Title")

app = db.flask_server()
'''
