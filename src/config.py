class Config:
    SECRET_KEY = 'no_c'

class DevelopmentConfig(Config):
    DEBUG = True
    SUPABASE_URL = 'https://xeudcfxkwzjnmbjlyorr.supabase.co'
    SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InhldWRjZnhrd3pqbm1iamx5b3JyIiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODQ0MDYxNDcsImV4cCI6MTk5OTk4MjE0N30.9G3UQp_QKsfXTTMlI8jVYudqeTFyHyrzhlkhsNHT6Ok'

config = {
    'development': DevelopmentConfig
}