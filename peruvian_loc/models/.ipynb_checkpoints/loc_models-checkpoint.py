# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = "res.partner"

    x_tipo_persona = fields.Selection([('01','01 - Persona Natural'),('02','02 - Persona Jurídica o Entidad'),
                                       ('03','03 - Sujeto No Domiciliado'),('04','04 - Adquiriente - Ticket')],string='Tipo Persona')
    x_grupo_pago = fields.Selection([('01','Proveedor Operaciones'),
                                     ('02','Proveedor Servicios'),
                                     ('03','Gastos Básicos'),
                                     ('04','EPS'),
                                     ('04','Oracle')
                                    ],string='Grupo de Pago')
    x_tipo_documento_identidad = fields.Selection([('0','0 - Otros Tipos de Documentos'),('1','1 - Documento Nacional de Identidad'),
                                                   ('4','4 - Carnet de Extranjería'),('6','6 - Registro Único de Contribuyentes'),
                                                   ('7','7 - Pasaporte'),('A','A - Cédula Diplomática de Identidad')],
                                                  string='Tipo Documento Identidad')#,required=True)
    x_apellido_paterno = fields.Char(size=80,string='Apellido Paterno')
    x_apellido_materno = fields.Char(size=80,string='Apellido Materno')
    x_nombre = fields.Char(size=80,string='Nombre')
    x_segundo_nombre = fields.Char(size=80,string='Segundo Nombre')
    x_convenios = fields.Selection([('00','00 - Ninguno'),('01','01 - Canada'),('02','02 - Chile'),
                                    ('03','03 - Comunidad Andina de Naciones (CAN)'),('04','04 - Brasil'),
									('05','05 - Estados Unidos Mexicanos'),('06','06 - República de Corea'),
									('07','07 - Confederación Suiza'),('08','08 - Portugal')],string='Convenios')
    x_fecha_nacimiento = fields.Date(string='Fecha Nacimiento')
    x_tipo_doc_no_domiciliado = fields.Selection([('01','01 - TIN - Número de Identificación Tributaria de la PPNN No Domiciliada'),
                                                  ('02','02 - IN - Número de Identificación Tributaria de la PPJJ No Domiciliada'),
												  ('03','03 - Doc. Identificación Local del país de origen - Identifica a la persona No Domiciliada')],
												  string='Tipo Doc. No Domiciliado')
    x_tipo_dir_no_domiciliado = fields.Selection([('01','01 - Coincide con la dirección de residencia y la dirección de actividad'),
	                                              ('02','02 - Coincide con la dirección de residencia'),
												  ('03','03 - Coincide con la dirección de actividad')],
                                                  string='Tipo Dir. No Domiciliado')
    x_nro_certificado_residencia = fields.Char(size=20,string='Nro. Certificado Residencia')
    x_vinculo_contrib_extranjero = fields.Selection([('00','00 - Sin Vinculación'),('01','01 - Articulo 24° numeral 1'),
	                                                 ('02','02 - Articulo 24° numeral 2'),('03','03 - Articulo 24° numeral 3'),
													 ('04','04 - Articulo 24° numeral 4'),('05','05 - Articulo 24° numeral 5'),
													 ('06','06 - Articulo 24° numeral 6'),('07','07 - Articulo 24° numeral 7'),
													 ('08','08 - Articulo 24° numeral 8'),('09','09 - Articulo 24° numeral 9'),
													 ('10','10 - Articulo 24° numeral 10'),('11','11 - Articulo 24° numeral 11'),
													 ('12','12 - Articulo 24° numeral 12')],string='Vínculo Contribuyente/Extranjero')
    x_modalidad_servicio_no_domiciliado = fields.Selection([('01','01 - Servicio Prestado Íntegramente en el Perú'),
	                                                        ('02','02 - Servicio Prestado parte en el Perú y parte en el Extranjero'),
															('03','03 - Servicio Prestado Exclusivamente en el Extranjero')],string='Modalidad Servicio No Domiciliado')

