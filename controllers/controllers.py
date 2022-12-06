# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json


class StaffControl(http.Controller):
    @http.route('/staff/get_all_alerts', auth='user', type='json')
    def all_alerts(self, **kw):
        alert_rec = http.request.env['tools_control.tools_control'].sudo().search([])
        alerts = []
        for rec in alert_rec:
            alerts.append({
                'action': rec.action,
                'date': rec.date,
                'area': rec.area,
                'photo': rec.photo,
            })

        return alerts

    @http.route('/staff/create_alert', auth='user', type='json')
    def create(self, **rec):
        if http.request.render:
            if rec['action']:
                vals = {
                    'action': rec['action'],
                    'date': rec['date'],
                    'area': rec['area'],
                    'photo': rec['photo'],
                }
                new_alert = request.env['tools_control.tools_control'].sudo().create(vals)
                args = {'success': True, 'message': 'Success', 'id': new_alert.id}
        return args

    @http.route('/staff/ping', type='json', auth='public')
    def ping(self):
        return {'success': True}
