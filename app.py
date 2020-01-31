
from flask import Flask

from routes.index_routes import index
from routes.project_routes import projects


# we extract the mongo uri from the env


app = Flask(__name__)


app.register_blueprint(index)
app.register_blueprint(projects)

if __name__ == "__main__":

    app.run(debug=True)
