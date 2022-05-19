# converts the TSV file to a CSV file to be used for the GitHub page.
import csv
new_data = []
with open("riddle-arnold.tsv", "r", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter = "\t")
    for row in reader:
        new_row = f'"{row[0]}","<div style=""margin-left:1em"{row[1]}</div>'
        new_data.append(new_row)
with open("riddle-arnold_for_web.csv", "w", encoding="utf-8") as g:
    for row in new_data:
        g.write(row+"\n")
