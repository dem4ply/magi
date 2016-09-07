from facebook_app.models import Credential

def get_credential_test():
    return Credential.objects.get( facebook_id='110738792683813' )
