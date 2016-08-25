from elasticsearch_dsl import analyzer, tokenizer, token_filter


spanish_stemmer = token_filter( 'spanish_stemmer', type='stemmer',
                                language='light_spanish' )

spanish_stop= token_filter( 'spanish_stop', type='stop',
                            stopwords='_spanish_' )

spanish_analizer = analyzer( 'spanish', tokenizer=tokenizer( 'standard' ),
                             filter=[ 'lowercase', 'asciifolding',
                                      spanish_stop, spanish_stemmer ] )

__all__ = [ 'spanish_analizer', 'spanish_stemmer', 'spanish_stop' ]
