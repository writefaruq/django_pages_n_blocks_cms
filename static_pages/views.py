from django.shortcuts import render_to_response
from static_pages.models import StaticPage, PageBlock


class CommonView():
    static_pages = StaticPage.objects.all()
    page_blocks = PageBlock.objects.all()


def home_view(request):
    v = CommonView()
    return render_to_response("home.html", {
                              'static_pages': v.static_pages,
                              'page_blocks': v.page_blocks,
                              })


def page_view(request, page_name):
    v = CommonView()
    page_title = request.path.split('/')[-1]
    return render_to_response("page.html", {
                              'static_pages': v.static_pages,
                              'page_highlights': v.page_blocks.filter(category = 'highlight'), # see model
                              'page_contents': v.page_blocks.filter(category = 'content'),
                              'right_highlights': v.page_blocks.filter(category = 'right'),
                              'page_title': page_title,
                              })
