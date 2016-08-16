from elasticsearch_dsl.connections import connections

connections.configure(
    default={
        'hosts': 'waifus:80',
        'sniff_on_start': True,
        'timeout': 30,
    },
)
