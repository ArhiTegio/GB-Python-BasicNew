from Lesson_8.Entities.State import State
import datetime as dt

class Database():
    @classmethod
    def GetNewRowDatabase(cls):
        '''
        Test-test-test
        '''
        return {
            '0.log': '',
            '1.title': '',
            '2.description': '',
            '3.state': 'New',
            '4.priority': '',
            '5.date_create': dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            '6.tags': [],
            '7.date_deadline': dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            '8.date_start': dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            '9.hours_work': str(0.0)
        }
