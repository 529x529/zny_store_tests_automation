# Автоматизация бизнес пути интернет магазина
https://znyworldwide.com/ 


## How to use
* Установите [актуальную](https://chromedriver.chromium.org/downloads) версию ChromeDriver для вашего Chrome
* Создайте виртуальное окружение и активируйте его:
```shell script
~ python3 -m venv env && source env/bin/activate
```
* Обновите pip до последней версии:
```shell script
~ pip install --upgrade pip
```
* Установите зависимости:
```shell script
~ pip install -r requirements.txt
```
* Запустите тесты:
```shell script
~  python3 -m pytest --alluredir=test_results/ 
```
* Для просмотра отчета Allure:
```shell script
~  allure serve test_results/  

```
