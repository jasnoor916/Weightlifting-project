from django.contrib import admin
from .models import Sports, Players, Matches, Bookings


class SportsAdmin(admin.ModelAdmin):
    search_fields = ['name']  
    list_filter = ['name'] 
    list_display = ['id', 'name', 'description']  


class PlayersAdmin(admin.ModelAdmin):
    search_fields = ['name'] 
    list_filter = ['sport']  
    list_display = ['id', 'name', 'sport']  


class MatchesAdmin(admin.ModelAdmin):
    search_fields = ['venue', 'date']  
    list_filter = ['date', 'venue']  
    list_display = ['id', 'sport', 'date', 'venue']  


class BookingsAdmin(admin.ModelAdmin):
    search_fields = ['user_name', 'booking_date']  
    list_filter = ['booking_date']  
    list_display = ['id', 'match', 'user_name', 'booking_date']  


admin.site.register(Sports, SportsAdmin)
admin.site.register(Players, PlayersAdmin)
admin.site.register(Matches, MatchesAdmin)
admin.site.register(Bookings, BookingsAdmin)