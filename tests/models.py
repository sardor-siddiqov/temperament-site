from django.db import models


class Question(models.Model):
    TEMPERAMENT_CHOICES = [
        ('Sangvinik', 'Sangvinik'),
        ('Xolerik', 'Xolerik'),
        ('Flegmatik', 'Flegmatik'),
        ('Melanxolik', 'Melanxolik'),
    ]

    question_number = models.PositiveSmallIntegerField(unique=True)
    text = models.TextField()
    temperament = models.CharField(max_length=20, choices=TEMPERAMENT_CHOICES)

    class Meta:
        ordering = ['question_number']

    def __str__(self):
        return f"{self.question_number}. {self.text}"


class AnswerOption(models.Model):
    text = models.CharField(max_length=50)
    score = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.text} ({self.score})"


class TestResult(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    sangvinik_score = models.PositiveSmallIntegerField(default=0)
    xolerik_score = models.PositiveSmallIntegerField(default=0)
    flegmatik_score = models.PositiveSmallIntegerField(default=0)
    melanxolik_score = models.PositiveSmallIntegerField(default=0)
    dominant_temperament = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name or 'Anonim'} - {self.dominant_temperament}"
