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