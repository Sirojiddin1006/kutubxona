from django.contrib import admin
from .models import News,Category,Contact, Category
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title','slug','pulish_time','status')
    list_filter = ('status','status','create_time')
    prepopulated_fields = {'slug':('title',)}
    search_fields = ('title',)
    ordering = ('-pulish_time','status',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)