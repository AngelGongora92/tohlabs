import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Header Button
content = content.replace(
    'href="https://wa.me/529996182892?text=Hola%20Toh%20Labs,%20me%20gustar%C3%ADa%20cotizar%20un%20proyecto"',
    'href="mailto:contacto@tohlabs.mx?subject=Cotizar%20un%20proyecto"'
)
content = content.replace(
    '<i data-lucide="message-circle" class="w-4 h-4"></i>\n          <span>WhatsApp Directo</span>',
    '<i data-lucide="mail" class="w-4 h-4"></i>\n          <span>Contacto Directo</span>'
)

# 2. Hero Section
content = content.replace(
    'href="https://wa.me/529996182892?text=Hola,%20solicito%20una%20sesi%C3%B3n%20de%20diagn%C3%B3stico%20para%20mi%20empresa"',
    'href="mailto:contacto@tohlabs.mx?subject=Diagnóstico%20Gratuito"'
)
content = content.replace(
    '<i data-lucide="phone-call" class="w-5 h-5"></i>\n          Agendar Diagnóstico Gratuito',
    '<i data-lucide="calendar" class="w-5 h-5"></i>\n          Agendar Diagnóstico Gratuito'
)

# 3. Card 1
content = content.replace(
    'href="https://wa.me/529996182892?text=Quiero%20probar%20el%20demo%20del%20Recepcionista%20Telef%C3%B3nico%20con%20Voz%20IA"',
    'href="mailto:contacto@tohlabs.mx?subject=Demo%20Recepcionista"'
)
content = content.replace(
    'Envío del resumen directo a WhatsApp',
    'Envío del resumen a tu correo o CRM'
)

# 4. Card 2
content = content.replace(
    'href="https://wa.me/529996182892?text=Me%20interesa%20el%20Mesero%20Virtual%20para%20men%C3%BA%20o%20cat%C3%A1logo"',
    'href="mailto:contacto@tohlabs.mx?subject=Mesero%20Virtual"'
)
content = content.replace(
    'Exporta la comanda armada a WhatsApp',
    'Exporta la comanda armada a tu sistema'
)

# 5. Card 3
content = content.replace(
    'href="https://wa.me/529996182892?text=Solicito%20informaci%C3%B3n%20sobre%20el%20Asistente%20RAG%20de%20Conocimiento%20Corporativo"',
    'href="mailto:contacto@tohlabs.mx?subject=Información%20Asistente%20RAG"'
)

# 6. Contact Section Buttons
# Original contact section has a WhatsApp button and a Mail button.
# Let's remove the WhatsApp button and just keep the email button, or keep both as different options?
# Actually, the user says "quita todo lo referente al numero de telefono y mejor pon el correo". 
# So let's replace the WhatsApp button entirely with just an action to email.
# To make it easier, let's just do a regex sub for the contact block.
contact_block_old = """        <!-- Botones de Contacto Inmediato -->
        <div class="flex flex-col sm:flex-row items-center justify-center gap-4">
          <!-- WhatsApp con el número indicado -->
          <a href="https://wa.me/529996182892?text=Hola%20Toh%20Labs,%20me%20gustar%C3%ADa%20cotizar%20un%20proyecto" 
             target="_blank"
             class="w-full sm:w-auto inline-flex items-center justify-center gap-3 px-8 py-4 rounded-xl bg-[#25D366] text-black font-bold text-base hover:bg-[#20ba5a] transition shadow-lg shadow-[#25D366]/20">
            <i data-lucide="message-circle" class="w-5 h-5"></i>
            WhatsApp: 999 618 2892
          </a>

          <!-- Correo tohlabs.mx -->
          <a href="mailto:contacto@tohlabs.mx" 
             class="w-full sm:w-auto inline-flex items-center justify-center gap-3 px-8 py-4 rounded-xl bg-white/5 border border-white/15 text-white font-medium text-base hover:bg-white/10 transition">
            <i data-lucide="mail" class="w-5 h-5"></i>
            contacto@tohlabs.mx
          </a>
        </div>"""
        
contact_block_new = """        <!-- Botones de Contacto Inmediato -->
        <div class="flex flex-col sm:flex-row items-center justify-center gap-4">
          <!-- Correo tohlabs.mx -->
          <a href="mailto:contacto@tohlabs.mx" 
             class="w-full sm:w-auto inline-flex items-center justify-center gap-3 px-8 py-4 rounded-xl bg-toh-turquoise text-black font-bold text-base hover:bg-toh-cyanGlow transition shadow-lg shadow-toh-turquoise/20">
            <i data-lucide="mail" class="w-5 h-5"></i>
            Escríbenos a contacto@tohlabs.mx
          </a>
        </div>"""
content = content.replace(contact_block_old, contact_block_new)

# 7. Floating Button
floating_old = """  <!-- BOTÓN FLOTANTE DE WHATSAPP -->
  <a href="https://wa.me/529996182892?text=Hola%20Toh%20Labs,%20quiero%20m%C3%A1s%20informaci%C3%B3n" 
     target="_blank" 
     class="fixed bottom-6 right-6 z-50 p-4 rounded-full bg-[#25D366] text-black shadow-2xl hover:scale-110 active:scale-95 transition duration-200 flex items-center justify-center group"
     aria-label="Contactar por WhatsApp">
    <i data-lucide="message-circle" class="w-6 h-6"></i>
  </a>"""
  
floating_new = """  <!-- BOTÓN FLOTANTE DE CONTACTO -->
  <a href="mailto:contacto@tohlabs.mx" 
     class="fixed bottom-6 right-6 z-50 p-4 rounded-full bg-toh-turquoise text-black shadow-2xl hover:scale-110 active:scale-95 transition duration-200 flex items-center justify-center group"
     aria-label="Contactar por Correo">
    <i data-lucide="mail" class="w-6 h-6"></i>
  </a>"""
content = content.replace(floating_old, floating_new)

# 8. Footer
footer_old = '<a href="https://wa.me/529996182892" class="hover:text-white transition">+52 (999) 618-2892</a>'
footer_new = ''
content = content.replace(footer_old, footer_new)

# 9. Also any other whatsapp mentions
content = content.replace('botón de WhatsApp inmediato', 'botón de contacto inmediato')
content = content.replace('directo a WhatsApp', 'directo a tu sistema')
content = content.replace('Bots de WhatsApp 24/7', 'Agentes Virtuales 24/7')
content = content.replace('WhatsApp:', 'Contacto:')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

