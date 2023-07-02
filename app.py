"""
Moduł Flask App
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    """
    Strona główna

    Funkcja obsługuje żądania na stronie głównej.
    Zwraca HTML z napisem "Hello WSB! Greetings from Flask!".
    """
    return '<h1>Hello WSB! Greetings from Flask!</h1>'

if __name__ == "__main__":
    app.run(debug=True)
