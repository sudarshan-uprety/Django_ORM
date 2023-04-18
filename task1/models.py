# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class A(models.Model):
    salesman_id = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)
    commission = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'a'


class Abc(models.Model):
    emp_dept = models.IntegerField(blank=True, null=True)
    emp_idno = models.IntegerField(blank=True, null=True)
    rnk2 = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'abc'


class Actor(models.Model):
    act_id = models.IntegerField(primary_key=True)
    act_fname = models.CharField(max_length=20, blank=True, null=True)
    act_lname = models.CharField(max_length=20, blank=True, null=True)
    act_gender = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'actor'


class Actorsbackup2017(models.Model):
    act_fname = models.CharField(max_length=20, blank=True, null=True)
    act_lname = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'actorsbackup2017'


class Address(models.Model):
    city = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'address'


class AffiliatedWith(models.Model):
    physician = models.OneToOneField('Physician', models.DO_NOTHING, db_column='physician', primary_key=True)  # The composite primary key (physician, department) found, that is not supported. The first column is selected.
    department = models.ForeignKey('Department', models.DO_NOTHING, db_column='department')
    primaryaffiliation = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'affiliated_with'
        unique_together = (('physician', 'department'),)


class Ahmed(models.Model):
    employee_id = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    department_id = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    salary = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ahmed'


class Appointment(models.Model):
    appointmentid = models.IntegerField(primary_key=True)
    patient = models.ForeignKey('Patient', models.DO_NOTHING, db_column='patient')
    prepnurse = models.ForeignKey('Nurse', models.DO_NOTHING, db_column='prepnurse', blank=True, null=True)
    physician = models.ForeignKey('Physician', models.DO_NOTHING, db_column='physician')
    start_dt_time = models.DateTimeField()
    end_dt_time = models.DateTimeField()
    examinationroom = models.TextField()

    class Meta:
        managed = False
        db_table = 'appointment'


class AsstRefereeMast(models.Model):
    ass_ref_id = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    ass_ref_name = models.CharField(max_length=40)
    country = models.ForeignKey('SoccerCountry', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'asst_referee_mast'


class Bh(models.Model):
    name = models.CharField(max_length=20)
    emp_id = models.IntegerField()
    process = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bh'


class Bitch(models.Model):
    sum = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bitch'


class Blah(models.Model):
    ord_no = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    purch_amt = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    ord_date = models.DateField(blank=True, null=True)
    customer_id = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    salesman_id = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'blah'


class Block(models.Model):
    blockfloor = models.IntegerField(primary_key=True)  # The composite primary key (blockfloor, blockcode) found, that is not supported. The first column is selected.
    blockcode = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'block'
        unique_together = (('blockfloor', 'blockcode'),)


class C(models.Model):
    cust_name = models.CharField(max_length=30, blank=True, null=True)
    customer_id = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    salesman_name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'c'


class Casino(models.Model):
    pricerange = models.DecimalField(max_digits=6, decimal_places=0)
    events = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=40)
    casino = models.CharField(primary_key=True, max_length=75)

    class Meta:
        managed = False
        db_table = 'casino'


class Categories(models.Model):
    categoryid = models.SmallIntegerField(primary_key=True)
    categoryname = models.CharField(max_length=15)
    description = models.TextField(blank=True, null=True)
    picture = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categories'


class CoachMast(models.Model):
    coach_id = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    coach_name = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'coach_mast'


class Col1(models.Model):
    field_column_field = models.IntegerField(db_column='?column?', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'col1'


class CompanyMast(models.Model):
    com_id = models.IntegerField(primary_key=True)
    com_name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'company_mast'


class Countries(models.Model):
    country_id = models.CharField(max_length=2, blank=True, null=True)
    country_name = models.CharField(max_length=40, blank=True, null=True)
    region_id = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'countries'


class Customer(models.Model):
    customer_id = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
    cust_name = models.CharField(max_length=30)
    city = models.CharField(max_length=15, blank=True, null=True)
    grade = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    salesman = models.ForeignKey('Salesman', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'customer'


class CustomerBackup(models.Model):
    customer_id = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    cust_name = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)
    grade = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    salesman_id = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_backup'


class CustomerId(models.Model):
    ord_no = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    purch_amt = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    ord_date = models.DateField(blank=True, null=True)
    customer_id = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    salesman_id = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_id'


class CustomerId123(models.Model):
    ord_no = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    purch_amt = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    ord_date = models.DateField(blank=True, null=True)
    customer_id = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    salesman_id = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_id_123'


class Customercustomerdemo(models.Model):
    customerid = models.OneToOneField('Customers', models.DO_NOTHING, db_column='customerid', primary_key=True)  # The composite primary key (customerid, customertypeid) found, that is not supported. The first column is selected.
    customertypeid = models.ForeignKey('Customerdemographics', models.DO_NOTHING, db_column='customertypeid')

    class Meta:
        managed = False
        db_table = 'customercustomerdemo'
        unique_together = (('customerid', 'customertypeid'),)


class Customerdemographics(models.Model):
    customertypeid = models.CharField(primary_key=True)
    customerdesc = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customerdemographics'


class Customers(models.Model):
    customerid = models.CharField(primary_key=True)
    companyname = models.CharField(max_length=40)
    contactname = models.CharField(max_length=30, blank=True, null=True)
    contacttitle = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=60, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)
    region = models.CharField(max_length=15, blank=True, null=True)
    postalcode = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=15, blank=True, null=True)
    phone = models.CharField(max_length=24, blank=True, null=True)
    fax = models.CharField(max_length=24, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customers'


class Customersbackup2017(models.Model):
    department_id = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    employee_id = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=25, blank=True, null=True)
    salary = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rnk = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customersbackup2017'


