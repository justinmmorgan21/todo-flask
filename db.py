import sqlite3


def connect_to_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


def initial_setup():
    conn = connect_to_db()
    conn.execute(
        """
        DROP TABLE IF EXISTS tasks;
        """
    )
    conn.execute(
        """
        CREATE TABLE tasks (
          id INTEGER PRIMARY KEY NOT NULL,
          name TEXT,
          estimated_time INTEGER,
          deadline TEXT
        );
        """
    )
    conn.commit()
    print("Table created successfully")

    tasks_seed_data = [
        ("change oil", 480, "2024-11-10"),
        ("clean garage", 120, "2024-11-03"),
        ("trim hedges", 150, "2024-11-01"),
    ]
    conn.executemany(
        """
        INSERT INTO tasks (name, estimated_time, deadline)
        VALUES (?,?,?)
        """,
        tasks_seed_data,
    )
    conn.commit()
    print("Seed data created successfully")

    conn.close()


if __name__ == "__main__":
    initial_setup()