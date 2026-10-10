import openpyxl

def get_login_data():
    workbook = openpyxl.load_workbook('C://Users//pparv//PycharmProjects//Selenium_E28//Selenium Part_C//DemoTricentistFrameWork//test_data/loginData.xlsx')
    sheet = workbook['LoginData']

    data = []
    for row in sheet.iter_rows(min_row=2,values_only=True):
        data.append(row)

    return data