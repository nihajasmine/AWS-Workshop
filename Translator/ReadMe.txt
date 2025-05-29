<<<<<<<<<<<<<<<<----------------A basic Python Application ---------------->>>>>>>>>>>>>>>

1.	create new folder "workshop".
2.	open folder in VSCode.
3.	Open terminal in vscode.
4.	>python -m venv venv
5.	Create new file "text-translator.py"
6.	Write the below code:
--------------------------------
#pip install deep-translator
from deep_translator import GoogleTranslator

def translate_text_deep():
    print("Language Translation Program (Deep Translator)")
    
    text = input("Enter the text you want to translate: ")
    source_lang = input("Enter source language code (e.g., 'en' for English, 'auto' for auto-detect): ")
    target_lang = input("Enter target language code (e.g., 'es' for Spanish): ")
    
    try:
        if source_lang.lower() == 'auto':
            translator = GoogleTranslator(source='auto', target=target_lang)
        else:
            translator = GoogleTranslator(source=source_lang, target=target_lang)
            
        translated_text = translator.translate(text)
        
        print("\nTranslation Results:")
        print(f"Original text: {text}")
        print(f"Translated text: {translated_text}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main_deep():
    while True:
        translate_text_deep()
        again = input("\nWould you like to translate another text? (yes/no): ").lower()
        if again != 'yes':
            print("Thank you for using the translator!")
            break

if __name__ == "__main__":
    main_deep()
--------------------------

7. Run these commands
>pip install deep-translator
>python .\text-translator.py

Code link: codefile.io/f/mAn78THU80

-------------------------------------------------------------------------------------------------





<<<<<<<<<<<<<<<<<<<---------------------With FLask API, Postman as FrontEnd -------------------------->>>>>>>>>>

1. Create a file in the "workshop" folder.
2. Create a new file called "translator.py" in the "workshop" folder.
3. write the below code in the translator.py:
---------------------------
from flask import Flask, request, jsonify
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

if __name__=="__main__":
    app.run(debug=True)  ##debug=True is used for development purpose

---------------------------------------------

4. Save the file and enter in venv environment
> .\venv\Scripts\activate
>python .\translator.py

5. copy the url
6. go to post man
7. method=post, url= url/translator,
body-->raw-->json
send the below json object
----------------------
{
    "text" :"hello",
    "source_lang":"en",
    "target_lang":"es"
}
----------------------
8. and click send the output will be shown as:
---------------------
{
    "original_text": "hello",
    "translated_text": "Hola"
}
----------------------


<<<<<<<<<<<<<<<<<<<-----------============== WIth Front End Python Application   ==========----->>>>>>>>>>>>>>>>>>>>

1. create two folders under "workshop" folder, one named templates, one named static
2. create a file under "templates" folder named "index.html"
3. create a file under "static" folder named "style.css"

Link for index.html: https://codefile.io/f/x93mo6iQ0t
-----------------------------------------------------------------------------
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Language Translator</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <div class="container">
        <h1>Language Translator</h1>
        
        <div class="input-section">
            <textarea id="inputText" placeholder="Enter text to translate" rows="4"></textarea>
            
            <div class="language-selection">
                <div class="lang-input">
                    <label for="sourceLang">Source Language:</label>
                    <input type="text" id="sourceLang" value="auto" placeholder="e.g., 'en' or 'auto'">
                </div>
                
                <div class="lang-input">
                    <label for="targetLang">Target Language:</label>
                    <input type="text" id="targetLang" placeholder="e.g., 'es'">
                </div>
            </div>
            
            <button onclick="translateText()">Translate</button>
        </div>

        <div class="result-section">
            <h3>Results:</h3>
            <div class="result-box">
                <p><strong>Original:</strong> <span id="originalResult"></span></p>
                <p><strong>Translated:</strong> <span id="translatedResult"></span></p>
            </div>
            <p id="error" class="error"></p>
        </div>
    </div>

    <script>
        async function translateText() {
            const text = document.getElementById('inputText').value;
            const sourceLang = document.getElementById('sourceLang').value;
            const targetLang = document.getElementById('targetLang').value;
            const errorElement = document.getElementById('error');
            const originalResult = document.getElementById('originalResult');
            const translatedResult = document.getElementById('translatedResult');

            // Clear previous results
            errorElement.textContent = '';
            originalResult.textContent = '';
            translatedResult.textContent = '';

            if (!text || !targetLang) {
                errorElement.textContent = 'Please fill in text and target language';
                return;
            }

            try {
                const response = await fetch('/translate', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        text: text,
                        source_lang: sourceLang,
                        target_lang: targetLang
                    })
                });

                const data = await response.json();

                if (data) {
                    originalResult.textContent = data.original_text;
                    translatedResult.textContent = data.translated_text;
                } else {
                    errorElement.textContent = data.error;
                }
            } catch (error) {
                errorElement.textContent = 'An error occurred while translating';
                console.error('Translation error:', error);
            }
        }
    </script>
