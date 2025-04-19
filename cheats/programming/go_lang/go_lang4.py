cheats = [
    {
        "command": "sql.Open(\"sqlite3\", \"my.db\")",
        "description": "Connect to an SQLite database",
        "example": "db, err := sql.Open(\"sqlite3\", \"file.db\")"
    },
    {
        "command": "db.Exec(\"CREATE TABLE ...\")",
        "description": "Execute SQL commands with Go",
        "example": "db.Exec(\"CREATE TABLE users (...)\""
    },
    {
        "command": "rows.Next() + rows.Scan()",
        "description": "Read data from a query result",
        "example": "for rows.Next() { rows.Scan(&id, &name) }"
    },
    {
        "command": "gorm.Open(sqlite.Open(\"gorm.db\"))",
        "description": "Use GORM ORM to manage models",
        "example": "db.AutoMigrate(&User{})"
    }
]
