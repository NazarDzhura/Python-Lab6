# Python-Lab6

### My task was to:
1. Implement REST-service (operations GET/POST/PUT/DELETE) for one of classes from lab3 with usage of python tools:
* ___Flask___
* ___Python 3.x___

2. Implement saving of object of the class from lab3 in database with usage of:
* ___SQLAlchemy-1.1.15___
* ___MySQL-5.7 / MySQL 8.0

### Content
* Wev-page for application using HTML, CSS
* Database MySQL (using PyMySQL)
* POST, PUT, DELETE methods

### How to run (Windows)
1. Go to directory where you want to clone this repository and type in: ___git clone https://github.com/NazarDzhura/Python-Lab6.git___
2. Move in this project directory.
3. Create your virtual environment in command line and activate it:
   * ___python -m venv venv___
   * ___venv\scripts\activate.bat___
4. Create MySQL database named flask-tutorial-db:
   * ___mysql -u root -p___
   * ___CREATE USER IF NOT EXISTS 'flask-user'@'localhost' IDENTIFIED BY '1050';___
   * ___exit___
   * ___mysql -u flask-user -p___
   * ___create database if not exists `lab6flask`;___
   * ___exit___
5. Install all project requirements ___pip install -r requirements.txt___
6. Create needed tables in the database:
   * Open python interpreter with the command ___python___
   * Import our database ___from app import db___
   * Create all needed tables with command ___db.create_all()___
   * ___exit()___
7. Run application ___python app.py___