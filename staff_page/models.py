from django.db import models
from django.utils import timezone

# 図書データのモデル
class Book(models.Model):
    book_id = models.IntegerField(primary_key=True, null=False, blank=False)
    book_title = models.CharField(max_length=200, null=False, blank=False)
    book_register_date = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 該当する図書の貸出データを取得する
    def get_rent_status(self):
        return BookRentStatus.objects.filter(is_book_returned=False).filter(target_book=self)

    # 該当する図書は貸し出し可能か？
    def can_rent(self):
        rent_status = self.get_rent_status()
        if rent_status:
            return False
        return True

    # 該当する図書を貸し出している生徒を取得
    def get_rented_student(self):
        rent_status = self.get_rent_status()
        if rent_status:
            return rent_status.first().book_rent_student
        return None
    
    # 該当する図書の貸し出し期限を取得
    def get_return_deadline(self):
        rent_status = self.get_rent_status()
        if rent_status:
            return rent_status.first().book_return_deadline
        return None
    
    # 該当する図書の貸し出し期限が期限切れかどうかを取得する
    def is_deadline_expired(self):
        rent_status = self.get_rent_status()
        if rent_status:
            return rent_status.first().is_deadline_expired()
        return False
    
    # __str__は本のタイトルを取得する
    def __str__(self):
        return self.book_title

# 生徒データのモデル
class Student(models.Model):
    student_id = models.IntegerField(primary_key=True, null=False, blank=False)
    student_name = models.CharField(max_length=100, null=False, blank=False)
    student_email = models.EmailField(null=True, blank=True)
    student_joined_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 生徒の現在の貸出状況を取得する
    def get_rent_status(self):
        return BookRentStatus.objects.filter(is_book_returned=False).filter(book_rent_student=self)
    
    # 生徒が現在借りている図書の期限を取得
    def get_return_deadline(self):
        rent_status = self.get_rent_status()
        if rent_status:
            return rent_status.first().book_return_deadline
        return None

    # 生徒が現在借りている図書データを取得
    def get_rented_book(self):
        rent_status = self.get_rent_status()
        if rent_status:
            return rent_status.first().target_book
        return None
    
    # 生徒は図書を借りているか？
    def is_rented_book(self):
        return self.get_rented_book() != None

    # 生徒の借りている図書は返却期限を過ぎているか？
    def is_deadline_expired(self):
        rent_status = self.get_rent_status()
        if rent_status:
            return rent_status.first().is_deadline_expired()

    # __str__は生徒の名前を返す
    def __str__(self):
        return self.student_name

# 図書貸出状況のモデル
class BookRentStatus(models.Model):
    book_rent_student = models.ForeignKey(Student, on_delete=models.CASCADE)
    target_book = models.ForeignKey(Book, on_delete=models.CASCADE)
    is_book_returned = models.BooleanField(default=False)
    book_returned_date = models.DateField(null=True, blank=True)
    book_return_deadline = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # その図書は貸し出し期限切れか?
    def is_deadline_expired(self):
        return self.book_return_deadline < timezone.now().date()