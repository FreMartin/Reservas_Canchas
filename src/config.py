class Config:
    SECRET_KEY = '1234'

class DevelopmentConfig(Config):
    DEBUG = True
    dbname="dbCancha",
    user="postgres",
    password="ElMartin",
    host="localhost",
    port="5432"

config = {
    'development':DevelopmentConfig()
}