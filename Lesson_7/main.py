from fastapi import FastAPI, Request, Form, templating
from fastapi.responses import FileResponse
from Controllers.Controller_PhoneNumbers import Controller_PhoneNumbers
from Entities.TypeSaveFile import TypeSaveFile
from Logs.logger_phone import LoggerPhone

import uvicorn

app = FastAPI()
logger = LoggerPhone('Logs/logger')
control = Controller_PhoneNumbers('Data/phones.csv',
                                  ['Телефон', 'ФИО', 'Описание'],
                                  {'Основное меню': 'Views/index.html'},
                                  TypeSaveFile.CSV_point_comma)


@app.get("/")
async def root():
    #return {"message": "Hello World"}
    logger.write('Пользователь зашел на сайт')
    control.UpdateIndexForm("Основное меню","Телефонный справочник")
    return FileResponse('Views/index.html')

@app.post('/add')
def form_post(request: Request, val_0: str = Form(...), val_1: str = Form(...), val_2: str = Form(...)):
    logger.write('Пользователь добавил запись')
    control.model.data.append([val_0, val_1, val_2])
    control.model.save_data()
    control.UpdateIndexForm("Основное меню","Телефонный справочник")
    return FileResponse('Views/index.html')

@app.post('/delete')
def form_delete(request: Request, idx: int = Form(...)):
    logger.write('Пользователь удалил запись')
    control.model.data.pop(idx)
    control.model.save_data()
    control.UpdateIndexForm("Основное меню","Телефонный справочник")
    return FileResponse('Views/index.html')

if __name__ == '__main__':
    app.debug = True
    uvicorn.run(app, host='0.0.0.0', port=1024)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
