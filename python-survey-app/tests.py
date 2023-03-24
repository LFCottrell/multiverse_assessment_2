from csvhelper import *

ticket_1 = read_csv('results.csv')

ticket_2 = remove_duplicates(ticket_1)

ticket_3 = ignore_empty_lines(ticket_2)

ticket_4 = capitalize_lines(ticket_3)

ticket_5 = validate_response(ticket_4)

ticket_6 = new_csv('clean_results.csv', ticket_5)


# testing if the output of the csv reader function is a list

def test_if_list():
    #arrange
    expected_output = list
    
    #act
    output = ticket_1

    #assert
    assert type(output) == expected_output


# testing if the first duplicate has been removed properly

# def test_if_unique():
#     #arrange
#     expected_output = ['7','Bryar','cooley','yes','a','11']

#     #act
#     output = ticket_2[8]

#     #assert
#     assert output == expected_output

# test to see whether there are any blank lines still in output

def test_if_lines_empty():
    #arrange
    expected_output = 0
    empty_line = ['', '', '', '', '']

    #act
    number_of_empty_lines=0
    for line in ticket_3:
        if line == ['', '', '', '', '']:
            number_of_empty_lines+=1
    output = number_of_empty_lines

    #assert
    assert output == expected_output

# test whether lines are all starting with capitals

def test_check_capitalization():
    #arrange
    csv_list = ticket_4
    #expecting all rows except for header to include the capitalization
    expected_output = len(csv_list)-1

    #act
    number_of_capitalized_lines=0
    for line in csv_list:
        if ((line[1][0].isupper()) & (line[2][0].isupper())):
            number_of_capitalized_lines+=1
    
    #assert
    assert expected_output==number_of_capitalized_lines

# test whether responses to answer 3 have been validated 

def test_validation():
    #arrange
    csv_list=ticket_5
    expected_output = 0

    #act
    number_of_lines_more_than_10=0
    for line in csv_list:
        if ((int(line[-1])>10) | (int(line[-1])<1)):
            number_of_lines_more_than_10+=1
    
    #assert
    assert expected_output==number_of_lines_more_than_10

# test whether new csv file has been created properly

# def test_new_csv():
#     #arrange
#     expected_output = True

#     #act 
#     if new_csv():
#         rows = []
#         with open('clean_results', 'r') as f:
#             reader = csv.reader(f, delimiter=',')
#             for row in reader:
#                 rows.append(row)
#         return rows
    
#     #assert
#     assert 
