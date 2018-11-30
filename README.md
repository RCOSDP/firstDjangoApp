

## 環境構築

git clone https://github.com/RCOSDP/firstDjangoApp.git
cd firstDjangoApp/
pip install django==1.11
pip install coverage
pip install django-nose

## テスト実行

coverage run manage.py test
python manage.py test

## DB作成

python manage.py migrate

## アプリ実行

python manage.py runserver
