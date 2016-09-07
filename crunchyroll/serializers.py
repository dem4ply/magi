import logging

from rest_framework import serializers


logger = logging.getLogger( __name__ )


class Video_list( serializers.ListSerializer ):
    def validate( self, data ):
        if data and isinstance( data[0], str ):
            data = [ { 'link': l } for l in data ]
        return super().validate( data )


class Video( serializers.Serializer ):
    link = serializers.CharField()

    class Meta:
        list_serializer_class = Campaign_list


class Tag( serializers.Serializer ):
    link = serializers.CharField()
    name = serializers.CharField()


class Article( serializers.Serializer ):
    content = serializers.CharField()
    date    = serializers.DateTimeField()
    link    = serializers.URLField()
    source  = serializers.URLField()
    title   = serializers.CharField()
    videos  = Video( many=True )
    tags    = Tag( many=True )
