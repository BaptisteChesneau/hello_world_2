from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return '''
    <html>
        <head>
            <style>
                body {
                    background-color: #1A1A1A;  /* Dark background */
                    font-family: Arial, sans-serif; /* Font style */
                }
                .animated-text {
                    color: burlywood;
                    animation: bounceIn 2s ease; /* Bounce-in animation */
                }
                @keyframes bounceIn {
                    0% { transform: scale(0.5); }
                    50% { transform: scale(1.2); }
                    70% { transform: scale(0.9); }
                    100% { transform: scale(1); }
                }
            </style>
        </head>
        <body>
            <div class="animated-text">Hello, World!</div>
        </body>
    </html>
    '''

    app.run(debug=True)








