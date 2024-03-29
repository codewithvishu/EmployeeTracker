from django.db import models


# Create your models here.
class Employee(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    salary = models.FloatField()
    mobile = models.IntegerField()
    email = models.EmailField()
    DOB = models.DateField()
    joining_date = models.DateField()
    termination_date = models.DateField()
    create_ts = models.DateTimeField()
    mod_ts = models.DateTimeField()
    is_active = models.BooleanField(default=False)

    class Meta:
        db_table = "employee"

    """
    emp2 = Employee(
    firstname = "Nayan",
    lastname = "Jain",
    salary = 25000,
    mobile = 9981086243,
    email = "Vishant.jain@gmail.com",
    DOB = datetime.date(1999, 3, 14),
    joining_date  = datetime.date(2021, 11, 11),
    termination_date = datetime.date(2022, 11, 11),
    create_ts = datetime.datetime.utcnow(),
    mod_ts = datetime.datetime.utcnow(),
    is_active = True,
    )
    # datetime.datetime(2024, 3, 28, 17, 4, 37, 762649)
    emp = Employee(
    "Vishant",
    "Jain",
    datetime.date(1999, 3, 14)
    ....
    True
    )
    """
    """
    Create model Employee

    CREATE TABLE "employee" (
        "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
        "firstname" varchar(100) NOT NULL, 
        "lastname" varchar(100) NOT NULL, 
        "salary" real NOT NULL, 
        "mobile" integer NOT NULL, 
        "email" varchar(254) NOT NULL, 
        "DOB" date NOT NULL, 
        "joining_date" date NOT NULL, 
        "termination_date" date NOT NULL, 
        "create_ts" datetime NOT NULL, 
        "mod_ts" datetime NOT NULL, 
        "is_active" bool NOT NULL
    );
    COMMIT;
    """
