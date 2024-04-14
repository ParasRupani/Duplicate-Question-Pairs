# Import necessary modules for text preprocessing
from nltk.tokenize import word_tokenize  # Tokenization
from nltk.corpus import stopwords  # Stop word removal
import string  # String-related operations
from nltk import pos_tag  # Part-of-speech tagging
from nltk.corpus import wordnet  # Lemmatization
from nltk.stem import WordNetLemmatizer  # Lemmatization
import re  # Regular expressions
import emoji  # Handling emojis
import nltk
nltk.download('punkt')
nltk.download('stopwords')

def preprocess(data):

    """
    Preprocesses text data by performing tokenization, lowercasing, stopword removal,
    part-of-speech tagging, lemmatization, hashtag removal, emoji removal, special character removal, 
    and extra whitespace removal.
    
    Args:
    - data: Input text data to be preprocessed
    
    Returns:
    - cleaned_text: Preprocessed text data
    """
    
    #1. Tokenization:
    tokenize = word_tokenize(data)

    #2. Lowercasing:
    chars = set(string.punctuation)
    norm_token = [token for token in tokenize if token.lower() not in chars]
    
    #3. Stopwords Removal:
    stop_words = set(stopwords.words('english'))
    new_token = [token for token in norm_token if token.lower() not in stop_words]

    #4. Consider POS tagging 
    pos_tagging = pos_tag(new_token)

    #5. Lemmatization:
    lemmatizor = WordNetLemmatizer()
    token_list = []

    for word, tag in pos_tagging:
        if tag.startswith('N'): #NN,NNS,NNP,NNPS tags
            pos_word = wordnet.NOUN
        elif tag.startswith('V'): #VB, VBD, VBG, VBN, VBP tags
            pos_word = wordnet.VERB
        elif tag.startswith('J'): #JJ, JJR, JJS tags
            pos_word = wordnet.ADJ
        elif tag.startswith('R'): # RB, RBR, RBS tags
            pos_word = wordnet.ADV
        else:
            pos_word = wordnet.NOUN

        lemmatization = lemmatizor.lemmatize(word, pos_word)
        token_list.append(lemmatization)

    
    #6. Remove hashtags:
    text = ' '.join(token_list)
    text_without_hashtags = re.sub(r'\s?#\w+\b', '', text)

    #7. Emoji removal:
    text_without_emojis = emoji.replace_emoji(text_without_hashtags, replace='')
    cleaned_text = re.sub(r'\s+', ' ', text_without_emojis).strip()
    
    # 8. Remove special characters:
    cleaned_text = re.sub(r'[^\w\s]', '', text_without_emojis)
    
    # 9. Remove extra whitespaces:
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()

    return cleaned_text
    