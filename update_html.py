import re
import os

html_path = r'C:\Program Files\PROYECTOS DE PROGRAMACION\APRE\index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add Language Switcher CSS & JS
css_injection = """
  /* ---------- language switcher & shipping banner ---------- */
  .lang-switch { display: flex; gap: 8px; margin-left: auto; align-items: center; }
  .lang-switch button { background: none; border: none; color: var(--muted); cursor: pointer; font-size: 11px; letter-spacing: 0.1em; text-transform: uppercase; padding: 4px; transition: color 0.3s; }
  .lang-switch button.active { color: var(--gold); font-weight: 500; }
  [lang="en"] { display: none; }
  body.lang-en [lang="es"] { display: none; }
  body.lang-en [lang="en"] { display: block; }
  span[lang] { display: inline; }
  body.lang-en span[lang="en"] { display: inline; }
  .shipping-banner { background: var(--emerald-line); color: var(--gold-soft); text-align: center; font-size: 11.5px; letter-spacing: 0.1em; padding: 6px; text-transform: uppercase; font-weight: 500; }
"""
html = html.replace('/* ---------- capas cinematográficas globales ---------- */', css_injection + '\n  /* ---------- capas cinematográficas globales ---------- */')

js_injection = """
  /* ---------- 8. Language Switcher ---------- */
  const langButtons = document.querySelectorAll('.lang-switch button');
  langButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const lang = btn.dataset.lang;
      document.body.className = lang === 'en' ? 'lang-en' : '';
      langButtons.forEach(b => b.classList.toggle('active', b === btn));
    });
  });
})();
</script>
"""
html = html.replace('})();\n</script>', js_injection, 1)

# 2. Add Shipping Banner at top of body
banner_html = """
<div class="shipping-banner">
  <span lang="es">Envíos internacionales asegurados (FedEx/Brink's) &bull; Esmeraldas Certificadas</span>
  <span lang="en">Worldwide Insured Shipping (FedEx/Brink's) &bull; Certified Emeralds</span>
</div>
"""
html = html.replace('<body>\n', '<body>\n' + banner_html)

# 3. Header modifications
nav_orig = """<nav>
        <a href="#about">Nosotros</a>
        <a href="#process">Proceso</a>
        <a href="#team">Equipo</a>
        <a href="#contact">Contacto</a>
      </nav>"""
nav_new = """<nav>
        <a href="#about"><span lang="es">Nosotros</span><span lang="en">About Us</span></a>
        <a href="#process"><span lang="es">Proceso</span><span lang="en">Process</span></a>
        <a href="#team"><span lang="es">Equipo</span><span lang="en">Team</span></a>
        <a href="#contact"><span lang="es">Contacto</span><span lang="en">Contact</span></a>
      </nav>
      <div class="lang-switch">
        <button data-lang="es" class="active">ES</button>
        <button data-lang="en">EN</button>
      </div>"""
html = html.replace(nav_orig, nav_new)

# 4. Hero section
html = html.replace('<h1>Esmeraldas <em>colombianas</em> para Asia</h1>', 
                    '<h1><span lang="es">Esmeraldas <em>colombianas</em> para Asia</span><span lang="en"><em>Colombian</em> Emeralds for Asia</span></h1>')

html = html.replace('<p class="lede">Diseño, gemología, atelier y exportación en un solo equipo. Conectamos la mina colombiana con la alta joyería de Asia.</p>',
                    '<p class="lede"><span lang="es">Diseño, gemología, atelier y exportación en un solo equipo. Conectamos la mina colombiana con la alta joyería de Asia.</span><span lang="en">Design, gemology, atelier and export in a single team. We connect Colombian mines with high jewelry markets in Asia and globally.</span></p>')

html = html.replace('Ver piezas', '<span lang="es">Ver piezas</span><span lang="en">View Pieces</span>')

