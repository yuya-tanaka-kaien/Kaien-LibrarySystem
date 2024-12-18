from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Book, Student, BookRentStatus
from .forms import RentBookForm, ReturnBookForm
from django.utils import timezone as tz

is_login = True

# ログイン画面
def login(request):
    if request.method == "POST":
        global is_login
        is_login = True
        return redirect(reverse("staff_page:index"))
    return render(request, "staff_page/login.html", {})

# ログアウト処理
def logout(request):
    global is_login
    is_login = False
    return redirect(reverse("staff_page:login"))

# 図書館システムのトップ画面
def index(request):
    # ログインしていない場合はログイン画面へリダイレクトする
    if is_login == False:
        return redirect(reverse("staff_page:login"))
    
    return render(request, "staff_page/index.html", {})

# 図書館システムの図書貸出画面
def rent_book(request):
    # ログインしていない場合はログイン画面へリダイレクトする
    if is_login == False:
        return redirect(reverse("staff_page:login"))
    
    status = {"info": "", "error": ""}
    form = RentBookForm()
    
    # フォームが送信された際の処理
    if request.method == "POST":
        form = RentBookForm(request.POST)
        if form.is_valid() == False:
            status["error"] = form.non_field_errors()
        else:
            student_id = form.cleaned_data["student_id"]
            book_id = form.cleaned_data["book_id"]
            
            error_msg = _do_rent_book(book_id, student_id, 7)

            if error_msg != "":
                status["error"] = error_msg
            else:
                form = RentBookForm()
                status["info"] = "図書の貸し出しが完了しました"
    
    status["form"] = form

    return render(request, "staff_page/rent.html", status)

# エラー時はエラーメッセージを返す。エラーがない場合は空文字を返す。
def _do_rent_book(target_book_id: int, target_student_id: int, deadline_days: int):
    try:
        target_student = Student.objects.get(pk=target_student_id)
    except Student.DoesNotExist:
        return "ID{}の生徒は存在しません".format(target_student_id)
    
    try:
        target_book = Book.objects.get(pk=target_book_id)
    except Book.DoesNotExist:
        return "ID{}の本は存在しません".format(target_book_id)

    if target_book.can_rent() == False:
        return "その図書は貸し出し中です"
    if target_student.is_rented_book():
        return "その生徒はすでに本を借りています"

    book_rent_status = BookRentStatus()

    book_rent_status.target_book = target_book
    book_rent_status.book_rent_student = target_student
    book_rent_status.book_return_deadline = (tz.now() + tz.timedelta(deadline_days)).date()
    
    book_rent_status.save()

    return ""


def return_book(request):
    # ログインしていない場合はログイン画面へリダイレクトする
    if is_login == False:
        return redirect(reverse("staff_page:login"))
    
    form = ReturnBookForm()

    status = {"info": "", "error": ""}

    if request.method == "POST":
        form = ReturnBookForm(request.POST)
        if form.is_valid() == False:
            status["error"] = form.non_field_errors()
        else:
            target_book_id = form.cleaned_data["book_id"]
            
            error_msg = _do_return_book(target_book_id)

            if error_msg == "":
                status["info"] = "図書の返却が完了しました"
                form = ReturnBookForm()
            else:
                status["error"] = error_msg
    
    status["form"] = form
    
    return render(request, "staff_page/return.html", status)

def _do_return_book(target_book_id: int):
    try:
        target_book = Book.objects.get(pk=target_book_id)
    except Book.DoesNotExist:
        return "ID{}の本は存在しません".format(target_book_id)
    
    try:
        book_rent_status = BookRentStatus.objects.get(target_book=target_book, is_book_returned=False)
    except BookRentStatus.DoesNotExist:
        return "その本は貸し出されていません"
    
    book_rent_status.is_book_returned = True
    book_rent_status.book_returned_date = tz.now().date()
    book_rent_status.save()

    return ""

def book_list(request):
    # ログインしていない場合はログイン画面へリダイレクトする
    if is_login == False:
        return redirect(reverse("staff_page:login"))
    
    books = []
    for book in Book.objects.all():
        rented_student = book.get_rented_student()
        returen_deadline = book.get_return_deadline()
        is_deadline_expired = book.is_deadline_expired()
        books.append({
            "id": book.book_id,
            "title": book.book_title,
            "rent_status": "貸し出し可能" if book.can_rent() else "貸し出し中",
            "rent_student": rented_student if rented_student else "",
            "rent_deadline": returen_deadline if returen_deadline else "",
            "is_deadline_over": "延滞中" if is_deadline_expired else ""
        })
    status = {"books": books}

    return render(request, "staff_page/book_list.html", status)

def student_list(request):
    # ログインしていない場合はログイン画面へリダイレクトする
    if is_login == False:
        return redirect(reverse("staff_page:login"))
    
    students = []

    for student in Student.objects.all():
        rented_book = student.get_rented_book()
        return_deadline = student.get_return_deadline()
        is_deadline_expired = student.is_deadline_expired()
        students.append({
            "id": student.student_id,
            "name": student.student_name,
            "status": "貸し出し中({}まで)".format(return_deadline) if rented_book else "",
            "alert": "延滞中" if is_deadline_expired else ""
        })
    status = {
        "students": students
    }

    return render(request, "staff_page/student_list.html", status)