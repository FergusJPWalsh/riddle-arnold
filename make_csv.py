# converts the TSV file to a CSV file to be used for the GitHub page.
import io
import csv
import re
from collections import defaultdict
from lingua import Language, LanguageDetectorBuilder

languages = [Language.ENGLISH, Language.LATIN]
detector = LanguageDetectorBuilder.from_languages(*languages).build()

def format_latin(string):
    delimiters = "( \|\| )|(\. )|(, )|(: )|(; )|( \()|(\?)|(\!)|( or )|( = )|( and )|( \[)|(\] )|( is )|(☞)"
    tokens = re.split(delimiters, string)
    tokens = list(filter(None, tokens))
    formatted = []
    for token in tokens:
        lang = detector.detect_language_of(token)
        if lang == None:
            formatted.append(token)
        elif lang.name == "LATIN":
            token = f'<i lang="lt">{token}</i>'
            formatted.append(token)
        else:
            formatted.append(token)
    formatted = "".join(formatted)
    italic_orig = re.escape(")</i>")
    italic_sub = "</i>)"
    eg_orig = re.escape('<i lang="lt">e.g.</i>')
    eg_sub = "e.g."
    num_orig = "(\(\d\))"
    num_sub = "<b>\g<1></b>"
    formatted = re.sub(italic_orig, italic_sub, formatted)
    formatted = re.sub(eg_orig, eg_sub, formatted)
    formatted = re.sub(num_orig, num_sub, formatted)
    return formatted

def format_headword(string):
    return fr"<b>{string}</b>"

with open("riddle-arnold.tsv", "r", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter = "\t")
    data = defaultdict(lambda: [])
    for row in reader:
        data[row[0]].append(format_latin(row[1]))
        print(row[0])

with open("riddle-arnold-proper-names.tsv", "r", encoding="utf-8") as h:
    reader = csv.reader(h, delimiter = "\t")
    for row in reader:
        data[row[0]].append(row[1])
        print(row[0])

data = sorted(data.items())
data = dict(data)
print(type(data))

# Needs to be changed to allow headwords with multiple parts of speech as in old csv file.
# Regex post-factum fix Find: (.)(\n) Replace: $1</div>\n<div style="margin-left:1em">
with open("data/riddle-arnold_for_web.csv", "w", encoding="utf-8", newline="\n") as g:
    for k, v in data.items():
        g.write(f'"{k}","<div style="margin-left:1em">{format_headword(k)} ')
        g.write("\n".join(v))
        g.write('</div>"\r\n')