import xlrd
loc = ("C:\\Users\\Larry\\OneDrive\\Documents\\water_usage_and_savings.xlsx")
# To open Workbook 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
sheet.cell_value(0, 0) 
  
for i in range(sheet.nrows): 
    print(sheet.cell_value(i, 0)) 