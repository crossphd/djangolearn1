"""
Customizations for the Django administration interface.
"""

from django.contrib import admin
from app.models import Choice, Poll, Stock, Portfolio

#class ChoiceInline(admin.TabularInline):
#    """Choice objects can be edited inline in the Poll editor."""
#    model = Choice
#    extra = 3

#class PollAdmin(admin.ModelAdmin):
#    """Definition of the Poll editor."""
#    fieldsets = [
#        (None, {'fields': ['text']}),
#        ('Date information', {'fields': ['pub_date']}),
#    ]
#    inlines = [ChoiceInline]
#    list_display = ('text', 'pub_date')
#    list_filter = ['pub_date']
#    search_fields = ['text']
#    date_hierarchy = 'pub_date'

#admin.site.register(Poll, PollAdmin)


class StockInline(admin.TabularInline):
    """Choice objects can be edited inline in the Poll editor."""
    model = Stock
    extra = 3

class PortfolioAdmin(admin.ModelAdmin):
    """Definition of the Poll editor."""
    fieldsets = [
        (None, {'fields': ['text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [StockInline]
    list_display = ('text', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['text']
    date_hierarchy = 'pub_date'

admin.site.register(Portfolio, PortfolioAdmin)