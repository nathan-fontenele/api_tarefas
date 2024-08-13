from app import app
from app.main_db import MainDB

if __name__ == '__main__':
    db = MainDB()
    db.create_table()
    app.run(debug=True)
