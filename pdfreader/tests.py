from .pdf2 import read_pdf, strip_line, get_applicants_data
# Create your tests here.

def test_get_length_pdf_lines():
    """
        Test to calculate length of lines in raw list
    """
    raw_list = read_pdf()
    assert len(raw_list) == 92556



def test_count_no_sex_found():
    """
        Test to count number of applicants with no sex found
    """
    raw_list = read_pdf()
    stripped_data = strip_line()
    count = 0
    for i in range(len(stripped_data)):
        if stripped_data[i][4] == 'Not found':
            count += 1
    assert count == 72


def test_get_length_of_data():
    """
        Test to count number of applicants data
    """
    applicants_data = get_applicants_data()
    
    assert len(applicants_data) == 7354
        
