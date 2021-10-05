import csv
import os
import pandas as pd
from pathlib import Path


csv_path = Path(os.path.abspath(os.path.dirname(__file__))).parent.parent.resolve() / "input" /  "question-2" / "main.csv"

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
    occupation_map = {}
    for row in row_data:
        for col in csv_header:
            if col == 'occupation':
                occupation_type = row[header_index_map['occupation']]
                age =  row[header_index_map['age']]
                try:
                    occupation_map[occupation_type][0] = min(occupation_map[occupation_type][0],age)
                    occupation_map[occupation_type][1] = max(occupation_map[occupation_type][1],age)
                except:
                    occupation_map[occupation_type] = [age,age]
    res_header = ['occupation', 'min', 'max']
    res_2d_array = []
    for (k,v) in occupation_map.items():
        arr = [k,v[0],v[1]]
        res_2d_array.append(arr)
    res_2d_array = sorted(res_2d_array)
    df = pd.DataFrame(res_2d_array)
    df.to_csv("solution-2.csv", header=res_header, index=False)
