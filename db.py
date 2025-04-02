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

def barcha_talabalar():
    sorov = """
    SELECT student_id, first_name, last_name, email, major, status
    FROM Student
    ORDER BY last_name, first_name
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

def main():
    talabalar = barcha_talabalar()
    print(talabalar)

if __name__ == "__main__":
    main()