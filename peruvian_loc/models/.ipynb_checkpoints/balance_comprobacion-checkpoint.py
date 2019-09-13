# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from odoo.tools.sql import drop_view_if_exists

import datetime

class BalanceComprobacion(models.Model):
    _name = "balance.comprobacion"
    _description = "Balance de Comprobacion"
    _auto = False

    id = fields.Char()
    account_period = fields.Char(size=6)
    code = fields.Char()
    name = fields.Char()
    debit_init = fields.Float()
    credit_init = fields.Float()
    debit = fields.Float()
    credit = fields.Float()
    debit_fin = fields.Float()
    credit_fin = fields.Float()
    debit_bg_fin = fields.Float()
    credit_bg_fin = fields.Float()
    debit_eg_fin = fields.Float()
    credit_eg_fin = fields.Float()
    debit_na_fin = fields.Float()
    credit_na_fin = fields.Float()
        
    @api.model_cr
    def init(self):
       drop_view_if_exists(self.env.cr,self._table)
       self._cr.execute('''
             create or replace view 
             balance_comprobacion as (

                select a.acc_id as id,
                       a.account_period, 
                       aa.code, 
                       aa.name, 
                       coalesce(SUM(b.debit),0) debit_init, 
                       coalesce(SUM(b.credit),0) credit_init, 
                       a.debit, 
                       a.credit,
                       case when (coalesce(SUM(b.debit),0) + a.debit) - (coalesce(SUM(b.credit),0) + a.credit) > 0 
                            then (coalesce(SUM(b.debit),0) + a.debit) - (coalesce(SUM(b.credit),0) + a.credit)
                            else 0
                       end debit_fin,
                       case when (coalesce(SUM(b.credit),0) + a.credit) - (coalesce(SUM(b.debit),0) + a.debit) > 0 
                            then (coalesce(SUM(b.credit),0) + a.credit) - (coalesce(SUM(b.debit),0) + a.debit)
                            else 0
                       end credit_fin,
                       case when (aa.code <= '599999') and ((coalesce(SUM(b.debit),0) + a.debit) - (coalesce(SUM(b.credit),0) + a.credit) > 0) 
                            then (coalesce(SUM(b.debit),0) + a.debit) - (coalesce(SUM(b.credit),0) + a.credit)
                            else 0
                       end debit_bg_fin,
                       case when (aa.code <= '599999') and ((coalesce(SUM(b.credit),0) + a.credit) - (coalesce(SUM(b.debit),0) + a.debit) > 0) 
                            then (coalesce(SUM(b.credit),0) + a.credit) - (coalesce(SUM(b.debit),0) + a.debit)
                            else 0
                       end credit_bg_fin,
                       case when (aa.code >= '700000') and ((coalesce(SUM(b.debit),0) + a.debit) - (coalesce(SUM(b.credit),0) + a.credit) > 0) 
                            then (coalesce(SUM(b.debit),0) + a.debit) - (coalesce(SUM(b.credit),0) + a.credit)
                            else 0
                       end debit_eg_fin,
                       case when (aa.code >= '700000') and ((coalesce(SUM(b.credit),0) + a.credit) - (coalesce(SUM(b.debit),0) + a.debit) > 0) 
                            then (coalesce(SUM(b.credit),0) + a.credit) - (coalesce(SUM(b.debit),0) + a.debit)
                            else 0
                       end credit_eg_fin,
                       case when (aa.code >= '600000' and aa.code <= '699999') and ((coalesce(SUM(b.debit),0) + a.debit) - (coalesce(SUM(b.credit),0) + a.credit) > 0) 
                            then (coalesce(SUM(b.debit),0) + a.debit) - (coalesce(SUM(b.credit),0) + a.credit)
                            else 0
                       end debit_na_fin,
                       case when (aa.code >= '600000' and aa.code <= '699999') and ((coalesce(SUM(b.credit),0) + a.credit) - (coalesce(SUM(b.debit),0) + a.debit) > 0) 
                            then (coalesce(SUM(b.credit),0) + a.credit) - (coalesce(SUM(b.debit),0) + a.debit)
                            else 0
                       end credit_na_fin
                from account_acum a
                     inner join account_account aa
                          on (a.account_id = aa.id)
                     left join account_acum b
                          on (a.account_id = b.account_id AND b.account_period < a.account_period)
                group by a.acc_id,
                         a.account_period, 
                         aa.code, 
                         aa.name, 
                         a.debit, 
                         a.credit
                order by aa.code
             )
        ''')
