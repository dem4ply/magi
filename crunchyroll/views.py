import logging

from rest_framework import viewsets


logger = logging.getLogger( __name__ )

class Article( viewsets.ViewSet ):
    def create( self, request, format=None ):
        pass
