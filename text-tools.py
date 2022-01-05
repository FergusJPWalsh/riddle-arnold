import csv
import re
headwords = []
entry_texts = []
with open ("riddle-arnold.tsv", "r", encoding="utf-8") as f:
    lexicon = csv.reader(f, delimiter="\t")
    for entry in lexicon:
        headword = entry[0]
        entry_text = entry[1]
        headwords.append(headword)
        entry_texts.append(entry_text)
for i, headword in enumerate(headwords):
    if re.search("[^A-Z]", headword):
        print(i+1, headword)

    # proper_names = f.readlines()
    # for i, entry in enumerate(proper_names):
        # tabs = entry.count("\t")
        # if tabs == 0:
            # print(i+1)
            # bad_entries.append(entry)
        # elif tabs > 1:
            # print(i+1)
            # bad_entries.append(entry)
# print(len(bad_entries))

# all_text = " ".join(proper_names)
# letter_set = set(all_text)
# print(letter_set)