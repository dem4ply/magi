from rest_framework import status, viewsets
from rest_framework.response import Response

#__all__ = [ 'Test' ]

class Test( viewsets.ViewSet ):

    def create( self, request, format=None ):
        import pdb
        pdb.set_trace()
        return Response( status=status.HTTP_204_NO_CONTENT )