class Department(models.Model):
    departmentid = models.IntegerField(primary_key=True)
    name = models.TextField()
    head = models.ForeignKey('Physician', models.DO_NOTHING, db_column='head')

    class Meta:
        managed = False
        db_table = 'department'


class DepartmentDetail(models.Model):
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=25, blank=True, null=True)
    department_id = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    department_name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'department_detail'


class DepartmentId(models.Model):
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=25, blank=True, null=True)
    salary = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    field_column_field = models.IntegerField(db_column='?column?', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'department_id'


class Departments(models.Model):
    department_id = models.DecimalField(primary_key=True, max_digits=4, decimal_places=0)
    department_name = models.CharField(max_length=30)
    manager_id = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    location_id = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departments'


class Director(models.Model):
    dir_id = models.IntegerField(primary_key=True)
    dir_fname = models.CharField(max_length=20, blank=True, null=True)
    dir_lname = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'director'


class Duplicate(models.Model):
    salesman_id = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)
    commission = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'duplicate'


class Elephants(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'elephants'


class Emp(models.Model):
    ename = models.CharField(max_length=13, blank=True, null=True)
    salary = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    eid = models.DecimalField(primary_key=True, max_digits=3, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'emp'


class EmpDepartment(models.Model):
    dpt_code = models.IntegerField(primary_key=True)
    dpt_name = models.CharField(max_length=15)
    dpt_allotment = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'emp_department'


class EmpDetails(models.Model):
    emp_idno = models.IntegerField(primary_key=True)
    emp_fname = models.CharField(max_length=15)
    emp_lname = models.CharField(max_length=15)
    emp_dept = models.ForeignKey(EmpDepartment, models.DO_NOTHING, db_column='emp_dept')

    class Meta:
        managed = False
        db_table = 'emp_details'


class Employee(models.Model):
    empno = models.IntegerField(blank=True, null=True)
    ename = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee'


class Employees(models.Model):
    employeeid = models.SmallIntegerField(primary_key=True)
    lastname = models.CharField(max_length=20)
    firstname = models.CharField(max_length=10)
    title = models.CharField(max_length=30, blank=True, null=True)
    titleofcourtesy = models.CharField(max_length=25, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    hiredate = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=60, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)
    region = models.CharField(max_length=15, blank=True, null=True)
    postalcode = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=15, blank=True, null=True)
    homephone = models.CharField(max_length=24, blank=True, null=True)
    extension = models.CharField(max_length=4, blank=True, null=True)
    photo = models.BinaryField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    reportsto = models.ForeignKey('self', models.DO_NOTHING, db_column='reportsto', blank=True, null=True)
    photopath = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employees'


class Employeescopy(models.Model):
    employee_id = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=25, blank=True, null=True)
    email = models.CharField(max_length=25, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    hire_date = models.DateField(blank=True, null=True)
    job_id = models.CharField(max_length=10, blank=True, null=True)
    salary = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    commission_pct = models.DecimalField(max_digits=2, decimal_places=2, blank=True, null=True)
    manager_id = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    department_id = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employeescopy'


class Employeeterritories(models.Model):
    employeeid = models.OneToOneField(Employees, models.DO_NOTHING, db_column='employeeid', primary_key=True)  # The composite primary key (employeeid, territoryid) found, that is not supported. The first column is selected.
    territoryid = models.ForeignKey('Territories', models.DO_NOTHING, db_column='territoryid')

    class Meta:
        managed = False
        db_table = 'employeeterritories'
        unique_together = (('employeeid', 'territoryid'),)


class Ff(models.Model):
    salesman_id = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)
    commission = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    subject = models.CharField(max_length=25, blank=True, null=True)
    winner = models.CharField(max_length=45, blank=True, null=True)
    country = models.CharField(max_length=25, blank=True, null=True)
    category = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ff'


