import re


def clean_text(text: str) -> str:
    contractions = {
        "I'm": "I am",
        "you're": "you are",
        "he's": "he is",
        "she's": "she is",
        "it's": "it is",
        "we're": "we are",
        "they're": "they are",
        "I've": "I have",
        "you've": "you have",
        "we've": "we have",
        "they've": "they have",
        "isn't": "is not",
        "aren't": "are not",
        "wasn't": "was not",
        "weren't": "were not",
        "won't": "will not",
        "wouldn't": "would not",
        "don't": "do not",
        "doesn't": "does not",
        "didn't": "did not",
        "can't": "cannot",
        "couldn't": "could not",
        "shouldn't": "should not",
        "mightn't": "might not",
        "mustn't": "must not"
    }
    text = text.lower()
    for contraction, full_form in contractions.items():
        text = text.replace(contraction.lower(), full_form.lower())
    text = re.sub(r'[^a-zA-Záéíóúüñ\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text
