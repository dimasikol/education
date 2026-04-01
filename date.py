class Date:
    sep = '/'  # атрибут класса – разделитель по умолчанию

    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        # Приведение двухзначного года к XXI веку
        if 0 <= year < 100:
            year += 2000
        self.year = year

    def __str__(self) -> str:
        """Возвращает дату с текущим разделителем."""
        return f"{str(self.day).rjust(2,'0')}{self.sep}{self.month:02d}{self.sep}{self.year}"
    @staticmethod
    def str2num(string):
        string = string.replace('/','.').replace('-','.')
        return list(map(int,string.split('.')))
    
    @classmethod
    def from_str(cls,string):
        return cls(*Date.str2num(string))

    @staticmethod
    def isleap(year):
        if year%400 == 0:
            return True
        if year%100 == 0:
            return False
        if year% 4 == 0:
            return True
        return False
date = Date.from_str("08.03.25")
print(date)


class Date:
    sep = '/'  # атрибут класса – разделитель по умолчанию
    def __init__(self, day: int, month: int, year: int):
        self.__day = day
        self.__month = month
        if 0 <= year < 100:
            year += 2000
        self.__year = year
        self.__holiday = False

    def __str__(self) -> str:
        """Возвращает дату с текущим разделителем."""
        if self.__holiday:
           return f"{str(self.__day).rjust(2, '0')}{self.sep}{self.__month:02d}{self.sep}{self.__year}" + f"\n{self.__holiday}"
        return f"{str(self.__day).rjust(2, '0')}{self.sep}{self.__month:02d}{self.sep}{self.__year}"

    @staticmethod
    def str2num(string):
        string = string.replace('/', '.').replace('-', '.')
        return list(map(int, string.split('.')))

    @classmethod
    def from_str(cls, string):
        return cls(*Date.str2num(string))

    @staticmethod
    def isleap(year):
        if year % 400 == 0:
            return True
        if year % 100 == 0:
            return False
        if year % 4 == 0:
            return True
        return False

    def to_start(self):
        add = self.isleap(self.year)
        day, mon, year = self.__day, self.__month, self.__year
        date_cal = {0: 0, 1: 31, 2: 59, 3: 90, 4: 120, 5: 151, 6: 181, 7: 212, 8: 243, 9: 273, 10: 304, 11: 334}

        if date_cal[mon - 1] + day - 1 == 0:
            return 0
        if mon > 2:
            return date_cal[mon - 1] + day - 1 + add
        return date_cal[mon - 1] + day - 1

    def to_end(self):
        if self.isleap(self.year):
            return 366 - self.to_start() - 1
        return 365 - self.to_start() - 1

    def get_day(self):
        return self.__day

    def get_month(self):
        return self.__month

    def get_year(self):
        return self.__year

    def set_day(self, day):
        self.__day = day

    def set_month(self, month):
        self.__month = month

    def set_year(self, year):
        if year <= 100:
            year = 2000 + year
        self.__year = year

    @property
    def holiday(self):
        return self.__holiday

    @holiday.setter
    def holiday(self,string):
        self.__holiday = string
class Task:
    tasklist = []
    def __init__(self,start,end,description):
        self.start = Date(*Date.str2num(start))
        self.end = Date(*Date.str2num(end))
        self.description = description
        Task.tasklist.append(self)
    def __str__(self):
        return f'с {self.start} по {self.end}\n{self.description}'
for i in Task.tasklist:
    print(i)
