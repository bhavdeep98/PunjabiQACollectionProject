from googletrans import Translator



def translate_to_punjabi_from_english(text):
    # Create a Translator object
    translator = Translator()

    try:
        # Translate the text from English to Punjabi
        translation = translator.translate(text, src='en', dest='pa')

        # Return the translated text
        return translation.text

    except Exception as e:
        return str(e)



def translate_to_english_from_punjabi(text):
    # Create a Translator object
    translator = Translator()

    try:
        # Translate the text from Punjabi to English
        translation = translator.translate(text, src='pa', dest='en')

        # Return the translated text
        return translation.text

    except Exception as e:
        return str(e)