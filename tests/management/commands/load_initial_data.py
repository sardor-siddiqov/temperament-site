from django.core.management.base import BaseCommand
from tests.models import AnswerOption, Question


class Command(BaseCommand):
    help = 'Barcha savollar va javob variantlarini bazaga yuklaydi.'

    def handle(self, *args, **options):
        questions = [
            (1, 'Men yangi odamlar bilan tez chiqishib ketaman', 'Sangvinik'),
            (2, 'Men tez jahlim chiqadi', 'Xolerik'),
            (3, 'Men ko‘pincha tinch va sokin bo‘lishni afzal ko‘raman', 'Flegmatik'),
            (4, 'Men tez xafa bo‘lib qolaman', 'Melanxolik'),
            (5, 'Men doimo faol va energiyaga to‘laman', 'Sangvinik'),
            (6, 'Men qarorlarni tez qabul qilaman', 'Xolerik'),
            (7, 'Men sabrli odamman', 'Flegmatik'),
            (8, 'Men ko‘pincha ichimda o‘ylab yuraman', 'Melanxolik'),
            (9, 'Men davralarda bo‘lishni yoqtiraman', 'Sangvinik'),
            (10, 'Men tez asabiylashaman', 'Xolerik'),
            (11, 'Men barqaror va o‘zgarmas kayfiyatdaman', 'Flegmatik'),
            (12, 'Men ko‘p narsadan xavotirlanaman', 'Melanxolik'),
            (13, 'Men kulishni va hazil qilishni yaxshi ko‘raman', 'Sangvinik'),
            (14, 'Men boshqalarga tez buyruq beraman', 'Xolerik'),
            (15, 'Men mojarolardan qochaman', 'Flegmatik'),
            (16, 'Men o‘zimni tez aybdor his qilaman', 'Melanxolik'),
            (17, 'Men tez moslashuvchanman', 'Sangvinik'),
            (18, 'Men ba’zida agressiv bo‘lib qolaman', 'Xolerik'),
            (19, 'Men sekin, lekin aniq ishlayman', 'Flegmatik'),
            (20, 'Men ko‘pincha yolg‘iz qolishni xohlayman', 'Melanxolik'),
        ]

        for number, text, temperament in questions:
            Question.objects.update_or_create(
                question_number=number,
                defaults={
                    'text': text,
                    'temperament': temperament,
                },
            )

        answer_options = [
            ('Ha', 2),
            ('Ba’zan', 1),
            ('Yo‘q', 0),
        ]

        for text, score in answer_options:
            AnswerOption.objects.update_or_create(text=text, defaults={'score': score})

        self.stdout.write(self.style.SUCCESS('Baza uchun 20 ta savol va javob variantlari yuklandi.'))