class Fg(models.Model):
    customer_id = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    avg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fg'


class GameScores(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'game_scores'


class Genres(models.Model):
    gen_id = models.IntegerField(primary_key=True)
    gen_title = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'genres'


class GoalDetails(models.Model):
    goal_id = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    match_no = models.ForeignKey('MatchMast', models.DO_NOTHING, db_column='match_no')
    player = models.ForeignKey('PlayerMast', models.DO_NOTHING)
    team = models.ForeignKey('SoccerCountry', models.DO_NOTHING)
    goal_time = models.DecimalField(max_digits=65535, decimal_places=65535)
    goal_type = models.CharField(max_length=1)
    play_stage = models.CharField(max_length=1)
    goal_schedule = models.CharField(max_length=2)
    goal_half = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goal_details'


class Grade(models.Model):
    city = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'grade'


class Grades(models.Model):
    id = models.IntegerField(primary_key=True)
    grade_1 = models.IntegerField(blank=True, null=True)
    grade_2 = models.IntegerField(blank=True, null=True)
    grade_3 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'grades'


class Hello(models.Model):
    number_one = models.IntegerField(blank=True, null=True)
    number_two = models.IntegerField(blank=True, null=True)
    number_three = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hello'


class Hello11122(models.Model):
    abc = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hello1_1122'


class Hello112(models.Model):
    abc = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hello1_12'


class Hello12(models.Model):
    abc = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hello_12'


class Item(models.Model):
    com_name = models.CharField(max_length=20, blank=True, null=True)
    max = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item'


class ItemId(models.Model):
    com_name = models.CharField(max_length=20, blank=True, null=True)
    max = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item_id'


class ItemMast(models.Model):
    pro_id = models.IntegerField(primary_key=True)
    pro_name = models.CharField(max_length=25)
    pro_price = models.DecimalField(max_digits=8, decimal_places=2)
    pro_com = models.ForeignKey(CompanyMast, models.DO_NOTHING, db_column='pro_com')

    class Meta:
        managed = False
        db_table = 'item_mast'


class JobGrades(models.Model):
    grade_level = models.CharField(primary_key=True, max_length=20)
    lowest_sal = models.DecimalField(max_digits=5, decimal_places=0)
    highest_sal = models.DecimalField(max_digits=5, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'job_grades'


class JobHistory(models.Model):
    employee_id = models.DecimalField(primary_key=True, max_digits=6, decimal_places=0)  # The composite primary key (employee_id, start_date) found, that is not supported. The first column is selected.
    start_date = models.DateField()
    end_date = models.DateField()
    job_id = models.CharField(max_length=10)
    department_id = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_history'
        unique_together = (('employee_id', 'start_date'),)


class Jobs(models.Model):
    job_id = models.CharField(primary_key=True, max_length=10)
    job_title = models.CharField(max_length=35)
    min_salary = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    max_salary = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jobs'


class Kk(models.Model):
    salesman_id = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)
    commission = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kk'


class Kkk(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kkk'


class Locations(models.Model):
    location_id = models.DecimalField(primary_key=True, max_digits=4, decimal_places=0)
    street_address = models.CharField(max_length=40, blank=True, null=True)
    postal_code = models.CharField(max_length=12, blank=True, null=True)
    city = models.CharField(max_length=30)
    state_province = models.CharField(max_length=25, blank=True, null=True)
    country_id = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'locations'


class Londoncustomers(models.Model):
    cust_name = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'londoncustomers'


class Manufacturers(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'manufacturers'


class Marco(models.Model):
    emp_idno = models.IntegerField(blank=True, null=True)
    emp_fname = models.CharField(max_length=15, blank=True, null=True)
    emp_lname = models.CharField(max_length=15, blank=True, null=True)
    emp_dept = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'marco'


class MatchCaptain(models.Model):
    match_no = models.ForeignKey('MatchMast', models.DO_NOTHING, db_column='match_no')
    team = models.ForeignKey('SoccerCountry', models.DO_NOTHING)
    player_captain = models.ForeignKey('PlayerMast', models.DO_NOTHING, db_column='player_captain')

    class Meta:
        managed = False
        db_table = 'match_captain'


class MatchDetails(models.Model):
    match_no = models.ForeignKey('MatchMast', models.DO_NOTHING, db_column='match_no')
    play_stage = models.CharField(max_length=1)
    team = models.ForeignKey('SoccerCountry', models.DO_NOTHING)
    win_lose = models.CharField(max_length=1)
    decided_by = models.CharField(max_length=1)
    goal_score = models.DecimalField(max_digits=65535, decimal_places=65535)
    penalty_score = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ass_ref = models.ForeignKey(AsstRefereeMast, models.DO_NOTHING, db_column='ass_ref')
    player_gk = models.ForeignKey('PlayerMast', models.DO_NOTHING, db_column='player_gk')

    class Meta:
        managed = False
        db_table = 'match_details'


class MatchMast(models.Model):
    match_no = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    play_stage = models.CharField(max_length=1)
    play_date = models.DateField()
    results = models.CharField(max_length=5)
    decided_by = models.CharField(max_length=1)
    goal_score = models.CharField(max_length=5)
    venue = models.ForeignKey('SoccerVenue', models.DO_NOTHING)
    referee = models.ForeignKey('RefereeMast', models.DO_NOTHING)
    audence = models.DecimalField(max_digits=65535, decimal_places=65535)
    plr_of_match = models.ForeignKey('PlayerMast', models.DO_NOTHING, db_column='plr_of_match')
    stop1_sec = models.DecimalField(max_digits=65535, decimal_places=65535)
    stop2_sec = models.DecimalField(max_digits=65535, decimal_places=65535)

    class Meta:
        managed = False
        db_table = 'match_mast'


class Maxim00(models.Model):
    num = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maxim00'


class Maximum(models.Model):
    num = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maximum'


class Maximum00(models.Model):
    num = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maximum00'


class Maximum899(models.Model):
    num = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maximum899'


class Medication(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.TextField()
    brand = models.TextField()
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'medication'


class Meow(models.Model):
    max = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ord_date = models.DateField(blank=True, null=True)
    namemax = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meow'


class Movie(models.Model):
    mov_id = models.IntegerField(primary_key=True)
    mov_title = models.CharField(max_length=50, blank=True, null=True)
    mov_year = models.IntegerField(blank=True, null=True)
    mov_time = models.IntegerField(blank=True, null=True)
    mov_lang = models.CharField(max_length=15, blank=True, null=True)
    mov_dt_rel = models.DateField(blank=True, null=True)
    mov_rel_country = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movie'


class MovieCast(models.Model):
    act = models.ForeignKey(Actor, models.DO_NOTHING)
    mov = models.ForeignKey(Movie, models.DO_NOTHING)
    role = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movie_cast'


class MovieDirection(models.Model):
    dir = models.ForeignKey(Director, models.DO_NOTHING)
    mov = models.ForeignKey(Movie, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'movie_direction'


class MovieGenres(models.Model):
    mov = models.ForeignKey(Movie, models.DO_NOTHING)
    gen = models.ForeignKey(Genres, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'movie_genres'


class My(models.Model):
    customer_id = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    avg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'my'


class Mytemptable(models.Model):
    customer_id = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    avg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mytemptable'


class Mytest(models.Model):
    ord_num = models.DecimalField(unique=True, max_digits=6, decimal_places=0)
    ord_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    ord_date = models.DateField()
    cust_code = models.CharField(max_length=6)
    agent_code = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'mytest'


class Mytest1(models.Model):
    ord_num = models.DecimalField(unique=True, max_digits=6, decimal_places=0)
    ord_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    ord_date = models.DateField()
    cust_code = models.CharField(max_length=6)
    agent_code = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'mytest1'


class New(models.Model):
    city = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'new'


class New123(models.Model):
    customer = models.CharField(db_column='Customer', max_length=30, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(max_length=15, blank=True, null=True)
    salesman = models.CharField(db_column='Salesman', max_length=30, blank=True, null=True)  # Field name made lowercase.
    commission = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'new123'


class NewTable(models.Model):
    salesman_id = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)
    commission = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'new_table'


class Newsalesman(models.Model):
    salesman_id = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)
    commission = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'newsalesman'


class Newtab(models.Model):
    ord_no = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    purch_amt = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    ord_date = models.DateField(blank=True, null=True)
    customer_id = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    salesman_id = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'newtab'


class Newtable2(models.Model):
    roomnumber = models.IntegerField(blank=True, null=True)
    roomtype = models.CharField(max_length=30, blank=True, null=True)
    blockfloor = models.IntegerField(blank=True, null=True)
    blockcode = models.IntegerField(blank=True, null=True)
    unavailable = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'newtable2'


class NobelWin(models.Model):
    year = models.IntegerField(blank=True, null=True)
    subject = models.CharField(max_length=25, blank=True, null=True)
    winner = models.CharField(max_length=45, blank=True, null=True)
    country = models.CharField(max_length=25, blank=True, null=True)
    category = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nobel_win'


class Nros(models.Model):
    uno = models.IntegerField(blank=True, null=True)
    dos = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nros'


class Nuevo(models.Model):
    city = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nuevo'


class Numbers(models.Model):
    one = models.IntegerField(blank=True, null=True)
    two = models.IntegerField(blank=True, null=True)
    three = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'numbers'


class Numeri(models.Model):
    id = models.IntegerField(primary_key=True)
    data = models.DateField(blank=True, null=True)
    decimali = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'numeri'


class Numeros(models.Model):
    uno = models.IntegerField(blank=True, null=True)
    dos = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'numeros'


class Nurse(models.Model):
    employeeid = models.IntegerField(primary_key=True)
    name = models.TextField()
    position = models.TextField()
    registered = models.BooleanField()
    ssn = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nurse'


class Oi(models.Model):
    customer_id = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    avg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oi'


class OnCall(models.Model):
    nurse = models.OneToOneField(Nurse, models.DO_NOTHING, db_column='nurse', primary_key=True)  # The composite primary key (nurse, blockfloor, blockcode, oncallstart, oncallend) found, that is not supported. The first column is selected.
    blockfloor = models.ForeignKey(Block, models.DO_NOTHING, db_column='blockfloor')
    blockcode = models.IntegerField()
    oncallstart = models.DateTimeField()
    oncallend = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'on_call'
        unique_together = (('nurse', 'blockfloor', 'blockcode', 'oncallstart', 'oncallend'),)


class OrderDetails(models.Model):
    orderid = models.OneToOneField('Orders', models.DO_NOTHING, db_column='orderid', primary_key=True)  # The composite primary key (orderid, productid) found, that is not supported. The first column is selected.
    productid = models.ForeignKey('Products', models.DO_NOTHING, db_column='productid')
    unitprice = models.FloatField()
    quantity = models.SmallIntegerField()
    discount = models.FloatField()

    class Meta:
        managed = False
        db_table = 'order_details'
        unique_together = (('orderid', 'productid'),)


class Orders(models.Model):
    orderid = models.SmallIntegerField(primary_key=True)
    customerid = models.ForeignKey(Customers, models.DO_NOTHING, db_column='customerid', blank=True, null=True)
    employeeid = models.ForeignKey(Employees, models.DO_NOTHING, db_column='employeeid', blank=True, null=True)
    orderdate = models.DateField(blank=True, null=True)
    requireddate = models.DateField(blank=True, null=True)
    shippeddate = models.DateField(blank=True, null=True)
    shipvia = models.ForeignKey('Shippers', models.DO_NOTHING, db_column='shipvia', blank=True, null=True)
    freight = models.FloatField(blank=True, null=True)
    shipname = models.CharField(max_length=40, blank=True, null=True)
    shipaddress = models.CharField(max_length=60, blank=True, null=True)
    shipcity = models.CharField(max_length=15, blank=True, null=True)
    shipregion = models.CharField(max_length=15, blank=True, null=True)
    shippostalcode = models.CharField(max_length=10, blank=True, null=True)
    shipcountry = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'


class Orders2(models.Model):
    ord_no = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    purch_amt = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    ord_date = models.DateField(blank=True, null=True)
    customer_id = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    salesman_id = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders2'


class Orozco(models.Model):
    city = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orozco'


class Partest1(models.Model):
    ord_num = models.DecimalField(unique=True, max_digits=6, decimal_places=0)
    ord_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    ord_date = models.DateField()
    cust_code = models.CharField(max_length=6)
    agent_code = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'partest1'


class Participant(models.Model):
    participant_id = models.IntegerField()
    part_name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'participant'


class Participants(models.Model):
    participant_id = models.IntegerField()
    part_name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'participants'


class Patient(models.Model):
    ssn = models.IntegerField(primary_key=True)
    name = models.TextField()
    address = models.TextField()
    phone = models.TextField()
    insuranceid = models.IntegerField()
    pcp = models.ForeignKey('Physician', models.DO_NOTHING, db_column='pcp')

    class Meta:
        managed = False
        db_table = 'patient'


class PenaltyGk(models.Model):
    match_no = models.ForeignKey(MatchMast, models.DO_NOTHING, db_column='match_no')
    team = models.ForeignKey('SoccerCountry', models.DO_NOTHING)
    player_gk = models.ForeignKey('PlayerMast', models.DO_NOTHING, db_column='player_gk')

    class Meta:
        managed = False
        db_table = 'penalty_gk'


class PenaltyShootout(models.Model):
    kick_id = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    match_no = models.ForeignKey(MatchMast, models.DO_NOTHING, db_column='match_no')
    team = models.ForeignKey('SoccerCountry', models.DO_NOTHING)
    player = models.ForeignKey('PlayerMast', models.DO_NOTHING)
    score_goal = models.CharField(max_length=1)
    kick_no = models.DecimalField(max_digits=65535, decimal_places=65535)

    class Meta:
        managed = False
        db_table = 'penalty_shootout'

    # def __str__(self):
    #     return self.player


class Persons(models.Model):
    personid = models.IntegerField(blank=True, null=True)
    lastname = models.CharField(max_length=255, blank=True, null=True)
    firstname = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'persons'


class Physician(models.Model):
    employeeid = models.IntegerField(primary_key=True)
    name = models.TextField()
    position = models.TextField()
    ssn = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'physician'


class PlayerBooked(models.Model):
    match_no = models.ForeignKey(MatchMast, models.DO_NOTHING, db_column='match_no')
    team = models.ForeignKey('SoccerCountry', models.DO_NOTHING)
    player = models.ForeignKey('PlayerMast', models.DO_NOTHING)
    booking_time = models.DecimalField(max_digits=65535, decimal_places=65535)
    sent_off = models.CharField(max_length=1, blank=True, null=True)
    play_schedule = models.CharField(max_length=2)
    play_half = models.DecimalField(max_digits=65535, decimal_places=65535)

    class Meta:
        managed = False
        db_table = 'player_booked'


class PlayerInOut(models.Model):
    match_no = models.ForeignKey(MatchMast, models.DO_NOTHING, db_column='match_no')
    team = models.ForeignKey('SoccerCountry', models.DO_NOTHING)
    player = models.ForeignKey('PlayerMast', models.DO_NOTHING)
    in_out = models.CharField(max_length=1)
    time_in_out = models.DecimalField(max_digits=65535, decimal_places=65535)
    play_schedule = models.CharField(max_length=2)
    play_half = models.DecimalField(max_digits=65535, decimal_places=65535)

    class Meta:
        managed = False
        db_table = 'player_in_out'


class PlayerMast(models.Model):
    player_id = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    team = models.ForeignKey('SoccerCountry', models.DO_NOTHING)
    jersey_no = models.DecimalField(max_digits=65535, decimal_places=65535)
    player_name = models.CharField(max_length=40)
    posi_to_play = models.ForeignKey('PlayingPosition', models.DO_NOTHING, db_column='posi_to_play')
    dt_of_bir = models.DateField(blank=True, null=True)
    age = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    playing_club = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'player_mast'


class PlayingPosition(models.Model):
    position_id = models.CharField(primary_key=True, max_length=2)
    position_desc = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'playing_position'


class Prescribes(models.Model):
    physician = models.OneToOneField(Physician, models.DO_NOTHING, db_column='physician', primary_key=True)  # The composite primary key (physician, patient, medication, date) found, that is not supported. The first column is selected.
    patient = models.ForeignKey(Patient, models.DO_NOTHING, db_column='patient')
    medication = models.ForeignKey(Medication, models.DO_NOTHING, db_column='medication')
    date = models.DateTimeField()
    appointment = models.ForeignKey(Appointment, models.DO_NOTHING, db_column='appointment', blank=True, null=True)
    dose = models.TextField()

    class Meta:
        managed = False
        db_table = 'prescribes'
        unique_together = (('physician', 'patient', 'medication', 'date'),)


class Procedure(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.TextField()
    cost = models.FloatField()

    class Meta:
        managed = False
        db_table = 'procedure'


class Products(models.Model):
    productid = models.SmallIntegerField(primary_key=True)
    productname = models.CharField(max_length=40)
    supplierid = models.ForeignKey('Suppliers', models.DO_NOTHING, db_column='supplierid', blank=True, null=True)
    categoryid = models.ForeignKey(Categories, models.DO_NOTHING, db_column='categoryid', blank=True, null=True)
    quantityperunit = models.CharField(max_length=20, blank=True, null=True)
    unitprice = models.FloatField(blank=True, null=True)
    unitsinstock = models.SmallIntegerField(blank=True, null=True)
    unitsonorder = models.SmallIntegerField(blank=True, null=True)
    reorderlevel = models.SmallIntegerField(blank=True, null=True)
    discontinued = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'products'


class Ramyasales(models.Model):
    salesman_id = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)
    commission = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ramyasales'


class Rating(models.Model):
    mov = models.ForeignKey(Movie, models.DO_NOTHING)
    rev = models.ForeignKey('Reviewer', models.DO_NOTHING)
    rev_stars = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    num_o_ratings = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rating'


class RefereeMast(models.Model):
    referee_id = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    referee_name = models.CharField(max_length=40)
    country = models.ForeignKey('SoccerCountry', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'referee_mast'


class Region(models.Model):
    regionid = models.SmallIntegerField(primary_key=True)
    regiondescription = models.CharField()

    class Meta:
        managed = False
        db_table = 'region'


class Regions(models.Model):
    region_id = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    region_name = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'regions'


class Related(models.Model):
    city = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'related'


class Reviewer(models.Model):
    rev_id = models.IntegerField(primary_key=True)
    rev_name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reviewer'


class Room(models.Model):
    roomnumber = models.IntegerField(primary_key=True)
    roomtype = models.CharField(max_length=30)
    blockfloor = models.ForeignKey(Block, models.DO_NOTHING, db_column='blockfloor')
    blockcode = models.IntegerField()
    unavailable = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'room'


class Rt(models.Model):
    ord_no = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    purch_amt = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    ord_date = models.DateField(blank=True, null=True)
    customer_id = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    salesman_id = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rt'


class Salesman(models.Model):
    salesman_id = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=15, blank=True, null=True)
    commission = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'salesman'


class Salesman2(models.Model):
    salesman_id = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)
    commission = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'salesman2'


class SalesmanDo1304(models.Model):
    salesman_id = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=40, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    commission = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'salesman_do1304'


class SampleTable(models.Model):
    salesman_id = models.CharField(max_length=4, blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    commission = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sample_table'


class Scores(models.Model):
    id = models.IntegerField(primary_key=True)
    score = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scores'


class Shippers(models.Model):
    shipperid = models.SmallIntegerField(primary_key=True)
    companyname = models.CharField(max_length=40)
    phone = models.CharField(max_length=24, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shippers'


class SoccerCity(models.Model):
    city_id = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    city = models.CharField(max_length=25)
    country = models.ForeignKey('SoccerCountry', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'soccer_city'


class SoccerCountry(models.Model):
    country_id = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    country_abbr = models.CharField(max_length=4)
    country_name = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'soccer_country'


class SoccerTeam(models.Model):
    team = models.ForeignKey(SoccerCountry, models.DO_NOTHING)
    team_group = models.CharField(max_length=1)
    match_played = models.DecimalField(max_digits=65535, decimal_places=65535)
    won = models.DecimalField(max_digits=65535, decimal_places=65535)
    draw = models.DecimalField(max_digits=65535, decimal_places=65535)
    lost = models.DecimalField(max_digits=65535, decimal_places=65535)
    goal_for = models.DecimalField(max_digits=65535, decimal_places=65535)
    goal_agnst = models.DecimalField(max_digits=65535, decimal_places=65535)
    goal_diff = models.DecimalField(max_digits=65535, decimal_places=65535)
    points = models.DecimalField(max_digits=65535, decimal_places=65535)
    group_position = models.DecimalField(max_digits=65535, decimal_places=65535)

    class Meta:
        managed = False
        db_table = 'soccer_team'


class SoccerVenue(models.Model):
    venue_id = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    venue_name = models.CharField(max_length=30)
    city = models.ForeignKey(SoccerCity, models.DO_NOTHING)
    aud_capacity = models.DecimalField(max_digits=65535, decimal_places=65535)

    class Meta:
        managed = False
        db_table = 'soccer_venue'


class Statements(models.Model):
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'statements'


class Stay(models.Model):
    stayid = models.IntegerField(primary_key=True)
    patient = models.ForeignKey(Patient, models.DO_NOTHING, db_column='patient')
    room = models.ForeignKey(Room, models.DO_NOTHING, db_column='room')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'stay'


class String(models.Model):
    text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'string'


class Student(models.Model):
    roll = models.IntegerField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'


class Student1(models.Model):
    roll = models.IntegerField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student1'


class Suppliers(models.Model):
    supplierid = models.SmallIntegerField(primary_key=True)
    companyname = models.CharField(max_length=40)
    contactname = models.CharField(max_length=30, blank=True, null=True)
    contacttitle = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=60, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)
    region = models.CharField(max_length=15, blank=True, null=True)
    postalcode = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=15, blank=True, null=True)
    phone = models.CharField(max_length=24, blank=True, null=True)
    fax = models.CharField(max_length=24, blank=True, null=True)
    homepage = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'suppliers'


class Sybba(models.Model):
    ord_num = models.DecimalField(unique=True, max_digits=6, decimal_places=0)
    ord_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    ord_date = models.DateField()
    cust_code = models.CharField(max_length=6)
    agent_code = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'sybba'


class T1(models.Model):
    customer_id = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    cust_name = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)
    grade = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    salesman_id = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't1'


class Tab2(models.Model):
    city = models.CharField(max_length=15, blank=True, null=True)
    customer_id = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tab2'


class Table1(models.Model):
    customer_name = models.CharField(db_column='Customer Name', max_length=30, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    city = models.CharField(max_length=15, blank=True, null=True)
    salesman = models.CharField(db_column='Salesman', max_length=30, blank=True, null=True)  # Field name made lowercase.
    commission = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'table1'


class TeamCoaches(models.Model):
    team = models.ForeignKey(SoccerCountry, models.DO_NOTHING)
    coach = models.ForeignKey(CoachMast, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'team_coaches'


class Temp(models.Model):
    customer_id = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    cust_name = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)
    grade = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    salesman_id = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp'


class TempArray(models.Model):
    min = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp_array'


class TempReviewer(models.Model):
    rev_id = models.IntegerField(blank=True, null=True)
    rev_name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp_reviewer'


class TempSamesman(models.Model):
    salesman_id = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)
    commission = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp_samesman'


class TempTable(models.Model):
    customer_id = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    max = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp_table'


class Tempa(models.Model):
    customer_id = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    cust_name = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)
    grade = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    salesman_id = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tempa'


class Tempcustomer(models.Model):
    customer_id = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    cust_name = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)
    grade = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    salesman_id = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tempcustomer'


class Temphi(models.Model):
    salesman_id = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)
    commission = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temphi'


class Tempp(models.Model):
    customer_id = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    cust_name = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)
    grade = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    salesman_id = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tempp'


