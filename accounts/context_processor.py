# myapp/context_processors.py
import os
from django.conf import settings

# myapp/context_processors.py
def versioned_static(request):
     version = 'v1.1' # Increment this version number
     return {
          'STATIC_VERSION': version,
 }