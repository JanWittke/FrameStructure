from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/CheckDimensions', methods=['POST'])
def CheckDimensions():
    try:
        # Hier erhältst du die Daten aus dem Frontend
        height = float(request.form['height'])
        width = float(request.form['width'])
        length = float(request.form['length'])

        # Hier kannst du deine Berechnungen durchführen
        Volume = height * width * length

        # Hier gibst du das Ergebnis an das Frontend zurück
        return jsonify({'result': Volume, 'status': 'success'})
    except ValueError:
        # Fehler, falls die Eingabe keine gültigen Zahlen waren
        return jsonify({'status': 'error', 'message': 'Ungültige Eingabe'})

if __name__ == '__main__':
    app.run(debug=True)