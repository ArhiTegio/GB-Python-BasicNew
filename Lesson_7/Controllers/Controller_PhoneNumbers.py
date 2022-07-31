from Models.model import Model
from Entities.TypeSaveFile import TypeSaveFile
from typing import List,Dict


class Controller_PhoneNumbers():
    def __init__(self, path:str, columns:List[str], path_forms:Dict, type_save:TypeSaveFile = TypeSaveFile.CSV_point_comma):
        self.model = Model(path, columns, type_save)
        self.path_forms = path_forms

    def UpdateIndexForm(self, name_form:str, name_table:str):
        header = "<!DOCTYPE html>\n" + \
"<html>\n"+ \
"  <head>\n"+ \
'    <meta charset="utf-8">\n'+ \
f'    <title>{name_form}</title>\n'+ \
'  </head>\n'+ \
"  <body>"
        footer = "  </body>\n" + \
"</html>"

        inpt = '\n'.join([f'<input type="text" name="val_{idx}" value=""/>' for idx, e in enumerate(self.model.columns)])
        panel = '<form method="post" action="/add">' + \
inpt + \
'    <input type="submit">'+\
'</form>'

        with open(self.path_forms[name_form], "w") as file:
            file.write(
                header + \
                self.create_table(self.model.data, self.model.columns, name_table) + \
                footer + \
                panel
            )


    def create_table(self, data:List[List[str]], columns:List[str], name_table:str):
        name_table = f'<caption>{name_table}</caption>'
        headings_table = '<tr>\n<td>№</td>' + ''.join(['<th>'+h+'</th>' for h in columns]) + '\n</tr>'
        body_table = ''.join([f'<tr>\n<td>{idx}.</td>' + ''.join(['<td>'+val+'</td>' for val in e]) + f'<td>{self.create_table_delete(idx)}</td>' + '\n</tr>' for idx, e in enumerate(data)])
        return f'<table>{name_table}{headings_table}{body_table}</table>'


    def create_table_delete(self, idx):
        return '<form method="post" action="/delete">'+ \
         f'<input type="submit" name="idx" value="{idx}">'+\
      '</form>'