import streamlit as st
import pandas as pd

# Configuración de página (adaptada para móvil)
st.set_page_config(page_title="Mi Menú Semanal", page_icon="🥗", layout="centered")

st.title("🥗 NutriApp La Solana")

# Base de datos simulada para intercambios (Swaps)
alternativas_comida = [
    "Arroz integral (65g) con atún al natural (2 latas) y calabacín",
    "Macarrones integrales (70g) con lomo adobado (120g) y tomate",
    "Quinoa (65g) con pollo a la plancha (120g) y pimientos"
]

# Inicializar estado para los platos si no existe
if 'plato_lunes' not in st.session_state:
    st.session_state.plato_lunes = "Ensalada de pasta integral (70g) con pollo (120g), cherrys y pepino"

# Pestañas de navegación
tab_menu, tab_compra, tab_chat = st.tabs(["📅 Menú", "🛒 Compra", "🤖 IA"])

with tab_menu:
    st.header("Tus Comidas y Cenas")
    st.info("Objetivo por comida+cena: ~700 kcal | 52g Prot | 100g Carb | 40g Grasa")
    
    st.subheader("Lunes")
    st.write("**Comida:**", st.session_state.plato_lunes)
    if st.button("🔄 Cambiar comida del Lunes"):
        import random
        st.session_state.plato_lunes = random.choice(alternativas_comida)
        st.rerun()
        
    st.write("**Cena:** Fajitas caseras (2 tortillas maíz) con ternera (110g), vegetales y salsa burger (15g).")
    st.divider()
    
    st.subheader("Martes")
    st.write("**Comida:** Arroz integral (65g) con tiras de pollo (100g) y anacardos (20g).")
    st.write("**Cena:** Salmorejo casero (300g) con huevo cocido y pavo (50g).")
    st.divider()
    
    st.subheader("Miércoles")
    st.write("**Comida:** Pollo plancha (140g) con patata asada (220g) y calabacín salteado.")
    st.write("**Cena:** Ensalada verde con atún (2 latas), queso light (30g) y 2 tostadas.")

with tab_compra:
    st.header("Lista de la Compra Semanal")
    
    st.subheader("📦 Cash El Almacén")
    st.checkbox("Garbanzos cocidos (1 tarro)")
    st.checkbox("Arroz integral (1 kg)")
    st.checkbox("Pasta integral (1 kg)")
    st.checkbox("Tostadas integrales (1 paq.)")
    
    st.subheader("🛒 Mercadona")
    st.checkbox("Salsa Burger Hacendado (1 bote)")
    st.checkbox("Queso light en lonchas (1 paq.)")
    st.checkbox("Tortillas de maíz (1 paq.)")
    st.checkbox("Fiambre de pavo (1 paq.)")
    
    st.subheader("🍏 Supermercados Consum")
    st.checkbox("Tomates (3 kg)")
    st.checkbox("Tomates cherry (2 tarrinas)")
    st.checkbox("Lechuga / Canónigos (3 bolsas)")
    st.checkbox("Calabacines y Pimientos (1 kg c/u)")
    
    st.subheader("🥩 Family Cash (Tomelloso)")
    st.checkbox("Pechuga de pollo (1,5 kg)")
    st.checkbox("Ternera magra (1 kg)")
    st.checkbox("Lomo adobado magro (1 kg)")

with tab_chat:
    st.header("Actualizar con IA")
    st.write("Dime qué te ha sobrado o qué quieres cambiar para la semana que viene:")
    
    mensaje_usuario = st.text_input("Escribe tu mensaje aquí...")
    if st.button("Enviar"):
        st.success("¡Mensaje recibido! En una versión completa, me conectaría a tu base de datos para generar los nuevos PDFs al instante.")
