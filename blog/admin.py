from django.contrib import admin

from blog.models import Post

class BlogAdmin(admin.ModelAdmin):
    
    exclude = ('author',)
    
    
    def get_queryset(self, request):
        qs = super(BlogAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(author=request.user)
    
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
            obj.save()
    

admin.site.register(Post, BlogAdmin)
