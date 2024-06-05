from config import conn, cursor


class Student:

    def __init__(
        self, first_name, last_name, gender, age, phone, username, email, id=None
    ):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.phone = phone
        self.username = username
        self.email = email

    def __repr__(self):
        return f"<Student {self.first_name} {self.last_name} {self.gender} {self.age} {self.phone} {self.username} {self.email}>"

    # class method responsible for creating the database table
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE students (
            id INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            gender TEXT,
            age INTEGER,
            phone TEXT NOT NULL,
            username TEXT,
            email TEXT
            )
        """

        cursor.execute(sql)
        conn.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS students;
        """

        cursor.execute(sql)
        conn.commit()

    # when saving data into a database table, we need an instance of the class- hence an instance method
    # we use bounded params to avoid directly passing malicious characters and gettig sql injections
    def save(self):
        # we dont need to pass in the id in the query because it is auto incrementing.
        sql = """
            INSERT INTO students (
            first_name, last_name, gender, age, phone, username, email
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
        """

        cursor.execute(
            sql,
            (
                self.first_name,
                self.last_name,
                self.gender,
                self.age,
                self.phone,
                self.username,
                self.email,
            ),
        )
        conn.commit()
        # update the object to contain the auto generated id from the db
        # this id will be required on other queries like update and delete
        self.id = cursor.lastrowid
        # print(f"The last row id: {cursor.lastrowid}")

    # create a class method that automatically creates the instance and saves it in the db
    # class method because the object doesnt yet exist when we call this method
    @classmethod
    def create(cls, first_name, last_name, gender, age, phone, username, email):
        # create a student instance
        student = cls(first_name, last_name, gender, age, phone, username, email)

        # save the instance
        student.save()

        # return the instantiated object
        return student

    # method to update an existing record that corresponds to the object instance
    def update(self):
        sql = """
            UPDATE students SET first_name = ?, last_name = ?, gender = ?, age = ?, phone = ?, username = ?, email = ?
            WHERE id = ?
        """

        cursor.execute(
            sql,
            (
                self.first_name,
                self.last_name,
                self.gender,
                self.age,
                self.phone,
                self.username,
                self.email,
                self.id,
            ),
        )

        conn.commit()

    def delete(self):
        sql = """
            DELETE FROM students
            WHERE id = ?
        """

        cursor.execute(sql, (self.id,))
        conn.commit()
