from django.conf import settings

def global_template_vars(request):
    return settings.SITE_SETTINGS