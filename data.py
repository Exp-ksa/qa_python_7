import random
from faker import Faker
from datetime import datetime, timedelta

class DataCourier:
    courier_id = random.randint(100000000, 999999999)

class DataOrder:
    order =[{
    
    "firstName": "Яна",
    "lastName": "Павлова",
    "address": "Москва, пр. Коммунаров, д. 7",
    "metroStation": 214,
    "phone": "83211234567",
    "rentTime": 7,
    "deliveryDate": "2026-06-20",
    "comment": "Вход со двора, второй подъезд",
    "color": ['BLACK','GREY']
    }, 
    {
    
    "firstName": "Яна",
    "lastName": "Павлова",
    "address": "Москва, пр. Коммунаров, д. 7",
    "metroStation": 214,
    "phone": "83211234567",
    "rentTime": 7,
    "deliveryDate": "2026-06-20",
    "comment": "Вход со двора, второй подъезд",
    "color": ['GREY']
    },
    {
    
    "firstName": "Яна",
    "lastName": "Павлова",
    "address": "Москва, пр. Коммунаров, д. 7",
    "metroStation": 214,
    "phone": "83211234567",
    "rentTime": 7,
    "deliveryDate": "2026-06-20",
    "comment": "Вход со двора, второй подъезд",
    "color": ['Black']
    },
    {
    "firstName": "Яна",
    "lastName": "Павлова",
    "address": "Москва, пр. Коммунаров, д. 7",
    "metroStation": 214,
    "phone": "83211234567",
    "rentTime": 7,
    "deliveryDate": "2026-06-20",
    "comment": "Вход со двора, второй подъезд",
    "color": []
    }
    ] 