from student import Student

# drop the table if it exists
Student.drop_table()

# create the table
Student.create_table()


# create an instance of the student class
student1 = Student.create(
    "Vincent", "Lemuel", "Male", 30, "0712323634", "LemmyC", "lemmy@example.com"
)

student2 = Student.create(
    "Agnes", "Gitau", "Female", 18, "0712345634", "Aggie", "agnes@example.com"
)

# update a recorde
# student1.age = 25
# student2.phone = "0712121212"

# student1.update()
# student2.update()


# delete record from the table
# student1.delete()
# student1.delete()