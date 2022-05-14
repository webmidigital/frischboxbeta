from django.contrib import admin


# Models Registrations

from .models import Packages
from .models import our_cities
from .models import Bulk_orders
from .models import Post
from .models import Policies
from .models import Statelist
from .models import General_enquiries
from .models import sliderimages






# Admin Table Show


admin.site.register(Packages)
admin.site.register(Policies)
admin.site.register(our_cities)
admin.site.register(Bulk_orders)
admin.site.register(Post)
admin.site.register(Statelist)
admin.site.register(General_enquiries)
admin.site.register(sliderimages)