# 5. Facts
html = html.replace('<span>Piezas exportadas</span>', '<span><span lang="es">Piezas exportadas</span><span lang="en">Pieces Exported</span></span>')
html = html.replace('<span>Quilates procesados</span>', '<span><span lang="es">Quilates procesados</span><span lang="en">Carats Processed</span></span>')
html = html.replace('<span>Mercados activos</span>', '<span><span lang="es">Mercados activos</span><span lang="en">Active Markets</span></span>')

# 6. What we do
html = html.replace('<h2>Qué hacemos</h2>', '<h2><span lang="es">Qué hacemos</span><span lang="en">What We Do</span></h2>')
html = html.replace('<p>Nuestra propuesta de valor es centralizar todo el proceso. Desde la piedra en bruto hasta la pieza final puesta en su destino.</p>',
                    '<p><span lang="es">Nuestra propuesta de valor es centralizar todo el proceso. Desde la piedra en bruto hasta la pieza final puesta en su destino.</span><span lang="en">Our value proposition is to centralize the entire process. From the rough stone to the final piece delivered to its destination.</span></p>')

html = html.replace('<h3>Diseño</h3>', '<h3><span lang="es">Diseño</span><span lang="en">Design</span></h3>')
html = html.replace('<p>Conceptualizamos joyería de alta gama adaptada a las estéticas del mercado asiático, con renders 3D de precisión milimétrica.</p>',
                    '<p><span lang="es">Conceptualizamos joyería de alta gama adaptada a las estéticas del mercado asiático, con renders 3D de precisión milimétrica.</span><span lang="en">We conceptualize high-end jewelry tailored to Asian market aesthetics, with millimeter-precision 3D renders.</span></p>')

html = html.replace('<h3>Gemología</h3>', '<h3><span lang="es">Gemología</span><span lang="en">Gemology</span></h3>')
html = html.replace('<p>Selección exhaustiva en origen. Certificación independiente para garantizar origen, tratamiento y calidad de la esmeralda.</p>',
                    '<p><span lang="es">Selección exhaustiva en origen. Certificación independiente para garantizar origen, tratamiento y calidad de la esmeralda.</span><span lang="en">Exhaustive selection at the source. Independent certification to guarantee origin, treatment, and quality of the emerald.</span></p>')

html = html.replace('<h3>Exportación</h3>', '<h3><span lang="es">Exportación</span><span lang="en">Export</span></h3>')
html = html.replace('<p>Logística y trámites aduaneros optimizados. Envío seguro y garantizado puerta a puerta para piezas de alto valor.</p>',
                    '<p><span lang="es">Logística y trámites aduaneros optimizados. Envío seguro y garantizado puerta a puerta para piezas de alto valor.</span><span lang="en">Optimized logistics and customs procedures. Secure and guaranteed door-to-door shipping for high-value pieces.</span></p>')

# 7. Featured pieces
html = html.replace('<h2>Piezas destacadas</h2>', '<h2><span lang="es">Piezas destacadas</span><span lang="en">Featured Pieces</span></h2>')
html = html.replace('Especificaciones', '<span lang="es">Especificaciones</span><span lang="en">Specs</span>')
html = html.replace('Esmeralda Muzo', 'Muzo Emerald')
html = html.replace('Oro 18k, Platino', '18k Gold, Platinum')
html = html.replace('Diamantes talla brillante', 'Brilliant-cut Diamonds')

# 8. Team
html = html.replace('<h2>Equipo experto</h2>', '<h2><span lang="es">Equipo experto</span><span lang="en">Expert Team</span></h2>')
html = html.replace('Director General', 'CEO')
html = html.replace('Por confirmar', 'TBD')
html = html.replace('<b>', '<b><span lang="es">')
html = html.replace('</b>', '</span><span lang="en">Expert</span></b>') # simplified replacement

# 9. Priority Markets
html = html.replace('<h2>Mercados prioritarios</h2>', '<h2><span lang="es">Mercados prioritarios</span><span lang="en">Priority Markets</span></h2>')
html = html.replace('<p class="eyebrow reveal">Expansión global</p>', '<p class="eyebrow reveal"><span lang="es">Expansión global</span><span lang="en">Global Expansion</span></p>')
html = html.replace('<p>Operativa logística establecida</p>', '<p><span lang="es">Operativa logística establecida</span><span lang="en">Established Logistics</span></p>')
html = html.replace('<p>Alianzas estratégicas locales</p>', '<p><span lang="es">Alianzas estratégicas locales</span><span lang="en">Local Strategic Alliances</span></p>')

