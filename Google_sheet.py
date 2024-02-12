import gspread

gc = gspread.service_account(filename='apointment-with-a-psychologist-79324b1b06cd.json')

sh = gc.open("Appointment")

# начало заполнения таблицы
worksheet = sh.sheet1
worksheet.update_cell(1, 1, 'id стдуента')
worksheet.update_cell(1, 2, 'Имя студента')
worksheet.update_cell(1, 3, 'Номер учебной группы')
worksheet.update_cell(1, 4, 'Дата записи')
worksheet.update_cell(1, 5, 'Электронная почта')
worksheet.update_cell(1, 6, 'Краткое описание проблемы')
worksheet.update_cell(1, 7, 'Дата и время приема')
worksheet.update_cell(1, 8, 'id психолога')
worksheet.update_cell(1, 9, 'Отмена записи')
worksheet.update_cell(1, 10, 'Количество бесплатных посещений из 2')
worksheet.update_cell(1, 11, 'Столбик для рукописных пометок')