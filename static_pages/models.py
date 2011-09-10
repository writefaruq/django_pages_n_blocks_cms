from django.db import models
from django.contrib import admin


class StaticPage(models.Model):
    """
    # Static pages for top menu and footer
    Menus should be generated using these pages.
    """
    # Menu order choices
    MENU_ORDER_CHOICES = tuple(
		zip(range(1,7), ('First', 'Second', 'Third', 'Fourth', 'Fifth', 'Sixth', 'Seventh'))
    )
    title = models.CharField( max_length=150)
    flash_file = models.FileField(upload_to='images/', blank=True, null=True)
    position_in_menu = models.PositiveIntegerField(choices=MENU_ORDER_CHOICES)
    active = models.BooleanField()
    homepage = models.BooleanField(blank=True)

    
    class Meta:
        ordering = ('position_in_menu' , )

    def __unicode__(self):
        return self.title


class PageBlock(models.Model):
    """
    Each page consits of different kinds of blocks
    """

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

    # visible attributes
    headline = models.CharField(max_length=150)
    short_description = models.TextField()
    more_link = models.URLField(null=True, blank=True, verify_exists=False)
    image = models.FileField(upload_to='images/test_etc/', blank=True)
    # positional attributes
    target_page = models.ForeignKey(StaticPage, null=True, blank=True )
    active = models.BooleanField() # can be used to show/hide
    priority = models.CharField(max_length=1, choices=HIGHLIGHT_PRIORITY, blank=True) # for ordering
    size = models.CharField(max_length=1, choices=BLOCK_SIZE, blank=True) # for css dispaly
    category = models.CharField(max_length=15, choices=BLOCK_CATEGORY, blank=True) # for positioning


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
