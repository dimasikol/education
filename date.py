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
