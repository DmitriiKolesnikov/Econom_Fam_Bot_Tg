import gspread

gc = gspread.service_account(filename='google_sheet_1.json')

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

gc2 = gspread.service_account(filename='google_sheet_2.json')
sh2 = gc2.open("DASMSU")
das_worksheet = sh2.sheet1
das_worksheet.update_cell(1, 1, 'id стдуента')
das_worksheet.update_cell(1, 2, 'Ник в Телеграме')
das_worksheet.update_cell(1, 3, 'Отметка времени')
das_worksheet.update_cell(1, 4, 'Электронная почта')
das_worksheet.update_cell(1, 5, 'Номер телефона')
das_worksheet.update_cell(1, 6, 'Имя')
das_worksheet.update_cell(1, 7, 'Фамилия')
das_worksheet.update_cell(1, 8, 'Отчество(при наличии), если нет отчества, то прочерк')
das_worksheet.update_cell(1, 9, 'Бюджет/договор')
das_worksheet.update_cell(1, 10, 'Бакалавр или магистр набора 2024 года?')
das_worksheet.update_cell(1, 11, 'Выход из академического отпуска да / нет')
das_worksheet.update_cell(1, 12, 'Ссылка на ВК или ТГ')
das_worksheet.update_cell(1, 13, 'Пол')
das_worksheet.update_cell(1, 14, 'Гражданство')
das_worksheet.update_cell(1, 15, 'Есть ли основания для включения в БНДС(базу нуждающихся студентов)')
das_worksheet.update_cell(1, 16, 'Для граждан России: регион( область, край или республика) и населенный пункт')
das_worksheet.update_cell(1, 17, 'Дата посещения Отдела расселения')
das_worksheet.update_cell(1, 18, 'Время посещения Отдела расселения')
das_worksheet.update_cell(1, 19., 'Отказ')
