from odoo import api, models
from datetime import datetime
import pytz
from pytz import timezone
import logging

class ReportOrdenTrabajo(models.AbstractModel):
    _name = 'report.kraken.reporte_orden_trabajo'

    def hora_actual(self):
        hora = False
        timezone = pytz.timezone(self._context.get('tz') or self.env.user.tz or 'UTC')
        fecha_hora_actual = datetime.now(timezone)
        hora = fecha_hora_actual.strftime("%H:%M:%S")
        return hora

    @api.model
    def _get_report_values(self, docids, data=None):
        model = 'sale.order'
        docs = self.env[model].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': model,
            'docs': docs,
            'hora_actual': self.hora_actual,
        }
