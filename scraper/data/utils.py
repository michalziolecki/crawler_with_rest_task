def include_django_orm():
    import os
    from django.core.wsgi import get_wsgi_application
    os.environ.clear()
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "data.settings")
    get_wsgi_application()