</body>
</html>
------------------------------------------------------------------------------------

Link for style.css: https://codefile.io/f/T7B8jtsULA
-------------------------------------------------------------------------------------
body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
    margin: 0;
    padding: 20px;
}

.container {
    max-width: 800px;
    margin: 0 auto;
    background-color: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

h1 {
    color: #333;
    text-align: center;
}

.input-section {
    margin: 20px 0;
}

textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 15px;
    border: 1px solid #ddd;
    border-radius: 4px;
    box-sizing: border-box;
}

.language-selection {
    display: flex;
    gap: 20px;
    margin-bottom: 15px;
}

.lang-input {
    flex: 1;
}

input[type="text"] {
    width: 100%;
    padding: 8px;
    border: 1px solid #ddd;
    border-radius: 4px;
    box-sizing: border-box;
}

button {
    width: 100%;
    padding: 10px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
}

button:hover {
    background-color: #45a049;
}

.result-section {
    margin-top: 20px;
}

.result-box {
    background-color: #f9f9f9;
    padding: 15px;
    border-radius: 4px;
    border: 1px solid #ddd;
}

.error {
    color: #d32f2f;
    margin-top: 10px;
}

-----------------------------------------------------------------------------

4.Update the code inside "translator.py" to :
-------------------------------------------------------------------------------------
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
    app.run(debug=True)  ##debug=True is used for development purpose
--------------------------------------------------------------------------------------

5.
> .\venv\Scripts\activate
> python ./translator.py

Open http://127.0.0.1:5000 in the web browser.

-------------------------------------------------------------------------------------------------------------------------

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<================================= deployment =============================>>>>>>>>>

Steps:
1. Go to https://aws.amazon.com/console/

2. SIgn in to account.

3. search for ec2., set region to mumbai.

4. on ec2->dashboard-->launch instance button.

5. name it, select ubuntu as os, select key pair, select ssh, http,https.
    TO create key pair:
    name key pair, select ppk file. and create

6. click on launch instance.

7. go to ec2->dashboard, check for running instances

8. select the instance-> select details, copy the public ip of the instance.

9. open winscp->create new ->
    options---> ssh, hostname: ip address copied, username: ubuntu, password: none

10. select advanced-> ssh->authentication->private key file: path to the ppk file.

11. save and login the instance

12. open session in putty (commands->open in putty)

13. execute these commands :
        >ls
        >mkdir foldername
        >cd foldername
        >ls
        >python3 --version
        >python3 -m venv venv
        >sudo apt install python3.12-venv
        >sudo apt update
        >sudo apt install python3.12-venv
        >python3 -m venv venv
        >ls
        >source venv/bin/activate
-------------------------------------install requirements for the application --here---
        >pip install flask
        >pip install deep-translator
        >exit

14. refresh winscp-> open the folder created.

15. make chnage in the line of code under main function for the translator.py:
            app.run(debug=True,host='0.0.0.0')

16. save the file.

17. on the left side window of the winscp->open the folder
    drag and drop the files and folders (---here , translator.py, templates, static)

18. refresh the winscp

19. in ec2, select the instance
    click on security groups->inbound rules->edit inbound rules->add rule
    type: custom TCP
    port range:5000
    search: 0.0.0.0
    click on save rules

20. in winscp open session in putty, execute these commands:
    >cd foldername
    >ls
    >source venv/bin/activate
    >python3 translator.py


<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<====================>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Basic lines for Flask Application:
from flask import Flask
app=Flask(__name__)
if __name__=="__main__":
    app.run(debug=True)