class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    x_tipo_comprobante_pago = fields.Selection([('00','00 - Otros'),('01','01 - Factura'),('02','02 - Recibo por Honorarios'),
	                                            ('03','03 - Boleta de Venta'),('04','04 - Liquidación de Compra'),
												('05','05 - Boletos de Transporte Aéreo que emiten las Compañías de Aviación Comercial por el servicio de transporte aéreo regular de pasajeros, emitido de manera manual, mecanizada o por medios electrónicos (BME)'),
												('06','06 - Carta de porte aéreo por el servicio de transporte de carga aérea'),
												('07','07 - Nota de Crédito'),('08','08 - Nota de Débito'),
												('09','09 - Guía de remisión - Remitente'),('10','10 - Recibo por Arrendamiento'),
												('11','11 - Póliza emitida por las Bolsas de Valores, Bolsas de Productos o Agentes de Intermediación por operaciones realizadas en las Bolsas de Valores o Productos o fuera de las mismas, autorizadas por SMV'),
												('12','12 - Ticket o cinta emitido por máquina registradora'),
												('13','13 - Documentos emitidos por las empresas del sistema financiero y de seguros, y por las cooperativas de ahorro y crédito no autorizadas a captar recursos del público, que se encuentren bajo el control de la Superintendencia de Banca, Seguros y AFP.'),
												('14','14 - Recibo por servicios públicos de suministro de energía eléctrica, agua, teléfono, telex y telegráficos y otros servicios complementarios que se incluyan en el recibo de servicio público'),
												('15','15 - Boletos emitidos por el servicio de transporte terrestre regular urbano de pasajeros y el ferroviario público de pasajeros prestado en vía férrea local.'),
												('16','16 - Boletos de viaje emitidos por las empresas de transporte nacional de pasajeros, siempre que cuenten con la autorización de la autoridad competente, en las rutas autorizadas. Vía terrestre o ferroviario público no emitido por medios electrónicos (BVME)'),
												('17','17 - Documento emitido por la Iglesia Católica por el arrendamiento de bienes inmuebles'),
												('18','18 - Documento emitido por las Administradoras Privadas de Fondo de Pensiones que se encuentran bajo la supervisión de la Superintendencia de Banca, Seguros y AFP'),
												('19','19 - Boleto o entrada por atracciones y espectáculos públicos'),
												('20','20 - Comprobante de Retención'),
												('21','21 - Conocimiento de embarque por el servicio de transporte de carga marítima'),
												('22','22 - Comprobante por Operaciones No Habituales'),
												('23','23 - Pólizas de Adjudicación emitidas con ocasión del remate o adjudicación de bienes por venta forzada, por los martilleros o las entidades que rematen o subasten bienes por cuenta de terceros'),
												('24','24 - Certificado de pago de regalías emitidas por PERUPETRO S.A'),
												('25','25 - Documento de Atribución (Ley del Impuesto General a las Ventas e Impuesto Selectivo al Consumo, Art. 19º, último párrafo, R.S. N° 022-98-SUNAT).'),
												('26','26 - Recibo por el Pago de la Tarifa por Uso de Agua Superficial con fines agrarios y por el pago de la Cuota para la ejecución de una determinada obra o actividad acordada por la Asamblea General de la Comisión de Regantes o Resolución expedida por el Jefe de la Unidad de Aguas y de Riego (Decreto Supremo N° 003-90-AG, Arts. 28 y 48)'),
												('27','27 - Seguro Complementario de Trabajo de Riesgo'),
												('28','28 - Documentos emitidos por los servicios aeroportuarios prestados a favor de los pasajeros, mediante mecanismo de etiquetas autoadhesivas.'),
												('29','29 - Documentos emitidos por la COFOPRI en calidad de oferta de venta de terrenos, los correspondientes a las subastas públicas y a la retribución de los servicios que presta'),
												('30','30 - Documentos emitidos por las empresas que desempeñan el rol adquirente en los sistemas de pago mediante tarjetas de crédito y débito, emitidas por bancos e instituciones financieras o crediticias, domiciliados o no en el país.'),
												('31','31 - Guía de Remisión - Transportista'),
												('32','32 - Documentos emitidos por las empresas recaudadoras de la denominada Garantía de Red Principal a la que hace referencia el numeral 7.6 del artículo 7° de la Ley N° 27133 – Ley de Promoción del Desarrollo de la Industria del Gas Natural'),
												('33','33 - Manifiesto de Pasajeros'),('34','34 - Documento del Operador'),
												('35','35 - Documento del Partícipe'),('36','36 - Recibo de Distribución de Gas Natural'),
												('37','37 - Documentos que emitan los concesionarios del servicio de revisiones técnicas vehiculares, por la prestación de dicho servicio'),
												('40','40 - Comprobante de Percepción'),
												('41','41 - Comprobante de Percepción - Venta interna'),
												('42','42 - Documentos emitidos por las empresas que desempeñan el rol adquiriente en los sistemas de pago mediante tarjetas de crédito emitidas por ellas mismas'),
												('43','43 - Boletos emitidos por las Compañías de Aviación Comercial que prestan servicios de transporte aéreo no regular de pasajeros y transporte aéreo especial de pasajeros.'),
												('44','44 - Billetes de lotería, rifas y apuestas.'),
												('45','45 - Documentos emitidos por centros educativos y culturales, universidades, asociaciones y fundaciones, en lo referente a actividades no gravadas con tributos administrados por la SUNAT.'),
												('46','46 - Formulario de Declaración - pago o Boleta de pago de tributos Internos'),
												('48','48 - Comprobante de Operaciones - Ley N° 29972'),
												('49','49 - Constancia de Depósito - IVAP (Ley 28211)'),
												('50','50 - Declaración Única de Aduanas - Importación definitiva'),
												('51','51 - Póliza o DUI Fraccionada'),
												('52','52 - Despacho Simplificado - Importación Simplificada'),
												('53','53 - Declaración de Mensajería o Courier'),
												('54','54 - Liquidación de Cobranza'),
												('55','55 - BVME para transporte ferroviario de pasajeros'),
												('56','56 - Comprobante de pago SEAE'),('87','87 - Nota de Crédito Especial'),
												('88','88 - Nota de Débito Especial'),('89','89 - Nota de Ajuste de Operaciones - Ley N° 29972'),
												('91','91 - Comprobante de No Domiciliado'),
												('96','96 - Exceso de crédito fiscal por retiro de bienes'),
												('97','97 - Nota de Crédito - No Domiciliado')],string='Tipo Comprobante Pago')
    x_cod_detraccion = fields.Many2one('account.tax',string='Detracción')

    @api.depends('x_cod_detraccion','amount_total')
    def _total_detraccion(self):
        for x_inv in self:
            x_inv.x_total_detraccion = round(-x_inv.x_cod_detraccion.amount * x_inv.amount_total_company_signed / 100)
    
    x_total_detraccion = fields.Monetary(string='Monto Detracción',compute=_total_detraccion)    
    
    x_cod_dependencia_aduanera = fields.Char(size=30,string='Código Dependencia Aduanera')
    x_fecha_emision_detraccion = fields.Date(string='Fecha Emisión Detracción')
    x_nro_constancia_detraccion = fields.Char(size=30,string='Nro. Constancia Detracción')
    x_clasificacion_bienes_y_servicios = fields.Selection([('01','01 - Mercadería, Materia Prima, Suministro, Envases y Embalajes'),
                                                           ('02','02 - Activos Fijos'),
                                                           ('03','03 - Otros Activos no Considerados en los Numerales 1 y 2'),
                                                           ('04','04 - Gastos de Educación, Recreación, Salud, Culturales, Representación, Capacitación, De Viaje, Mantenimiento de Vehículos y de Premios'),
                                                           ('05','05 - Otros Gastos no Incluidos en el Numeral 4')],
                                                          string='Clasificación de Bienes y Servicios')
    x_nro_comprobante_doc_referencia = fields.Char(size=30,string='Nro. Comprobante Doc. Referencia')
  
    
