
class DataTimest:
    def __init__(self, **kwargs):
        self.week_days = {
            0: {"name":"Понедельник", "is_weekend":False },
            1: {"name":"Вторник", "is_weekend":False },
            2: {"name":"Среда", "is_weekend":False },
            3: {"name":"Четверг", "is_weekend":False },
            4: {"name":"Пятница", "is_weekend":False },
            5: {"name":"Суббота", "is_weekend":True },
            6: {"name":"Воскресение", "is_weekend":True },
        }
        self.key_max = max(self.week_days.keys())
        self.key_min = min(self.week_days.keys())

    def __len__(self):
        return self.week_days

    def __getitem__(self, idx:int):
        if idx < self.key_min:
            idx = self.key_min
        if idx > self.key_max:
            idx = self.key_max
        if idx not in self.week_days.keys():
            idx = self.key_min
        return self.week_days[idx]