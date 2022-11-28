# generate XML file from TSV file.
import io
import csv
import re
import string
from collections import defaultdict
from lingua import Language, LanguageDetectorBuilder

languages = [Language.ENGLISH, Language.LATIN, Language.GREEK]
detector = LanguageDetectorBuilder.from_languages(*languages).build()

def format_latin(string):
    delimiters = "( \|\| )|(\. )|(, )|(: )|(; )|( \()|(\?)|(\!)|( or )|( = )|( and )|( \[)|(\] )|(☞)|(† )|( - )|(,” )"
    tokens = re.split(delimiters, string)
    tokens = list(filter(None, tokens))
    formatted = []
    for token in tokens:
        lang = detector.detect_language_of(token)
        if lang == None:
            formatted.append(token)
        elif lang.name == "LATIN":
            token = f'<foreign xml:lang="lat">{token}</foreign>'
            formatted.append(token)
        elif lang.name == "GREEK":
            token = f'<foreign xml:lang="grc">{token}</foreign>'
            formatted.append(token)
        else:
            formatted.append(token)
    formatted = "".join(formatted)
    italic_orig = re.escape(")</foreign>")
    italic_sub = "</foreign>)"
    eg_orig = re.escape('<foreign xml:lang="lat">e.g.</foreign>')
    eg_sub = "e.g."
    num_orig = "(\(\d\))"
    num_sub = "\g<1>"
    cic_orig = re.escape('<foreign xml:lang="lat">Cic.</foreign>')
    cic_sub = "Cic."
    caes_orig = re.escape('<foreign xml:lang="lat">Caes.</foreign>')
    caes_sub = "Caes."
    s_orig = re.escape('<foreign xml:lang="lat">s</foreign>.')
    s_sub = "s."
    v_orig = re.escape('<foreign xml:lang="lat">v</foreign>.')
    v_sub = "v."
    formatted = re.sub(italic_orig, italic_sub, formatted)
    formatted = re.sub(eg_orig, eg_sub, formatted)
    formatted = re.sub(num_orig, num_sub, formatted)
    formatted = re.sub(cic_orig, cic_sub, formatted)
    formatted = re.sub(caes_orig, caes_sub, formatted)
    formatted = re.sub(s_orig, s_sub, formatted)
    formatted = re.sub(v_orig, v_sub, formatted)
    return formatted

def format_headword(string):
    headword = f'<head lang="eng" orth_orig="{string}">{string.lower()}</head>'
    return headword

with open("riddle-arnold.tsv", "r", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter = "\t")
    data = defaultdict(lambda: []) #https://realpython.com/python-defaultdict/
    for row in reader:
        data[row[0]].append(format_latin(row[1]))
        print(row[0])

# with open("riddle-arnold-proper-names.tsv", "r", encoding="utf-8") as h:
    # reader = csv.reader(h, delimiter = "\t")
    # for row in reader:
        # data[row[0]].append(row[1])
        # print(row[0])

data = sorted(data.items())
data = dict(data)

with open("riddle-arnold2.xml", "w", encoding="utf-8", newline="\n") as g:
    g.write("<body>")
    for k, v in data.items():
        g.write("\n<entry>")
        g.write(f"{format_headword(k)}<sense>")
        g.write("</sense>sense>".join(v))
        g.write("</sense></entry>")
    g.write("</body>")

print("Finished!\a")
# with open("author_names.txt", "r", encoding="utf-8") as f:
        # authors = f.readlines()
        
    # with open("author_names.txt", "r", encoding="utf-8") as f:
        # authors = f.readlines()
        # authors = " ".join(authors)
    # for token in tokens:
        # lang = detector.detect_language_of(token)
        # token_for_author = token.translate(None, string.punctuation)
        # if re.search(token_for_author, authors):
            # token = f"<author>{token}</author>"
        # el
        
        #</sense><sense>