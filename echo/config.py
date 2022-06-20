import logging.config

TG_TOKEN = "5260089448:AAGsd6iYsyLdeLLJB22RlO-HIOinX-oLqK0"

# Логирование
LOGGING = {
    'disable_existing_loggers': True,
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(module)s.%(funcName)s | %(asctime)s | %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}
logging.config.dictConfig(LOGGING)
