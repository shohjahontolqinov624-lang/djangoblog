from django.db import models

class Bloglar(models.Model):
    title = models.CharField(max_length=255, verbose_name="Sarlavhasi")
    shortdesc = models.CharField(max_length=255, verbose_name="Qisqacha ma'lumot")
    longdesc = models.TextField(verbose_name="To'liq ma'lumot")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Bloglar"