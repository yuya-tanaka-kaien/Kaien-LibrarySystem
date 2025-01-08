from django.urls import path
from . import views

app_name = "staff_page"
urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("rent/", views.rent_book, name="rent_book"),
    path("return/", views.return_book, name="return_book"),
    path("books/", views.book_list, name="book_list"),
    path("books/<int:book_id>/", views.book_detail, name="book_detail"),
    path("students/", views.student_list, name="student_list"),
    path("students/<int:student_id>/", views.student_detail, name="student_detail"),
]