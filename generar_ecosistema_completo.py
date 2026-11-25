# -*- coding: utf-8 -*-
"""
Generador de Ecosistema Completo de HTMLs para PESCA-CLICK PAITA v2.4 y Sesión 15
Genera:
1. 4 Fichas Técnicas de Productos B2B (Cabrilla, Tollo, Pota, Mero) con imágenes y calculadora de ahorro.
2. Portal Central de Navegación de Sesión 15 (Hub interactivo con tarjetas clickeables a cada punto).
3. 12 HTMLs independientes para cada punto de la presentación (Puntos 1 al 10, Parte 2 y Parte 3).
"""

import os

BASE_DIR = r"c:\Users\USER\Downloads\PESCA CL8IK"
IMG_DIR = os.path.join(BASE_DIR, "img")
os.makedirs(IMG_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. GENERACIÓN DE FICHAS DE PRODUCTO B2B
# -------------------------------------------------------------
products = [
    {
        'id': 'cabrilla',
        'file': 'producto-cabrilla.html',
        'name': 'Cabrilla Norteña',
        'scientific': 'Paralabrax humeralis',
        'category': 'Pescado de Roca • Primera Calidad Marina',
        'img': 'img/cabrilla.jpg',
        'fallback_img': 'https://images.unsplash.com/photo-1534482421-64566f976cfa?auto=format&fit=crop&w=1200&q=80',
        'price_playa': 'S/ 6.00',
        'price_intermediario': 'S/ 22.00',
        'price_pescaclick': 'S/ 13.50',
        'unit_price': 13.50,
        'rev_price': 22.00,
        'saving_pct': '38.6%',
        'gain_fisherman': '+125% (S/ 7.50 más por kg)',
        'temp': '1.2 °C',
        'sanipes': 'SANIPES-DPA-PAITA-2026-0881',
        'gear': 'Pinta de mano / Espinel artesanal selectivo',
        'vessel': 'Lancha "Siempre San Pedro" (PT-45210-BM)',
        'captain': 'Don Pedro Chunga Eche (32 años de faena en Paita)',
        'dock': 'Desembarcadero Pesquero Artesanal (DPA) de Paita',
        'culinary': 'Pescado insignia para Cebiche Clásico Piurano, Sudado a la Paitana con chicha de jora, y Frito crocante con yucas.',
        'texture': 'Carne blanca semi-firme, hojuelas gruesas, sabor limpio a mar abierto, bajo contenido graso (< 1.5%).',
        'specs': [
            ('Talla Comercial Mínima', '32 cm (Conforme a R.M. PRODUCE)'),
            ('Método de Conservación', 'Hielo en escamas 1:1 en altamar'),
            ('Cadena de Frío Garantizada', '0.5 °C a 1.8 °C en furgón isotérmico'),
            ('Tiempo Muelle a Cocina', '55 minutos por Autopista IIRSA Norte'),
            ('Presentación', 'Entero eviscerado / Entero fresco en jaba oficial')
        ]
    },
    {
        'id': 'tollo',
        'file': 'producto-tollo.html',
        'name': 'Tollo de Leche',
        'scientific': 'Mustelus whitneyi',
        'category': 'Carne Blanca Sin Espinas • Preferido Familiar',
        'img': 'img/tollo.jpg',
        'fallback_img': 'https://images.unsplash.com/photo-1519708227418-c8fd9a32b7a2?auto=format&fit=crop&w=1200&q=80',
        'price_playa': 'S/ 5.00',
        'price_intermediario': 'S/ 18.00',
        'price_pescaclick': 'S/ 11.00',
        'unit_price': 11.00,
        'rev_price': 18.00,
        'saving_pct': '38.8%',
        'gain_fisherman': '+120% (S/ 6.00 más por kg)',
        'temp': '1.4 °C',
        'sanipes': 'SANIPES-DPA-PAITA-2026-0882',
        'gear': 'Cortina artesanal reglamentaria con luz de malla legal',
        'vessel': 'Embarcación "Don Lucho I" (PT-38194-BM)',
        'captain': 'Don Luis Morales Fiestas (Caleta Yacila)',
        'dock': 'DPA Paita / Caleta Yacila',
        'culinary': 'Ideal para Cebiche de Tollo, Chicharrón crocante sin espinas, Milanesa marina y Arroz con mariscos.',
        'texture': 'Carne magra, desprovista de espinas intramusculares, textura suave y homogénea, alto rendimiento (92%).',
        'specs': [
            ('Talla Comercial Mínima', '60 cm (Supera norma Sanipes)'),
            ('Método de Conservación', 'Eviscerado inmediato en bote y salmuera fría'),
            ('Cadena de Frío Garantizada', '1.0 °C a 2.0 °C'),
            ('Tiempo Muelle a Cocina', '50 minutos directo a Piura/Sullana'),
            ('Presentación', 'Tronchos limpios sin piel o filete fresco en jaba')
        ]
    },
    {
        'id': 'pota',
        'file': 'producto-pota.html',
        'name': 'Pota Manto Limpio',
        'scientific': 'Dosidicus gigas (Calamar Gigante)',
        'category': 'Cefalópodo del Pacífico Sur • Chicharrón y Wok',
        'img': 'img/pota.jpg',
        'fallback_img': 'https://images.unsplash.com/photo-1544551763-46a013bb70d5?auto=format&fit=crop&w=1200&q=80',
        'price_playa': 'S/ 2.00',
        'price_intermediario': 'S/ 8.00',
        'price_pescaclick': 'S/ 4.80',
        'unit_price': 4.80,
        'rev_price': 8.00,
        'saving_pct': '40.0%',
        'gain_fisherman': '+140% (S/ 2.80 más por kg)',
        'temp': '0.9 °C',
        'sanipes': 'SANIPES-DPA-PAITA-2026-0883',
        'gear': 'Línea de potera artesanal manual luminiscente nocturna',
        'vessel': 'Embarcación "Virgen de las Mercedes" (PT-19402-BM)',
        'captain': 'Don Carlos Fiestas Querevalú (La Islilla - Paita)',
        'dock': 'Caleta La Islilla / Muelle Paita',
        'culinary': 'Chicharrón de pota crocante, Arroz chaufa de mariscos al wok, Anticuchos marinos y Tiraditos nikkei.',
        'texture': 'Manto grueso y blanco de 18 mm, libre de amoniaco por frío inmediato en altamar, textura tierna al corte.',
        'specs': [
            ('Espesor de Manto', '18 mm promedio (Sin ablandadores químicos)'),
            ('Procesamiento Primario', 'Descabezado y desviscerado en alta mar a 0 °C'),
            ('Rendimiento en Cocina', '98% utilizable (cero mermas de víscera)'),
            ('Certificación', 'Trazabilidad PRODUCE y protocolo Sanipes'),
            ('Presentación', 'Manto limpio en planchas con film alimentario')
        ]
    },
    {
        'id': 'mero',
        'file': 'producto-mero.html',
        'name': 'Mero Murique',
        'scientific': 'Epinephelus quinquefasciatus',
        'category': 'Alta Gama Gourmet • El Rey de la Gastronomía Norteña',
        'img': 'img/mero.jpg',
        'fallback_img': 'https://images.unsplash.com/photo-1524704654690-b56c05c78a00?auto=format&fit=crop&w=1200&q=80',
        'price_playa': 'S/ 25.00',
        'price_intermediario': 'S/ 60.00',
        'price_pescaclick': 'S/ 42.00',
        'unit_price': 42.00,
        'rev_price': 60.00,
        'saving_pct': '30.0%',
        'gain_fisherman': '+68% (S/ 17.00 más por kg)',
        'temp': '1.0 °C',
        'sanipes': 'SANIPES-DPA-PAITA-2026-0884',
        'gear': 'Espinel vertical de fondo en arrecifes de piedra a 40 brazas',
        'vessel': 'Lancha "San José Bendito" (PT-51203-BM)',
        'captain': 'Don Manuel Rumiche Vite (Tierra Colorada - Paita)',
        'dock': 'DPA Paita',
        'culinary': 'Plato estrella de los mejores restaurantes gourmet: Mero en costra de sal, Sudado imperial a la norteña, Ceviche de mero.',
        'texture': 'Carne blanca perlada excepcional, sabor dulce yodado inconfundible, hojuela gelatinosa que retiene jugosidad.',
        'specs': [
            ('Talla Comercial', 'Piezas selectas de 3 a 6 kg (Madurez garantizada)'),
            ('Captura', 'Pesca 100% selectiva con anzuelo de fondo'),
            ('Frecuencia de Arribo', '2 a 3 lanchas por semana (Stock limitado B2B)'),
            ('Cadena de Custodia', 'Precinto de seguridad QR inviolable'),
            ('Entrega VIP', 'Directo a la mesa de preparación del Chef')
        ]
    }
]

def render_product_page(prod):
    specs_html = ""
    for i, (param, val) in enumerate(prod['specs']):
        bg = 'bg-slate-50' if i % 2 == 0 else 'bg-white'
        specs_html += f"""
        <tr class="border-b border-slate-100 {bg}">
            <td class="py-3 px-4 font-bold text-slate-700 w-1/3">{param}</td>
            <td class="py-3 px-4 text-slate-600 font-mono">{val}</td>
        </tr>
        """

    return f"""<!DOCTYPE html>
<html lang="es" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{prod['name']} — Ficha Técnica B2B | PESCA-CLICK PAITA</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    colors: {{
                        brand: {{
                            50: '#F0F9FF',
                            100: '#E0F2FE',
                            500: '#0284C7',
                            600: '#0369A1',
                            900: '#0A2540'
                        }}
                    }}
                }}
            }}
        }}
    </script>
</head>
<body class="bg-slate-50 text-slate-800 font-sans antialiased min-h-screen flex flex-col">

    <!-- TOP BAR -->
    <header class="bg-brand-900 text-white text-xs py-2.5 px-4 sticky top-0 z-50 border-b border-brand-800 shadow-sm">
        <div class="max-w-7xl mx-auto flex items-center justify-between gap-4">
            <div class="flex items-center space-x-3">
                <a href="index.html#modulo-catalogo" class="bg-brand-800 hover:bg-brand-700 text-cyan-200 px-3 py-1 rounded-lg border border-brand-700 transition flex items-center font-semibold">
                    <i class="fas fa-arrow-left mr-1.5"></i> Volver al Catálogo B2B
                </a>
                <span class="text-slate-400">|</span>
                <span class="font-mono text-cyan-300 hidden sm:inline"><i class="fas fa-certificate mr-1 text-emerald-400"></i> FICHA TÉCNICA SANIPES D.S. 040</span>
            </div>
            <div class="flex items-center space-x-3">
                <a href="portal_sesion15.html" class="bg-cyan-600/30 hover:bg-cyan-600/50 text-cyan-200 border border-cyan-400/40 px-3 py-1 rounded font-semibold transition flex items-center">
                    <i class="fas fa-graduation-cap mr-1.5"></i> Hub Sesión 15
                </a>
                <a href="index.html" class="bg-emerald-600 hover:bg-emerald-500 text-white px-3 py-1 rounded font-bold transition flex items-center shadow-sm">
                    <i class="fas fa-store mr-1.5"></i> Plataforma Comercial
                </a>
            </div>
        </div>
    </header>

    <main class="max-w-7xl mx-auto px-4 py-8 flex-grow w-full">

        <!-- BREADCRUMBS -->
        <nav class="flex items-center space-x-2 text-xs text-slate-500 font-mono mb-6">
            <a href="index.html" class="hover:text-brand-600">PESCA-CLICK PAITA</a>
            <span>/</span>
            <a href="index.html#modulo-catalogo" class="hover:text-brand-600">Catálogo B2B</a>
            <span>/</span>
            <span class="text-slate-800 font-bold">{prod['name']}</span>
        </nav>

        <!-- MAIN PRODUCT HERO GRID -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start mb-12">

            <!-- LEFT: IMAGE GALLERY & REAL TIME TELEMETRY -->
            <div class="lg:col-span-6 space-y-4">
                <div class="relative rounded-3xl overflow-hidden bg-slate-900 border border-slate-200 shadow-xl group aspect-[4/3] flex items-center justify-center">
                    <img src="{prod['img']}" onerror="this.onerror=null; this.src='{prod['fallback_img']}';" alt="{prod['name']}" class="w-full h-full object-cover group-hover:scale-105 transition duration-700">
                    <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent"></div>
                    
                    <!-- Floating badges -->
                    <div class="absolute top-4 left-4 flex flex-col gap-2">
                        <span class="bg-emerald-500 text-white font-mono text-xs px-3 py-1 rounded-full font-bold shadow flex items-center">
                            <span class="w-2 h-2 rounded-full bg-white animate-pulse mr-1.5"></span> PESCA DEL DÍA FRESCA
                        </span>
                        <span class="bg-brand-900/90 text-cyan-200 font-mono text-[11px] px-3 py-1 rounded-full backdrop-blur-sm border border-brand-700">
                            <i class="fas fa-snowflake mr-1 text-cyan-400"></i> {prod['temp']} en Cámara de Frío
                        </span>
                    </div>

                    <div class="absolute bottom-4 left-4 right-4 text-white">
                        <div class="text-xs text-cyan-300 font-mono uppercase tracking-wider mb-1">{prod['category']}</div>
                        <h1 class="text-2xl sm:text-3xl font-black">{prod['name']}</h1>
                        <p class="text-xs text-slate-300 italic font-mono">{prod['scientific']}</p>
                    </div>
                </div>

                <!-- DOCK & CAPTAIN INFO CARD -->
                <div class="bg-white rounded-2xl p-5 border border-slate-200 shadow-sm space-y-3">
                    <div class="flex items-center justify-between border-b border-slate-100 pb-3">
                        <div class="text-xs font-bold text-slate-800 uppercase tracking-wide flex items-center">
                            <i class="fas fa-ship text-brand-600 mr-2"></i> Trazabilidad del Patrón de Lancha
                        </div>
                        <span class="text-[11px] bg-slate-100 text-slate-700 font-mono px-2 py-0.5 rounded font-semibold">Certificado Sanipes</span>
                    </div>
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
                        <div>
                            <span class="text-slate-400 block text-[10px] uppercase font-mono">Embarcación:</span>
                            <strong class="text-slate-800">{prod['vessel']}</strong>
                        </div>
                        <div>
                            <span class="text-slate-400 block text-[10px] uppercase font-mono">Patrón Responsable:</span>
                            <strong class="text-slate-800">{prod['captain']}</strong>
                        </div>
                        <div>
                            <span class="text-slate-400 block text-[10px] uppercase font-mono">Puerto de Desembarque:</span>
                            <span class="text-slate-700">{prod['dock']}</span>
                        </div>
                        <div>
                            <span class="text-slate-400 block text-[10px] uppercase font-mono">Arte de Pesca Selectivo:</span>
                            <span class="text-slate-700">{prod['gear']}</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- RIGHT: PRICE COMPARISON, SAVINGS & SIMULATOR -->
            <div class="lg:col-span-6 space-y-6">

                <!-- PRICE TRANSPARENCY CARD -->
                <div class="bg-white rounded-3xl p-6 sm:p-8 border border-slate-200 shadow-xl space-y-6">
                    <div class="flex items-center justify-between">
                        <div>
                            <span class="text-xs font-mono font-bold text-brand-600 uppercase tracking-wider">Cotización Oficial B2B</span>
                            <div class="flex items-baseline space-x-2 mt-1">
                                <span class="text-4xl sm:text-5xl font-black text-brand-900 font-mono">{prod['price_pescaclick']}</span>
                                <span class="text-slate-500 font-semibold text-sm">/ Kilogramo Neto</span>
                            </div>
                        </div>
                        <div class="bg-emerald-50 text-emerald-800 border border-emerald-300 rounded-2xl px-4 py-2.5 text-center">
                            <span class="text-xs font-bold block uppercase">Ahorro Cebichería</span>
                            <span class="text-2xl font-black text-emerald-600 font-mono">-{prod['saving_pct']}</span>
                        </div>
                    </div>

                    <!-- 3-WAY COMPARISON BAR -->
                    <div class="bg-slate-50 rounded-2xl p-4 border border-slate-200 space-y-3">
                        <div class="text-xs font-bold text-slate-700 flex items-center justify-between">
                            <span>Comparativa de Precios del Mercado (Paita - Piura):</span>
                            <span class="text-emerald-600 font-bold"><i class="fas fa-balance-scale mr-1"></i> Precio Justo Simétrico</span>
                        </div>
                        <div class="grid grid-cols-3 gap-2 text-center text-xs font-mono">
                            <div class="bg-red-50 text-red-800 p-2.5 rounded-xl border border-red-200">
                                <span class="text-[10px] text-red-500 uppercase block font-sans">Abuso Intermediario</span>
                                <strong class="text-base block text-red-600 line-through">{prod['price_playa']}</strong>
                                <span class="text-[10px] text-red-500">Paga al pescador</span>
                            </div>
                            <div class="bg-amber-50 text-amber-800 p-2.5 rounded-xl border border-amber-200">
                                <span class="text-[10px] text-amber-600 uppercase block font-sans">Revendedor Piura</span>
                                <strong class="text-base block text-amber-700 line-through">{prod['price_intermediario']}</strong>
                                <span class="text-[10px] text-amber-600">Cobra a cebichería</span>
                            </div>
                            <div class="bg-emerald-100 text-emerald-900 p-2.5 rounded-xl border-2 border-emerald-500 shadow-sm">
                                <span class="text-[10px] text-emerald-700 uppercase block font-sans font-bold">PESCA-CLICK B2B</span>
                                <strong class="text-base block text-emerald-800">{prod['price_pescaclick']}</strong>
                                <span class="text-[10px] text-emerald-700 font-bold">{prod['gain_fisherman']}</span>
                            </div>
                        </div>
                    </div>

                    <!-- INSTANT ORDER CALCULATOR -->
                    <div class="border-t border-slate-100 pt-5 space-y-4">
                        <div class="flex items-center justify-between">
                            <label for="calc-kg" class="text-xs font-bold text-slate-800 uppercase">
                                <i class="fas fa-calculator text-brand-600 mr-1.5"></i> Calcular Pedido en Kilogramos:
                            </label>
                            <span class="text-xs text-slate-500 font-mono">Tara oficial: -2.5 kg/jaba</span>
                        </div>
                        
                        <div class="flex items-center space-x-3">
                            <div class="relative flex-1">
                                <input type="number" id="calc-kg" value="30" min="5" max="500" step="5" oninput="updateProductCalc()" class="w-full bg-white border border-slate-300 rounded-xl px-4 py-3 text-lg font-mono font-bold text-slate-800 focus:outline-none focus:ring-2 focus:ring-brand-500">
                                <span class="absolute right-4 top-3.5 text-slate-400 font-mono text-sm font-semibold">KG</span>
                            </div>
                            <button onclick="addFromProduct()" class="bg-brand-600 hover:bg-brand-700 text-white font-bold px-6 py-3.5 rounded-xl shadow-md transition flex items-center space-x-2 text-sm">
                                <i class="fas fa-cart-plus"></i>
                                <span>Añadir Pedido</span>
                            </button>
                        </div>

                        <!-- LIVE CALC RESULT -->
                        <div class="bg-brand-50 rounded-2xl p-4 border border-brand-100 flex items-center justify-between text-xs">
                            <div>
                                <span class="text-slate-500 block">Inversión en PESCA-CLICK:</span>
                                <strong id="calc-total" class="text-xl font-black text-brand-900 font-mono">S/ 405.00</strong>
                            </div>
                            <div class="text-right">
                                <span class="text-slate-500 block">Ahorro frente al Revendedor:</span>
                                <strong id="calc-saving" class="text-xl font-black text-emerald-600 font-mono">+ S/ 255.00</strong>
                            </div>
                        </div>
                    </div>

                    <!-- SANIPES SEAL -->
                    <div class="bg-slate-50 rounded-xl p-3 border border-slate-200 flex items-center justify-between text-xs text-slate-600">
                        <div class="flex items-center space-x-2">
                            <i class="fas fa-shield-alt text-emerald-600 text-base"></i>
                            <span>Registro Sanitario Oficial: <strong class="font-mono">{prod['sanipes']}</strong></span>
                        </div>
                        <span class="text-emerald-700 font-bold"><i class="fas fa-check-circle mr-1"></i> Válido 2026</span>
                    </div>

                </div>

            </div>

        </div>

        <!-- DETAILS TABS: CULINARY, TEXTURE & TECHNICAL SPECS -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-12">

            <div class="bg-white rounded-2xl p-6 border border-slate-200 shadow-sm space-y-3">
                <div class="w-10 h-10 rounded-xl bg-orange-100 text-orange-600 flex items-center justify-center text-lg font-bold">
                    <i class="fas fa-utensils"></i>
                </div>
                <h3 class="text-base font-bold text-slate-800">Aplicación Culinaria</h3>
                <p class="text-xs text-slate-600 leading-relaxed">
                    {prod['culinary']}
                </p>
            </div>

            <div class="bg-white rounded-2xl p-6 border border-slate-200 shadow-sm space-y-3">
                <div class="w-10 h-10 rounded-xl bg-cyan-100 text-cyan-600 flex items-center justify-center text-lg font-bold">
                    <i class="fas fa-water"></i>
                </div>
                <h3 class="text-base font-bold text-slate-800">Textura y Propiedades</h3>
                <p class="text-xs text-slate-600 leading-relaxed">
                    {prod['texture']}
                </p>
            </div>

            <div class="bg-white rounded-2xl p-6 border border-slate-200 shadow-sm space-y-3">
                <div class="w-10 h-10 rounded-xl bg-purple-100 text-purple-600 flex items-center justify-center text-lg font-bold">
                    <i class="fas fa-clipboard-check"></i>
                </div>
                <h3 class="text-base font-bold text-slate-800">Control de Calidad DPA</h3>
                <ul class="text-xs text-slate-600 space-y-1.5 font-mono">
                    <li>• Ojos convexos y cristalinos</li>
                    <li>• Branquias rojo escarlata vivo</li>
                    <li>• Firmeza elástica al tacto (rigor mortis)</li>
                    <li>• Olor puro a brisa marina sin amoniaco</li>
                </ul>
            </div>

        </div>

        <!-- TECHNICAL SPECIFICATIONS TABLE -->
        <div class="bg-white rounded-3xl p-6 sm:p-8 border border-slate-200 shadow-sm mb-12">
            <h2 class="text-lg font-bold text-slate-900 mb-6 flex items-center">
                <i class="fas fa-table-list text-brand-600 mr-2.5"></i> Especificaciones Técnicas y Parámetros de Inocuidad
            </h2>
            <div class="overflow-x-auto">
                <table class="w-full text-left text-xs">
                    <tbody>
                        {specs_html}
                    </tbody>
                </table>
            </div>
        </div>

        <!-- OTHER PRODUCTS NAVIGATION -->
        <div class="border-t border-slate-200 pt-8 mb-12">
            <h3 class="text-sm font-bold text-slate-800 mb-4">Explorar Otras Especies del DPA Paita:</h3>
            <div class="grid grid-cols-2 sm:grid-cols-4 gap-4 text-xs font-bold">
                <a href="producto-cabrilla.html" class="bg-white p-3.5 rounded-xl border border-slate-200 hover:border-brand-500 hover:text-brand-600 transition text-center shadow-sm block">
                    🐟 Cabrilla Norteña
                </a>
                <a href="producto-tollo.html" class="bg-white p-3.5 rounded-xl border border-slate-200 hover:border-brand-500 hover:text-brand-600 transition text-center shadow-sm block">
                    🦈 Tollo de Leche
                </a>
                <a href="producto-pota.html" class="bg-white p-3.5 rounded-xl border border-slate-200 hover:border-brand-500 hover:text-brand-600 transition text-center shadow-sm block">
                    🦑 Pota Manto Limpio
                </a>
                <a href="producto-mero.html" class="bg-white p-3.5 rounded-xl border border-slate-200 hover:border-brand-500 hover:text-brand-600 transition text-center shadow-sm block">
                    👑 Mero Murique
                </a>
            </div>
        </div>

    </main>

    <!-- FOOTER -->
    <footer class="bg-white border-t border-slate-200 py-8 px-4 text-center text-xs text-slate-500 font-mono">
        <div class="max-w-7xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-4">
            <div>PESCA-CLICK PAITA v2.4 • Plataforma B2B Pesquera • Muelle DPA Paita</div>
            <div class="space-x-4">
                <a href="index.html" class="hover:text-brand-600">Inicio</a>
                <a href="index.html#modulo-catalogo" class="hover:text-brand-600">Catálogo</a>
                <a href="portal_sesion15.html" class="hover:text-brand-600">Hub Sesión 15</a>
            </div>
        </div>
    </footer>

    <script>
        const unitPrice = {prod['unit_price']};
        const revendedorPrice = {prod['rev_price']};

        function updateProductCalc() {{
            const kg = parseFloat(document.getElementById('calc-kg').value) || 0;
            const total = kg * unitPrice;
            const revendedorTotal = kg * revendedorPrice;
            const saving = revendedorTotal - total;

            document.getElementById('calc-total').innerText = 'S/ ' + total.toFixed(2);
            document.getElementById('calc-saving').innerText = '+ S/ ' + Math.max(0, saving).toFixed(2);
        }}

        function addFromProduct() {{
            const kg = parseFloat(document.getElementById('calc-kg').value) || 30;
            alert('¡Excelente! Se han añadido ' + kg + ' kg de {prod['name']} al pedido B2B de tu cebichería.\\n\\nRedirigiendo a la plataforma para finalizar el despacho en frío...');
            window.location.href = 'index.html#modulo-catalogo';
        }}
    </script>
</body>
</html>
"""

for p in products:
    content = render_product_page(p)
    path = os.path.join(BASE_DIR, p['file'])
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Producto generado: {p['file']}")

print("Fichas de producto creadas con éxito.")
