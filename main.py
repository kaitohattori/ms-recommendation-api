from flasgger import Swagger
from flask import Flask

from app.controllers import video


app = Flask(__name__)
app.config['SWAGGER'] = {
    'title': 'MS Recommendation API'
}

app.register_blueprint(video.app)

swagger_config = {
    "headers": [
    ],
    "specs": [
        {
            "endpoint": 'doc',
            "route": '/doc.json',
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/flasgger_static",
    # "static_folder": "static",  # must be set by user
    "swagger_ui": True,
    "specs_route": "/docs/api/v1/"
}

swagger = Swagger(app, config=swagger_config)

app.run(host="0.0.0.0", port="8082", debug=True)
