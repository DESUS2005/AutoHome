from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 14", "+79100000001"),
    Smartphone("Samsung", "Galaxy S21", "+79200000002"),
    Smartphone("Huawei", "P40", "+79300000003"),
    Smartphone("Xiaomi", "Mi 11", "+79400000004"),
    Smartphone("Nokia", "G50", "+79500000005"),
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.number}")
