import os
from flask_example import create_app

env_name = os.environ.get('APP_ENV')
app = create_app(env_name)


if __name__ == "__main__":
    app.run(port=5678)
