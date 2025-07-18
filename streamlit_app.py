import streamlit as st
import sqlite3

# Conexión a la base de datos
conn = sqlite3.connect('comisaria.db')
cursor = conn.cursor()

st.title("BASE DE DATOS COMISARÍA TERMINAL DE ÓMNIBUS")

st.subheader("DATOS PERSONALES")

dni_input = st.text_input("Ingrese DNI para buscar:")

if dni_input:
    cursor.execute("SELECT * FROM Personal WHERE dni=?", (dni_input,))
    personal = cursor.fetchone()

    if personal:
        st.write(f"**Nombre y Apellido:** {personal[1]}")
        st.write(f"**Legajo Personal:** {personal[2]}")
        st.write(f"**Obra Social:** {personal[4]}")
        st.write(f"**Número de Contacto:** {personal[5]}")
        st.write(f"**Domicilio:** {personal[6]}")

        st.subheader("ARMAMENTO ASIGNADO")
        cursor.execute("SELECT * FROM Armamento WHERE id_personal=?", (personal[0],))
        arma = cursor.fetchone()
        if arma:
            st.write(f"**Marca:** {arma[2]}")
            st.write(f"**Modelo:** {arma[3]}")
            st.write(f"**N° Serie:** {arma[4]}")
            st.write(f"**N° Arma:** {arma[5]}")
        else:
            st.write("Sin armamento asignado.")

        st.subheader("CHALECO BALÍSTICO")
        cursor.execute("SELECT * FROM Chaleco_Balistico WHERE id_personal=?", (personal[0],))
        chaleco = cursor.fetchone()
        if chaleco:
            st.write(f"**Marca:** {chaleco[2]}")
            st.write(f"**Modelo:** {chaleco[3]}")
            st.write(f"**N° Chaleco:** {chaleco[4]}")
        else:
            st.write("Sin chaleco asignado.")
    else:
        st.warning("No se encontró personal con ese DNI.")
