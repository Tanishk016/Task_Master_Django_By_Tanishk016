from django.contrib import admin
from .models import Task
from simple_history.admin import SimpleHistoryAdmin

# 1. Register the Main Task (Active stuff)
admin.site.register(Task, SimpleHistoryAdmin)

# 2. Register the Shadow Table (Deleted/Old stuff) 🕵️‍♂️
# This adds a "Historical Tasks" section to your Admin Panel
admin.site.register(Task.history.model)