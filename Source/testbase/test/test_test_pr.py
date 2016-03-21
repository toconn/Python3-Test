from testbase.test_pr import *

pr_title('Testing - test_pr')

pr('Print Item.')
pr_dbl('Print, skip line')

pr('Print Item.', 'with value')
pr('Print Item (int)', 4)
pr('Print Item (bool)', True)
pr('Print Exception', Exception('Test exception.'))
pr_dbl('Print, skip line', 'with value')

pr_ind(1, 'Indented')
pr_ind(2, 'Indented', 'With an item')
pr_dbl_ind(1, 'Indent, skip line', 'with value')

list1 = ['Item 1', 'Item 3', 'Item 2']
dict1 = {'Item 1': 'Value 1', 'Item 3': 'Value 3', 'Item 2': 'Value 2'}

pr_ind(1, "List", list1)
pr()

pr_ind(1, list1)
pr()

pr_ind(1, "Dict", dict1)
pr()

pr_done()
