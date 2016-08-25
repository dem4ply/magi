from elasticsearch_dsl import Index

default_settings = {
    'number_of_shards': 2,
    'number_of_replicas': 1,
}

crunchyroll_news_es_mx = Index( 'crunchyroll_news_es-MX' )

crunchyroll_news_es_mx.settings( **default_settings )

__all__ = [ 'default_settings', 'crunchyroll_news_es_mx' ]
