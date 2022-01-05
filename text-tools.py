import csv
import re
headwords = []
entry_texts = []
bad_entries = []
with open ("riddle-arnold.tsv", "r", encoding="utf-8") as f:
    # lexicon = csv.reader(f, delimiter="\t")
    # for entry in lexicon:
        # headword = entry[0]
        # entry_text = entry[1]
        # headwords.append(headword)
        # entry_texts.append(entry_text)
# for i, headword in enumerate(headwords):
    # if re.search("[^A-Z]", headword):
        # print(i+1, headword)

    lexicon = f.readlines()
    for i, entry in enumerate(lexicon):
        tabs = entry.count("\t")
        if tabs == 0:
            print(i+1)
            bad_entries.append(entry)
        elif tabs > 1:
            print(i+1)
            bad_entries.append(entry)
print("Len bad_entries:",len(bad_entries))
print("bad_entries:\n",bad_entries)

all_text = " ".join(lexicon)
letter_set = set(all_text)
print(sorted(letter_set))