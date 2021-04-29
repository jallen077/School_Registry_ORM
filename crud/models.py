from django.db import models
from django.utils.timezone import now

# Define your models from here:
class User(models.Model):
    first_name = models.CharField(null=False, max_length=30, default='john')
    last_name = models.CharField(null=False, max_length=30, default='doe')
    dob = models.DateField(null=True) 

    # Create a toString method for object string representation
    def __str__(self):
        return self.first_name + " " + self.last_name

class Instructor(User):
    full_time = models.BooleanField(default=True)
    total_learners = models.IntegerField()

    # Create a toString method for object string representation
    def __str__(self):
        return "First name: " + self.first_name + "," + \
               "Last name: " + self.last_name + "," + \
                "Is full time: " + str(self.full_time) + "," + \
                "Total learners: " + str(self.total_learners)

# Course model
class Course(models.Model):
    name = models.CharField(null=False, max_length=100, default='online course')
    description = models.CharField(max_length=500)
    # Many-To-Many relationship with Instructor
    instructors = models.ManyToManyField(Instructor)
    # Many-To-Many relationship with Learner via Enrollment Relationship
    learners = models.ManyToManyField(Learner, through='Enrollement')

    # Create a toString method for object string representation
    def __str__(self):
        return "Name: " + self.name + "," + \
            "Description: " + self.description

# Appending a lesson 
class Lesson(models.Model):
    title = models.CharField(max_length=200, default="title")
    course = models.ForeignKey(Course, null=True, on_delete=models.CASCADE)
    content = models.TextField()

# Learner Model 
class Learner(User):
    STUDENT = 'student'
    DEVELOPER = 'developer'
    DATA_SCIENTIST = 'dba'
    OCCUPATION_CHOICES = [
        (STUDENT, 'Student'),
        (DEVELOPER, 'Developer'),
        (DATA_SCIENTIST, 'Data Scientist'),
        (DATABASE_ADMIN, 'Database Admin')
    ]
    occupation = models.CharField(
        null=False,
        max_length=20,
        choices=OCCUPATION_CHOICES,
        default=STUDENT
    )
    social_link = models.URLField(max_length=200)

    ## Create a string method for returning a string presentation
    def __str__(self):
        return  "First Name: " self.first_name + \ 
                "Last Name: " + self.last_name + \
                "Occupation: " + self.occupation + \ 
                "Social Link: " + social_link

# Enrollment model as a lookup table with additiona enrollment info
class Enrollment(models.Model):
    AUDIT = 'audit'
    HONOR = 'honor'
    COURSE_MODES = [
        (AUDIT,'Audit'),
        (HONOR,'Honor'),
    ]
    
    # add a learner foreign key
    learner = models.ForeignKey(Learner, on_delete=models.CASCADE)
    # add a course foreign key
    course = models.FOreignKey(Course, on_delete=models.CASCADE)
    # Enrollment date
    date_enrolled = models.DateField(default=now)
    # Enrollment mode
    mode = models.CharField(max_length=5, choices=COURSE_MODES, default=AUDIT)

    # Create a toString model to print the information
    def __str__(self):
        return "Learner: " + self.learner + "," + \
               "Course: " + self.course + "," + \
               "Date Enrolled: " + self.date_enrolled + "," + \
               "Mode: " + self.mode
    

