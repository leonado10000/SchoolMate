from django.contrib import admin
from .models import Student, Teacher


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "student_id",
        "roll_number",
        "name",
        "batch",
        "school",
        "contact_number",
    )

    list_filter = (
        "school",
        "batch",
    )

    search_fields = (
        "student_id",
        "name",
        "fathers_name",
        "contact_number",
    )

    ordering = ("roll_number",)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("teacher_id", "name")
    search_fields = ("teacher_id", "name")