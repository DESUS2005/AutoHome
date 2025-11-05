from address import Address
from mailing import Mailing

to_addr = Address("123456", "Москва", "Ленинградский проспект", "10A", "101")
from_addr = Address("654321", "Санкт-Петербург", "Невский проспект", "20",
                    "202")
mailing = Mailing(to_addr, from_addr, 250, "TRK1234567890")

print(
    f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, "
    f"{mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} "
    f"в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, "
    f"{mailing.to_address.house} - {mailing.to_address.apartment}. "
    f"Стоимость {mailing.cost} рублей."
)
