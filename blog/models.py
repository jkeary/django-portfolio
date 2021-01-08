from django.db import models

# create blog model
# title 
# pub date
# body
# image
class Blog(models.Model):
    title = models.CharField(max_length=250)
    pub_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

# add blog app to settings

# create migration

# migrate

# add to admin