from Entities.TypeSaveFile import TypeSaveFile
from typing import List
import json


class Model:
    def __init__(self, path:str, columns:List[str], type_save:TypeSaveFile = TypeSaveFile.CSV_point_comma):
        self.type_save = type_save
        self.path = path
        self.data = []
        self.columns = columns

        self.load_data()

    def load_data(self):
        with open(self.path, "r") as file:
            if self.path.split('.')[-1] == 'csv':
                if self.type_save == TypeSaveFile.CSV_point_comma:
                    for line in file:
                        if len(line) > 0 and line != '\n':
                            self.data.append(line.split(';'))
                if self.type_save == TypeSaveFile.CSV_colon:
                    for line in file:
                        if len(line) > 0 and line != '\n':
                            self.data.append(line.split(':'))

            if self.type_save == TypeSaveFile.Json:
                for line in file:
                    self.data.append(json.loads(line))

            if self.type_save == TypeSaveFile.Txt:
                    for line in file:
                        self.data.append(line.split(';'))



    def save_data(self):
        with open(self.path, "w") as file:
            if self.type_save in [TypeSaveFile.CSV_point_comma, TypeSaveFile.CSV_colon]:
                camma = [e[1] for e in [
                    (TypeSaveFile.CSV_point_comma, ';'),
                    (TypeSaveFile.CSV_colon, ':'),
                ] if e[0] == self.type_save][0]
                for d in self.data:
                    if len(d)> 0:
                        file.write(camma.join(d) +'\n')

            if self.type_save == TypeSaveFile.Json:
                for d in self.data:
                    file.write(json.dumps(d))

            if self.type_save == TypeSaveFile.Txt:
                for d in self.data:
                    file.write(';'.join(d))



