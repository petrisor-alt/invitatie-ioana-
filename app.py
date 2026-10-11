import streamlit as st
from datetime import datetime, time
import urllib.parse

# ⚠️ PUNE NUMĂRUL TĂU AICI (cu 40 în față, fără spatii sau +):
NUMAR_TELEFON = "400749824848"  # <--- Schimbă cu numărul tău!

st.set_page_config(page_title="O întrebare importantă...", page_icon="❤️", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .title-text { text-align: center; color: #ff4b4b; font-size: 2.5rem; font-weight: bold; }
    .subtitle-text { text-align: center; color: #31333F; font-size: 1.2rem; }
    </style>
""", unsafe_allow_html=True)

if "raspuns_confirmat" not in st.session_state:
    st.session_state.raspuns_confirmat = False

if "buton_nu_apasari" not in st.session_state:
    st.session_state.buton_nu_apasari = 0

st.markdown('<p class="title-text">Hei! Am o întrebare serioasă pentru tine... 🫵</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle-text">Vrei să ieșim la o întâlnire săptămâna asta? ☕✨</p>', unsafe_allow_html=True)

st.write("")
st.write("")

if not st.session_state.raspuns_confirmat:
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🥰 DA, evident!", use_container_width=True):
            st.session_state.raspuns_confirmat = True
            st.rerun()

    with col2:
        mesaje_nu = [
            "Nu 😢", 
            "Sigur ești sigură?", 
            "Mai gândește-te!", 
            "Butonul ăsta e stricat 🤖", 
            "Nici o șansă să apeși aici!", 
            "Ia mai apasă o dată pe DA 😌"
        ]
        
        text_nu_curent = mesaje_nu[min(st.session_state.buton_nu_apasari, len(mesaje_nu) - 1)]
        
        if st.button(text_nu_curent, use_container_width=True):
            st.session_state.buton_nu_apasari += 1
            st.rerun()
            
    if st.session_state.buton_nu_apasari > 0:
        st.info("💡 Hint: Sistemul a detectat că butonul de 'Nu' nu funcționează corect. Singura opțiune validă a rămas cea stângă! 😇")

else:
    st.balloons()
    st.success("Yuhuu! Știam eu! 🎉 Acum, partea logistică:")

    st.subheader("🗓️ Alege data și ora care îți convin:")
    
    ziua_aleasa = st.date_input("În ce zi ne vedem?", min_value=datetime.today())
    ora_aleasa = st.time_input("La ce oră?", value=time(18, 0))

    locatie_aleasa = st.selectbox(
        "Unde mergem?",
        ["☕ O cafenea drăguță în oraș", "🍰 La o prăjitură bună", "🧋 Bubble tea", "🚶‍♂️ O plimbare în parc"]
    )

    data_str = ziua_aleasa.strftime('%A, %d %B %Y')
    ora_str = ora_aleasa.strftime('%H:%M')
    
    # Textul care se va trimite pe WhatsApp
    mesaj_wa = f"Hei! Am ales detaliile pentru întâlnire:\n- 📅 Data: {data_str}\n- ⏰ Ora: {ora_str}\n- 📍 Locația: {locatie_aleasa}\n\nAbia aștept! ✨"
    mesaj_encoded = urllib.parse.quote(mesaj_wa)
    
    link_whatsapp = f"https://wa.me/{NUMAR_TELEFON}?text={mesaj_encoded}"

    st.write("")
    st.markdown(f'''
        <a href="{link_whatsapp}" target="_blank" style="text-decoration: none;">
            <div style="
                background-color: #25D366;
                color: white;
                padding: 14px 20px;
                text-align: center;
                border-radius: 10px;
                font-size: 18px;
                font-weight: bold;
                box-shadow: 0px 4px 10px rgba(0,0,0,0.15);
            ">
                📲 Trimite-mi confirmarea pe WhatsApp! 🚀
            </div>
        </a>
    ''', unsafe_allow_html=True)

    st.markdown(f"""
    <br>
    
    ### Detalii selectate: 🥳
    - **Data:** {data_str}
    - **Ora:** {ora_str}
    - **Locația:** {locatie_aleasa}
    """, unsafe_allow_html=True)