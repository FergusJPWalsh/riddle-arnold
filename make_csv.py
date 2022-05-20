# converts the TSV file to a CSV file to be used for the GitHub page.
import csv
from collections import defaultdict
from pathlib import Path

INF = Path("data/riddle-arnold_for_web.csv")


def safe(s):
    return s.replace("constructor", "usedtobeaconstructor")


with INF.open(encoding="utf-8") as f:
    reader = csv.reader(f)
    data = defaultdict(lambda: [])
    for row in reader:
        data[safe(row[0])].append(safe(row[1]))

INF.rename(INF.with_stem(INF.stem + "_original"))

with INF.open("w", encoding="utf-8", newline="\n") as f:
    for k, vs in data.items():
        f.write(f'"{k}","')
        f.write("\n".join(vs))
        f.write('"\r\n')
# import io
# import csv
# new_data = []
# with open("riddle-arnold.tsv", "r", encoding="utf-8") as f:
    # reader = csv.reader(f, delimiter = "\t")
    # for row in reader:
        # row[0] = row[0].lower()
        # new_row = f'"{row[0]}","<div style=""margin-left:1em"">{row[1]}</div>"'
        # new_data.append(new_row)
# g = io.open("data/riddle-arnold_for_web.csv", "w", encoding="utf-8", newline="\n")
# for row in new_data:
    # g.write(row+"\r\n")
