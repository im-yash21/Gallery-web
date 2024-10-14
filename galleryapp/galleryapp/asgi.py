# Owned by Yash Jangid 
# github_id = im-yash21
# leetcode_id = im-yash21
# linkeldn_id = im-yash21 

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'galleryapp.settings')

application = get_asgi_application()
