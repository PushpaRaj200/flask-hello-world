import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Idhi Thirgubatudarula Rule uh.."

if __name__ == '__main__':
    # Binding to 0.0.0.0 ensures the cloud provider can route traffic to it
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
