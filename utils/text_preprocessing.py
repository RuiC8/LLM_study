import spacy
import string
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords


spacy_nlp = spacy.load('en_core_web_sm')

#create list of punctuations and stopwords
punctuations = string.punctuation
stop_words = spacy.lang.en.stop_words.STOP_WORDS

#function for data cleaning and processing

#This can be further enhanced by adding / removing reg-exps as desired.
def preprocess_text(sentence):

    sentence = sentence.lower()

    # Remove punctuation
    sentence = re.sub(f'[{re.escape(string.punctuation)}]', '', sentence)
    sentence = re.sub(r'\d+', '', sentence)

    #remove distracting single quotes
    sentence = re.sub('\'','',sentence)
    #remove digits adnd words containing digits
    sentence = re.sub('\w*\d\w*','',sentence)
    #replace extra spaces with single space
    sentence = re.sub(' +',' ',sentence)

    #remove unwanted lines starting from special charcters
    sentence = re.sub(r'\n: \'\'.*','',sentence)
    sentence = re.sub(r'\n!.*','',sentence)
    sentence = re.sub(r'^:\'\'.*','',sentence)

    #remove non-breaking new line characters
    sentence = re.sub(r'\n',' ',sentence)
    #remove punctunations
    sentence = re.sub(r'[^\w\s]',' ',sentence)

    #creating token object
    tokens = nltk.word_tokenize(sentence)
    # Remove stop words
    stop_words = set(stopwords.words('english'))

    tokens = [word for word in tokens if word not in stop_words]

    # Lemmatize the words
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    
    # Join tokens back to a single string
    processed_text = ' '.join(tokens)

    return processed_text
