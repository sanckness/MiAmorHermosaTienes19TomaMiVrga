
import streamlit as st
import streamlit.components.v1 as components
import random
import textwrap
from pathlib import Path


# ==============================================
# EL TESORO MÁS BONITO DEL GRAND LINE
# ==============================================

ELLA = "Mami shica"
YO = "Tu Papi rico"

st.set_page_config(
    page_title="El universo de Mami shica 💗",
    page_icon="💖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==============================================
# ESTADO DE LA AVENTURA
# ==============================================

valores = {
    "islas": [],
    "actual": None,
    "vela": False,
    "deseo": False,
    "tesoro": False,
    "mensaje": None,
    "planes": [],
    "reto": None,
    "capsula": False,
}

for clave, valor in valores.items():
    if clave not in st.session_state:
        st.session_state[clave] = valor



def mostrar_html(contenido):
    """Renderiza las cartas como HTML real."""
    st.html(textwrap.dedent(contenido).strip())



def tarjeta(titulo, texto, emoji="💗"):
    mostrar_html(
        f'<div class="tarjeta">'
        f'<div class="emoji-grande">{emoji}</div>'
        f'<h3>{titulo}</h3>'
        f'<p>{texto}</p>'
        f'</div>'
    )


def visitar(numero):
    if numero not in st.session_state.islas:
        st.session_state.islas.append(numero)
    st.session_state.actual = numero


# ==============================================
# DISEÑO MÁGICO
# ==============================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Quicksand:wght@400;500;600;700&display=swap');

.stApp {
    background:
      radial-gradient(ellipse at 20% 10%, #7b286055, transparent 45%),
      radial-gradient(ellipse at 85% 65%, #743c9855, transparent 45%),
      linear-gradient(145deg, #08091d, #20102f, #11091e);
    color: #fff0fa;
}

html, body, p, div, span, button {
    font-family: 'Quicksand', sans-serif;
}

.block-container {
    max-width: 1050px;
    padding-top: 2rem;
    padding-bottom: 5rem;
}

h1, h2, h3 {
    color: #ffe1f2 !important;
}

.titulo {
    font-family: 'Great Vibes', cursive;
    text-align: center;
    font-size: clamp(56px, 9vw, 105px);
    line-height: 1.2;
    background: linear-gradient(
        90deg, #ffa8dc, #fff3bc, #ff9adb
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    filter: drop-shadow(0 0 15px #ff72bb66);
    margin: 30px auto;
}

.seccion {
    font-family: 'Great Vibes', cursive;
    font-size: clamp(40px, 6vw, 65px);
    color: #ffc3e5;
    text-align: center;
    margin: 50px auto 20px;
}

.subtitulo {
    text-align: center;
    font-size: 18px;
    color: #f9cce9;
}

.tarjeta, .carta {
    background: rgba(255, 255, 255, 0.065);
    border: 1px solid rgba(255, 181, 223, 0.3);
    border-radius: 25px;
    padding: 30px;
    margin: 18px 0;
    text-align: center;
    box-shadow: 0 15px 40px #00000033;
}

.tarjeta {
    min-height: 190px;
}

.tarjeta h3 {
    color: #ffe4a8 !important;
    margin: 10px 0;
}

.tarjeta p, .carta p {
    color: #ffe7f5;
    font-size: 18px;
    line-height: 2;
    margin-bottom: 22px;
}

.carta p:last-child {
    margin-bottom: 0;
}

.emoji-grande {
    font-size: 43px;
    text-align: center;
}

.firma {
    font-family: 'Great Vibes', cursive;
    font-size: 38px !important;
    color: #ffe7aa !important;
}

.tesoro {
    background: linear-gradient(
        145deg, #40214f, #752e66, #3c2054
    );
    border: 2px solid #f8d6a0;
    border-radius: 28px;
    padding: 35px;
    box-shadow: 0 0 40px #f07bb255;
    text-align: center;
}

.tesoro p {
    font-size: 19px;
    line-height: 2.1;
    color: #fff1f8;
}

.nota {
    text-align: center;
    color: #e8bddd;
    font-size: 15px;
}

.stButton > button {
    width: 100%;
    color: white !important;
    background: linear-gradient(
        120deg, #a12d83, #e54f9e
    ) !important;
    border: 1px solid #ffaad9 !important;
    border-radius: 28px !important;
    padding: 12px 16px !important;
    font-weight: 700;
    transition: 0.3s;
}

.stButton > button:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 25px #ff8fc366;
}

[data-testid="stExpander"] {
    background: #ffffff0a;
    border-radius: 14px;
}

.stProgress > div > div {
    background: linear-gradient(
        90deg, #f45baa, #ffe5a4
    );
}

hr {
    border-color: #edb7dd44;
}
</style>
""", unsafe_allow_html=True)


# ==============================================
# CIELO ANIMADO
# ==============================================

components.html("""
<style>
body {
    margin: 0;
    background: transparent;
    overflow: hidden;
}
.estrella {
    position: absolute;
    color: #fff1c9;
    animation: brillar 3s infinite alternate;
}
.corazon {
    position: absolute;
    bottom: -30px;
    animation: subir linear infinite;
}
@keyframes brillar {
    from { opacity: .15; transform: scale(.6); }
    to { opacity: 1; transform: scale(1.4); }
}
@keyframes subir {
    from { transform: translateY(0); opacity: 0; }
    20% { opacity: 1; }
    80% { opacity: .8; }
    to { transform: translateY(-500px); opacity: 0; }
}
</style>
<script>
for(let i=0;i<80;i++){
    let e=document.createElement("span");
    e.className="estrella";
    e.textContent="✦";
    e.style.left=Math.random()*100+"%";
    e.style.top=Math.random()*100+"%";
    e.style.fontSize=(Math.random()*12+3)+"px";
    e.style.animationDelay=Math.random()*3+"s";
    document.body.appendChild(e);
}
for(let i=0;i<16;i++){
    let e=document.createElement("span");
    e.className="corazon";
    e.textContent=["💗","💕","✨","🌸"][
        Math.floor(Math.random()*4)
    ];
    e.style.left=Math.random()*100+"%";
    e.style.animationDuration=(Math.random()*8+7)+"s";
    e.style.animationDelay=(-Math.random()*12)+"s";
    document.body.appendChild(e);
}
</script>
""", height=110)


# ==============================================
# PORTADA
# ==============================================

mostrar_html("""
<div class="titulo">
    El tesoro más bonito<br>
    del Grand Line
</div>
""")

mostrar_html(f"""
<p class="subtitulo">
    🏴‍☠️ Una aventura escrita con amor para {ELLA} 💗
</p>
""")

mostrar_html(f"""
<div class="carta">
    <p>Había una vez un pirata que soñaba con
    encontrar el tesoro más extraordinario
    de todos los mares.</p>

    <p>Navegó entre estrellas, tormentas,
    aventuras y miles de sueños.</p>

    <p>Pero un día descubrió que el tesoro
    más bonito no estaba escondido en
    ninguna isla.</p>

    <p>Tenía una sonrisa preciosa,
    una mirada especial y un nombre
    que hacía latir su corazón.</p>

    <p><strong>Ese nombre era {ELLA}.</strong></p>

    <p>Y aquel pirata era...</p>

    <p class="firma">{YO} 💗</p>
</div>
""")


# ==============================================
# MÚSICA
# ==============================================

mostrar_html("""
<div class="seccion">
    La melodía de nuestra aventura 🎶
</div>
""")

ruta_audio = Path("assets/one_piece.mp3")

if ruta_audio.is_file():
    st.audio(str(ruta_audio), format="audio/mpeg")
else:
    st.info(
        "🎵 Coloca tu canción de One Piece como "
        "assets/one_piece.mp3 para escucharla aquí."
    )


# ==============================================
# MAPA DE SEIS ISLAS
# ==============================================

mostrar_html("""
<div class="seccion">
    El mapa de nuestro amor 🗺️
</div>
""")

mostrar_html("""
<div class="carta">
    <p>Mi princesa, he escondido seis pedacitos
    de mi corazón alrededor de este océano.</p>

    <p>Cada isla tiene algo especial
    que quiero decirte.</p>

    <p>Explóralas todas para encontrar
    nuestro tesoro legendario.</p>

    <p><strong>¿Lista para navegar conmigo? 💗</strong></p>
</div>
""")

islas = [
    ("🌸", "Tu sonrisa"),
    ("💌", "La carta secreta"),
    ("🌟", "Nuestro universo"),
    ("💍", "Mis promesas"),
    ("🎂", "Tu cumpleaños"),
    ("👑", "Mi reina"),
]

cantidad = len(st.session_state.islas)
st.progress(cantidad / 6)
st.caption(f"✨ Islas descubiertas: {cantidad}/6")

columnas = st.columns(3)

for numero, (emoji, nombre) in enumerate(islas):
    with columnas[numero % 3]:
        mostrar_html(
            f'<div class="tarjeta">'
            f'<div class="emoji-grande">{emoji}</div>'
            f'<h3>{nombre}</h3>'
            f'</div>'
        )

        if numero in st.session_state.islas:
            st.caption("💗 Descubierta")

        if st.button("Explorar ✨", key=f"i_{numero}"):
            visitar(numero)
            st.rerun()


# ==============================================
# CONTENIDOS DE LAS ISLAS
# ==============================================

actual = st.session_state.actual

if actual is not None:

    st.divider()

    emoji, nombre = islas[actual]

    mostrar_html(
        f'<div class="seccion">{emoji} {nombre}</div>'
    )

    # ISLA 1
    if actual == 0:
        mostrar_html("""
        <div class="carta">
            <p>Mi niña hermosa...</p>

            <p>Si me preguntaran cuál es el paisaje
            más bonito que he visto en mi vida,
            no diría el océano ni las estrellas.</p>

            <p>Diría que es tu sonrisa.</p>

            <p>Porque tienes una manera
            tan especial de iluminar mis días.</p>

            <p>A veces quizá no te das cuenta
            de lo hermosa que eres.</p>

            <p>Pero quiero que sepas que
            mi corazón siempre encuentra
            motivos para admirarte.</p>

            <p><strong>Ojalá nunca dejes
            de sonreír, mi princesa. 💗</strong></p>
        </div>
        """)

    # ISLA 2
    elif actual == 1:
        mostrar_html(f"""
        <div class="carta">
            <p class="firma">Mi carta para ti 💌</p>

            <p><strong>Mi {ELLA}:</strong></p>

            <p>Hoy quiero celebrar mucho más
            que tu cumpleaños.</p>

            <p>Quiero celebrar que existes.
            Que llegaste a este mundo y que,
            entre tantas personas y tantos caminos,
            la vida permitió que nos encontráramos.</p>

            <p>A veces pienso en lo increíble
            que es que una sola persona pueda
            convertirse en tantas cosas bonitas
            al mismo tiempo.</p>

            <p>En mi alegría.<br>
            En mi paz.<br>
            En mi sonrisa favorita.<br>
            En alguien a quien quiero cuidar,
            abrazar y hacer feliz.</p>

            <p>Si pudiera regalarte algo imposible,
            te regalaría la oportunidad
            de verte a través de mis ojos,
            aunque fuera por un instante.</p>

            <p>Así entenderías por qué
            eres tan especial para mí.</p>

            <p>Quiero que nunca dudes
            de lo mucho que vales,
            de lo hermosa que eres
            y de todas las cosas bonitas
            que mereces en esta vida.</p>

            <p>Y aunque no siempre encuentre
            las palabras perfectas,
            quiero que sepas que
            te quiero con muchísimo amor.</p>

            <p>Feliz cumpleaños,
            mi niña preciosa.</p>

            <p>Con todo mi cariño,</p>

            <p class="firma">{YO} 💗</p>
        </div>
        """)

    # ISLA 3
    elif actual == 2:
        mostrar_html("""
        <div class="carta">
            <p>Dicen que el universo tiene
            millones de estrellas.</p>

            <p>Pero si cada estrella representara
            una razón por la que te quiero,
            todavía me faltaría cielo.</p>

            <p>✨ Tu sonrisa.<br>
            ✨ Tus ojitos.<br>
            ✨ Tu manera de ser.<br>
            ✨ Tus ocurrencias.<br>
            ✨ Nuestros momentos.<br>
            ✨ La alegría de tenerte en mi vida.</p>

            <p><strong>Eres mi constelación
            favorita. 🌌</strong></p>
        </div>
        """)

        if st.button("🌠 Pedir un deseo"):
            st.session_state.deseo = True
            st.balloons()

        if st.session_state.deseo:
            st.success(
                "✨ Deseo que tus sueños se cumplan "
                "y que nunca te falten razones para sonreír."
            )

    # ISLA 4
    elif actual == 3:
        mostrar_html("""
        <div class="carta">
            <p>💍 Mis promesas para ti.</p>

            <p>Prometo seguir buscando
            maneras de hacerte sonreír.</p>

            <p>Prometo escucharte y cuidar
            lo que sentimos.</p>

            <p>Prometo apoyarte en tus sueños
            y alegrarme por cada logro tuyo.</p>

            <p>Prometo esforzarme para construir
            recuerdos bonitos contigo.</p>

            <p>No puedo prometer que
            todo será perfecto.</p>

            <p>Pero sí puedo prometer
            que quiero poner amor,
            paciencia y cariño
            en nuestra historia.</p>

            <p><strong>Porque eres alguien
            demasiado importante para mí. 💗</strong></p>
        </div>
        """)

    # ISLA 5
    elif actual == 4:
        mostrar_html(f"""
        <div class="carta">
            <p class="firma">
                Feliz cumpleaños, {ELLA} 🎂
            </p>

            <p>Hoy es un día maravilloso
            porque celebramos tu vida.</p>

            <p>Quiero que este nuevo año
            esté lleno de cosas bonitas,
            sueños cumplidos, salud,
            aventuras y felicidad.</p>

            <p>Quiero que nunca olvides
            cuánto mereces ser feliz.</p>

            <p>Ahora cierra tus ojitos,
            piensa en algo hermoso
            y pide un deseo.</p>

            <p>🎂 🕯️ 🎂</p>
        </div>
        """)

        if not st.session_state.vela:
            if st.button("💨 Soplar la velita"):
                st.session_state.vela = True
                st.balloons()
                st.rerun()
        else:
            st.success(
                "🎉 ¡Velita apagada! "
                "Que tu deseo se haga realidad, princesa."
            )

    # ISLA 6
    elif actual == 5:
        mostrar_html("""
        <div class="carta">
            <p class="firma">Mi reina hermosa 👑</p>

            <p>No necesitas una corona
            para ser mi princesa.</p>

            <p>No necesitas un castillo
            para merecer lo mejor del mundo.</p>

            <p>Mereces respeto,
            cariño, paz y muchísima felicidad.</p>

            <p>Me encanta pensar en todos
            los pequeños momentos bonitos
            que todavía podemos compartir.</p>

            <p>Las risas que faltan.<br>
            Las aventuras que nos esperan.<br>
            Los abrazos inesperados.<br>
            Los sueños que podemos cumplir.</p>

            <p>Porque para mí eres
            mucho más que una persona especial.</p>

            <p><strong>Eres mi reina,
            mi niña preciosa
            y mi tesoro más bonito. 💗</strong></p>
        </div>
        """)


# ==============================================
# NUEVO: NUESTRO FUTURO JUNTOS
# ==============================================

mostrar_html("""
<div class="seccion">
    Nuestro futuro juntos 💞
</div>
""")

mostrar_html("""
<div class="carta">
    <p>No necesito fotografías para imaginar
    todas las cosas bonitas que
    quiero vivir contigo.</p>

    <p>Porque nuestra historia
    no solamente está hecha
    de recuerdos.</p>

    <p>También está hecha de
    los momentos que todavía
    nos esperan.</p>

    <p><strong>Y quiero compartir
    muchos de ellos contigo. 💗</strong></p>
</div>
""")

# PLANES DE PAREJA

planes = [
    ("🌅", "Ver un atardecer juntos",
     "Encontrar un lugar bonito y quedarnos "
     "abrazaditos mirando el cielo."),

    ("🍿", "Nuestra noche de películas",
     "Mantas, comida rica, muchos abrazos "
     "y una película que elijamos juntos."),

    ("🌧️", "Una tarde de lluvia",
     "Escuchar la lluvia mientras hablamos, "
     "nos abrazamos y disfrutamos del momento."),

    ("🍰", "Una cita sorpresa",
     "Preparar un día especial "
     "solo para consentirte."),

    ("🌊", "Una aventura inolvidable",
     "Conocer un lugar nuevo juntos "
     "y crear otra historia para recordar."),

    ("⭐", "Mirar las estrellas",
     "Hablar de nuestros sueños "
     "y de todo lo que queremos vivir."),
]

mostrar_html("""
<div class="seccion">
    Nuestra lista de aventuras ✨
</div>
""")

st.caption(
    "Selecciona los planes que quieras vivir conmigo."
)

for i in range(0, len(planes), 2):
    cols = st.columns(2)

    for j, col in enumerate(cols):
        indice = i + j

        if indice >= len(planes):
            continue

        emoji, nombre, descripcion = planes[indice]

        with col:
            tarjeta(nombre, descripcion, emoji)

            marcado = indice in st.session_state.planes

            if st.checkbox(
                "💗 Quiero vivir esto contigo",
                value=marcado,
                key=f"plan_{indice}"
            ):
                if indice not in st.session_state.planes:
                    st.session_state.planes.append(indice)
            else:
                if indice in st.session_state.planes:
                    st.session_state.planes.remove(indice)

seleccionados = len(st.session_state.planes)

if seleccionados:
    st.success(
        f"💖 Tenemos {seleccionados} aventura(s) "
        "marcadas para nuestro futuro."
    )


# ==============================================
# JUEGO: NUESTRA CITA PERFECTA
# ==============================================

mostrar_html("""
<div class="seccion">
    Diseñemos nuestra cita perfecta 💕
</div>
""")

st.markdown(
    "Escoge cómo te gustaría pasar "
    "un día especial conmigo."
)

c1, c2 = st.columns(2)

with c1:
    lugar = st.selectbox(
        "🌸 ¿Dónde vamos?",
        [
            "A ver el atardecer 🌅",
            "A un café bonito ☕",
            "A la playa 🌊",
            "A un parque lleno de flores 🌷",
            "A una cena romántica 🍽️"
        ]
    )

    comida = st.selectbox(
        "🍓 ¿Qué comemos?",
        [
            "Pizza 🍕",
            "Sushi 🍣",
            "Hamburguesas 🍔",
            "Postrecitos 🍰",
            "Lo que se te antoje 💗"
        ]
    )

with c2:
    actividad = st.selectbox(
        "✨ ¿Qué hacemos?",
        [
            "Tomarnos de la mano 💞",
            "Ver una película 🍿",
            "Contarnos secretos 💌",
            "Escuchar música juntos 🎶",
            "Mirar las estrellas 🌟"
        ]
    )

    final_cita = st.selectbox(
        "🌙 ¿Cómo termina?",
        [
            "Con un abrazo gigante 🫂",
            "Con muchos besitos 😘",
            "Con otra aventura 💗",
            "Con una sorpresa 🎁"
        ]
    )

if st.button("💘 Crear nuestra cita perfecta"):
    mostrar_html(f"""
    <div class="carta">
        <p class="firma">Nuestra cita soñada 💗</p>

        <p>Primero iremos a:</p>
        <p><strong>{lugar}</strong></p>

        <p>Después comeremos:</p>
        <p><strong>{comida}</strong></p>

        <p>Y disfrutaremos de:</p>
        <p><strong>{actividad}</strong></p>

        <p>Hasta terminar nuestro día...</p>
        <p><strong>{final_cita}</strong></p>

        <p>Lo bonito no será el lugar.</p>

        <p><strong>Será estar contigo. 💞</strong></p>
    </div>
    """)
    st.balloons()


# ==============================================
# RETOS ROMÁNTICOS
# ==============================================

mostrar_html("""
<div class="seccion">
    Pequeñas misiones de amor 💗
</div>
""")

retos = [
    "💗 Dame un abrazo de al menos 20 segundos.",
    "😘 Dame tres besitos sorpresa.",
    "💌 Dime algo bonito que recuerdes de nosotros.",
    "🌸 Dime qué aventura quieres vivir conmigo.",
    "🎶 Escoge una canción para escuchar abrazaditos.",
    "🫶 Cuéntame cuál es tu recuerdo favorito juntos.",
    "⭐ Pide un deseo que podamos cumplir los dos.",
    "🥹 Mírame a los ojitos y regálame una sonrisa."
]

if st.button("🎲 Descubrir nuestra misión"):
    st.session_state.reto = random.choice(retos)

if st.session_state.reto:
    mostrar_html(
        '<div class="carta">'
        '<p class="firma">¡Misión desbloqueada!</p>'
        f'<p>{st.session_state.reto}</p>'
        '</div>'
    )


# ==============================================
# CÁPSULA DEL TIEMPO
# ==============================================

mostrar_html("""
<div class="seccion">
    Una carta para nuestro futuro 💌
</div>
""")

mostrar_html("""
<div class="carta">
    <p>Imagina que pasan muchos años
    y volvemos a abrir esta página.</p>

    <p>Quizá nuestras vidas hayan cambiado,
    quizá hayamos conocido muchos lugares
    y vivido incontables aventuras.</p>

    <p>Pero quiero que al leer esto
    recuerdes cuánto cariño había
    detrás de este pequeño regalo.</p>

    <p>Quise darte algo hecho con mi esfuerzo,
    con mis pensamientos y con el deseo
    de verte feliz.</p>

    <p>Y si algún día volvemos a leerlo,
    espero que sonriamos recordando
    cómo comenzó esta aventura.</p>

    <p><strong>Porque lo más bonito
    nunca fue llegar a una isla.</strong></p>

    <p><strong>Fue tener a alguien
    con quien navegar. 💗</strong></p>
</div>
""")

if st.button("⏳ Abrir mensaje del futuro"):
    st.session_state.capsula = True

if st.session_state.capsula:
    mostrar_html(f"""
    <div class="tesoro">
        <p class="firma">Para nosotros, en el futuro 💗</p>

        <p>Hola, mi {ELLA}.</p>

        <p>Si estás leyendo esto otra vez,
        quiero que recuerdes algo.</p>

        <p>Hubo un día en el que
        {YO} quiso construirte
        un universo lleno de estrellas,
        islas, cartas y sorpresas.</p>

        <p>Y todo por una razón muy sencilla.</p>

        <p><strong>Hacerte sonreír.</strong></p>

        <p>Ojalá nuestra historia siga
        llenándose de momentos bonitos.</p>

        <p>Y ojalá nunca dejemos
        de encontrar pequeñas razones
        para elegirnos y cuidarnos.</p>

        <p class="firma">Con todo mi amor 💗</p>
    </div>
    """)


# ==============================================
# MENSAJES INFINITOS
# ==============================================

mostrar_html("""
<div class="seccion">
    Una razón más para sonreír 💖
</div>
""")

mensajes = [
    "Tu sonrisa es mi paisaje favorito. 🌸",
    "Me encanta la tranquilidad de estar contigo. 💗",
    "Eres una de las coincidencias más bonitas de mi vida.",
    "Contigo hasta los planes pequeños son especiales. ✨",
    "Quiero seguir creando momentos felices a tu lado.",
    "Ojalá nunca olvides lo mucho que vales. 👑",
    "Me gusta imaginar nuevas aventuras contigo. 🏴‍☠️",
    "Mi tesoro favorito siempre será verte feliz. 💕"
]

if st.button("💗 Dame otro mensajito"):
    st.session_state.mensaje = random.choice(mensajes)

if st.session_state.mensaje:
    tarjeta(
        "Solo para ti",
        st.session_state.mensaje,
        "💌"
    )


# ==============================================
# EL TESORO FINAL
# ==============================================

mostrar_html("""
<div class="seccion">
    El tesoro legendario 💎
</div>
""")

faltan = 6 - len(st.session_state.islas)

if faltan > 0:

    tarjeta(
        "🔒 Tesoro sellado",
        f"Debes descubrir {faltan} isla(s) más "
        "para abrir el tesoro de nuestra aventura.",
        "🗝️"
    )

else:

    tarjeta(
        "¡Todas las islas descubiertas!",
        "Has encontrado las seis piezas "
        "del mapa de mi corazón.",
        "🏆"
    )

    if st.button("💎 ABRIR EL TESORO LEGENDARIO"):
        st.session_state.tesoro = True
        st.balloons()

    if st.session_state.tesoro:

        mostrar_html(f"""
        <div class="tesoro">
            <p class="firma">
                El verdadero tesoro 💗
            </p>

            <p>Mi {ELLA}...</p>

            <p>Después de navegar por
            todos estos pequeños mundos,
            has llegado hasta aquí.</p>

            <p>Tal vez esperabas encontrar
            una montaña de oro,
            joyas preciosas o
            un cofre lleno de riquezas.</p>

            <p>Pero hay algo que
            ninguna de esas cosas
            podría comprar.</p>

            <p>La alegría de coincidir contigo.</p>

            <p>La emoción de compartir
            nuestras pequeñas aventuras.</p>

            <p>Las sonrisas,
            las conversaciones,
            los abrazos y
            los sueños que construimos.</p>

            <p>Si yo fuera un pirata
            navegando el Grand Line,
            no necesitaría encontrar
            ningún otro tesoro.</p>

            <p>Porque al conocerte,
            encontré algo
            verdaderamente especial.</p>

            <p><strong>Te encontré a ti.</strong></p>

            <p>Quise hacerte esta aventura
            para que tengas un lugar
            lleno de palabras bonitas
            al que puedas regresar.</p>

            <p>Un pequeño universo
            hecho especialmente para ti.</p>

            <p>Porque mereces sentirte querida,
            valorada y celebrada.</p>

            <p>Y porque hoy,
            en tu cumpleaños,
            quiero desearte toda
            la felicidad del mundo.</p>

            <p class="firma">
                Feliz cumpleaños,<br>
                mi Mami shica hermosa.
            </p>

            <p>Que esta sea solo una
            de muchísimas aventuras
            que nos esperan.</p>

            <p>Con muchísimo amor,</p>

            <p class="firma">
                Tu Papi rico 💗🏴‍☠️
            </p>
        </div>
        """)

        st.snow()


# ==============================================
# DESPEDIDA
# ==============================================

st.divider()

mostrar_html(f"""
<div class="carta">
    <p>🌙 ⭐ 💗 ⭐ 🌙</p>

    <p class="firma">
        Te quiero hasta el infinito
        y mucho más allá.
    </p>

    <p>Una aventura de {YO}</p>

    <p>Para {ELLA}</p>

    <p>🏴‍☠️💗</p>
</div>
""")
