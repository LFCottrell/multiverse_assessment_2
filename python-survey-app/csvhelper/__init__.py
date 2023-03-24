import csv

#function to read in a csv 
def read_csv(filename):
    rows = []
    with open(filename, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            rows.append(row)
    return rows

#function to remove duplicates from csv
def remove_duplicates(input_list):
    survey_list = input_list
    empty_list_1 = []
    empty_list_2 = []
    for i in survey_list:
        if i[0] not in empty_list_2:
            empty_list_2.append(i[0])
            empty_list_1.append(i)
    return empty_list_1


#function to ignore empty lines
def ignore_empty_lines(input_list):
    survey_list = input_list
    empty_list_1 = []
    for i in survey_list:
        if ((len(i[0]) > 0)):
            empty_list_1.append(i)
    return empty_list_1

#function to capitalize name columns in list
def capitalize_lines(input_list):
    survey_list = input_list
    for i in survey_list[1:]:
        i[1] = i[1].capitalize()
        i[2] = i[2].capitalize()
    return survey_list

#function to validate results for given column are between 1 and 10
def validate_response(input_list):
    survey_list = input_list
    empty_list_1 = []
    for i, j in enumerate(survey_list[1:]):
        print(i,j)
        if (int(j[-1]) > 10):         
            continue
        elif (int(j[-1]) < 1):
            continue
        else:
            empty_list_1.append(j)
        

    return empty_list_1

# function to output a list to a new csv file entitled 'clean results'. 
def new_csv(output_file, input_list):
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(['user_id','first_name','last_name','answer_1','answer_2','answer_3'])
        for i in input_list:
            writer.writerow(i)