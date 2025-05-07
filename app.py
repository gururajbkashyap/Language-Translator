from flask import Flask, render_template, request, jsonify
from deep_translator import GoogleTranslator

app = Flask(__name__)

# Language codes for translation
LANGUAGE_CODES = {
    'kannada': 'kn',
    'hindi': 'hi',
    'tamil': 'ta',
    'telugu': 'te',
    'malayalam': 'ml',
    'sanskrit': 'sa',
    'brazilian_portuguese': 'pt',  # Same as Portuguese
    'german': 'de'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    text = data.get('text')
    lang = data.get('language')

    # Validate input
    if not text or lang not in LANGUAGE_CODES:
        return jsonify({'error': 'Invalid input'}), 400

    try:
        translated_text = GoogleTranslator(source='en', target=LANGUAGE_CODES[lang]).translate(text)
        return jsonify({'translated_text': translated_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
