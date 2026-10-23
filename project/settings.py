from pathlib import Path
SECRET_KEY = 'django-insecure-m#$v8(9v7g^6d5s4f3a2z1x0c9v8b7n6m5l4k3j2h1g0f9d8s7'

# Построение путей внутри проекта
BASE_DIR = Path(__file__).resolve().parent.parent

# Режим отладки (обязательно True для локальной разработки)
DEBUG = True

# Разрешенные хосты для локального запуска
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Обязательные модули для flatpages
    'django.contrib.sites',
    'django.contrib.flatpages',
]

SITE_ID = 1

# Блок MIDDLEWARE для работы админки и авторизации
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Папка для шаблонов
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # Важно для доступа к объекту user!
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Настройка базы данных по умолчанию (SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Настройки статических файлов

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]