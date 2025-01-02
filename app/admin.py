from django.contrib import admin
from .models import Post
from .models import Resident
from .models import BarangayOfficials
from .models import Requests
from .models import Announcements
from .models import EmergencyHotlines







admin.site.register(EmergencyHotlines)
admin.site.register(Requests)
admin.site.register(Post)
admin.site.register(Resident)
admin.site.register( BarangayOfficials)
admin.site.register(Announcements)