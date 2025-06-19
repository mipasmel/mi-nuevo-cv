🚀 Mi CV Interactivo | Miguel Pastor Melcón
¡Bienvenido al repositorio de mi Curriculum Vitae interactivo, diseñado como una aplicación web con Flask! Este proyecto es más que un simple documento; es una demostración práctica de mis habilidades en desarrollo Backend con Python y un ejemplo de cómo aplico tecnologías web para crear soluciones dinámicas y eficientes.

✨ Características Destacadas
Aplicación Web Dinámica: Construido con Flask, este CV se sirve como una aplicación web completa, demostrando mi capacidad para configurar y gestionar proyectos Python basados en la web.
Contenido Gestionado por Python: Toda la información del CV (proyectos, habilidades, formación, etc.) se define en el código Python (app.py), y es inyectada en la plantilla HTML (index.html) usando Jinja2. Esto facilita la actualización y el mantenimiento del contenido sin tocar el HTML.
Diseño Moderno y Responsivo: Utiliza Tailwind CSS para un diseño limpio, moderno y completamente adaptable a cualquier dispositivo (móvil, tablet, escritorio).
Experiencia de Usuario Mejorada: Incorpora animaciones sutiles con JavaScript para una interacción fluida y atractiva.
Enlaces Externos Seguros: Todos los enlaces a mis perfiles externos (LinkedIn, GitHub) y correo electrónico se abren en nuevas pestañas con seguridad mejorada (target="_blank" rel="noopener noreferrer").
Facilidad de Despliegue: Preparado para un despliegue sencillo en plataformas de hosting como Heroku, Railway o Render.
🛠️ Tecnologías Utilizadas
Python 3.12.10: El corazón del proyecto, manejando la lógica y la gestión de datos.
Flask: Micro-framework web para Python, utilizado para servir la aplicación.
Jinja2: Motor de plantillas de Flask, que permite la inyección de datos Python en el HTML.
HTML5: Estructura del contenido.
CSS3 (Tailwind CSS): Framework CSS de utilidad-first para un diseño rápido y responsivo.
JavaScript: Para interacciones y animaciones en el lado del cliente (Scroll Reveal).
Font Awesome: Iconografía profesional.
📂 Estructura del Proyecto
mi-nuevo-cv/
├── app.py                  # La aplicación Flask principal
├── templates/
│   └── index.html          # Plantilla HTML con Jinja2
└── static/
    ├── profile.jpg         # Mi foto de perfil
    └── CV_Miguel_Pastor_Melcon.pdf # Versión descargable del CV en PDF
├── .gitignore              # Archivos y carpetas a ignorar por Git
└── README.md               # Este archivo
🚀 Cómo Ejecutarlo Localmente
Sigue estos sencillos pasos para tener mi CV funcionando en tu máquina:

Clona el repositorio:
Bash

git clone https://github.com/mipasmel/mi-nuevo-cv.git
cd mi-nuevo-cv
Crea y activa un entorno virtual (recomendado):
Bash

python -m venv venv
En Windows:

Bash

.\venv\Scripts\activate
En macOS/Linux:

Bash

source venv/bin/activate
Instala las dependencias:
Bash

pip install Flask
Ejecuta la aplicación Flask:
Bash

python app.py
Accede al CV:
Abre tu navegador web y visita http://127.0.0.1:5000 (o el puerto que se muestre en la terminal).

📬 Contacto
Si tienes alguna pregunta, sugerencia, o simplemente quieres conectar, no dudes en contactarme:

Email: miguelpasmel@gmail.com
LinkedIn: Miguel Pastor Melcón
GitHub: mipasmel
© 2025 Miguel Pastor Melcón. Diseñado con ❤️ y código.
