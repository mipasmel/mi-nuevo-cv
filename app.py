from flask import Flask, render_template, url_for
import os

app = Flask(__name__)

# --- 1. Definir todos los datos de tu CV en Python ---
# Esto hace que sea más fácil de modificar y menos "HTML" en tu HTML
cv_data = {
    "nombre_completo": "Miguel Pastor Melcón",
    "titulo_profesional": "Backend & Automation Python Developer",
    "descripcion_general": (
        "Desarrollador especializado en Python, con un fuerte interés en la construcción de APIs REST robustas, "
        "la automatización de procesos y la gestión de bases de datos. Busco aplicar mi conocimiento en entornos "
        "backend para crear soluciones eficientes y escalables."
    ),
    "email_contacto": "miguelpasmel@gmail.com",
    "linkedin_url": "https://linkedin.com/in/miguel-pastor-melcon",
    "github_url": "https://github.com/mipasmel",
    "cv_pdf_filename": "CV_Miguel_Pastor_Melcon.pdf", # Nombre del archivo en static
    "foto_perfil_filename": "profile.jpg", # Nombre del archivo en static
    "ubicacion": "Oviedo, Asturias, España",

    "sobre_mi_contenido": (
        "Como desarrollador Python, mi objetivo es transformar problemas complejos en soluciones de software elegantes y eficientes. "
        "Cuento con una base sólida en el ecosistema de Python, incluyendo frameworks como <strong>Flask</strong> y librerías para la "
        "manipulación de datos como <strong>Pandas</strong> y <strong>NumPy</strong>. Mi experiencia se complementa con el manejo de bases de datos "
        "<strong>SQL (SQLite, PostgreSQL)</strong> y el control de versiones con <strong>Git</strong>. Busco una posición de desarrollador junior donde "
        "pueda contribuir al desarrollo de productos backend, optimizar flujos de trabajo mediante la <strong>automatización</strong> y "
        "crecer junto a un equipo innovador."
    ),

    "proyectos": [
        {
            "titulo": "Sistema de gestión de tareas",
            "descripcion": "App web en Flask para gestionar tareas, con edición, colaboración y carga de imágenes.",
            "link": "https://github.com/mipasmel/Sistema-de-Gestion-de-Tareas-Web"
        },
        {
            "titulo": "Adivina un número aleatorio",
            "descripcion": "Juego en Python donde el usuario intenta adivinar un número generado por la máquina. Manejo de errores incluido.",
            "link": "https://github.com/mipasmel/Adivina-un-n-mero-aleatorio"
        },
        {
            "titulo": "Calculadora",
            "descripcion": "Calculadora de operaciones básicas con gestión de errores. Proyecto desarrollado en Python.",
            "link": "https://github.com/mipasmel/Mi-primera-calculadora"
        },
    ],

    "habilidades_tecnicas": [
        "Python", "Flask", "Pandas", "NumPy", "requests",
        "SQLite", "PostgreSQL", "Git", "GitHub", "VS Code", "Windows", "Análisis de datos"
    ],

    "soft_skills": [
        "Resolución de Problemas", "Aprendizaje Continuo y Rápido", "Pensamiento Lógico y Analítico",
        "Comunicación Efectiva", "Trabajo en Equipo", "Adaptabilidad", "Proactividad"
    ],

    "formacion_academica": [
        {"fecha": "Jul. 2025", "titulo": "Python for Data Science", "institucion": "IBM"},
        {"fecha": "Jul. 2025", "titulo": "Introducción al análisis de datos con Python", "institucion": "Desafío Latam"},
        {"fecha": "Jun. 2025", "titulo": "Certificate of Accomplishment Python", "institucion": "HackerRank"},
        {"fecha": "Feb. 2025", "titulo": "Curso de Python", "institucion": "Santander Open Academy"},
        {"fecha": "Jun. 2015", "titulo": "Facultad de Formación del Profesorado y Educación", "institucion": "Oviedo"},
    ]
}

@app.route("/")
def index():
    # Pasa el diccionario cv_data completo a la plantilla
    return render_template("index.html", **cv_data) # **cv_data desempaqueta el diccionario en argumentos de palabra clave

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)