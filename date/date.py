from flask import Flask, render_template_string
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello, World!</title>
    <style>
        body {
            background-color: lightblue;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        #date-time {
            position: absolute;
            top: 0;
            padding: 10px;
        }
        h1 {
            font-size: 22px;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div id="date-time">{{ current_datetime }}</div>
    <h1>Hello, World!, Welcome to ZSoftly</h1>
</body>
</html>
'''
    return render_template_string(template, current_datetime=current_datetime)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

