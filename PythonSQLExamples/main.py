import sqlite3
import os

'''
KOD İÇERİĞİ
1- Veritabanı Oluşturma ve Silme
Eğer students.lb veritabanı varsa sil. Yeni bir SQLite db oluştur
conn ile bağlan ve cursor(imleç) nesneleri oluştur

2- Tablo Oluşturma (CREATE TABLE)
Students ve Courses tablolarını oluştur

3- Veri Ekleme ( INSERT INTO )
Tablolara executeMany() ile veri ekle

4- Temel SQL Sorguları (basic_sql_operations(cursors))
SELECT * , SELECT col1, col2 , WHERE, ORDER BY, LIMIT

5- Veri Güncelleme ve Silme (sql_update_delete_insert_operations(conn,cursor))
dikkat !!! bu kısımda veritabanında değişiklikler yapacağımız için conn da gelmeli !!!!
INSERT, UPDATE, DELETE 

6- Toplu İşlevler (Aggregate Functions)- (aggregate_functions())
COUNT(*), AVG(column), MAX/MIN, GROUP BY

7- Sorgu Alıştırmaları

'''








def create_database():
    if os.path.exists("students.db"): #kodun her yerde düzgün çalışmasını sağlar
        os.remove("students.db") #eğer bu database varsa sil

    conn = sqlite3.connect("students.db") #bağlantı oluştur
    cursor = conn.cursor() #bağlantı içinde imleç oluştur. Bu imleç, bağlantıyı kullanarak database içinde gezinir. ve istediğimiz veri işlemlerini yapar
    return conn, cursor



def create_tables(cursor):

    cursor.execute('''
    CREATE TABLE Students (
        id INTEGER PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        age INTEGER,
        email VARCHAR UNIQUE,
        city VARCHAR)
    ''')

    cursor.execute('''
        CREATE TABLE Courses(
            id INTEGER PRIMARY KEY,
            course_name VARCHAR NOT NULL,
            instructor TEXT,
            credits INTEGER)
        ''')

#PYTHON İLE DB'YE VERİ EKLEME
def insert_sample_data(cursor):

    students = [
        (1, 'Alice Johnson', 20, 'alice@gmail.com', 'New York'),
        (2, 'Bob Smith', 19, 'bob@gmail.com', 'Chicago'),
        (3, 'Carol White', 21, 'carol@gmail.com', 'Boston'),
        (4, 'David Brom', 20, 'david@gmail.com', 'New York'),
        (5, 'Emma Davis', 22, 'emma@gmail.com', 'Seattle')
    ]
    #liste tupleı olduğu için, yani birden fazla işlem yapacağımız için ->executemany
    cursor.executemany("INSERT INTO Students VALUES (?,?,?,?,?)", students)


    courses= [
        (1, 'Python Programming', 'Dr. Anderson', 3),
        (2, 'Web Development', 'Dr. Wilson', 4),
        (3, 'Data Science', 'Dr. Taylor', 3),
        (4, 'Mobile Apps', 'Dr. Garcia', 2)
    ]

    cursor.executemany("INSERT INTO Courses VALUES (?,?,?,?)", courses)
    print("Sample data inserted successfully")

def basic_sql_operations(cursor):
    # 1- SELECT ALL
    print("-----------------SELECT ALL-------------------")
    cursor.execute("SELECT * FROM Students")
    records= cursor.fetchall() #dataları alabileceğimiz fonksiyon
    for row in records: #kolon kolon alıyor verileri
        print(row)


    # 2- SELECT COLUMNS
    print("-----------------SELECT COLUMNS----------------")
    cursor.execute("SELECT name, age FROM Students")
    records = cursor.fetchall()
    print(records)

    # 3- FİLTER
    print("---------------- WHERE AGE = 20 -------------------")
    cursor.execute("SELECT * FROM Students WHERE age=20")
    records = cursor.fetchall()
    print(records)

    # 4- WHERE with string
    print("---------------- Where city = New York -----------------")
    cursor.execute("SELECT * FROM Students WHERE city = 'New York' ")
    records= cursor.fetchall()
    print(records)

    # 5- ORDER BY : alınan sonuçları belli kolona göre sıralı dizer
    print("---------------- ORDER BY age -------------------")
    cursor.execute("SELECT * FROM Students ORDER BY age")
    records=cursor.fetchall()
    print(records)
    for row in records:
        print(row)

    # 6- LİMİTS
    print("-------------- LIMITS ---------------")
    cursor.execute("SELECT * FROM Students LIMIT 3")
    records = cursor.fetchall()
    for row in records:
        print(row)



def sql_update_delete_insert_operations(conn, cursor):

    # 1- INSERT
    cursor.execute("INSERT INTO Students VALUES (6, 'Frank Miller', 23, 'frank@gmail.com', 'Miami')")
    conn.commit() #db'de yaptığımız değişikliklerin kalıcı olması için -> conn


    # 2- UPDATE
    cursor.execute("UPDATE Students SET age = 24 WHERE id=6 ")
    conn.commit()

    # 3- DELETE
    cursor.execute("DELETE FROM Students WHERE id= 6")
    conn.commit()


