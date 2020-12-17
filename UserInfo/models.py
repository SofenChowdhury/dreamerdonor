from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django.utils.timezone import now
import datetime
import uuid
# Create your models here.

Role = (
    ('Dreamer', 'Dreamer'),
    ('Donor', 'Donor'),
)
class UserInfo(models.Model):

	user_id 		= models.ForeignKey(User,on_delete=models.CASCADE)
	phone 			= models.CharField(max_length=15,blank=True,null=True)
	country 		= models.CharField(max_length=100,blank=True,null=True)
	address 		= models.TextField(blank=True, null=True)
	image 			= models.ImageField(upload_to='assets/uploads/user',blank=True, null=True)
	role            = models.CharField(blank=True,choices=Role,max_length=20, default='Dreamer')
	user_code 		= models.CharField(max_length=100,blank=True,unique=True, default=uuid.uuid4)
	join_date       = models.DateField(default=datetime.date.today,blank=True)

	def __str__(self):
		return self.user_id.username