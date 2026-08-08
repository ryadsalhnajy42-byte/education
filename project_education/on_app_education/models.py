from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200)              # عنوان الدورة
    description = models.TextField()                      # وصف مختصر
    duration = models.CharField(max_length=50)            # مدة الدورة (مثال: "4 أسابيع")
    price = models.DecimalField(max_digits=8, decimal_places=2)  # سعر الدورة
    created_at = models.DateTimeField(auto_now_add=True)  # تاريخ الإضافة
    updated_at = models.DateTimeField(auto_now=True)      # تاريخ آخر تعديل

    def __str__(self):
        return self.title