from odoo import api, models
import logging

class ReportOrdenTrabajo(models.AbstractModel):
    _name = 'report.kraken.reporte_orden_trabajo'

    @api.model
    def _get_report_values(self, docids, data=None):
        # model = 'sale.order'
        # logging.warning('test')
        # docs = self.env[model].browse(docids)

        model = 'sale.order'
        docs = self.env[model].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': model,
            'docs': docs,
        }
