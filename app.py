from flask import Flask, render_template, request
from langdetect import detect_langs
from googletrans import Translator

app = Flask(__name__)

# Language codes and names
LANGUAGES = {
    'en': 'English',
    'fr': 'French',
    # 'te': 'Telugu',
    'es': 'Spanish',
    'pt': 'Portuguese',
    'it': 'Italian',
    'ru': 'Russian',
    'sv': 'Swedish',
    'ml': 'Malayalam',
    'nl': 'Dutch',
    'ar': 'Arabic',
    'tr': 'Turkish',
    'de': 'German',
    'ta': 'Tamil',
    'da': 'Danish',
    'kn': 'Kannada',
    'el': 'Greek',
    'hi': 'Hindi',
    'ko': 'Korean',  # Korean
    'zh-CN': 'Chinese (Simplified)',  # Chinese (Simplified)
    'ja': 'Japanese',  # Japanese
}

# Function to detect language and return full name
def detect_language_full_name(text):
    try:
        lang_results = detect_langs(text)
        if lang_results:
            # Get the language with the highest probability
            most_probable_lang = lang_results[0].lang
            language_name = LANGUAGES.get(most_probable_lang, 'Unknown')
        else:
            language_name = 'Unknown'
    except:
        language_name = 'Unknown'
    return language_name

# Function to translate text
def translate_text(text, target_language):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None

    if request.method == 'POST':
        text_to_translate = request.form['text']
        target_language = request.form['target_language']

        # Detect language
        source_language = detect_language_full_name(text_to_translate)

        # Translate text
        result = translate_text(text_to_translate, target_language)

        return render_template('index.html', result=result, detected_language=source_language,
                               text_to_translate=text_to_translate, target_language=target_language,
                               languages=LANGUAGES)

    return render_template('index.html', result=result, languages=LANGUAGES)

if __name__ == '__main__':
    app.run(debug=True)
