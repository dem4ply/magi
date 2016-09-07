import factory
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

def name_for_retrive( namespace, name_pre, sub ):
    return "{}:{}-{}".format( namespace, name_pre, sub )

class Test_basic_api( APITestCase ):
    namespace = ''
    name_pre_function = ''
    factory_class = None
    content_type = 'json'
    model_class = None

    def test_create( self, data=None ):
        name_url = name_for_retrive( self.namespace, self.name_pre_function,
                                     'list' )
        url = reverse( name_url )
        if data is None:
            data = factory.build( dict, FACTORY_CLASS=self.factory_class )
        response = self.client.post( url, data )
        self.assertIn( response.status_code, ( status.HTTP_201_CREATED,
                                               status.HTTP_200_OK ),
                       ( "the status code should be 200 or 201 instead of {}"
                         "\ndata:{}" ).format( response.status_code,
                                               response.data ) )

    def test_retrieve( self ):
        data = factory.build( dict, FACTORY_CLASS=self.factory_class )
        self.test_create( data )
        model = self.model_class( **data )
        pk = model.build_id()
        name_url = name_for_retrive( self.namespace, self.name_pre_function,
                                     'detail' )
        url = reverse( name_url,
                       kwargs={
                           'pk': pk
                       } )
        response = self.client.get( url, pk=pk )
        self.assertEqual( response.status_code, status.HTTP_200_OK,
                          ( "the status code should be 200 instead "
                            "of {}\ndata:{}" ).format( response.status_code,
                                                       response.data ) )

    def test_retrieve_not_found( self, pk="NOT_EXIST"):
        name_url = name_for_retrive( self.namespace, self.name_pre_function,
                                     'detail' )
        url = reverse( name_url,
                       kwargs={
                           'pk': pk
                       } )
        response = self.client.get( url, pk=pk )
        self.assertEqual( response.status_code, status.HTTP_404_NOT_FOUND,
                          ( "the status code should be 404 instead "
                            "of {}\ndata:{}" ).format( response.status_code,
                                                       response.data ) )

    def test_delete( self ):
        data = factory.build( dict, FACTORY_CLASS=self.factory_class)
        self.test_create( data )
        model = self.model_class( **data )
        pk = model.build_id()
        name_url = name_for_retrive( self.namespace, self.name_pre_function,
                                     'detail' )
        url = reverse( name_url,
                       kwargs={
                           'pk': pk
                       } )
        response = self.client.delete( url, pk=pk )
        self.assertEqual( response.status_code, status.HTTP_204_NO_CONTENT,
                          ( "the status code should be 204 instead "
                            "of {}\ndata:{}" ).format( response.status_code,
                                                       response.data ) )
        self.test_retrieve_not_found( pk )

    def test_create_many( self, data=None ):
        name_url = name_for_retrive( self.namespace, self.name_pre_function,
                                     'list' )
        url = reverse( name_url )
        data = factory.create_batch( dict, 20, FACTORY_CLASS=self.factory_class)
        response = self.client.post( url, data )
        self.assertIn( response.status_code, ( status.HTTP_201_CREATED,
                                               status.HTTP_200_OK ),
                       ( "the status code should be 200 or 201 instead of {}"
                         "\ndata:{}" ).format( response.status_code,
                                               response.data ) )
        created = response.data[ 'created' ]
        self.assertEqual( created, 20)
