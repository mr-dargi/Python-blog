from django.contrib import admin, messages
from django.utils.translation import ngettext
from .models import Article, Category, IPAddress

# Register your models here.
@admin.action(description="انتشار مقالات انتخاب شده")
def make_published(modeladmin, request, queryset):
  updated = queryset.update(status="p")
  modeladmin.message_user(
    request,
    ngettext(
        "%d مقاله منتشر شد",
        "%d تا از مقاله ها منتشر شدند",
        updated,
    )
    % updated,
    messages.SUCCESS,
)
  

@admin.action(description="پیش نویس مقالات انتخاب شده")
def make_draft(modeladmin, request, queryset):
  queryset.update(status="d")
    

class CategoryAdmin(admin.ModelAdmin):
  list_display = (
    "position",
    "title",
    "parent",
    "slug",
    "status"
  )
  
  list_filter = (
    ["status"]
  )
  
  search_fields = (
    "title",
    "slug"
  )
  
  prepopulated_fields = {"slug": ("title",)}


admin.site.register(Category, CategoryAdmin)


class ArticleAdmin(admin.ModelAdmin):
  list_display = (
    "title",
    "thumbnail_tag",
    "slug",
    "author",
    "jpublish",
    "is_special",
    "status",
    "category_to_str"
  )
  
  list_filter = (
    "publish",
    "status",
    "author"
  )
  
  search_fields = (
    "title",
    "description"
  )
  
  prepopulated_fields = {"slug": ("title",)}
  ordering = [ "-status", "-publish" ]
  actions = [make_published, make_draft]
  

admin.site.register(Article, ArticleAdmin)
admin.site.register(IPAddress)