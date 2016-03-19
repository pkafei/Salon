from django.contrib import admin
from .models import Post

#http://www.djangobook.com/en/2.0/chapter06.html

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'published_date' )
	list_filter = ('published_date',)
	date_hierarchy = 'published_date'
	ordering = ('-published_date',)

admin.site.register(Post, PostAdmin)

