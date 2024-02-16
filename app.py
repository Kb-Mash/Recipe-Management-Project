#!/usr/bin/env python3
# create an application
from recipe_website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True) # to-do - False for production