# AGGREGATE FONKSİYONLAR
def aggregate_functions(cursor):
    print("-------------- AGGREGATE FUNCTIONS - COUNT ------------- ")
    # 1- COUNT :sayma işlemi
    cursor.execute("SELECT COUNT(*) FROM Students ")
    # Students tablosundaki her şeyin sayısını söyle
    result = cursor.fetchone() #yaptığımız işlemin tek sonuç vereceğini biliyorsak -> fetchone()
    #örneğin ıd'ye göre arama yapcaksak tek sonuç geleceği belli. ama isme göre vs yapacaksak fetchall() kullanmalıyız
    print(result[0])


    # 2- AVERAGE :ortalama alma
    print("------------------ AGGREGATE FUNCTIONS - AVERAGE ------------------")
    cursor.execute("SELECT AVG(age) FROM Students ")
    result = cursor.fetchone()
    print(result[0])

    # 3- MAX/MIN
    print("----------------AGGREGATE FUNCTIONS - MAX/MIN---------------")
    cursor.execute("SELECT MAX(age), MIN(age) FROM Students ")
    result = cursor.fetchone()
    print(result)

    # 4- GROUP BY
    print("----------------AGGREGATE FUNCTIONS - GROUP BY------------")
    cursor.execute("SELECT city,COUNT(*) FROM Students GROUP BY city")
    #hangi şehirden kaç tane geldiğini gösterir
    result=cursor.fetchall()
    print(result)



def questions(cursor):
    # Bütün kursların bilgilerini getirin
    print("-------------Bütün kurs bilgileri-------------")
    cursor.execute("SELECT * FROM Courses")
    result=cursor.fetchall()
    print(result)


    #Sadece eğitmenlerin ismini ve ders isim bilgilerini getirin
    print("-------------- Eğitmen- Ders --------------")
    cursor.execute("SELECT course_name,instructor FROM Courses ")
    result=cursor.fetchall()
    print(result)

    #Sadece 21 yaşındaki öğrencileri getirin
    print("---------------21 Yaşındaki Öğrenciler-------------")
    cursor.execute("SELECT name FROM Students WHERE age=21")
    result = cursor.fetchall()
    print(result)

    #Sadece Chicago'da yaşayan öğrencileri getirin
    print("---------------- Sadece Chicago'da Yaşayanlar--------------")
    cursor.execute("SELECT * FROM Students WHERE city='Chicago'")
    result=cursor.fetchall()
    for row in result:
        print(result)


    #Sadece 'Dr. Anderson' tarafından verilen dersleri getirin
    print("---------------------Dr Anderson Tarafından Verilen Dersler ----------")
    cursor.execute("SELECT course_name FROM Courses WHERE instructor='Dr. Anderson' ")
    result=cursor.fetchall()
    print(result)

    #Sadece ismi 'A' ile başlayan öğrencileri getirin
    print("------------- İsmi A ile Başlayan Öğrenciler------------")
    cursor.execute("SELECT name FROM Students WHERE name LIKE 'A%' ")
    result=cursor.fetchall()
    print(result)

    #Sadece 3 ve üzeri kredi alan dersleri getirin
    print("-------------3 ve ÜZERİ KREDİ ALAN DERSLER----------")
    cursor.execute("SELECT course_name FROM Courses WHERE credits>=3")
    result=cursor.fetchall()
    print(result)


    #Öğrencileri alphabetic şekilde dizerek getirin
    print("---------------alphabetic sıralama------------")
    cursor.execute("SELECT name FROM Students ORDER BY name")
    result=cursor.fetchall()
    print(result)

    # 20 yaşından büyük öğrencileri, ismine göre sıralayarak getirin
    print("-------------20 yaşından büyük öğrencileri sıralama---------------")
    cursor.execute("SELECT name,age FROM Students WHERE age>20 ORDER BY name")
    result=cursor.fetchall()
    print(result)


    # Sadece 'New York' veya 'Chicago' da yaşayan öğrenciler
    print("--------------New York veya Chicago'da yaşayan Öğrenciler---------")
    #cursor.execute("SELECT city,name FROM Students WHERE city='New York' or city='Chicago' ")
    cursor.execute("SELECT name, city FROM Students WHERE city IN ('New York', 'Chicago')")
    result=cursor.fetchall()
    print(result)


    #Sadece 'New York' ta yaşamayan öğrencileri getirin
    print("-------------New York'da yaşamayan öğrenciler------------")
    cursor.execute("SELECT city, name FROM Students WHERE NOT city='New York' ")
    result=cursor.fetchall()
    print(result)














def main():
    conn, cursor = create_database() #db oluştur, bağlantı ve imleci ver

    try:
        create_tables(cursor)
        insert_sample_data(cursor)
        basic_sql_operations(cursor)
        sql_update_delete_insert_operations(conn, cursor)
        aggregate_functions(cursor)
        questions(cursor)
        conn.commit()  # cursor(imlecin) yaptığı işleri uygula
    except sqlite3.Error as e:
        print(e)

    finally:
        conn.close() #db'de bağlantı açtıktan sonra onu mutlaka kapatmak gerekir




if __name__== "__main__":
    main()
#main tek başına çalıştırılacaksa ilk burdan başla
