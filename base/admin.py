from pyexpat import model
from django.contrib import admin
from .models import Hotel, ImageHotel, Forfait
from django.utils.html import format_html

# Register your models here.
class ImageHotelInline(admin.TabularInline):
    model = ImageHotel
    extra = 0

class ForfaitIline(admin.TabularInline):
    model = Forfait
    extra = 0



@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):

    

    list_display = ('cover','name','contact','contact2', 'lng','lat')

    list_display_links = ('name',)

    @admin.display(description='couverture')
    def cover (self, obj):
        return format_html(f"<img src={obj.cover} />")
    
    @admin.display(description='second contact', empty_value="aucun")
    def contact2(self, obj):
        return format_html(f"<b>{obj.contact2}</b>")

    list_filter = ('forfaits__type','forfaits__prix',)

    search_fields = ('name', 'longitude','latitude','localisation')

    

    
    fieldsets = (
        (None, {
            'fields':('name','cover','contact','contact2', 'lng','lat')
        }),
        (
            'localisation',
            {
                'fields':('place','localisation')
            }
        ),
        ('Extra',{
            'classes':('collapse',),
            'fields':('wifi','climatisation','piscine','parking')
        })
    )
    
    inlines = [ImageHotelInline, ForfaitIline]



