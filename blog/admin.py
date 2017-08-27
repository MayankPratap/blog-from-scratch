from django.contrib import admin

# We import(include) the Post model defined in the previous chapter.

from .models import Post

# To make our model visible on admin page, we need to register the model with admin.site.register(Post).

admin.site.register(Post)