class HrExpense(models.Model):
    _inherit = "hr.expense"

    x_tipo_comprobante_pago = fields.Selection([('00','00 - Otros'),('01','01 - Factura'),('02','02 - Recibo por Honorarios'),
	                                            ('03','03 - Boleta de Venta'),('04','04 - Liquidación de Compra'),
												('05','05 - Boletos de Transporte Aéreo que emiten las Compañías de Aviación Comercial por el servicio de transporte aéreo regular de pasajeros, emitido de manera manual, mecanizada o por medios electrónicos (BME)'),
												('06','06 - Carta de porte aéreo por el servicio de transporte de carga aérea'),
												('07','07 - Nota de Crédito'),('08','08 - Nota de Débito'),
												('09','09 - Guía de remisión - Remitente'),('10','10 - Recibo por Arrendamiento'),
												('11','11 - Póliza emitida por las Bolsas de Valores, Bolsas de Productos o Agentes de Intermediación por operaciones realizadas en las Bolsas de Valores o Productos o fuera de las mismas, autorizadas por SMV'),
												('12','12 - Ticket o cinta emitido por máquina registradora'),
												('13','13 - Documentos emitidos por las empresas del sistema financiero y de seguros, y por las cooperativas de ahorro y crédito no autorizadas a captar recursos del público, que se encuentren bajo el control de la Superintendencia de Banca, Seguros y AFP.'),
												('14','14 - Recibo por servicios públicos de suministro de energía eléctrica, agua, teléfono, telex y telegráficos y otros servicios complementarios que se incluyan en el recibo de servicio público'),
												('15','15 - Boletos emitidos por el servicio de transporte terrestre regular urbano de pasajeros y el ferroviario público de pasajeros prestado en vía férrea local.'),
												('16','16 - Boletos de viaje emitidos por las empresas de transporte nacional de pasajeros, siempre que cuenten con la autorización de la autoridad competente, en las rutas autorizadas. Vía terrestre o ferroviario público no emitido por medios electrónicos (BVME)'),
												('17','17 - Documento emitido por la Iglesia Católica por el arrendamiento de bienes inmuebles'),
												('18','18 - Documento emitido por las Administradoras Privadas de Fondo de Pensiones que se encuentran bajo la supervisión de la Superintendencia de Banca, Seguros y AFP'),
												('19','19 - Boleto o entrada por atracciones y espectáculos públicos'),
												('20','20 - Comprobante de Retención'),
												('21','21 - Conocimiento de embarque por el servicio de transporte de carga marítima'),
												('22','22 - Comprobante por Operaciones No Habituales'),
												('23','23 - Pólizas de Adjudicación emitidas con ocasión del remate o adjudicación de bienes por venta forzada, por los martilleros o las entidades que rematen o subasten bienes por cuenta de terceros'),
												('24','24 - Certificado de pago de regalías emitidas por PERUPETRO S.A'),
												('25','25 - Documento de Atribución (Ley del Impuesto General a las Ventas e Impuesto Selectivo al Consumo, Art. 19º, último párrafo, R.S. N° 022-98-SUNAT).'),
												('26','26 - Recibo por el Pago de la Tarifa por Uso de Agua Superficial con fines agrarios y por el pago de la Cuota para la ejecución de una determinada obra o actividad acordada por la Asamblea General de la Comisión de Regantes o Resolución expedida por el Jefe de la Unidad de Aguas y de Riego (Decreto Supremo N° 003-90-AG, Arts. 28 y 48)'),
												('27','27 - Seguro Complementario de Trabajo de Riesgo'),
												('28','28 - Documentos emitidos por los servicios aeroportuarios prestados a favor de los pasajeros, mediante mecanismo de etiquetas autoadhesivas.'),
												('29','29 - Documentos emitidos por la COFOPRI en calidad de oferta de venta de terrenos, los correspondientes a las subastas públicas y a la retribución de los servicios que presta'),
												('30','30 - Documentos emitidos por las empresas que desempeñan el rol adquirente en los sistemas de pago mediante tarjetas de crédito y débito, emitidas por bancos e instituciones financieras o crediticias, domiciliados o no en el país.'),
												('31','31 - Guía de Remisión - Transportista'),
												('32','32 - Documentos emitidos por las empresas recaudadoras de la denominada Garantía de Red Principal a la que hace referencia el numeral 7.6 del artículo 7° de la Ley N° 27133 – Ley de Promoción del Desarrollo de la Industria del Gas Natural'),
												('33','33 - Manifiesto de Pasajeros'),('34','34 - Documento del Operador'),
												('35','35 - Documento del Partícipe'),('36','36 - Recibo de Distribución de Gas Natural'),
												('37','37 - Documentos que emitan los concesionarios del servicio de revisiones técnicas vehiculares, por la prestación de dicho servicio'),
												('40','40 - Comprobante de Percepción'),
												('41','41 - Comprobante de Percepción - Venta interna'),
												('42','42 - Documentos emitidos por las empresas que desempeñan el rol adquiriente en los sistemas de pago mediante tarjetas de crédito emitidas por ellas mismas'),
												('43','43 - Boletos emitidos por las Compañías de Aviación Comercial que prestan servicios de transporte aéreo no regular de pasajeros y transporte aéreo especial de pasajeros.'),
												('44','44 - Billetes de lotería, rifas y apuestas.'),
												('45','45 - Documentos emitidos por centros educativos y culturales, universidades, asociaciones y fundaciones, en lo referente a actividades no gravadas con tributos administrados por la SUNAT.'),
												('46','46 - Formulario de Declaración - pago o Boleta de pago de tributos Internos'),
												('48','48 - Comprobante de Operaciones - Ley N° 29972'),
												('49','49 - Constancia de Depósito - IVAP (Ley 28211)'),
												('50','50 - Declaración Única de Aduanas - Importación definitiva'),
												('51','51 - Póliza o DUI Fraccionada'),
												('52','52 - Despacho Simplificado - Importación Simplificada'),
												('53','53 - Declaración de Mensajería o Courier'),
												('54','54 - Liquidación de Cobranza'),
												('55','55 - BVME para transporte ferroviario de pasajeros'),
												('56','56 - Comprobante de pago SEAE'),('87','87 - Nota de Crédito Especial'),
												('88','88 - Nota de Débito Especial'),('89','89 - Nota de Ajuste de Operaciones - Ley N° 29972'),
												('91','91 - Comprobante de No Domiciliado'),
												('96','96 - Exceso de crédito fiscal por retiro de bienes'),
												('97','97 - Nota de Crédito - No Domiciliado')],'Tipo Comprobante Pago')
    x_clasificacion_bienes_y_servicios = fields.Selection([('01','01 - Mercadería, Materia Prima, Suministro, Envases y Embalajes'),
                                                           ('02','02 - Activos Fijos'),
                                                           ('03','03 - Otros Activos no Considerados en los Numerales 1 y 2'),
                                                           ('04','04 - Gastos de Educación, Recreación, Salud, Culturales, Representación, Capacitación, De Viaje, Mantenimiento de Vehículos y de Premios'),
                                                           ('05','05 - Otros Gastos no Incluidos en el Numeral 4')],
                                                          string='Clasificación de Bienes y Servicios')
    x_fecha_factura = fields.Date(string='Fecha Factura')
    x_proveedor = fields.Many2one('res.partner',string='Proveedor')
    x_nro_constancia_detraccion = fields.Char(size=30,string='Nro. Constancia Detracción')
    x_fecha_constancia_detraccion = fields.Date(string='Fecha Constancia Detracción')
    
class PurchaseOrder(models.Model):
    _inherit = "purchase.order"
     
    @api.depends('order_line.qty_received')
    def _compute_received_all(self):        
        for order in self:
            l_tot_qty = 0
            l_tot_received = 0
            for line in order.order_line:
                l_tot_qty += line.product_qty
                l_tot_received += line.qty_received
            if l_tot_qty > l_tot_received:
                order.x_received_all = 0
            else:
                order.x_received_all = 1       

    x_received_all = fields.Integer(string='Total Recibido', compute='_compute_received_all', store=True)
    x_solicitante = fields.Many2one('hr.employee', string="Solicitante", required=True)    
    
class SaleOrder(models.Model):
    _inherit = "sale.order"
    
    @api.depends('order_line.qty_invoiced', 'order_line.price_total')
    def _total_facturado(self):        
        for order in self:
            order.x_total_facturado = 0            
            for line in order.order_line:
                if line.qty_invoiced > 0:
                    order.x_total_facturado += line.price_total
            order.x_total_saldo = order.amount_total - order.x_total_facturado
    
    x_total_facturado = fields.Monetary(string='Total Facturado',compute=_total_facturado)    
    x_total_saldo = fields.Monetary(string='Saldo por Facturar',compute=_total_facturado)
        