import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

analyzer = SentimentIntensityAnalyzer()
lemmatizer = WordNetLemmatizer()

dict = {"pos" : "positive",
        "neg" : "negative",
        "neu" : "neutral",
        "compound" : "compound"}

def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    filtered_tokens = [token for token in tokens if token not in stopwords.words("english")]
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    return " ".join(lemmatized_tokens)

def sentiment_analysis(text):
    scores = analyzer.polarity_scores(preprocess_text(text))
    sorted_keys = sorted(zip(scores.keys(), scores.values()), key = lambda s: scores[s[0]], reverse = True)
    return sorted_keys

def stringify(values):
    for i,j in values:
        if i == "compound":
            continue
        if j > 0.8:
            return ("Mostly " + dict[i])
        elif j > 0.5:
            return ("Slightly " + dict[i])
        else:
            return ("Mixed, but leaning towards " + dict[i])

if __name__ == "__main__":
    print(sentiment_analysis("i hate you"))