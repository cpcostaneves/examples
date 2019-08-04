from django.db import models

# Create your models here.

class Person(models.Model):
    PERSON_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 128, db_index = True)
    email = models.EmailField(blank = True)
    location = models.CharField("Verbose Location Title", max_length = 20, blank = True)
    add_date = models.DateField(blank = True)
    num_stars = models.IntegerField(blank = True)
    sizes = models.CharField(max_length = 1, blank = True, choices = PERSON_SIZES)
    #extrainfo = models.ForeignKey(ExtraInfo, on_delete=models.CASCADE)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.location == "Forbidden location":
            return
        else:
            #do_something()
            super().save(*args, **kwargs)  # Call the "real" save() method.
            #do_something_else()

    def add_status(self):
        import datetime
        if self.add_date < datetime.date(2000, 1, 1):
            return "Long time added"
        else:
            return "New one"

# ForeignKey - One to one
class ExtraInfo(models.Model):
    category = models.IntegerField()

# ForeignKey One to many
class Orders(models.Model):
    number = models.IntegerField()
    user = models.ForeignKey(Person, on_delete=models.CASCADE)


# ManyToManyField + through
class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):
        return self.name

class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)


# OneToOne - extends
class PersonExtended(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE, primary_key=True, )
    moreinfo = models.CharField(max_length=128)


# Query examples
def queries():

    # Create with save
    person1 = Person(name='Person 1', add_date=date(2008, 8, 16))
    person1.save()

    # Create - single step
    person2 = Person.objects.create(name="Person Name 2", add_date=date(2008, 8, 16))

    # Retrieve
    person1ret = Person.objects.get(name='Person 1')
    print(person1ret.name)

    # Update
    person1upd = Person.objects.get(name='Person 1')
    person1upd.name = 'New name'
    person1upd.save()

    # Delete
    person1del = Person.objects.get(name='Person 1')
    person1del.delete()

    #Person.objects.get(pk=1)
    
    # Queries

    # Get all
    all_entries = Person.objects.all()


    # Retrieving a single object with get()

    #Filters



# Query Relationships
def queries_relations():

    # Create
    person1 = Person.objects.create(name="Person Name 1")
    person2 = Person.objects.create(name="Person Name 2")
    person3 = Person.objects.create(name="Person Name 3")

    group = Group.objects.create(name="Group of persons")

    # Create Association
    m1 = Membership(person=person1, group=group, date_joined=date(2008, 8, 16),
                    invite_reason="Needed a new member.")
    m1.save()

    Membership.objects.create(person=person2, group=group, date_joined=date(2008, 8, 17),
                                invite_reason="Needed a new member.")

    
    # Add an existing member
    group.members.add(person3, through_defaults={'date_joined': date(2008, 8, 18)})

    # Create and add member
    group.members.create(name="Person Name 4", through_defaults={'date_joined': date(2008, 8, 19)})

    # Remove member
    group.members.remove(person2)


    # Sets members
    group.members.set([person1, person2], through_defaults={'date_joined': date(2008, 8, 16)})


    # Clear members
    group.members.clear()


    # Get results

    # Get all members
    group.members.all()
    
    # Get a membership's info using Membership
    person1_membership = Membership.objects.get(group=group, person=person1)
    #person1_membership.date_joined

    # Get a membership's info using person
    person1_membership = person1.membership_set.get(group=group)
    
    # Find all the groups with a member whose name starts with 'Paul'
    Group.objects.filter(members__name__startswith='Paul')

    # Find all the members that joined after 1 Jan 2008
    Person.objects.filter(group__name='Group of persons', membership__date_joined__gt=date(2008,1,1))


