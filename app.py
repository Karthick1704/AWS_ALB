from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Example: Read an environment variable if set
    target = os.environ.get('TARGET', 'World')
    return f'Hello {target}!\nWelcome to my AWS ECS Fargate App!\n'

if __name__ == "__main__":
    # Run on port 8080, accessible from outside the container
    app.run(host='0.0.0.0', port=8080)