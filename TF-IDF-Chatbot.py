import nltk
import ssl
import string
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Desactivar la verificación SSL
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# Configurar la ruta del directorio para los recursos de NLTK en el directorio del usuario
nltk.data.path.append("/ruta/a/tu/directorio/nltk_data")

# Instalar y descargar los recursos de NLTK
try:
    nltk.download('punkt')
    nltk.download('wordnet')
    nltk.download('omw-1.4')
except Exception as e:
    print(f"Error al descargar los recursos de NLTK: {e}")

# Leyendo el corpus
f = open('Data_Science_Overview.txt', 'r', errors='ignore')
raw_doc = f.read()
raw_doc = raw_doc.lower()  # Convertir texto a minúsculas
nltk.download('punkt')  # Utilizando el tokenizador Punkt
nltk.download('wordnet')  # Utilizando el diccionario WordNet
sent_tokens = nltk.sent_tokenize(raw_doc)  # Convertir el documento en una lista de oraciones
word_tokens = nltk.word_tokenize(raw_doc)

# Preprocesamiento de texto
lemmer = nltk.stem.WordNetLemmatizer()

def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

remove_punc_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punc_dict)))

# Definiendo la función de saludo
GREET_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey",)
GREET_RESPONSES = ["hi", "hey", "nods", "hi there", "hello", "Me alegra! Estás hablando conmigo"]

def greet(sentence):
    for word in sentence.split():
        if word.lower() in GREET_INPUTS:
            return random.choice(GREET_RESPONSES)

# Generación de respuesta
def response(user_response):
    robo1_response = ''
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if req_tfidf == 0:
        robo1_response = "Lo siento, ¡No te entiendo!"
    else:
        robo1_response = sent_tokens[idx]
    return robo1_response

# Definiendo los protocolos de inicio/fin de la conversación
flag = True
print("BOT: Mi nombre es Stark. ¡Tengamos una conversación! Además, si quieres salir en cualquier momento, simplemente escribe Adiós.")

while flag:
    user_response = input()
    user_response = user_response.lower()
    
    if user_response != 'bye':
        if user_response == 'thanks' or user_response == 'thank you':
            flag = False
            print("BOT: De nada...")
        else:
            if greet(user_response) is not None:
                print("BOT: " + greet(user_response))
            else:
                sent_tokens.append(user_response)
                word_tokens = word_tokens + nltk.word_tokenize(user_response)
                final_words = list(set(word_tokens))
                print("BOT:  ", end="")
                print(response(user_response))
                sent_tokens.remove(user_response)
    else:
        flag = False
        print("BOT: ¡Adiós!")