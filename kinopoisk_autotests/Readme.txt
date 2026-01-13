# Kinopoisk Autotests

## Описание
Проект автоматизирует UI- и API-тесты для сайта Kinopoisk на основе финальной работы по ручному тестированию.

## Структура проекта
- `test/` — тесты (UI и API)
- `pages/` — Page Object классы
- `configs/` — конфиги и тестовые данные
- `requirements.txt` — зависимости
- `README.md` — инструкция и описание проекта

## Установка
1. Клонировать репозиторий:
   git clone <URL>
2. Перейти в папку проекта:
   cd kinopoisk_autotests
3. Создать виртуальное окружение:
   python -m venv venv
4. Активировать окружение:
   venv\Scripts\activate
5. Установить зависимости:
   pip install -r requirements.txt

## Запуск тестов
- Запуск всех UI-тестов:
  pytest -m ui -v
- Запуск всех API-тестов:
  pytest -m api -v
- Запуск всех тестов:
  pytest -v

## Ссылка на финальный проект по ручному тестированию
https://denis2005.yonote.ru/doc/finalnyj-proekt-po-ruchnomu-testirovaniyu-kinopoisk-yBABl8KFv7
