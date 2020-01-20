# Social network API
Simple DRF application with JWT. Uses sqlite intentionally to make this work
 checking more simple

## Install

1) clone or download the repo
2) init your virtual env
3) install packages
4) run `python manage.py migrate`
5) make superuser with `python manage.py createsuperuser` and type the stuff

## Check
1) make sure you have set all the values filled on `bot_rules.ini`
2) run management command `python manage.py fill_data_with_api`
