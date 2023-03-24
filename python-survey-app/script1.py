from csvhelper import *

ticket_1 = read_csv('results.csv')

ticket_2 = remove_duplicates(ticket_1)

ticket_3 = ignore_empty_lines(ticket_2)

ticket_4 = capitalize_lines(ticket_3)

ticket_5 = validate_response(ticket_4)

ticket_6 = new_csv('clean_results.csv', ticket_5)

print(ticket_1)