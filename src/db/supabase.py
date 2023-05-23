import supabase

SUPABASE_URL = 'https://xeudcfxkwzjnmbjlyorr.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InhldWRjZnhrd3pqbm1iamx5b3JyIiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODQ0MDYxNDcsImV4cCI6MTk5OTk4MjE0N30.9G3UQp_QKsfXTTMlI8jVYudqeTFyHyrzhlkhsNHT6Ok'

supabase = supabase.Client(SUPABASE_URL, SUPABASE_KEY)
