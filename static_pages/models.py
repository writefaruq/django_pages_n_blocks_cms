from django.db import models
from django.contrib import admin

# Menu order choices
MENU_ORDER_CHOICES = (
    (1, 'First'),
    (2, 'Second'),
    (3, 'Third'),
    (4, 'Fouth'),
    (5, 'Fifth'),
    (6, 'Sixth'),
    (7, 'Seventh'),
    (8, 'Eighth'),
    (9, 'Ninth'),
    (10, 'Tenth'),
)

# Static pages for top menu and footer
class StaticPage(models.Model):
    title = models.CharField( max_length=150)
    flash_file = models.FileField(upload_to='images/', blank=True, null=True)
    #in_topmenu = models.BooleanField()
    #in_footer = models.BooleanField()
    position_in_menu = models.PositiveIntegerField(choices=MENU_ORDER_CHOICES)
    active = models.BooleanField()
    homepage = models.BooleanField(blank=True)

    
    class Meta:
        ordering = ('position_in_menu' , )

    def __unicode__(self):
        return self.title



HIGHLIGHT_PRIORITY = (
    ('1', "High"),
    ('2', "Medium"),
    ('3', "Low"),
)

BLOCK_SIZE = (
    ('1', "Large"), # full or 75% width
    ('2', "Medium"), # 33% width
    ('3', "Small"), # page submenu
    ('4', "Mini"), # page submenu
)

BLOCK_CATEGORY = (
    ('highlight', "Highlight"),
    ('content', "PageContent"),
    ('left', "LeftSidebar"),
    ('right', "RightSidebar"), 
)

class PageBlock(models.Model):
    # visible attributes
    headline = models.CharField(max_length=150)
    short_description = models.TextField()
    more_link = models.URLField(null=True, blank=True)
    image = models.FileField(upload_to='images/test_etc/', blank=True)
    # positional attributes
    target_page = models.ForeignKey(StaticPage, null=True, blank=True )
    active = models.BooleanField()
    priority = models.CharField(max_length=1, choices=HIGHLIGHT_PRIORITY, blank=True)
    size = models.CharField(max_length=1, choices=BLOCK_SIZE, blank=True)
    category = models.CharField(max_length=15, choices=BLOCK_CATEGORY, blank=True)


    def __unicode__(self):
        return self.headline


class PageBlockAdmin(admin.ModelAdmin):

    list_display = ('headline', 'target_page', 'active', 'more_link', 'priority', 'category')

class PageContent(PageBlock):
    long_description = models.TextField()

    def __unicode__(self):
        return self.headline

class PageContentAdmin(admin.ModelAdmin):

    list_display = ('headline', 'target_page', 'active', 'more_link', 'priority', 'category')

admin.site.register(StaticPage)
admin.site.register(PageBlock, PageBlockAdmin)
admin.site.register(PageContent, PageContentAdmin )
