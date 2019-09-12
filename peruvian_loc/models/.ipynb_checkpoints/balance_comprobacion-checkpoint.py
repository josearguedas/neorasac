# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from odoo.tools.sql import drop_view_if_exists

import datetime

class BalanceComprobacion(models.Model):
    _name = "balance.comprobacion"
    _description = "Balance de Comprobacion"
    _auto = False

    account_period = fields.Char(size=6)
    code = fields.Char()
    name = fields.Char()
    debit_init = fields.Float()
    credit_init = fields.Float()
    debit = fields.Float()
    credit = fields.Float()
        
    @api.model_cr
    def init(self):
       drop_view_if_exists(self.env.cr,self._table)
       self._cr.execute('''
             create or replace view 
             balance_comprobacion as (
                    
                select a.account_period, 
                       aa.code, 
                       aa.name, 
                       SUM(b.debit) debit_init, 
                       SUM(b.credit) credit_init, 
                       a.debit, 
                       a.credit 
                from account_sum a
                     inner join account_account aa
                          on (a.account_id = aa.id)
                     left join account_sum b
                          on (a.account_id = b.account_id AND b.account_period < a.account_period)
                group by a.account_period, 
                         aa.code, 
                         aa.name, 
                         a.debit, 
                         a.credit
             )
        ''')
