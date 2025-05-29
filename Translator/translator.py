from flask import Flask, request, jsonify, render_template
from deep_translator import GoogleTranslator

app=Flask(__name__)     ##app is a variable, can use another name

##add api
@app.route("/translate",methods=["POST"])

def translate():
    # print("Language Translation Program (Deep Translator)")  -->remove this
    
    ##we need to return the text to display to user
    
    # text = input("Enter the text you want to translate: ") -->replace this
    text=request.json['text']

    # source_lang = input("Enter source language code (e.g., 'en' for English, 'auto' for auto-detect): ")
    source_lang=request.json['source_lang']
    
    # target_lang = input("Enter target language code (e.g., 'es' for Spanish): ")
    target_lang=request.json['target_lang']
    
    
    try:
        if source_lang.lower() == 'auto':
            translator = GoogleTranslator(source='auto', target=target_lang)
        else:
            translator = GoogleTranslator(source=source_lang, target=target_lang)
            
        translated_text = translator.translate(text)
        
        print("\nTranslation Results:")
        print(f"Original text: {text}")
        print(f"Translated text: {translated_text}")
        
        return jsonify({"original_text": text,"translated_text":translated_text}),200
        
    except Exception as e:
        return jsonify({"error": f"Translation failed: {str(e)}"}), 500


## another API, just give "/", just we need to send request
@app.route("/",methods=["GET"])
def index():
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0')  ##debug=True is used for development purpose