import csv
import os
import pandas as pd
from pathlib import Path


csv_path = Path(os.path.abspath(os.path.dirname(__file__))).parent.parent.resolve() / "input" /  "question-1" / "main.csv"

with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csv_reader)
    row_data = []
    for row in csv_reader:
        int_row = []
        for val in row:
            int_row.append(int(val))
        row_data.append(int_row[:])
    header_index_map = {
    }
    cur_index = 0
    for col in csv_header:
        header_index_map[col] = cur_index
        cur_index += 1
    res = {}
    lc = 0
    last_index = len(row_data)
    for (index,row) in enumerate(row_data):
        year =  int(row[0])
        if year % 10 == 0:
            res[year] = row
        else:
            decade_year = year - (year % 10)
            if year%10 == 9 or index == last_index - 1:
                res[decade_year][1] = row[1]
            for col in csv_header:
                if col != 'Year' and col != 'Population':
                    col_index = header_index_map[col]
                    res[decade_year][col_index] += row[col_index]
    res_2d_array = []
    for (k,v) in res.items():
        res_2d_array.append(v)
    df = pd.DataFrame(res_2d_array)
    df.to_csv("solution-1.csv", header=csv_header, index=False)
