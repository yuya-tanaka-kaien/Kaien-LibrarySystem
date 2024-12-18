from django import forms

# 図書貸出画面のフォーム
class RentBookForm(forms.Form):
    student_id = forms.IntegerField(label="生徒ID")
    book_id = forms.IntegerField(label="図書ID")

# 図書返却画面のフォーム
class ReturnBookForm(forms.Form):
    book_id = forms.IntegerField(label="図書ID")