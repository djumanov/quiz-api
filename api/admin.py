from django.contrib import admin
from .models import (
    Quiz,
    Question,
    Option,
)

admin.site.register([Question, Quiz, Option])
