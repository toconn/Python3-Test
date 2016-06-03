from .testisfirst import TestIsFirst

'''
    This module provides print methods to help display information while
    testing code.
'''


COLUMN_2_START_POSITION = 24
INDENT_STRING = '    '
TITLE_WIDTH = 80


def pr(item1 = None, item2 = None, indent = ''):

    """
    :type item2: dict, tuple,string, int
    """
    if isinstance(item1, (list, tuple)):
        
        for item in item1:
            item = indent + to_string(item)
            print (item)
        
    elif item1 is not None:
    
        item1 = indent + to_string(item1)
    
        if isinstance(item2,(list, tuple)):
            pr_list(item1, item2)
            return
        
        elif isinstance(item2, dict):
            pr_dict(item1, item2)
            return
                
        elif item2 is not None:
            item2 = to_string(item2)
    
        if item1 is None and item2 is None:
            # both are empty strings:
            print('')
        elif item2 is None:            
            print(item1)
        else:
            print(item1 + ' ' *(COLUMN_2_START_POSITION - len(item1)) + ": " + item2)
    else:

        print('')

def pr_dict(item1, dict1):

    first = TestIsFirst()

    for key, value in dict1.items():
        
        key_str = to_string(key)
        value_str = to_string(value)
        
        if first.is_first():
            pr(item1, key_str + ' = ' + value_str)
        else:
            pr('', key_str + ' = ' + value_str)
    return

def pr_dbl(item1 = None, item2 = None):

    pr(item1, item2)
    print('')

def pr_dbl_ind(indent_count, item1 = '', item2 = ''):

    pr_ind(indent_count, item1, item2)
    print('')

def pr_done():

    print('')
    pr_section ('Done.')
    print('')

def pr_ind(indent_count, item1 = None, item2 = None):
    
    indent = INDENT_STRING * indent_count
    pr (item1, item2, indent)

def pr_list(item1, list1):

    first = TestIsFirst()

    for value in list1:
        if first.is_first():
            pr(item1, value)
        else:
            pr('', value)
    return

def pr_section(title):
    
    pr()
    print("* " + title + ' ' + '*' * (TITLE_WIDTH - 3 - len(title)))
    pr()

def pr_title(title):

    print('')
    print("*" * TITLE_WIDTH)
    print("* " + title + ' ' *(TITLE_WIDTH - 4 - len(title)) + " *")
    print("*" * TITLE_WIDTH)
    print('')

def to_string(value):
    
    if value is None:
        value_str = ''
    elif isinstance(value, bool):
        value_str = 'True' if value else 'False'
    elif isinstance(value, (bytes, int, complex, float)):
        value_str = str(value)
    elif isinstance(value, BaseException):
        if value.args:
            value_str = 'Exception: ' + type(value).__name__ + ': ' + value.args[0]
        else:
            value_str = 'Exception: ' + type(value).__name__
    elif type(value).__str__ is not object.__str__:
        value_str = value.__str__()
    else:
        value_str = value
    
    return value_str
