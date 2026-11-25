# -*- coding: utf-8 -*-
"""
Generador de Diapositivas en PDF y DOCX (Formato Apaisado / Landscape)
Sesión 15: Proyecto de Innovación PESCA-CLICK PAITA v2.4
Alumno: Gerson Misael Pintado Huaman
Docente: Mg. Fiorella Pazos (100 Puntos)
"""

import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.section import WD_SECTION, WD_ORIENTATION
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx2pdf import convert

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill_hex)
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('w:top', top), ('w:bottom', bottom), ('w:left', left), ('w:right', right)]:
        node = OxmlElement(m)
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def create_slides_doc():
    doc = docx.Document()
    
    # Configure Landscape Orientation
    section = doc.sections[0]
    section.orientation = WD_ORIENTATION.LANDSCAPE
    section.page_width = Inches(11.0)
    section.page_height = Inches(8.5)
    section.top_margin = Inches(0.6)
    section.bottom_margin = Inches(0.6)
    section.left_margin = Inches(0.7)
    section.right_margin = Inches(0.7)

    navy = RGBColor(10, 21, 38)
    cyan_dark = RGBColor(2, 132, 199)
    slate_dark = RGBColor(51, 65, 85)
    emerald = RGBColor(21, 128, 61)
    amber = RGBColor(180, 83, 9)

    slides_data = [
        # Slide 1: Carátula
        {
            "tag": "SESIÓN 15 • EVALUACIÓN DE PROYECTO FINAL (100 PUNTOS)",
            "title": "PESCA-CLICK PAITA v2.4",
            "subtitle": "Plataforma B2B Pesquera, Telemetría Marina e IoT: Del Muelle a la Cebichería a 1.4 °C",
            "content": [
                ("INSTITUTO DE EDUCACIÓN SUPERIOR TECNOLÓGICO", True),
                ("Carrera Profesional: Administración de Plataformas y Servicios de TI (APSTI VI)", False),
                ("Alumno Expositor: Gerson Misael Pintado Huaman | Docente Evaluadora: Mg. Fiorella Pazos", True),
                ("Ámbito de Aplicación: DPA Paita, Caleta La Islilla, Yacila -> Cebicherías de Piura y Sullana (58 km)", False),
                ("Evidencia del Piloto Real: 6,850 kg transaccionados • 25 lanchas • 45 cebicherías aliadas", True)
            ]
        },
        # Slide 2: Nombre y Descripción
        {
            "tag": "PARTE 1 • PUNTO 1: DESCRIPCIÓN DEL NEGOCIO",
            "title": "1. Nombre y Modelo de Negocio",
            "subtitle": "PESCA-CLICK PAITA: Ecosistema Digital B2B del Mar a la Mesa",
            "content": [
                ("• Plataforma Web PWA Offline-First: Reporte anticipado desde altamar vía radio AIS (161.975 MHz) o bot de WhatsApp.", True),
                ("• Balanza Digital Certificada DPA Paita: Pesaje honesto con tara automática de caja (-2.5 kg exactos).", True),
                ("• Logística de Frío Express: Furgón isotérmico a 1.4 °C con sensor sumergible IoT DS18B20 en autopista IIRSA Norte.", True),
                ("• Bóveda Escrow Fintech: Liquidación inmediata a Yape/Plin en 2.1 segundos tras confirmación por código QR.", True),
                ("• Modelo de Ingresos: Comisión logística de S/ 1.50 por kg movilizado + membresía B2B (Cero comisión al pescador).", False)
            ]
        },
        # Slide 3: Problema
        {
            "tag": "PARTE 1 • PUNTO 2: EL PROBLEMA REAL",
            "title": "2. Problema y Necesidad Identificada",
            "subtitle": "Diagnóstico de Campo con 25 Pescadores y 45 Cebicherías",
            "content": [
                ("• Asimetría y Abuso en Muelle: Pescador recibe apenas S/ 6.00/kg de cabrilla por falta de frío y canales de venta.", True),
                ("• Fraude en el Pesaje ('el machete'): Acopiadores descuentan arbitrariamente del 15% al 18.5% alegando agua y cajas.", True),
                ("• Ruptura de Frío en Carretera: Pescado viaja tapado con costales a 14 °C - 18 °C, provocando 18.5% de merma.", True),
                ("• Sobrecosto Abusivo en Piura (+250%): Cebicherías pagan S/ 22.00/kg por pescado tardío recibido a las 09:30 AM.", True)
            ]
        },
        # Slide 4: Propuesta de Valor
        {
            "tag": "PARTE 1 • PUNTO 3: PROPUESTA DE VALOR",
            "title": "3. Propuesta de Valor y Diferenciación",
            "subtitle": "Beneficio Mutuo Comprobado (Win-Win)",
            "content": [
                ("• Para el Pescador Artesanal: Duplica su ganancia líquida (+125%, de S/ 6.00 a S/ 13.50/kg) y pago inmediato por Yape.", True),
                ("• Para la Cebichería de Piura: Ahorro neto del 31.8% al 40% (paga S/ 15.00 vs S/ 22.00 puesto en local) a las 06:45 AM.", True),
                ("• Garantía Sanitaria Sanipes D.S. 040: Temperatura controlada a 1.4 °C y reducción de merma de 18.5% a 1.2%.", True),
                ("• Trazabilidad Criptográfica SHA-256: Precinto QR que certifica qué embarcación y qué pescador extrajo el lote.", False)
            ]
        },
        # Slide 5: Público Objetivo
        {
            "tag": "PARTE 1 • PUNTO 4: PÚBLICO Y MERCADO",
            "title": "4. Público Objetivo y Mercado Potencial",
            "subtitle": "Mercado B2B de Alta Demanda Hidrobiológica",
            "content": [
                ("• Oferta: 120 patrones de embarcación agremiados en DPA Paita, Caleta La Islilla y Yacila.", True),
                ("• Demanda: 180 cebicherías y restaurantes marinos en Piura, Castilla, Veintiséis de Octubre y Sullana.", True),
                ("• TAM (Mercado Total Regional): S/ 48.6 Millones anuales en consumo pesquero artesanal regional.", False),
                ("• SAM (Mercado Disponible Piura-Sullana): S/ 14.2 Millones anuales en demanda de cebicherías.", False),
                ("• SOM (Mercado Objetivo Inicial 15%): S/ 2.1 Millones anuales con 45 cebicherías asociadas fijas.", True)
            ]
        },
        # Slide 6: Marketing
        {
            "tag": "PARTE 1 • PUNTO 5: ESTRATEGIAS COMERCIALES",
            "title": "5. Estrategias de Marketing y Comercialización",
            "subtitle": "Penetración en Puerto y Posicionamiento Gastronómico",
            "content": [
                ("• Activación en Muelle (05:00 AM): Demostración en vivo de la balanza digital y cobros Yape frente a los pescadores.", True),
                ("• Sello de Origen 'Pesca Justa en tu Mesa': Placas acrílicas con código QR para las mesas de comensales.", True),
                ("• Garantía Cero Riesgo: Si el pedido supera 2.0 °C en la entrega a la cebichería, el pescado es 100% gratuito.", True),
                ("• Canal Automatizado WhatsApp Business API: Pedidos rápidos mediante botones interactivos y notas de voz.", False)
            ]
        },
        # Slide 7: Proceso Productivo
        {
            "tag": "PARTE 1 • PUNTO 6: PROCESO Y RECURSOS",
            "title": "6. Proceso Productivo y Recursos Necesarios",
            "subtitle": "Ciclo Logístico Integrado de 5 Etapas de Madrugada",
            "content": [
                ("1. Altamar (04:00 AM): Reporte de captura estimada por radio AIS VHF (161.975 MHz).", True),
                ("2. Preventa (04:30 AM): Confirmación en PWA por cebicherías y custodia en Bóveda Escrow.", True),
                ("3. Muelle DPA (05:15 AM): Pesaje digital con tara (-2.5 kg), hielo en escamas y precinto QR.", True),
                ("4. Ruta IIRSA Norte (05:45 AM): Furgón isotérmico a 1.4 °C con sensor IoT DS18B20 (58 km en 48 min).", True),
                ("5. Piura (06:30 AM): Entrega conforme, escaneo QR y liberación instantánea del pago al pescador en 2s.", True)
            ]
        },
        # Slide 8: Inversión y Costos
        {
            "tag": "PARTE 1 • PUNTO 7: FINANZAS Y PRESUPUESTO",
            "title": "7. Inversión Inicial (CAPEX) y Costos (OPEX)",
            "subtitle": "Estructura de Costos Reales de Implementación",
            "content": [
                ("• Total Inversión Inicial (CAPEX): S/ 25,250.00", True),
                ("  - Acondicionamiento furgón isotérmico (S/ 12,000) | Balanza Torrey RS-232 (S/ 2,400)", False),
                ("  - Receptor VHF AIS + Antena (S/ 1,850) | Kit IoT DS18B20 + 4G (S/ 1,200) | Jabas (S/ 3,500)", False),
                ("• Total Costos Operativos Mensuales (OPEX): S/ 6,650.00", True),
                ("  - Combustible Paita-Piura (S/ 1,820) | Hielo certificado Sanipes (S/ 950) | Chofer (S/ 1,600)", False),
                ("  - Supervisor de muelle (S/ 1,400) | Servidor Cloud y chip celular IoT (S/ 380)", False),
                ("• Costo Unitario de Operación: S/ 0.55 por kilogramo transportado (Margen bruto: S/ 0.95/kg).", True)
            ]
        },
        # Slide 9: Proyecciones
        {
            "tag": "PARTE 1 • PUNTO 8: EVALUACIÓN ECONÓMICA",
            "title": "8. Proyección de Ingresos y Rentabilidad (3 Años)",
            "subtitle": "Viabilidad Financiera Basada en los 6,850 kg del Piloto",
            "content": [
                ("• Año 1 (45 Cebicherías): 144,000 kg | Ingresos: S/ 243,000.00 | Utilidad Neta: S/ 73,500.00", True),
                ("• Año 2 (80 Cebicherías): 256,000 kg | Ingresos: S/ 432,000.00 | Utilidad Neta: S/ 144,900.00", True),
                ("• Año 3 (140 Cebicherías): 448,000 kg | Ingresos: S/ 756,000.00 | Utilidad Neta: S/ 270,200.00", True),
                ("• Valor Actual Neto (VAN a tasa 12%): S/ 285,410.00 (Proyecto altamente rentable)", True),
                ("• Tasa Interna de Retorno (TIR): 142.8% | Período de Recuperación (Payback): 4.8 meses.", True),
                ("• Punto de Equilibrio Operativo: 4,430 kg/mes (~15 cebicherías aliadas).", False)
            ]
        },
        # Slide 10: Sostenibilidad
        {
            "tag": "PARTE 1 • PUNTO 9: MODELO DE TRIPLE IMPACTO",
            "title": "9. Estrategias de Sostenibilidad",
            "subtitle": "Alineado a los Objetivos de Desarrollo Sostenible (ODS 8, 12 y 14)",
            "content": [
                ("• Pilar Ambiental: Reducción de mermas de 18.5% a 1.2% (cero pescado botado); sustitución de costales por jabas reutilizables; y respeto de tallas mínimas biológicas.", True),
                ("• Pilar Social: Dignificación del pescador (+125% ingreso neto); inclusión financiera formal con Yape/Plin; erradicación del monopolio usuro de acopiadores.", True),
                ("• Pilar Económico: Modelo autosostenible con TIR de 142.8%; ahorro del 31.8% para restaurantes piuranos; y fondo de reinversión para expansión de flota en frío.", True)
            ]
        },
        # Slide 11: Ética y Datos Reales vs Proyecciones
        {
            "tag": "PARTE 2: FUNDAMENTACIÓN DE ÉTICA Y DATOS",
            "title": "10. Compromisos Éticos y Verificación de Datos",
            "subtitle": "Diferenciación Rigurosa entre Piloto Real y Proyecciones",
            "content": [
                ("• DATOS REALES VERIFICADOS (PILOTO 15 JORNADAS):", True),
                ("  - 6,850 kg transaccionados | 137 pedidos | 99.1% cumplimiento.", False),
                ("  - 1.4 °C promedio en ruta monitoreado con sensor DS18B20 IP68.", False),
                ("  - Pescador incrementó ingreso de S/ 6.00 a S/ 13.50/kg (+125%).", False),
                ("  - Cebichería ahorró 31.8% | Merma cayó de 18.5% a 1.2% | Test SUS: 88.5/100.", False),
                ("• ESTIMACIONES Y PROYECCIONES FINANCIERAS:", True),
                ("  - Crecimiento a 140 cebicherías y 448,000 kg al Año 3 (basado en censo de 180 locales).", False),
                ("  - VAN de S/ 285,410 y TIR de 142.8% sujeto a estabilidad de precios de combustible.", False)
            ]
        },
        # Slide 12: Conclusiones y Recomendaciones
        {
            "tag": "PARTE 1 • PUNTO 10: DICTAMEN DE INNOVACIÓN",
            "title": "11. Conclusiones y Recomendaciones",
            "subtitle": "Aporte Técnico y Social de la Carrera APSTI VI",
            "content": [
                ("• Conclusión 1: La tecnología aplicada resuelve de raíz la asimetría de precios en el muelle de Paita.", True),
                ("• Conclusión 2: Beneficio dual demostrado: pescador duplica ingresos y cebicherías ahorran 31.8%.", True),
                ("• Conclusión 3: La inocuidad y frío a 1.4 °C garantiza cebiches de excelencia organoléptica.", True),
                ("• Recomendación 1: Escalar en Fase II hacia Parachique (Sechura), Cabo Blanco y Talara.", False),
                ("• Recomendación 2: Homologar los códigos QR con Sanipes como precinto oficial regional.", False),
                ("• Calificación Objetivo: 100 PUNTOS (Nota de Excelencia) - Mg. Fiorella Pazos.", True)
            ]
        },
        # Slide 13: Guion de Exposición Oral (Pitch)
        {
            "tag": "PARTE 3: EXPOSICIÓN Y SUSTENTACIÓN",
            "title": "12. Guion de Sustentación Oral (100 Puntos)",
            "subtitle": "Estructura de Exposición de 3 Minutos ante la Docente Evaluadora",
            "content": [
                ("• Minuto 0:00 - 0:45 (Apertura): Diagnóstico del abuso en el DPA Paita (S/ 6.00 vs S/ 22.00) y presentación de Pesca-Click.", True),
                ("• Minuto 0:45 - 1:30 (Tecnología TI): Radar AIS, Balanza Digital con tara fija (-2.5 kg), Sensor IoT a 1.4 °C y Bóveda Escrow.", True),
                ("• Minuto 1:30 - 2:15 (Resultados Reales): 6,850 kg transaccionados, +125% para pescador, -31.8% ahorro cebichería, SUS 88.5.", True),
                ("• Minuto 2:15 - 2:45 (Cierre y Finanzas): VAN de S/ 285,410, Payback 4.8 meses, invitación a ver la web en vivo.", True),
                ("• Enlace Web en Vivo: index.html (Simulador de Radar, Balanza con tara, Sensor IoT y Bóveda Escrow).", True)
            ]
        }
    ]

    for s_idx, slide in enumerate(slides_data):
        if s_idx > 0:
            doc.add_page_break()

        # Slide Container Table
        table = doc.add_table(rows=3, cols=1)
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        
        # Header Row
        cell_top = table.cell(0, 0)
        set_cell_background(cell_top, "0A1526")
        set_cell_margins(cell_top, 80, 80, 140, 140)
        p_top = cell_top.paragraphs[0]
        r_tag = p_top.add_run(slide["tag"] + "\n")
        r_tag.bold = True
        r_tag.font.size = Pt(9)
        r_tag.font.color.rgb = RGBColor(34, 211, 238)

        r_title = p_top.add_run(slide["title"])
        r_title.bold = True
        r_title.font.size = Pt(17)
        r_title.font.color.rgb = RGBColor(255, 255, 255)

        # Body Row
        cell_body = table.cell(1, 0)
        set_cell_background(cell_body, "F8FAFC")
        set_cell_margins(cell_body, 120, 120, 140, 140)
        p_body = cell_body.paragraphs[0]
        
        r_sub = p_body.add_run(slide["subtitle"] + "\n\n")
        r_sub.bold = True
        r_sub.font.size = Pt(11)
        r_sub.font.color.rgb = cyan_dark

        for text, is_bold in slide["content"]:
            p_item = cell_body.add_paragraph()
            p_item.paragraph_format.space_before = Pt(2)
            p_item.paragraph_format.space_after = Pt(2)
            run = p_item.add_run(text)
            run.bold = is_bold
            run.font.size = Pt(10)
            run.font.color.rgb = navy if is_bold else slate_dark

        # Footer Row
        cell_foot = table.cell(2, 0)
        set_cell_background(cell_foot, "F1F5F9")
        set_cell_margins(cell_foot, 60, 60, 140, 140)
        p_foot = cell_foot.paragraphs[0]
        r_foot = p_foot.add_run(f"PESCA-CLICK PAITA v2.4 • APSTI VI • Gerson Misael Pintado Huaman | Diapositiva {s_idx + 1} de {len(slides_data)}")
        r_foot.font.size = Pt(8.5)
        r_foot.font.color.rgb = slate_dark

    docx_path = r"c:\Users\USER\Downloads\PESCA CL8IK\DIAPOSITIVAS_PESCA_CLICK_SESION15.docx"
    pdf_path = r"c:\Users\USER\Downloads\PESCA CL8IK\DIAPOSITIVAS_PESCA_CLICK_SESION15.pdf"

    doc.save(docx_path)
    print(f"Diapositivas DOCX generadas exitosamente: {docx_path}")
    
    print("Convirtiendo diapositivas a PDF...")
    convert(docx_path, pdf_path)
    print(f"Diapositivas PDF generadas exitosamente: {pdf_path}")

if __name__ == "__main__":
    create_slides_doc()
