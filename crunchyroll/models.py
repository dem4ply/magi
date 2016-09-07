from elasticsearch_dsl import DocType, String, Date, InnerObjectWrapper, Nested
from .index import crunchyroll_news_es_mx
from .analizers import spanish_analizer


#@crunchyroll_news_es_mx.doc_type
class Videos( InnerObjectWrapper ):
    pass
    #link = String( index='not_analyzed', store=True )


#@crunchyroll_news_es_mx.doc_type
class Tags( InnerObjectWrapper ):
    pass
    #link = String( index='not_analyzed', store=True )
    #title = String( index='analyzed', store=True )


@crunchyroll_news_es_mx.doc_type
class Articles( DocType ):
    link = String( index='not_analyzed', store=True )
    source = String( index='not_analyzed', store=True )
    title = String( index='analyzed', store=True,
                    analyzer=spanish_analizer )
    date = Date( store=True )
    content = String( index='analyzed', store=True,
                      analyzer=spanish_analizer )
    Videos = Nested( doc_class=Videos,
        properties={
            'link': String( index='not_analyzed', store=True ),
        } )
    tags = Nested( doc_class=Tags,
        properties={
            'link': String( index='not_analyzed', store=True ),
            'title': String( index='analyzed', store=True ),
        } )
