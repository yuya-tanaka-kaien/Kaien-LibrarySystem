from django.contrib import admin
from .models import Book, Student, BookRentStatus

# 図書データのAdminモデル
class BookAdmin(admin.ModelAdmin):
    list_display = ["book_id", "book_title", "book_register_date"]
    list_display_links = ["book_id", "book_title"]

# 生徒データのAdminモデル
class StudentAdmin(admin.ModelAdmin):
    list_display = ["student_id", "student_name", "student_joined_date"]
    list_display_links = ["student_id", "student_name"]

# 図書貸出データのAdminモデル
class BookRentStatusAdmin(admin.ModelAdmin):
    list_display = ["id", "target_book", "book_rent_student", "is_book_returned", "book_return_deadline"]
    list_display_links = ["id"]

# DjangoAdminに各モデルを登録
admin.site.register(Book, BookAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(BookRentStatus, BookRentStatusAdmin)