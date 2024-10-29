import sqlite3

def tasks_all():
    conn = connect_to_db()
    rows = conn.execute(
        """
        SELECT * FROM tasks
        """
    ).fetchall()
    return [dict(row) for row in rows]

def tasks_create(name, estimated_time, deadline):
    conn = connect_to_db()
    row = conn.execute(
        """
        INSERT INTO tasks (name, estimated_time, deadline)
        VALUES (?, ?, ?)
        RETURNING *
        """,
        (name, estimated_time, deadline),
    ).fetchone()
    conn.commit()
    return dict(row)

def tasks_find_by_id(id):
    conn = connect_to_db()
    row = conn.execute(
        """
        SELECT * FROM tasks
        WHERE id = ?
        """,
        (id,),
    ).fetchone()
    return dict(row)


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