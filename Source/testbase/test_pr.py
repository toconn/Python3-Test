from .testisfirst import TestIsFirst

'''
    This module provides print methods to help display information while
    testing code.
'''


COLUMN_2_START_POSITION = 24
INDENT_STRING = '    '
TITLE_WIDTH = 80


def pr(item1 = None, item2 = None):

    """
    :type item2: dict, tuple,string, int
    """
    if item1 is not None:
    
        item1 = to_string(item1)
    
        if(isinstance(item2,(list, tuple))):
            pr_list(item1, item2)
            return
        elif(isinstance(item2, dict)):
            pr_dict(item1, item2)
            return
        elif(isinstance(item2, BaseException)):
            pr_except(item1, item2)
            return
        else:
            item2 = to_string(item2)
    
        if not item1 and not item2:
            # both are empty strings:
            print()
        elif not item2:
            print(item1)
        else:
            print(item1 + ' ' *(COLUMN_2_START_POSITION - len(item1)) + ": " + item2)
    else:
        print()

def pr_dict(item1, dict1):

    first = TestIsFirst()

    for key, value in dict1.items():
        if first.is_first():
            pr(item1, key + ' ' + value)
        else:
            pr('', key + ' ' + value)
    return

def pr_dbl(item1 = None, item2 = None):

    pr(item1, item2)
    print()

def pr_dbl_ind(indent_count, item1 = '', item2 = ''):

    pr_ind(indent_count, item1, item2)
    print()

def pr_done():

    print()
    print('Done.')
    print()

def pr_except(item1, exception2):

    pr(item1, type(exception2).__name__)
    pr('', exception2.args)

def pr_ind(indent_count, item1 = None, item2 = None):

    if item1 is not None:
        
        item1 = to_string(item1)
        
        #Indent if not empty:
        if item1:
            item1 = INDENT_STRING * indent_count + item1
        
        pr(item1, item2)
            
    else:
        print()

def pr_list(item1, list1):

    first = TestIsFirst()

    for value in list1:
        if first.is_first():
            pr(item1, value)
        else:
            pr('', value)
    return

def pr_title(item1):

    print()
    print("*" * TITLE_WIDTH)
    print("* " + item1 + ' ' *(TITLE_WIDTH - 4 - len(item1)) + " *")
    print("*" * TITLE_WIDTH)
    print()

def to_string(value):
    
    if value is None:
        value_str = ''
    elif isinstance(value, bool):
        value_str = 'True' if value else 'False'
    elif isinstance(value, (bytes, int, complex, float)):
        value_str = str(value)
    else:
        value_str = value
    
    return value_str
