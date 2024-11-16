import sqlite3
from config import DB_PATH

def connect():
    """Connect to the SQLite database."""
    try:
        conn = sqlite3.connect(DB_PATH)
        return conn
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        return None

def init_db():
    """Initialize the database with necessary tables."""
    conn = connect()
    if conn:
        cursor = conn.cursor()
        try:
            
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS professions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL UNIQUE,
                    description TEXT,
                    key_skills TEXT,
                    roadmap TEXT
                );
            """)

            seed_data(cursor)

           
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error initializing database: {e}")
        finally:
            conn.close()

def seed_data(cursor):
    """Add initial sample data to the professions table."""
    sample_data = [
        ("Software Developer", "Develops software applications", "Programming, Problem-Solving", "1. Learn programming\n2. Build projects\n3. Internships\n4. Get a job"),
        ("Graphic Designer", "Designs graphics for digital and print media", "Creativity, Adobe Suite", "1. Learn design tools\n2. Build a portfolio\n3. Freelance projects\n4. Find a job"),
        ("Data Scientist", "Analyzes data for insights", "Python, Statistics, Machine Learning", "1. Learn Python\n2. Learn statistics\n3. Work on datasets\n4. Apply for jobs"),
    ]
    for name, description, key_skills, roadmap in sample_data:
        cursor.execute("""
            INSERT OR IGNORE INTO professions (name, description, key_skills, roadmap)
            VALUES (?, ?, ?, ?);
        """, (name, description, key_skills, roadmap))

def get_all_professions():
    """Retrieve all professions from the database."""
    conn = connect()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM professions;")
            results = cursor.fetchall()
            return [row[0] for row in results]
        except sqlite3.Error as e:
            print(f"Error retrieving professions: {e}")
            return []
        finally:
            conn.close()
    return []

def get_profession_details(profession_name):
    """Retrieve details for a specific profession."""
    conn = connect()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT description, key_skills FROM professions WHERE name = ?;", (profession_name,))
            result = cursor.fetchone()
            if result:
                return {"description": result[0], "key_skills": result[1]}
            return None
        except sqlite3.Error as e:
            print(f"Error retrieving profession details: {e}")
            return None
        finally:
            conn.close()
    return None

def get_professions_by_interest(interest):
    """Search for professions by a keyword in their description or skills."""
    conn = connect()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT name FROM professions 
                WHERE description LIKE ? OR key_skills LIKE ?;
            """, (f"%{interest}%", f"%{interest}%"))
            results = cursor.fetchall()
            return [row[0] for row in results]
        except sqlite3.Error as e:
            print(f"Error searching professions by interest: {e}")
            return []
        finally:
            conn.close()
    return []

def get_profession_roadmap(profession_name):
    """Retrieve the roadmap for a specific profession."""
    conn = connect()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT roadmap FROM professions WHERE name = ?;", (profession_name,))
            result = cursor.fetchone()
            return result[0] if result else "No roadmap available."
        except sqlite3.Error as e:
            print(f"Error retrieving profession roadmap: {e}")
            return "No roadmap available."
        finally:
            conn.close()
    return "No roadmap available."