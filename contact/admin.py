from django.contrib import admin
from .models import Contact
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    
    fields = ['first_name', 'last_name', 'email', 'message_subject', 'message']

    search_fields = ['first_name', 'last_name', 'email', 'message_subject', 'message']

    list_filter = ['first_name', 'last_name', 'email', 'message_subject', 'message',]

    list_display = ['first_name', 'last_name', 'email', 'message_subject', 'message']

    # list_editable = ['match_result']



admin.site.register(Contact, ContactAdmin)