class Tempp11(models.Model):
    customer_id = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    cust_name = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)
    grade = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    salesman_id = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tempp11'


class Tempsalesman(models.Model):
    salesman_id = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)
    commission = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tempsalesman'


class Territories(models.Model):
    territoryid = models.CharField(primary_key=True, max_length=20)
    territorydescription = models.CharField()
    regionid = models.ForeignKey(Region, models.DO_NOTHING, db_column='regionid')

    class Meta:
        managed = False
        db_table = 'territories'


class Test(models.Model):
    x = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test'


class Teste(models.Model):
    salesman_id = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    count = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teste'


class Testtable(models.Model):
    col1 = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'testtable'
        db_table_comment = 'a temporary table for some queries '


class TrainedIn(models.Model):
    physician = models.OneToOneField(Physician, models.DO_NOTHING, db_column='physician', primary_key=True)  # The composite primary key (physician, treatment) found, that is not supported. The first column is selected.
    treatment = models.ForeignKey(Procedure, models.DO_NOTHING, db_column='treatment')
    certificationdate = models.DateField()
    certificationexpires = models.DateField()

    class Meta:
        managed = False
        db_table = 'trained_in'
        unique_together = (('physician', 'treatment'),)


class Trenta(models.Model):
    numeri = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trenta'


