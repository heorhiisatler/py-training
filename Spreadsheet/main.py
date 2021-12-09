from os import close
import openpyxl
import json
import codecs

inv_file = openpyxl.load_workbook('./training-code/py-training/'
                                  'Spreadsheet/mobile_users.xlsx')
product_list = inv_file["Sheet1"]
excess_abonents = {}

for mob_abonent_row in range(2, product_list.max_row):
    #print(product_list.cell(mob_abonent_row, 7).value)
    abonent_name = product_list.cell(mob_abonent_row, 2).value
    excess_perc = product_list.cell(mob_abonent_row, 7).value
    if excess_perc > 0:
        excess_abonents[abonent_name] = str(excess_perc) + " %"
    else:
        None

#print(excess_abonents)

json_object = json.dumps(excess_abonents, indent=5, ensure_ascii=False)
print(json_object)

with codecs.open("sample.json", "w+", "utf-8") as outfile:
    outfile.write(json_object)