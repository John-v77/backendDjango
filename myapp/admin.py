from django.contrib import admin
from .models import Feature, Post, Room, Message
# Register your models here.
admin.site.register(Feature)
admin.site.register(Post)
admin.site.register(Room)
admin.site.register(Message)