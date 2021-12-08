import openpyxl

inv_file = openpyxl.load_workbook("D:/Documents/src/training/training-code/py-training/Spreadsheet/mobile_users.xlsx")
product_list = inv_file["Sheet1"]

print(product_list.max_row)