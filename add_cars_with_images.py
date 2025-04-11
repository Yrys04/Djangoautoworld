import os
import django
from django.core.files import File

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoautoworld.settings')
django.setup()

from cars.models import Car

Car.objects.filter(image__isnull=True).delete()  

# Путь к папке с изображениями (замени на свой)
IMAGE_DIR = os.path.join(os.path.dirname(__file__), 'cars', 'car_images')

Car.objects.filter(image__isnull=True).delete()

cars_data = [
    {'name': 'Lexus ES300h', 'price': 35000, 'year': 2023, 'engine': '2.5 Hybrid', 'color': 'Белый', 'discount': 5, 'image': 'lexus_es300h.jpg'},
    {'name': 'Audi S7', 'price': 85000, 'year': 2022, 'engine': '4.0 V8', 'color': 'Черный', 'discount': 0, 'image': 'audi_s7.jpg'},
    {'name': 'Toyota Camry 70', 'price': 30000, 'year': 2023, 'engine': '2.5 л', 'color': 'Серебро', 'discount': 10, 'image': 'camry 70.jpg'},
    {'name': 'BMW M5 F90', 'price': 95000, 'year': 2021, 'engine': '4.4 V8', 'color': 'Синий', 'discount': 7, 'image': 'm5.jpg'},
    {'name': 'Li 9', 'price': 55000, 'year': 2023, 'engine': 'Electric', 'color': 'Красный', 'discount': 0, 'image': 'li 9.jpg'},
    {'name': 'Mercedes S-Class', 'price': 110000, 'year': 2022, 'engine': '3.0 л', 'color': 'Черный', 'discount': 8, 'image': 's class.jpg'},
    {'name': 'Toyota RAV4', 'price': 32000, 'year': 2023, 'engine': '2.5 л', 'color': 'Серый', 'discount': 0, 'image': 'rav4.jpg'},
    {'name': 'Honda CR-V', 'price': 31000, 'year': 2022, 'engine': '1.5 Turbo', 'color': 'Белый', 'discount': 5, 'image': 'cr v.jpg'},
    {'name': 'Ford Mustang', 'price': 45000, 'year': 2021, 'engine': '5.0 V8', 'color': 'Синий', 'discount': 10, 'image': 'mustang.jpg'},
    {'name': 'Chevrolet Camaro', 'price': 48000, 'year': 2022, 'engine': '6.2 V8', 'color': 'Желтый', 'discount': 0, 'image': 'camaro.jpg'},
    {'name': 'BMW X5', 'price': 45000, 'year': 2022, 'engine': '3.0 л', 'color': 'Белый', 'discount': 0, 'image': 'x5.jpg'},
    {'name': 'Audi Q7', 'price': 42500, 'year': 2021, 'engine': '3.0 disel', 'color': 'Белый', 'discount': 10, 'image': 'q7.jpg'},
    {'name': 'Mercedes GLE', 'price': 50000, 'year': 2023, 'engine': '2.0 л', 'color': 'Белый', 'discount': 5, 'image': 'gle.jpg'},
]

for car in cars_data:
    image_path = os.path.join(IMAGE_DIR, car.pop('image'))  # Удаляем 'image' из словаря
    car_obj, created = Car.objects.get_or_create(
        name=car['name'],
        defaults=car
    )
    
    if created and os.path.exists(image_path):
        with open(image_path, 'rb') as f:
            car_obj.image.save(os.path.basename(image_path), File(f))
        print(f"Добавлен: {car_obj.name} (Изображение: {car_obj.image})")
    else:
        print(f"Машина уже существует: {car_obj.name}")
        