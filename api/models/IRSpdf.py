from django.db import models

class IRSpdf(models.Model):
    form_number = models.TextField()
    form_title =  models.TextField()
    min_year = models.IntegerField()
    max_year = models.IntegerField()

    def __str__(self):
        return f"The form named '{self.form_title}' is a '{self.form_number}' first downloadable from '{self.min_year}' to '{self.max_year}'."

    def as_dict(self):
        return {
        'form_number': self.form_number,
        'form_title': self.form_title,
        'min_year': self.min_year,
        'max_year': self.max_year
        }
