from settings import create_app

app, celery = create_app()
app.app_context().push()
