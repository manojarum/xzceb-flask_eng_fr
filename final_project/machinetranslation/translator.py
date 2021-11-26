'''
Language Translator
'''
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)

language_translator.set_disable_ssl_verification(True)
languages = language_translator.list_identifiable_languages().get_result()
#print(json.dumps(languages, indent=2))

def englist_to_french(english_text):
    '''
    Converting English to French
    '''
    translation = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    val = json.loads((json.dumps(translation, indent=2, ensure_ascii=False)))
    frenchText = ""
    if val.get("translations"):
        for listval in val.get("translations"):
            frenchText = listval.get("translation")
    return frenchText

def french_to_english(french_text):
    '''
    Converting French to English
    '''
    translation = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    val =json.loads(json.dumps(translation, indent=2, ensure_ascii=False))
    englishText = ""   
    if val.get("translations"):
        for listval in val.get("translations"):
            englishText = listval.get("translation")
    return englishText

englist_to_french("Hello Welcome")
french_to_english("Bonjour Bienvenue")
