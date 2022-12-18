import pyodbc

try:
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\ШРЕК\Desktop\СПб ' \
                 r'КИТ\Работы\БД\Студенты.accdb; '
    conn = pyodbc.connect(con_string)

    Студенты_Шифр = 11

    cur = conn.cursor()
    cur.execute('DELETE FROM Студенты WHERE Шифр = ?', Студенты_Шифр)
    conn.commit()
    print("Data Deleted ")

except pyodbc.Error as e:
    print("Error in Connection")
