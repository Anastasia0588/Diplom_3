# Diplom_3
## Задание 3: веб-приложение
UI тесты для веб-приложения [Stellar Burgers](https://stellarburgers.nomoreparties.site/)

### Структура проекта:
tests - тесты  
locators - хранение локаторов  
pages - методы для взаимодействия со страницами и описание шагов  
urls.py - используемые ссылки  
requirements.txt - файл с внешними зависимостями



### Запустить тесты
запустить все тесты:
```bash
pytest -v tests
```
зпустить все тесты с генерацией отчетов  
```bash
pytest tests --alluredir=allure_results 
```
сгенерировать отчет
```bash
allure serve allure_results
```