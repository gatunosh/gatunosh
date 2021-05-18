# -*- coding:utf-8 -*-
from odoo import http
from odoo.http import request

class MultiWeb(http.Controller):
        
    @http.route('/usa',auth='public',website=True)
    def website_usa_awa(self):
        return request.render('website.homepage',{
            'city': 'New York', 
            'country_code': 'US', 
            'country_name': 'United States', 
            'region': 'NY', 
            'time_zone': 'America/New_York'
        })
        
    @http.route('/ecuador',auth='public',website=True)
    def website_ecua_awa(self):
        return request.render('website.homepage',{
            'city': 'Quito', 
            'country_code': 'EC', 
            'country_name': 'Ecuador', 
            'region': 'P', 
            'time_zone': 'America/Guayaquil'
        })