class Tt(models.Model):
    name = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tt'


class Undergoes(models.Model):
    patient = models.OneToOneField(Patient, models.DO_NOTHING, db_column='patient', primary_key=True)  # The composite primary key (patient, procedure, stay, date) found, that is not supported. The first column is selected.
    procedure = models.ForeignKey(Procedure, models.DO_NOTHING, db_column='procedure')
    stay = models.ForeignKey(Stay, models.DO_NOTHING, db_column='stay')
    date = models.DateTimeField()
    physician = models.ForeignKey(Physician, models.DO_NOTHING, db_column='physician')
    assistingnurse = models.ForeignKey(Nurse, models.DO_NOTHING, db_column='assistingnurse', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'undergoes'
        unique_together = (('patient', 'procedure', 'stay', 'date'),)


class Usstates(models.Model):
    stateid = models.SmallIntegerField()
    statename = models.CharField(max_length=100, blank=True, null=True)
    stateabbr = models.CharField(max_length=2, blank=True, null=True)
    stateregion = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usstates'


class Vowl(models.Model):
    cust_name = models.CharField(max_length=30, blank=True, null=True)
    substring = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vowl'


class Zebras(models.Model):
    id = models.IntegerField(primary_key=True)
    score = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zebras'


class Zz(models.Model):
    customer_id = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    avg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zz'
