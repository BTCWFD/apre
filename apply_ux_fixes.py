import re

html_path = r'C:\Program Files\PROYECTOS DE PROGRAMACION\APRE\index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add Auto-language detection
js_detection = """
  /* ---------- 8. Language Switcher & Auto-detect ---------- */
  const langButtons = document.querySelectorAll('.lang-switch button');
  
  function setLanguage(lang) {
    document.body.className = lang === 'en' ? 'lang-en' : '';
    langButtons.forEach(b => b.classList.toggle('active', b.dataset.lang === lang));
  }

  // Auto-detect based on browser language
  const userLang = navigator.language || navigator.userLanguage;
  if (!userLang.toLowerCase().startsWith('es')) {
    setLanguage('en');
  }

  langButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      setLanguage(btn.dataset.lang);
    });
  });
"""

# Replace the previous language switcher logic
old_js = """
  /* ---------- 8. Language Switcher ---------- */
  const langButtons = document.querySelectorAll('.lang-switch button');
  langButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const lang = btn.dataset.lang;
      document.body.className = lang === 'en' ? 'lang-en' : '';
      langButtons.forEach(b => b.classList.toggle('active', b === btn));
    });
  });
"""
html = html.replace(old_js.strip(), js_detection.strip())

# 2. Update WhatsApp link
old_wa = '<div><span>WhatsApp</span><a href="#">+57 300 000 0000</a></div>'
new_wa = '<div><span>WhatsApp</span><a href="https://wa.me/573000000000" target="_blank" rel="noopener noreferrer">+57 300 000 0000</a></div>'
html = html.replace(old_wa, new_wa)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("HTML refinements complete.")
