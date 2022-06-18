To run on windows, run celery with the command below:
`celery -A django_redis_celery worker -l info -P threads`

or

`celery -A django_redis_celery beat -l info -pool==solo`