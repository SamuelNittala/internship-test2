import csv
import os
import pandas as pd
from pathlib import Path
from functools import cmp_to_key

def compare(x,y):
    if x[2] == y[2]:
        return y[1] - x[1]
    else:
        return y[2] - x[2]

csv_path = Path(os.path.abspath(os.path.dirname(__file__))).parent.parent.resolve() / "input" /  "question-3" / "main.csv"

with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csv_reader)
    row_data = []
    for row in csv_reader:
        int_row = []
        for val in row:
            try:
                val = int(val)
            except:
                None
            int_row.append(val)
        row_data.append(int_row[:])
    header_index_map = {
    }
    cur_index = 0
    for col in csv_header:
        header_index_map[col] = cur_index
        cur_index += 1
    res = []
    for row in row_data:
        yc = row[header_index_map["Yellow Cards"]]
        rc = row[header_index_map["Red Cards"]]
        team = row[header_index_map["Team"]]
        res.append([team,yc,rc])

    res = sorted(res, key= cmp_to_key(compare))
    res_header = ['Team', 'Yellow Cards', 'Red Cards']

    df = pd.DataFrame(res)
    df.to_csv("solution-3.csv", header=res_header, index=False)

