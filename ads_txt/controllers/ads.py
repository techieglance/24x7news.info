from odoo import http
from odoo.http import request
import os

class AdsTxtController(http.Controller):

    @http.route(['/ads.txt'], type='http', auth='public', website=True, csrf=False)
    def ads_txt(self, **kwargs):
        content = "google.com, pub-1859259158173471, DIRECT, f08c47fec0942fa0"
        return request.make_response(content, headers=[
            ('Content-Type', 'text/plain'),
        ])
