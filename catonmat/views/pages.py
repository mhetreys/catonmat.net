#!/usr/bin/python
#
# Peteris Krumins (peter@catonmat.net)
# http://www.catonmat.net  --  good coders code, great reuse
#
# The new catonmat.net website. See this post for more info:
# http://www.catonmat.net/blog/50-ideas-for-the-new-catonmat-website/
#
# Code is licensed under GNU GPL license.
#

from catonmat.views.utils import render_template_with_quote
from catonmat.quotes      import get_random_quote

def main(request, map):
    template_data = {
        'page':      map.page,
        'page_path': map.request_path
    }
    map.page.content = map.page.content.replace("\r\n\r\n", "<p>")
    map.page.content = ""
    map.page.title = ""
    return render_template_with_quote("page", template_data)
