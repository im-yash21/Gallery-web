# Owned by Yash Jangid 
# github_id = im-yash21
# leetcode_id = im-yash21
# linkeldn_id = im-yash21 

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'galleryapp.settings')

application = get_wsgi_application()
