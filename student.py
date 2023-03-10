from datetime import date, timedelta

class Student:
    """
    A student class as a base for method testing
    """

    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        self._start_date = date.today()
        self.end_date = date.today() + timedelta(days=365)
        self.naughty_list = False
    
    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"

    def alert_santa(self):
        self.naughty_list = True

    @property
    def email(self):
        return f"{self._first_name}{self._last_name}@email.com"
    
    def apply_extension(self, extension):
        self.end_date += timedelta(days=extension)
