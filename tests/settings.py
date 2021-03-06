import environ


env = environ.Env()


DEBUG = True
DATABASES = {"default": env.db(default="sqlite://:memory:")}
ROOT_URLCONF = "tests.urls"
SECRET_KEY = "not-for-production"
INSTALLED_APPS = [
    "tests.app_a",
    "tests.app_b",
    "tests.app_c",
    "tests.app_d",
    "tests.basic",
    "tests.generic",
    "tests.inheritance",
    "tests.installed",
    "tests.proxy",
    "schema_graph",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
TEMPLATES = (
    {"BACKEND": "django.template.backends.django.DjangoTemplates", "APP_DIRS": True},
)
STATIC_URL = "/static/"
