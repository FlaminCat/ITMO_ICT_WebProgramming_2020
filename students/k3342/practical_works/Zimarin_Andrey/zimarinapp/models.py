from django.db import models

# Create your models here.


class Car(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    number = models.CharField(max_length=6)

    def __str__(self):
        return self.number


class Owner(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    birthday = models.DateField(blank=True, null=True)
    owns = models.ManyToManyField(Car, through='Owning')

    def __str__(self):
        return self.name


class License(models.Model):
    TYPE = (('A', 'Bike'),
            ('B', 'Light Rigid'),
            ('C', 'Medium Rigid'),
            ('D', 'Heavy Rigid'),
            ('E', 'Heavy Combination'))

    license_id = models.PositiveIntegerField()
    date = models.DateField(blank=True, null=True)
    type = models.CharField(max_length=5, choices=TYPE)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.owner}'


class Owning(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_started = models.DateField(blank=True, null=True)
    date_ended = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.owner} owns a car with number {self.car}'
