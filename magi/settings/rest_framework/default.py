REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    #'DEFAULT_AUTHENTICATION_CLASSES': [
        #'users.authentication.Token_keys_authentication',
        #'rest_framework.authentication.BasicAuthentication',
        #'rest_framework.authentication.SessionAuthentication',
    #],
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework_xml.renderers.XMLRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework_xml.parsers.XMLParser',
    ),
    'DEFAULT_CONTENT_NEGOTIATION_CLASS': 'rest_framework.negotiation.DefaultContentNegotiation',
    #'EXCEPTION_HANDLER': 'magi.exceptions.generic_exception_handler',
    'NON_FIELD_ERRORS_KEY': 'detail',
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.AcceptHeaderVersioning',
    'DEFAULT_VERSION': 'Sakura',
    'ALLOWED_VERSIONS': ( 'Sakura', ),
    'VERSION_PARAM': 'issue',
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
}
