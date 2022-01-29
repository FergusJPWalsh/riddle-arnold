# import csv
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

# check TSV formatting is valid
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

# get longest entries
entry_dict = {}
for entry in lexicon:
    entry_len = len(entry)
    entry_dict[entry_len] = entry

sorted_dict = dict(sorted(entry_dict.items(), key=lambda item: item[1]))

entry_list = list(sorted_dict.items())
entry_list = sorted(entry_list, reverse=True)
for i in range(10):
    printable = entry_list[i][1]
    print(printable[0:50])

# get character set
all_text = " ".join(lexicon)
# letter_set = set(all_text)
# print(sorted(letter_set))

greek = re.findall("[\u0370-\u1fff]+", all_text)
greek_set = sorted(set(greek))

for word in greek_set:
    print(f"{word}\n")