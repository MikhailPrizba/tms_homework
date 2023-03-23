class Config:
    ...


class Development(Config):
    DEBUG_MODE = True
    DB_HOST = 'localhost:5432'

