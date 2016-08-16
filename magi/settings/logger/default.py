import os
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'logstash': {
            'level': 'DEBUG',
            'class': 'logstash.LogstashHandler',
            'host': 'Ai',
            'port': 5400,
            'version': 1,
            'message_type': 'logstash',
            'fqdn': False,
            'tags': [ 'magi' ],
        },
        'logstash_exceptions': {
            'level': 'INFO',
            'class': 'logstash.LogstashHandler',
            'host': 'localhost',
            'port': 5400,
            'version': 1,
            'message_type': 'logstash',
            'fqdn': False,
            'tags': [ 'magi', 'django_exception_unhandled' ],
        },
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(name)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(name)s %(message)s'
        },
    },
    'loggers': {
        '': {
            'handlers': [ 'console' ],
            'level': os.getenv( 'DJANGO_LOG_LEVEL', 'INFO' ),
        },
        'django': {
            'handlers': [ 'console' ],
            'level': os.getenv( 'DJANGO_LOG_LEVEL', 'INFO' ),
        },
        'django.request': {
            'handlers': [ 'logstash_exceptions' ],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}
