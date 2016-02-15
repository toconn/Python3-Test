from .testisfirst import TestIsFirst


class TestBase:

    COLUMN_2_START_POSITION = 24
    TITLE_WIDTH = 80

    def done (self):

        print ('')
        print ('Done.')
        print ('')

    def pr (self, item1 = '', item2 = ''):

        """
        :type item2: dict, tuple,string, int
        """
        if (isinstance (item1, int)):
            item1 = str (item1)

        if (isinstance (item2, int)):
            item2 = str (item2)
        elif (isinstance (item2, (list, tuple))):
            self.prList(item1, item2)
            return
        elif (isinstance (item2, dict)):
            self.prDict(item1, item2)
            return
        elif (isinstance (item2, BaseException)):
            self.prException(item1, item2)
            return

        if (item1 == '' and item2 == ''):
            print ('')
        elif (item2 == ''):
            print (item1)
        else:
            print (item1 + ' ' * (TestBase.COLUMN_2_START_POSITION - len (item1)) + ": " + item2)

    def prDict (self, item1, dict1):

        first = TestIsFirst()

        for key, value in dict1.items():
            if first.is_first():
                self.pr(item1, key + ' ' + value)
            else:
                self.pr('', key + ' ' + value)
        return

    def prDouble (self, item1 = '', item2 = ''):

        self.pr (item1, item2)
        print('')

    def prException (self, item1, exception2):

        self.pr (item1, type(exception2).__name__)
        self.pr ('', exception2.args)

    def prList (self, item1, list1):

        first = TestIsFirst()

        for value in list1:
            if first.is_first():
                self.pr(item1, value)
            else:
                self.pr('', value)
        return

    def title (self, item1):

        print ('')
        print ("*" * TestBase.TITLE_WIDTH)
        print ("* " + item1 + ' ' * (TestBase.TITLE_WIDTH - 4 - len (item1)) + " *")
        print ("*" * TestBase.TITLE_WIDTH)
        print ('')
