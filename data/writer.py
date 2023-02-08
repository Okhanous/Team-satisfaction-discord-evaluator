import xlsxwriter


# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook('satisfaction.xlsx')
worksheet = workbook.add_worksheet()

worksheet.set_column('A:A', 20)

bold = workbook.add_format({'bold': True})

# Ajout de l'image liée à la motivation.
worksheet.write('A1', 'motivation: ')
worksheet.insert_image('A2', 'motivation/motivation.png',{'x_scale': 0.4, 'y_scale': 0.4})


# Ajout de l'image liée à la charge de travaill .
worksheet.write('F1', 'charge de travail: ')
worksheet.insert_image('F2', 'charge de travail/charge de travail.png',{'x_scale': 0.4, 'y_scale': 0.4})



# Ajout de l'image liée à la productivite.
worksheet.write('F15', 'productivite: ')
worksheet.insert_image('F16', 'productivite/productivite.png',{'x_scale': 0.4, 'y_scale': 0.4})

# Ajout de l'image liée à l'ambiance.
worksheet.write('A15', 'Ambiance: ')
worksheet.insert_image('A16', 'ambiance/ambiance.png',{'x_scale': 0.4, 'y_scale': 0.4})


workbook.close()