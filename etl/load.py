import psycopg2

def to_postgres(df):
    print("Loading data into PostgreSQL...")
    conn = psycopg2.connect(
        dbname="etl_demo",
        user="postgres",
        password="yourpassword",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name TEXT,
            age INT,
            email TEXT
        )
    """)
    for _, row in df.iterrows():
        cursor.execute(
            "INSERT INTO users (name, age, email) VALUES (%s, %s, %s)",
            (row['name'], row['age'], row['email'])
        )
    conn.commit()
    cursor.close()
    conn.close()
