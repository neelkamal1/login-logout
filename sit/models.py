from django.db import models



class uni(models.Model):
	  cname = models.CharField(max_length=60,null=True)
	  cpera = models.TextField()
	  chname =models.CharField(max_length=60) 
	  chist = models.TextField()
	  achiv = models.CharField(max_length=60)
	  achivhis=models.TextField()
	  depart=models.CharField(max_length=60)
	  departhis=models.TextField()
	  def __str__(self):
	  	return self.cname


