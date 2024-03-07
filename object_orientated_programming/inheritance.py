# 'Course' is the base class which has the class variables 'name', 'contact_website' and 'head_office'.
class Course:
    name = "Fundamentals of Computer Science"
    contact_website = "www.hyperiondev.com"
    head_office = 'Woodstock, Cape Town'

    # The method below prints out the contact details.
    def contact_details(self):
        print("Please contact us by visiting:", self.contact_website)

    # The method below prints out the location of the head office.
    def head_office_location(self):
        print("The head office location is:", self.head_office)


# 'OOPCourse' is a subclass of 'Course'.
# Its class variable is 'course_id' and the constructor variables are 'trainer' and 'description'.
class OOPCourse(Course):
    course_id = '#12345'

    def __init__(self, trainer, description):
        self.description = description
        self.trainer = trainer

    # The method below describes the details of the course
    def trainer_details(self):
        print(f'{self.description} briefly explains the fundamentals of Object '
              f'Orientated and is taught by {self.trainer}.')

    # The method below prints out the course id
    def show_course_id(self):
        print(f"The ID of this course is {self.course_id}")


# 'course_1' is an object of the 'OOPCourse' class
course_1 = OOPCourse("Mr Anon A. Mouse", "00P Fundamentals")

# The following methods are called
course_1.head_office_location()
course_1.contact_details()
course_1.trainer_details()
course_1.show_course_id()
