
import streamlit as st
import streamlit.components.v1 as components
import base64
import os
import random
from pathlib import Path

# ==========================================
# CONFIGURACIÓN PERSONALIZADA
# ==========================================

NOMBRE_ELLA = "Mami shica"
NOMBRE_TUYO = "Tu Papi rico"
TITULO = "El tesoro más bonito del Grand Line"

st.set_page_config(
    page_title="Para mi Mami shica 💗",
    page_icon="💖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ==========================================
# ESTADO DE LA AVENTURA
# ==========================================

if "islas" not in st.session_state:
    st.session_state.islas = []

if "deseo" not in st.session_state:
    st.session_state.deseo = False

if "vela" not in st.session_state:
    st.session_state.vela = False

if "tesoro" not in st.session_state:
    st.session_state.tesoro = False

if "carta" not in st.session_state:
    st.session_state.carta = False


def visitar_isla(numero):
    if numero not in st.session_state.islas:
        st.session_state.islas.append(numero)


def audio_base64():
    ruta = Path("assets/one_piece.mp3")
    if ruta.exists():
        return base64.b64encode(ruta.read_bytes()).decode()
    return None


# ==========================================
# ESTILO GENERAL
# ==========================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Quicksand:wght@400;500;600;700&display=swap');

html, body, [class*="css"], .stApp {
    font-family: 'Quicksand', sans-serif;
}

.stApp {
    background:
        radial-gradient(ellipse at 15% 20%, #56265b55, transparent 45%),
        radial-gradient(ellipse at 90% 80%, #872a6d44, transparent 40%),
        linear-gradient(145deg, #08071e, #171034 52%, #090817);
    color: #fff4fc;
}

.block-container {
    max-width: 1050px;
    padding-top: 2rem;
    padding-bottom: 5rem;
}

h1, h2, h3 {
    text-align: center;
    color: #ffe0f5 !important;
}

.stButton > button {
    border: 1px solid #ff92d4 !important;
    background: linear-gradient(120deg, #a22d8b, #e54a9c) !important;
    color: white !important;
    border-radius: 30px !important;
    font-weight: bold !important;
    padding: 0.6rem 1.5rem !important;
    width: 100%;
    transition: 0.3s;
}

.stButton > button:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 25px #ff66bb99;
}

.magic-title {
    font-family: 'Great Vibes', cursive;
    font-size: clamp(55px, 9vw, 105px);
    line-height: 1.2;
    text-align: center;
    background: linear-gradient(90deg, #ffc7e9, #fff5ba, #ff99d3);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    filter: drop-shadow(0 0 12px #f568b855);
    margin: 25px 0;
}

.subtitle {
    text-align: center;
    font-size: 20px;
    color: #f8d5ec;
    letter-spacing: 1px;
}

.glass {
    background: rgba(255, 255, 255, 0.065);
    border: 1px solid rgba(255, 188, 225, 0.25);
    border-radius: 23px;
    padding: 30px;
    margin: 20px 0;
    box-shadow: 0 10px 40px #00000030;
    backdrop-filter: blur(8px);
}

.romantic {
    text-align: center;
    line-height: 2.1;
    color: #ffe7f5;
    font-size: 18px;
}

.section-title {
    font-family: 'Great Vibes', cursive;
    text-align: center;
    font-size: 55px;
    color: #ffb8e2;
    margin-top: 40px;
}

.treasure {
    background: linear-gradient(135deg, #4a2355, #983d78, #57346d);
    border: 2px solid #ffe1a7;
    padding: 30px;
    border-radius: 25px;
    text-align: center;
    box-shadow: 0 0 35px #e18ec355;
}

.small-note {
    color: #e9bddd;
    text-align: center;
    font-size: 14px;
}

.stProgress > div > div {
    background: linear-gradient(90deg, #ed68c1, #ffe8a1);
}

[data-testid="stImage"] img {
    border-radius: 20px;
}

footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)


# ==========================================
# FONDO ANIMADO
# ==========================================

components.html("""
<style>
body { margin:0; overflow:hidden; background:transparent; }
.star {
    position:absolute;
    color:white;
    animation: shine 3s infinite alternate;
}
.heart {
    position:absolute;
    bottom:-40px;
    animation: floatUp linear infinite;
}
@keyframes shine {
    from {opacity:.1;transform:scale(.5)}
    to {opacity:1;transform:scale(1.4)}
}
@keyframes floatUp {
    from {transform:translateY(0);opacity:0}
    15% {opacity:.85}
    85% {opacity:.7}
    to {transform:translateY(-700px);opacity:0}
}
</style>
<script>
for(let i=0;i<75;i++){
    const el=document.createElement("span");
    el.className="star";
    el.textContent="✦";
    el.style.left=Math.random()*100+"%";
    el.style.top=Math.random()*100+"%";
    el.style.fontSize=(Math.random()*12+4)+"px";
    el.style.animationDelay=Math.random()*4+"s";
    document.body.appendChild(el);
}
for(let i=0;i<18;i++){
    const el=document.createElement("span");
    el.className="heart";
    el.textContent=["💗","💕","✨","🌸"][Math.floor(Math.random()*4)];
    el.style.left=Math.random()*100+"%";
    el.style.fontSize=(Math.random()*17+10)+"px";
    el.style.animationDuration=(Math.random()*9+8)+"s";
    el.style.animationDelay=(-Math.random()*15)+"s";
    document.body.appendChild(el);
}
</script>
""", height=125)


# ==========================================
# PORTADA
# ==========================================

st.markdown(
    '<div class="magic-title">El tesoro más bonito<br>del Grand Line</div>',
    unsafe_allow_html=True
)

st.markdown(
    f'<div class="subtitle">Una aventura creada para {NOMBRE_ELLA} 💗</div>',
    unsafe_allow_html=True
)

st.markdown(f"""
<div class="glass romantic">
    🏴‍☠️ Había una vez un pirata que recorrió miles de mares
    buscando el tesoro más extraordinario del universo.

    Pero un día descubrió que el tesoro no estaba escondido
    en ninguna isla...

    <b>Tenía una sonrisa hermosa, unos ojitos preciosos
    y un nombre que hacía latir su corazón.</b>

    Ese nombre era <b>{NOMBRE_ELLA}</b>.

    <br><br>
    Y aquel pirata era...

    <b>{NOMBRE_TUYO}</b> 💗
</div>
""", unsafe_allow_html=True)

st.markdown(
    '<p class="small-note">🌊 Nuestra aventura está por comenzar 🌊</p>',
    unsafe_allow_html=True
)

# ==========================================
# MÚSICA
# ==========================================

st.markdown(
    '<div class="section-title">La melodía de nuestra aventura 🎵</div>',
    unsafe_allow_html=True
)

audio = audio_base64()

if audio:
    st.audio(
        "assets/one_piece.mp3",
        format="audio/mpeg"
    )
else:
    st.info(
        "🎶 Para escuchar nuestro soundtrack de One Piece, "
        "coloca el archivo one_piece.mp3 dentro de la carpeta assets."
    )

st.caption("Presiona reproducir para comenzar a escuchar la música.")


# ==========================================
# MAPA DEL AMOR
# ==========================================

st.markdown(
    '<div class="section-title">🗺️ El mapa de nuestro amor</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="glass romantic">
    Seis islas mágicas.

    Seis pequeños pedacitos de mi corazón.

    En cada isla encontrarás algo que quiero decirte.

    Explóralas todas para desbloquear
    <b>el tesoro legendario de nuestro amor.</b>
</div>
""", unsafe_allow_html=True)

islas = [
    ("🌸", "Isla de tu sonrisa"),
    ("💌", "Isla de las cartas"),
    ("🌟", "Isla de las estrellas"),
    ("💍", "Isla de las promesas"),
    ("🎂", "Isla del cumpleaños"),
    ("👑", "Isla de mi reina"),
]

visitadas = len(st.session_state.islas)

st.progress(visitadas / 6)
st.markdown(
    f'<p class="small-note">✨ Islas descubiertas: {visitadas} de 6</p>',
    unsafe_allow_html=True
)

columnas = st.columns(3)

for indice, (emoji, nombre) in enumerate(islas):
    with columnas[indice % 3]:
        st.markdown(f"### {emoji}")
        st.markdown(f"**{nombre}**")

        if indice in st.session_state.islas:
            st.caption("💗 Descubierta")

        if st.button(
            "Descubrir isla ✨",
            key=f"isla_{indice}"
        ):
            visitar_isla(indice)

            st.session_state["isla_actual"] = indice
            st.rerun()


# ==========================================
# CONTENIDO DE LAS ISLAS
# ==========================================

actual = st.session_state.get("isla_actual", None)

if actual is not None:

    st.markdown("---")

    emoji, nombre = islas[actual]

    st.markdown(
        f'<div class="section-title">{emoji} {nombre}</div>',
        unsafe_allow_html=True
    )

    if actual == 0:
        st.markdown("""
        <div class="glass romantic">
            Si me preguntaran cuál es el paisaje
            más bonito que he visto en toda mi vida,
            no diría el océano, ni las estrellas,
            ni un atardecer.

            <br><br>

            Diría que es tu sonrisa.

            <br><br>

            Porque tienes esa forma tan tuya
            de hacer que incluso mis días más difíciles
            se sientan bonitos.

            <br><br>

            Mi niña preciosa, ojalá nunca olvides
            lo hermosa que eres,
            incluso en los días en que tú no logres verlo.

            <br><br>

            <b>Yo siempre voy a encontrar belleza en ti. 💗</b>
        </div>
        """, unsafe_allow_html=True)

    elif actual == 1:
        st.markdown("""
        <div class="glass romantic">
            💌 <b>Mi carta para ti</b>

            <br><br>

            Mi Mami shica:

            <br><br>

            Hoy quiero celebrar mucho más que tu cumpleaños.

            Quiero celebrar que existes.
            Que llegaste a este mundo y que,
            entre tantas personas y tantos caminos,
            la vida permitió que nos encontráramos.

            <br><br>

            A veces pienso en lo increíble que es
            que una sola persona pueda convertirse
            en tantas cosas bonitas al mismo tiempo.

            <br><br>

            En mi alegría.
            En mi paz.
            En mi sonrisa favorita.
            En alguien a quien quiero cuidar,
            abrazar y hacer feliz.

            <br><br>

            Si pudiera regalarte algo imposible,
            te regalaría la oportunidad
            de verte a través de mis ojos,
            aunque fuera por un instante.

            Así entenderías por qué eres
            tan especial para mí.

            <br><br>

            Y aunque no siempre encuentre
            las palabras perfectas,
            quiero que sepas que mi corazón
            te elige con muchísimo amor.

            <br><br>

            Feliz cumpleaños, mi niña hermosa.

            <br><br>

            Con muchísimo amor,

            <b>Tu Papi rico 💗</b>
        </div>
        """, unsafe_allow_html=True)

    elif actual == 2:
        st.markdown("""
        <div class="glass romantic">
            Dicen que en el universo existen
            más estrellas de las que podríamos contar.

            <br><br>

            Pero si cada estrella representara
            una razón para amarte,
            todavía me faltaría cielo.

            <br><br>

            ✨ Amo tu sonrisa.

            <br>
            ✨ Amo tus ojitos.

            <br>
            ✨ Amo tu manera de ser.

            <br>
            ✨ Amo compartir mis días contigo.

            <br>
            ✨ Amo nuestras pequeñas locuras.

            <br>
            ✨ Amo que seas tú, simplemente tú.

            <br><br>

            <b>Eres mi constelación favorita. 🌌</b>
        </div>
        """, unsafe_allow_html=True)

        if st.button("🌠 Pedir un deseo a una estrella"):
            st.session_state.deseo = True
            st.balloons()

        if st.session_state.deseo:
            st.success(
                "Que cada sueño que guardas en tu corazón "
                "encuentre un camino para hacerse realidad. 💗"
            )

    elif actual == 3:
        st.markdown("""
        <div class="glass romantic">
            💍 <b>Mis promesas para ti</b>

            <br><br>

            Prometo seguir buscando maneras
            de hacerte sonreír.

            <br><br>

            Prometo escucharte y valorar
            todo lo que sientes.

            <br><br>

            Prometo acompañarte en tus sueños
            y alegrarme de tus logros.

            <br><br>

            Prometo esforzarme para que nuestro amor
            no sea solamente algo bonito que decimos,
            sino algo bonito que construimos.

            <br><br>

            Porque no quiero que nuestra historia
            sea perfecta.

            <br><br>

            <b>Quiero que sea verdadera,
            bonita y nuestra. 💗</b>
        </div>
        """, unsafe_allow_html=True)

    elif actual == 4:
        st.markdown("""
        <div class="glass romantic">
            🎂 <b>¡FELIZ CUMPLEAÑOS, MAMI SHICA!</b>

            <br><br>

            Hoy el universo está de fiesta
            porque un día como hoy nació
            una personita demasiado especial.

            <br><br>

            Deseo que este nuevo año de vida
            te traiga aventuras hermosas,
            tranquilidad, salud,
            sueños cumplidos y mucho amor.

            <br><br>

            Y deseo que nunca te falten
            motivos para sonreír.

            <br><br>

            🎂 🕯️ 🎂

            <br><br>

            <b>Pide un deseo, mi amor.</b>
        </div>
        """, unsafe_allow_html=True)

        if not st.session_state.vela:
            if st.button("💨 Soplar la velita"):
                st.session_state.vela = True
                st.balloons()
                st.rerun()
        else:
            st.success(
                "✨ Velita apagada. "
                "Que tu deseo se haga realidad, princesa."
            )

    elif actual == 5:
        st.markdown("""
        <div class="glass romantic">
            👑 <b>La reina de mi mundo</b>

            <br><br>

            Mi Mami shica...

            <br><br>

            No necesitas una corona
            para ser mi reina.

            No necesitas un castillo
            para merecer lo más bonito del mundo.

            <br><br>

            Mereces respeto.
            Mereces ternura.
            Mereces tranquilidad.
            Mereces amor del bonito.

            <br><br>

            Y si de mí depende,
            quiero hacer todo lo posible
            por regalarte momentos
            que siempre quieras recordar.

            <br><br>

            Porque eres alguien
            verdaderamente especial para mí.

            <br><br>

            <b>Mi niña preciosa, mi reina,
            mi tesoro. 💗👑</b>
        </div>
        """, unsafe_allow_html=True)


# ==========================================
# ÁLBUM DE RECUERDOS
# ==========================================

st.markdown(
    '<div class="section-title">📸 Nuestro pequeño universo</div>',
    unsafe_allow_html=True
)

st.markdown("""
<p class="small-note">
Aquí viven algunos pedacitos de nuestra historia.
</p>
""", unsafe_allow_html=True)

recuerdos = [
    (
        "Nuestra primera aventura 💗",
        "Cada historia bonita tiene un comienzo."
    ),
    (
        "Un momento inolvidable 🌸",
        "Hay momentos que quisiera guardar para siempre."
    ),
    (
        "Nosotros dos ✨",
        "Mi lugar favorito siempre será donde podamos ser felices."
    ),
]

columnas_fotos = st.columns(3)

for i, (titulo, mensaje) in enumerate(recuerdos):
    with columnas_fotos[i]:
        ruta = Path(f"assets/foto{i+1}.jpg")

        if ruta.exists():
            st.image(str(ruta), use_container_width=True)
        else:
            st.markdown(
                f'<div class="glass romantic" '
                f'style="min-height:180px;">'
                f'📷<br><br>Foto {i+1}<br>💗</div>',
                unsafe_allow_html=True
            )

        st.markdown(f"**{titulo}**")
        st.caption(mensaje)


# ==========================================
# MENSAJES SORPRESA
# ==========================================

st.markdown(
    '<div class="section-title">💖 Un mensajito del corazón</div>',
    unsafe_allow_html=True
)

mensajes = [
    "Eres una de las coincidencias más bonitas de mi vida. 💗",
    "Si la felicidad tuviera una sonrisa, seguramente sería la tuya. 🌸",
    "Contigo hasta los momentos pequeños se vuelven especiales. ✨",
    "Si pudiera escoger otra vez, me encantaría volver a encontrarte. 💌",
    "No existe mapa que pueda medir todo el cariño que te tengo. 🏴‍☠️",
    "Ojalá te veas siempre tan hermosa como yo te veo. 👑",
]

if st.button("💗 Descubrir otro mensajito"):
    st.session_state["mensaje"] = random.choice(mensajes)

if "mensaje" in st.session_state:
    st.markdown(
        f'<div class="glass romantic">'
        f'{st.session_state["mensaje"]}</div>',
        unsafe_allow_html=True
    )


# ==========================================
# GRAN TESORO FINAL
# ==========================================

st.markdown(
    '<div class="section-title">💎 El tesoro legendario</div>',
    unsafe_allow_html=True
)

if len(st.session_state.islas) < 6:

    faltan = 6 - len(st.session_state.islas)

    st.markdown(f"""
    <div class="glass romantic">
        🔒 Hay un tesoro escondido al final
        de esta aventura.

        <br><br>

        Para descubrirlo, todavía debes
        visitar <b>{faltan} isla(s)</b>.

        <br><br>

        La aventura aún no termina, princesa.
    </div>
    """, unsafe_allow_html=True)

else:

    st.markdown("""
    <div class="treasure">
        <h2>🏆 ¡Encontraste el One Piece del amor!</h2>
        <p>
            Has recorrido todas las islas.

            Ahora puedes abrir el tesoro
            más importante de esta aventura.
        </p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("💎 ABRIR EL TESORO LEGENDARIO"):
        st.session_state.tesoro = True
        st.balloons()

    if st.session_state.tesoro:

        st.markdown(f"""
        <div class="treasure">
            <h1>💗 EL VERDADERO TESORO 💗</h1>

            <p style="font-size:19px;line-height:2.1;">
                Mi {NOMBRE_ELLA}...

                <br><br>

                Si nuestra vida fuera una aventura
                como las que soñábamos de pequeños,
                yo navegaría todos los mares del mundo
                con una sola ilusión.

                <br><br>

                Seguir construyendo recuerdos contigo.

                <br><br>

                Porque después de buscar entre
                islas, estrellas, promesas y sueños,
                entendí algo maravilloso.

                <br><br>

                El tesoro que tanto buscaba
                nunca fue el oro.

                <br><br>

                Nunca fueron las joyas.

                <br><br>

                Nunca fue llegar al final del mapa.

                <br><br>

                <b>El tesoro siempre fuiste tú.</b>

                <br><br>

                Tu sonrisa.
                Tu manera de ser.
                Tu existencia en mi vida.

                <br><br>

                Y aunque esta página algún día
                deje de tener animaciones,
                y aunque se apaguen todas sus estrellas,
                quiero que recuerdes algo.

                <br><br>

                Hay alguien que quiso crear
                un pequeño universo solo
                para verte sonreír.

                <br><br>

                Ese alguien soy yo.

                <br><br>

                <span style="font-size:29px;color:#ffe6a8;">
                    Feliz cumpleaños,
                    mi Mami shica hermosa.
                </span>

                <br><br>

                Con muchísimo amor,

                <br>

                <b>{NOMBRE_TUYO} 💗</b>
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.snow()


# ==========================================
# DESPEDIDA
# ==========================================

st.markdown("---")

st.markdown(f"""
<div class="romantic">
    🌙 ⭐ 🌸 💗 🌸 ⭐ 🌙

    <br><br>

    <span style="font-family:'Great Vibes',cursive;font-size:49px;">
        Te quiero hasta el infinito
        y mucho más allá.
    </span>

    <br><br>

    Una aventura de {NOMBRE_TUYO}

    <br>

    Para {NOMBRE_ELLA}

    <br><br>

    🏴‍☠️💗
</div>
""", unsafe_allow_html=True)
