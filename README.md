# temperament_site

Python + Django + Django REST Framework asosidagi temperament test backend loyihasi.

## Qo‘llab-quvvatlanadigan endpointlar

- `GET /api/questions/` - barcha 20 savolni olish
- `POST /api/submit-test/` - test javoblarini yuborish va natijani hisoblash
- `GET /api/results/` - test natijalarini ko‘rish

## Boshqaruv komandalar

1. `python -m pip install -r requirements.txt`
2. `python manage.py makemigrations`
3. `python manage.py migrate`
4. `python manage.py load_initial_data`
5. `python manage.py runserver`
