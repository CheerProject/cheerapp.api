from django.contrib.auth.models import User

#INGRESO DE USUARIO
user = User(username='user1')
user.save()
user = User(username='user2')
user.save()
user = User(username='user3')
user.save()
user = User(username='user4')
user.save()

#INGRESO DE INSTITUTION
institution = Institution(name='universitario')
institution.save()
institution = Institution(name='club')
institution.save()
institution = Institution(name='colegial')
institution.save()
institution = Institution(name='independiente')
institution.save()

#INGRESO DE GENDER
gender = Gender(name='all girl')
gender.save()
gender = Gender(name='coed')
gender.save()
gender = Gender(name='all male')
gender.save()
gender = Gender(name='girl')
gender.save()
gender = Gender(name='male')
gender.save()

#INGRESO DE LEVEL
level = Level(name='1')
level.save()
level = Level(name='2')
level.save()
level = Level(name='3')
level.save()
level = Level(name='4')
level.save()
level = Level(name='5')
level.save()
level = Level(name='6')
level.save()
level = Level(name='4.2')
level.save()

#INGRESO DE DIVISION
division = Division(name='baby junior')
division.save()
division = Division(name='mini junior')
division.save()
division = Division(name='junior')
division.save()
division = Division(name='senior')
division.save()
division = Division(name='open')
division.save()
division = Division(name='individual')
division.save()

#INGRESO DE CATEGORY
category = Category(name='flyer')
category.save()
category = Category(name='jumper')
category.save()
category = Category(name='tumbler')
category.save()
category = Category(name='pareja')
category.save()
category = Category(name='trio')
category.save()
category = Category(name='cuarteto')
category.save()
category = Category(name='equipo')
category.save()

#INGRESO DE GROUP
group = Group(name='grupo 1')
group.save()
group = Group(name='grupo 2')
group.save()
group = Group(name='grupo 3')
group.save()
group = Group(name='grupo 4')
group.save()
group = Group(name='grupo 5')
group.save()
group = Group(name='grupo 6')
group.save()
group = Group(name='grupo 7')
group.save()
group = Group(name='grupo 8')
group.save()
group = Group(name='grupo 9')
group.save()

#INGRESO DE ROUND
round = Round(name='1')
round.save()

#INGRESO DE SCORESHEETTYPE
scoresheettype = ScoreSheetType(name='anap 2017')
scoresheettype.save()

#INGRESO DE SCOREMETRIC
scoremetric = ScoreMetric(name='total')
scoremetric.save()

#INGRESO DE LOCATIONTYPE
locationtype = LocationType(name='pais')
locationtype.save()
locationtype = LocationType(name='departamento')
locationtype.save()
locationtype = LocationType(name='ciudad')
locationtype.save()
locationtype = LocationType(name='municipio')
locationtype.save()

#INGRESO DE STATUS
status = Status(name='on time')
status.save()
status = Status(name='delayed')
status.save()
status = Status(name='checked')
status.save()