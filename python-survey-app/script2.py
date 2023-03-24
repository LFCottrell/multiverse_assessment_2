# from csvhelper import read_csv
import csv
from script1 import ticket_6

# print(read_csv('clean_results.csv'))
for line in ticket_6:
    print(line)


print(read_csv())

# def read_csv(filename):
#     rows = []
#     with open(filename, 'r') as f:
#         reader = csv.reader(f, delimiter=',')
#         for row in reader:
#             rows.append(row)
#     return rows