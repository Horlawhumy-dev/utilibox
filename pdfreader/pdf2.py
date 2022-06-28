import os

# getting file path
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(THIS_FOLDER, 'data.txt')


def read_pdf():
    """
        This reads  the .txt file and extract data
    """
    raw_list = []
    with open(file, encoding='utf-8') as my_file:
        lines = my_file.readlines()

        for line in lines:
            stripped_line = line.strip('\n')
            raw_list.append(stripped_line)
    return raw_list



def strip_line():
    """
       This checks through all data from read_pdf() above and replace any
       record without sex.
    """
    raw_list = read_pdf()
    grand_list = []
    for x in range(len(raw_list)):
        #checking first 5 character in every line under applicant registration number
        if raw_list[x][0:5] == 'NNR33':
            temp_list = []
            temp_list.append(raw_list[x-2]) #append id
            temp_list.append(raw_list[x]) #append registration number
            temp_list.append(raw_list[x+2]) #append name
            temp_list.append(raw_list[x+4]) #append state
            temp_list.append(raw_list[x+6]) #append categories
            temp_list.append(raw_list[x+8]) #append sex

            if temp_list[5].isnumeric():
                temp_list[4] = 'Not found' #replacing no sex data
            
            grand_list.append(temp_list)
    return grand_list


def get_applicants_data():
    data = strip_line()
    data_list = []
    for i in range(len(data)):
        data_dict = {
            "reg_num": "",
            "name": "",
            "state": "",
            "categories": "",
            "sex": ""
        }
        data_dict["reg_num"] = data[i][1]
        data_dict["name"] = data[i][2]
        data_dict["state"] = data[i][3]
        data_dict["categories"] = data[i][4]
        data_dict["sex"] = data[i][5]

        data_list.append(data_dict)

    return data_list



