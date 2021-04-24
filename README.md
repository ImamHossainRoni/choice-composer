## Choice-composer:
It will help you to make choice filed in Django or anywhere in python script according to your choices :smiley:

## Installation
```pip install choice-composer```

## How to use it?
```python:
from choice_composer import Choice
# Write a class by extending Choice:
class UserRole(Choice):  
	ADMIN = 1  
	NORMAL_USER = 2  
	CLIENT = 3
# Let's see the how we can use it in django model:
class UserProfile(models.Model):  
	#......
	role = models.PositiveIntegerField(choices=UserRole.choices(), default=UserRole.NORMAL_USER)
	# If you want to get exact name of role then you can use property method by the following way:
	@property
	def user_role(self):
		return UserRole(self.role).name.title() 
```
***  If you want to filter data by specific role then you can use the following way:
```python:
def role_wise_users(role=UserRole.CLIENT):
	# It returns all the client users from UserProfile model.
	users = UserProfile.objects.filter(role=role)
	return users
```

## License

© 2021 Imam Hossain Roni

This repository is licensed under the MIT license. See LICENSE for details.