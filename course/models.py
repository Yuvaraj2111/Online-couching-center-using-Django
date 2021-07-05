from django.db import models
from django_cassandra_engine.models import DjangoCassandraModel
from cassandra.cqlengine import columns
import uuid
# Create your models here.

class Subject(DjangoCassandraModel):
	id=columns.UUID(primary_key=True,default=uuid.uuid4)
	name=columns.Text(max_length=30)
	description=columns.Text(max_length=1000)
	content=columns.Text(max_length=1000)
	video=columns.Text(max_length=100) 
	pdf=columns.Text(max_length=100)

class User_account(DjangoCassandraModel):
    name=columns.Text(max_length=20)
    user=columns.Text(primary_key=True,max_length=30)
    email=columns.Text(max_length=30) 
    phone=columns.Text(max_length=10)   
    password=columns.Text(max_length=30)
    
class Enroll(DjangoCassandraModel):
	id=columns.UUID(primary_key=True,default=uuid.uuid4)
	user=columns.Text(max_length=30)
	subject=columns.Text(max_length=30)    
