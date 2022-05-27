# from nltk.tokenize import word_tokenize # sent_tokenize
import re
from lingua import Language, LanguageDetectorBuilder

languages = [Language.ENGLISH, Language.LATIN]
detector = LanguageDetectorBuilder.from_languages(*languages).build()

string = "ABYSS	infinita or immensa altitudo: vorago (abyss; chasm): gurges (whirlpool): barathrum (is a poetical expression): profundum (with or without maris; abyss of the sea). || Figuratively, manifest overwhelming danger; vorago; pestis, pernicies. To plunge into an abyss of danger, ad pestem ante oculos positam proficisci; in praeceps ruere."

delimiters = "( \|\| )|(\. )|(, )|(: )|(; )|( \()|(\?)|(\!)|( or )|( = )"

tokens = re.split(delimiters,string)

new_tokens = []
for token in tokens:
    new_tokens.append(token)

new_tokens = list(filter(None, new_tokens))

entry = []
for token in new_tokens:
    conf = detector.detect_language_of(token)
    if conf == None:
        entry.append(token)
    elif conf.name == "LATIN":
        token = f'<i lang="lt">{token}</i>'
        entry.append(token)
    else:
        entry.append(token)
entry = "".join(entry)
italic_orig = re.escape(")</i>")
italic_sub = "</i>)"
eg_orig = re.escape('<i lang="lt">e.g.</i>')
eg_sub = "e.g."
entry = re.sub(italic_orig, italic_sub, entry)
entry = re.sub(eg_orig, eg_sub, entry)
print(entry)
