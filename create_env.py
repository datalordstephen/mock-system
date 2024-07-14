# creates a .env file with a secret key and a database URI
import os
import secrets

def generate_secret_key():
    return secrets.token_hex(16)

def generate_database_uri():
    basedir = os.path.abspath(os.path.dirname(__file__))
    db_path = os.path.join(basedir, 'app.db')
    # Convert Windows paths to URI format
    if os.name == 'nt':
        db_path = db_path.replace('\\', '/')
    
    return f'sqlite:///{db_path}'

def create_env_file():
    secret_key = generate_secret_key()
    database_uri = generate_database_uri()

    env_content = "SECRET_KEY={}\nDATABASE_URL={}".format(secret_key, database_uri)

    with open('.env', 'w') as env_file:
        env_file.write(env_content)

    print(".env file created successfully")

if __name__ == "__main__":
    create_env_file()
