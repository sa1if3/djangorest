from django.contrib import admin
from .models import Quote
# Register your models here.
@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
	list_display = ("author", "quote")