# 10. Process
html = html.replace('<h2>Proceso de exportación</h2>', '<h2><span lang="es">Proceso de exportación</span><span lang="en">Export Process</span></h2>')
html = html.replace('<p class="eyebrow reveal">Operativa de extremo a extremo</p>', '<p class="eyebrow reveal"><span lang="es">Operativa de extremo a extremo</span><span lang="en">End-to-End Operation</span></p>')
html = html.replace('<div class="t">Selección</div>', '<div class="t"><span lang="es">Selección</span><span lang="en">Selection</span></div>')
html = html.replace('<div class="d">Sourcing directo en Colombia y certificación.</div>', '<div class="d"><span lang="es">Sourcing directo en Colombia y certificación.</span><span lang="en">Direct sourcing in Colombia and certification.</span></div>')

html = html.replace('<div class="t">Producción</div>', '<div class="t"><span lang="es">Producción</span><span lang="en">Production</span></div>')
html = html.replace('<div class="d">Renders 3D, fundición y engaste en atelier propio.</div>', '<div class="d"><span lang="es">Renders 3D, fundición y engaste en atelier propio.</span><span lang="en">3D renders, casting and setting in our own atelier.</span></div>')

html = html.replace('<div class="t">Certificación</div>', '<div class="t"><span lang="es">Certificación</span><span lang="en">Certification</span></div>')
html = html.replace('<div class="d">Documentación gemológica y trámites aduaneros.</div>', '<div class="d"><span lang="es">Documentación gemológica y trámites aduaneros.</span><span lang="en">Gemological documentation and customs paperwork.</span></div>')

html = html.replace('<div class="t">Logística</div>', '<div class="t"><span lang="es">Logística</span><span lang="en">Logistics</span></div>')
html = html.replace('<div class="d">Envío internacional asegurado por transportadoras de valores.</div>', '<div class="d"><span lang="es">Envío internacional asegurado por transportadoras de valores.</span><span lang="en">Insured international shipping by secure transport carriers.</span></div>')

# 11. Contact
html = html.replace('<h2>Ponte en contacto</h2>', '<h2><span lang="es">Ponte en contacto</span><span lang="en">Get in Touch</span></h2>')
html = html.replace('<p>Agenda una reunión para discutir requerimientos específicos, compras al por mayor o comisiones privadas.</p>',
                    '<p><span lang="es">Agenda una reunión para discutir requerimientos específicos, compras al por mayor o comisiones privadas.</span><span lang="en">Schedule a meeting to discuss specific requirements, wholesale purchases, or private commissions.</span></p>')

# Add WhatsApp / WeChat
contact_orig = """<div class="kv">
          <div><span>Email</span><a href="mailto:info@apre.co">info@apre.co</a></div>
        </div>"""
contact_new = """<div class="kv">
          <div><span>Email</span><a href="mailto:info@apre.co">info@apre.co</a></div>
          <div><span>WhatsApp</span><a href="#">+57 300 000 0000</a></div>
          <div><span>WeChat</span><span>APRE_Jewelry</span></div>
        </div>"""
html = html.replace(contact_orig, contact_new)

html = html.replace('<div class="eyebrow">Sede Bogotá</div>', '<div class="eyebrow"><span lang="es">Sede Bogotá</span><span lang="en">Bogotá Headquarters</span></div>')
html = html.replace('<div class="eyebrow">Redes sociales</div>', '<div class="eyebrow"><span lang="es">Redes sociales</span><span lang="en">Social Media</span></div>')
html = html.replace('Todos los derechos reservados.', '<span lang="es">Todos los derechos reservados.</span><span lang="en">All rights reserved.</span>')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("HTML update complete.")
