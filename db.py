import psycopg2
from config import CONFIG

def boglanish():
    try:
        connection = psycopg2.connect(**CONFIG)
        return connection
    except (Exception, psycopg2.DatabaseError) as e:
        print(f"MB ga boglanishdagi muammo: {e}")

def select_sorovi(sorov):
    results = []
    
    try:
        connection = boglanish()
        cursor = connection.cursor()

        cursor.execute(sorov)

        results = cursor.fetchall()

        cursor.close()
    except (Exception, psycopg2.DatabaseError) as e:
        print(f"MB ga SELECT sorovida muammo: {e}")
    
    connection.close()
    return results


def insert_sorov(sorov):
    connection = None
    natija = False

    try:
        connection = boglanish()
        cursor = connection.cursor()

        cursor.execute(sorov)
        connection.commit()
        cursor.close()
        natija = True
    except (Exception, psycopg2.DatabaseError) as e:
        print(f"MB ga ma'lumot kiritishda muammo: {e}")

    connection.close()
    return natija

def barcha_talabalar():
    sorov = """
    SELECT student_id, first_name, last_name, email, major, status
    FROM Student
    """
    
    natija = select_sorovi(sorov)
    return natija

def barcha_professorlar():
    sorov = """
    SELECT professor_id, first_name, last_name, email, department, specialization
    FROM Professor
    ORDER BY last_name, first_name
    """
    
    natija = select_sorovi(sorov)
    return natija

def barcha_kafedralar():
    sorov = """
    SELECT department_id, name, building, budget, head_professor_id
    FROM Department
    ORDER BY name
    """
    natija = select_sorovi(sorov)
    return natija

def talaba_qoshish(first_name, last_name, email, phone, major, ed,status, dob=None, address=None):
    query = f"""
    INSERT INTO Student 
    (first_name, last_name, email, phone, major, enrollment_date, status, date_of_birth, address) 
    VALUES ('{first_name}', '{last_name}', '{email}', '{phone}', '{major}', '{ed}', '{status}', '{dob}', '{address}')
    """

    return insert_sorov(query)

def main():
    if talaba_qoshish("Sardor", "Obidov", "s.xxx@gmail.com", "123456789", "ATDT", "2012-12-12","Ikkichi", "2012-12-12", "Namangan"):
        print("Yaratildi")
    else:
        print("Xato!")

if __name__ == "__main__":
    main()