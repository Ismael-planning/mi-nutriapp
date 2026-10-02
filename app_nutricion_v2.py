import streamlit as st
import pandas as pd

# Configuración de página
st.set_page_config(page_title="Mi Menú y Compra", page_icon="🥗", layout="centered")

st.title("🥗 NutriApp La Solana")

# Base de datos maestra de alimentos (Inventario total)
# 'necesario' indica si hace falta para el menú de esta semana
# 'comprado' indica si ya lo tienes en la despensa/nevera
if 'inventario' not in st.session_state:
    st.session_state.inventario = {
        "📦 Cash El Almacén": [
            {"item": "Aceite de Oliva Virgen Extra (AOVE)", "peso": "Garrafa 5L", "necesario": False, "comprado": True},
            {"item": "Garbanzos cocidos", "peso": "1 tarro (800g escurrido)", "necesario": True, "comprado": True},
            {"item": "Arroz integral", "peso": "1 kg (seco)", "necesario": True, "comprado": True},
            {"item": "Pasta integral", "peso": "1 kg (seco)", "necesario": True, "comprado": True},
            {"item": "Tostadas integrales", "peso": "1 paq. grande", "necesario": True, "comprado": False},
        ],
        "🛒 Mercadona": [
            {"item": "Salsa Burger Hacendado", "peso": "1 bote", "necesario": True, "comprado": False},
            {"item": "Queso light en lonchas", "peso": "1 paq.", "necesario": True, "comprado": True},
            {"item": "Tortillas de maíz", "peso": "1 paq.", "necesario": True, "comprado": False},
            {"item": "Fiambre de pavo cocido", "peso": "1 paq.", "necesario": True, "comprado": True},
            {"item": "Frutos secos (Nueces/Anacardos/Pistachos)", "peso": "3 paq.", "necesario": True, "comprado": True},
            {"item": "Salmón ahumado", "peso": "2 paq.", "necesario": False, "comprado": False},
            {"item": "Queso crema light", "peso": "1 tarrina", "necesario": False, "comprado": False},
        ],
        "🍏 Supermercados Consum": [
            {"item": "Tomates (salmorejo/ensalada)", "peso": "3 kg", "necesario": True, "comprado": True},
            {"item": "Tomates cherry", "peso": "2 tarrinas", "necesario": True, "comprado": False},
            {"item": "Lechuga / Canónigos", "peso": "3 bolsas", "necesario": True, "comprado": False},
            {"item": "Pepinos", "peso": "1 kg", "necesario": True, "comprado": True},
            {"item": "Zanahorias", "peso": "1 kg", "necesario": True, "comprado": True},
            {"item": "Cebollas", "peso": "1 kg", "necesario": True, "comprado": False},
            {"item": "Calabacines", "peso": "1 kg", "necesario": True, "comprado": False},
            {"item": "Pimientos verde/rojo", "peso": "1 kg", "necesario": True, "comprado": False},
            {"item": "Patatas / Batatas", "peso": "2-3 kg", "necesario": True, "comprado": False},
            {"item": "Quinoa", "peso": "500g (seco)", "necesario": False, "comprado": False},
            {"item": "Merluza o Bacalao", "peso": "1 kg", "necesario": False, "comprado": False},
        ],
        "🥩 Family Cash (Tomelloso)": [
            {"item": "Pechuga de pollo", "peso": "1,5 kg", "necesario": True, "comprado": True},
            {"item": "Ternera magra", "peso": "1 kg", "necesario": True, "comprado": True},
            {"item": "Lomo adobado magro", "peso": "1 kg", "necesario": True, "comprado": True},
            {"item": "Tiras de pollo preparadas", "peso": "2 paq.", "necesario": True, "comprado": True},
        ]
    }

# Pestañas de navegación
tab_menu, tab_compra, tab_chat = st.tabs(["📅 Menú", "🛒 Lista de la Compra", "🤖 IA"])

with tab_menu:
    st.header("Menú de esta semana")
    st.info("Objetivo por comida+cena: ~700 kcal | 52g Prot | 100g Carb | 40g Grasa")
    
    st.write("**Lunes**")
    st.write("🍽️ **Comida:** Salmorejo sobrante (250g) con tiras de pollo (90g) y huevo duro.")
    st.write("🌙 **Cena:** Fajitas (2 tortillas) con ternera (110g), vegetales y salsa burger (15g).")
    st.divider()
    
    st.write("**Martes**")
    st.write("🍽️ **Comida:** Arroz integral (65g seco) con pollo plancha (120g) y calabacín.")
    st.write("🌙 **Cena:** Ensalada de lechuga, pepino y tomate con pavo (50g) y anacardos (15g).")
    st.divider()
    
    st.button("🔄 Cambiar comida del martes")

with tab_compra:
    st.header("Lista de la Compra Inteligente")
    st.write("Marca lo que ya tienes en casa o vayas metiendo en el carrito. Los productos que no necesitas esta semana están ocultos o marcados al final.")
    
    for super_name, productos in st.session_state.inventario.items():
        st.subheader(super_name)
        
        # Mostrar solo los necesarios para la semana
        necesarios = [p for p in productos if p['necesario']]
        no_necesarios = [p for p in productos if not p['necesario']]
        
        if necesarios:
            for i, prod in enumerate(necesarios):
                # Usar el estado de la sesión para el checkbox
                checked = st.checkbox(
                    f"{prod['item']} - {prod['peso']}", 
                    value=prod['comprado'], 
                    key=f"{super_name}_{i}"
                )
                # Actualizar el estado si cambia
                st.session_state.inventario[super_name][i]['comprado'] = checked
        else:
            st.write("*No necesitas comprar nada aquí esta semana.*")
            
        with st.expander(f"Ver catálogo completo de {super_name}"):
            st.write("Productos que sueles comprar pero NO necesitas esta semana:")
            for p in no_necesarios:
                st.write(f"- 💤 {p['item']} ({p['peso']})")
        
        st.divider()

with tab_chat:
    st.header("Habla con la IA")
    st.write("Ejemplo: 'Me he quedado sin pollo, añádelo a la lista' o 'Genera el menú de la próxima semana, me sobra arroz.'")
    st.text_input("Escribe tu instrucción...")
    st.button("Actualizar App")
