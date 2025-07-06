import streamlit as st
import pandas as pd
import os

DATA_FILE = "datos_personales.csv"

CAMPOS = [
    "Nombre y apellido", "Legajo personal", "DNI", "Domicilio", "Teléfono", "Número de obra social",
    "Situación de revista", "Marca de armamento", "Número de serie del arma", "Número de armamento",
    "Marca de chaleco balístico", "Modelo del chaleco", "Número de serie del chaleco",
    "Número de lote de chaleco", "Fecha de fabricación del chaleco",
    "¿Posee bastón tonfa asignado?", "¿Piloto de lluvia policial asignado?"
]

if os.path.exists(DATA_FILE):
    df = pd.read_csv(DATA_FILE)
else:
    df = pd.DataFrame(columns=CAMPOS)

st.title("🔍 Registro Policial Personalizado")

st.header("Buscar Persona")
nombre_buscar = st.text_input("Ingresá nombre y apellido")

if nombre_buscar:
    resultado = df[df["Nombre y apellido"].str.lower() == nombre_buscar.lower()]
    if not resultado.empty:
        st.success("Datos encontrados:")
        st.dataframe(resultado)
    else:
        st.warning("No se encontraron registros con ese nombre.")

st.divider()

st.header("Agregar / Editar Persona")
data = {}
for campo in CAMPOS:
    if "¿" in campo:
        data[campo] = st.selectbox(campo, ["Sí", "No"])
    elif "Fecha" in campo:
        data[campo] = st.date_input(campo)
    else:
        data[campo] = st.text_input(campo)

if st.button("Guardar Datos"):
    df = df[df["Nombre y apellido"].str.lower() != data["Nombre y apellido"].lower()]
    df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
    df.to_csv(DATA_FILE, index=False)
    st.success("✅ Datos guardados correctamente")

if st.checkbox("Mostrar todos los registros"):
    st.dataframe(df)
    import streamlit as st
import pandas as pd

# Cargar datos
df = pd.read_csv('empleados.csv')

# CSS para cambiar fondo
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1507525428034-b723cf961d3e");
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title('Base de Datos de Empleados')

# Buscador por DNI
dni = st.text_input('Buscar por DNI:')

if dni:
    resultado = df[df['DNI'] == int(dni)]
    st.write(resultado)
else:
    st.write(df)
    <style>
.stApp {
    background-image: "url(https://www.google.com/search?q=imagen+de+pfa&oq=imagen+de+pfa&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIICAEQABgWGB4yCggCEAAYgAQYogQyCggDEAAYgAQYogQyBwgEEAAY7wUyBwgFEAAY7wXSAQg2Mzg5ajBqN6gCFLACAfEF3dElwStEwzA&client=ms-android-samsung-ss&sourceid=chrome-mobile&ie=UTF-8#vhid=sH-et-wctkp1nM&vssid=_J4xqaIWyJZOf5OUP4qGemQI_50");
    background-size: cover;
}
</style>
