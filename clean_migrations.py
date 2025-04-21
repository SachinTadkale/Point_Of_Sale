import os
import shutil

def clean_migrations():
    # List of apps to clean migrations
    apps = ['authentication', 'products', 'reports', 'sales']
    
    # Remove database
    if os.path.exists('db.sqlite3'):
        try:
            os.remove('db.sqlite3')
            print("Removed db.sqlite3")
        except Exception as e:
            print(f"Could not remove database: {e}")
    
    # Remove migration files and __pycache__
    for app in apps:
        migrations_dir = os.path.join(app, 'migrations')
        if os.path.exists(migrations_dir):
            # Remove __pycache__ directory
            pycache_dir = os.path.join(migrations_dir, '__pycache__')
            if os.path.exists(pycache_dir):
                try:
                    shutil.rmtree(pycache_dir)
                    print(f"Removed {pycache_dir}")
                except Exception as e:
                    print(f"Could not remove {pycache_dir}: {e}")
            
            # Remove all migration files except __init__.py
            for filename in os.listdir(migrations_dir):
                if filename != '__init__.py':
                    file_path = os.path.join(migrations_dir, filename)
                    try:
                        if os.path.isfile(file_path):
                            os.remove(file_path)
                            print(f"Removed {file_path}")
                    except Exception as e:
                        print(f"Could not remove {file_path}: {e}")
            
            # Create empty __init__.py if it doesn't exist
            init_file = os.path.join(migrations_dir, '__init__.py')
            if not os.path.exists(init_file):
                with open(init_file, 'w') as f:
                    pass
                print(f"Created {init_file}")

if __name__ == '__main__':
    clean_migrations() 