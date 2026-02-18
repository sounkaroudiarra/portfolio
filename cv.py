import streamlit as st
from PIL import Image

# ---- Page config ----
st.set_page_config(page_title="CV Mamadou Sounkarou Diarra", layout="wide")

# ---- Sidebar ----
st.sidebar.image("profil.jpeg", width=250)  # Remplace par ton fichier image
st.sidebar.markdown("## 📇 Contact")
st.sidebar.markdown("📍 Adresse : [Dakar, Sénégal](https://maps.google.com/?q=14.722034,-17.480247)")  
st.sidebar.markdown("📞 Téléphone : 77 685 75 73")  
st.sidebar.markdown("✉️ Email : sounkaroudiarra@gmail.com")  

st.sidebar.markdown("---")
st.sidebar.markdown("## 🎯 Centres d'intérêt")
st.sidebar.markdown("""
- 📚 Recherche scientifique  
- 📖 Lecture  
- 🚴 Cyclisme
""")



# ---- CSS pour style ----
st.markdown(
    """
    <style>
    /* Sidebar background noir et texte blanc */
    [data-testid="stSidebar"] {
        background-color: #000000;
        color: white;
        padding: 20px;
    }
    [data-testid="stSidebar"] * {
        color: white;
    }

    /* Cercle pour la photo de profil */
    [data-testid="stSidebar"] img {
        border-radius: 50%;
        border: 2px solid white;
    }

    /* Titres du contenu principal */
    h1, h2, h3 {
        color: #0A4C75;
    }

    /* Badges pour logiciels */
    .badge {
        display:inline-block;
        padding: 5px 10px;
        margin: 3px;
        border-radius: 5px;
        color: white;
        font-weight: bold;
    }
    .sig { background-color: #1f77b4; }
    .tld { background-color: #ff7f0e; }
    .analyse { background-color: #2ca02c; }
    .bdd { background-color: #d62728; }
    .drone { background-color: #9467bd; }
    .dev { background-color: #8c564b; }
    </style>
    """, unsafe_allow_html=True
)

# ---- Main content ----
st.title("Mamadou Sounkarou DIARRA")
st.subheader("Géographe – Géomaticien | Master 2 Aménagement et Gestion Urbaine")

# Profil
st.header("📝 Profil")
with st.expander("Voir description du profil"):
    st.write("""
    Étudiant en Master 2 de Géographie, spécialisé en Aménagement du territoire et
gestion urbaine, et en BTS de Géomatique. Passionné par les enjeux territoriaux,
migratoires et environnementaux, je mobilise à la fois les outils d’analyse des
sciences humaines et les technologies de la géomatique pour contribuer à une
meilleure compréhension et gestion des dynamiques spatiales. Curieux,
autonome et doté d’un solide esprit d’équipe, je m’investis pleinement dans les
projets collaboratifs à forte valeur ajoutée
    """)


# ---------------- MASTER ----------------
st.header("🎓 Master - GEOGRAPHIE HUMAINE – Aménagement du Territoire & Gestion Urbaine, Université Cheikh Anta Diop, Dakar - 2025")

# Master 1
with st.expander("Master 1 – Dynamiques territoriales & Urbanisme", expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🌍 Dynamiques Territoriales")
        st.markdown("""
        - Aménagement du territoire  
        - Réseaux, flux et configuration des territoires  
        - Espaces, sociétés et identités  
        - Villes, population et santé  
        """)
    with col2:
        st.markdown("### 🌱 Environnement & Planification")
        st.markdown("""
        - Environnement, ressources et risques  
        - Aménagement urbain : principes & expériences  
        - Anglais spécialisé  
        - Rédaction et soutenance  
        """)

# Master 2
with st.expander("Master 2 – Stratégie territoriale & Gouvernance", expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🏛️ Gouvernance & Prospective")
        st.markdown("""
        - Prospective territoriale  
        - Géopolitique : approche territoriale  
        - Coopération et partenariats décentralisés  
        - Finances locales  
        """)
    with col2:
        st.markdown("### 🌆 Gestion & Outils Stratégiques")
        st.markdown("""
        - Gestion des risques urbains  
        - Politique de gestion environnementale  
        - Rédaction scientifique  
        - Système d’Information Géographique (SIG)  
        """)

# BTS Géomatique
st.header("🎓 Géomatique – Centre d'Entreprenariat et de Développement Technique Le G15, Dakar - 2026 ")
with st.expander("BTS Géomatique – CEDT Le G15 (2024 – 2025)", expanded=False):
    st.markdown("""
    - Maîtrise des outils SIG   
    - Cartographie thématiques, plans et modélisations, Autocad, Sketchup  
    - Topographie et levés de terrain  
    - Initiation au pilotage de drones  
    - Initiation à la programmation 
    - Photogrammétrie 
    - Gestion de bases de données spatiales
    - Télédétection 
    - Webmapping
    """)


    st.markdown("---")
st.header("🎓 Licence - Géographie, Université Cheikh Anta Diop, Dakar - 2022")

# ---------------- L1 ----------------
with st.expander("📘 Licence 1 – Fondements de la Géographie", expanded=False):

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🌍 Géographie Physique")
        st.markdown("""
        - Géodynamique interne  
        - Géodynamique externe  
        - Roches et processus sédimentaires  
        - Environnement et risques naturels  
        """)

        st.markdown("### 🏙️ Géographie Humaine")
        st.markdown("""
        - Géographie rurale  
        - Géographie urbaine  
        - Géographie du Sénégal  
        - Géographie de l’Afrique de l’Ouest  
        """)

    with col2:
        st.markdown("### 🧠 Méthodologie & Analyse")
        st.markdown("""
        - Analyse de documents géographiques I & II  
        - Travaux dirigés de géographie I & II  
        - Méthodologie historique  
        """)

        st.markdown("### 📚 Histoire")
        st.markdown("""
        - Histoire générale de l’Afrique  
        - Histoire générale du Sénégal  
        """)

# ---------------- L2 ----------------
with st.expander("📗 Licence 2 – Approfondissement & Outils Quantitatifs"):

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🌦️ Géographie Physique")
        st.markdown("""
        - Éléments de climatologie  
        - Éléments de géomorphologie  
        - Éléments d’hydrologie  
        - Éléments de biogéographie  
        - TD Géomorphologie structurale I & II  
        """)

        st.markdown("### 🌍 Dynamiques Globales")
        st.markdown("""
        - Questions de géographie actuelle  
        - Mondialisation et territoires  
        """)

    with col2:
        st.markdown("### 👥 Géographie Humaine")
        st.markdown("""
        - Géographie de la population  
        - Géographie économique  
        - Éléments de démographie  
        - Géographie régionale : Europe  
        - Géographie régionale : Amérique du Sud  
        """)

        st.markdown("### 📊 Outils")
        st.markdown("""
        - Cartographie  
        - Statistique descriptive (17.00 / 20)  
        """)

# ---------------- L3 ----------------
with st.expander("📙 Licence 3 – Aménagement & Analyse Spatiale"):

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🏙️ Aménagement & Territoire")
        st.markdown("""
        - Principes et outils de l’aménagement du territoire  
        - Gouvernance et développement territorial  
        - Analyse de l’espace  
        - Économie spatiale : théories et concepts  
        - Croissance et morphologie urbaines  
        - Dynamique des relations ville/campagne  
        - Géographie des transports  
        - Migrations  
        """)

    with col2:
        st.markdown("### 🌱 Environnement & Outils")
        st.markdown("""
        - Hydrologie de surface  
        - Dynamique du climat I  
        - Géomorphologie et formations superficielles  
        - Écosystèmes : production et valorisation  
        - Cartographie / SIG  
        - Collecte et traitement des données  
        - Anglais spécialisé  
        """)


    st.markdown("**2015 – 2018 : Baccalauréat Littéraire – Lycée de Bambey**")
    st.write("""
    - Formation généraliste avec un accent sur les sciences sociales, la littérature et l’analyse critique  
    - Développement des compétences en rédaction, synthèse et esprit critique
    """)


# ---- Certification avec description et partenaires ----
st.header("📜 Certification")  

with st.expander("Gestion environnementale des impacts des infrastructures sur les écosystèmes côtiers sensibles – Août 2022", expanded=False):
    st.markdown("### Compétences et acquis")
    st.markdown("""
    **Organisée par :** Institut des Sciences de l’Environnement (ISE/FST/UCAD), Wetlands International Afrique (WIA) et la Fondation MAVA  

    - Analyse des impacts environnementaux des infrastructures sur les zones côtières vulnérables  
    - Étude des écosystèmes côtiers et de leur résilience face aux interventions humaines  
    - Élaboration de stratégies d'atténuation et recommandations pour un aménagement durable  
    - Application de méthodologies scientifiques pour la gestion et la protection des écosystèmes  
    """)




# ---- Expériences professionnelles ----
st.header("💼 Expériences")

# --- Expérience 1 ---
with st.expander("2025 – Stagiaire Géomaticien – Bureau d'Études Techniques Plus", expanded=False):
    st.markdown("### Missions & responsabilités")
    st.markdown("""
    - Production cartographique et traitement de données spatiales  
    - Analyse SIG et appui aux études techniques  
    - Participation aux travaux de terrain  
    """)

# --- Expérience 2 ---
with st.expander("Août 2023 – Comité d’Organisation – ISRA / CERAS", expanded=False):
    st.markdown("### Missions & responsabilités")
    st.markdown("""
    - Organisation et coordination des activités scientifiques du programme Feed the Future Innovation Lab  
    - Gestion des participants et suivi des sessions  
    - Appui logistique et communication interne  
    """)

# --- Expérience 3 ---
with st.expander("Juillet 2022 – Membre, Équipe de Veille et d’Analyse – ONG 3D, Dakar", expanded=False):
    st.markdown("### Missions & responsabilités")
    st.markdown("""
    - Observation et suivi du processus électoral  
    - Collecte, traitement et analyse d’informations locales  
    - Rédaction de rapports de veille et recommandations  
    """)

# --- Expérience 4 ---
with st.expander("Janvier 2022 – Membre, Équipe de Veille et d’Analyse – ONG 3D", expanded=False):
    st.markdown("### Missions & responsabilités")
    st.markdown("""
    - Suivi des dynamiques locales et des droits humains  
    - Analyse des données et production de synthèses  
    """)

# --- Expérience 5 ---
with st.expander("2019 – Chargé de l'organisation – Club Littérature, Art et Philosophie, Bambey", expanded=False):
    st.markdown("### Missions & responsabilités")
    st.markdown("""
    - Organisation d’événements culturels et académiques  
    - Coordination des membres et suivi des activités  
    """)




# ---- CSS pour badges colorés ----
st.markdown("""
<style>
.badge {
    display: inline-block;
    padding: 0.25em 0.6em;
    margin: 0.2em;
    border-radius: 0.5em;
    color: white;
    font-size: 0.9em;
}

.sig { background-color: #1f77b4; }        /* bleu SIG */
.tld { background-color: #ff7f0e; }        /* orange télédétection */
.analyse { background-color: #2ca02c; }    /* vert analyse/statistiques */
.bdd { background-color: #d62728; }        /* rouge bases de données */
.amenagement { background-color: #9467bd; } /* violet aménagement */
.env { background-color: #8c564b; }        /* brun environnement */
.dev { background-color: #e377c2; }        /* rose développement */
.drone { background-color: #7f7f7f; }      /* gris drones */
.lang { background-color: #17becf; }       /* cyan langues/communication */
</style>
""", unsafe_allow_html=True)

# ---- Compétences & logiciels ----
st.header("💻 Compétences & Logiciels")

with st.expander("Voir toutes mes compétences techniques", expanded=False):

    st.markdown("### SIG & Cartographie")
    st.markdown("""
    <span class="badge sig">QGIS</span>
    <span class="badge sig">ArcGIS Pro</span>
    <span class="badge sig">ArcMap</span>
    <span class="badge sig">Cartographie thématique</span>
    <span class="badge sig">Analyse spatiale</span>
    <span class="badge sig">Collecte & traitement de données</span>
    """, unsafe_allow_html=True)

    st.markdown("### Télédétection & Analyse spatiale")
    st.markdown("""
    <span class="badge tld">Imagerie Satellitaire</span>
    <span class="badge tld">Calcul d'indice spectral</span>
    <span class="badge tld">Analyse diachronique</span>
    <span class="badge tld">Changement d’usage des sols</span>
    """, unsafe_allow_html=True)

    st.markdown("### Analyse & Statistiques")
    st.markdown("""
    
    
    <span class="badge analyse">Excel</span>
    <span class="badge analyse">Statistiques descriptives</span>
    <span class="badge analyse">Analyse de données démographiques</span>
    """, unsafe_allow_html=True)

    st.markdown("### Bases de données")
    st.markdown("""
    <span class="badge bdd">MySQL</span>
    <span class="badge bdd">PostgreSQL/GIS</span>
    <span class="badge bdd">Gestion de bases de données spatiales</span>
    """, unsafe_allow_html=True)

    st.markdown("### Aménagement & Gestion territoriale")
    st.markdown("""
    <span class="badge amenagement">Analyse de l’espace</span>
    <span class="badge amenagement">Économie spatiale</span>
    <span class="badge amenagement">Prospective territoriale</span>
    <span class="badge amenagement">Planification urbaine</span>
    <span class="badge amenagement">Gestion des flux & migrations</span>
    """, unsafe_allow_html=True)

    st.markdown("### Environnement & Ressources")
    st.markdown("""
    <span class="badge env">Gestion environnementale</span>
    <span class="badge env">Risques naturels</span>
    <span class="badge env">Écosystèmes & valorisation</span>
    <span class="badge env">Aménagement durable</span>
    """, unsafe_allow_html=True)

    st.markdown("### Développement & Automatisation")
    st.markdown("""
    <span class="badge dev">Python</span>
    <span class="badge dev">Streamlit</span>
    <span class="badge dev">Automatisation & modélisation</span>
    """, unsafe_allow_html=True)

    st.markdown("### Drones & Cartographie aérienne")
    st.markdown("""
    <span class="badge drone">QGroundControl</span>
    <span class="badge drone">Levés topographiques</span>
    <span class="badge drone">Cartographie aérienne</span>
    """, unsafe_allow_html=True)

    st.markdown("### Communication & Langues")
    st.markdown("""
    <span class="badge lang">Rédaction scientifique</span>
    <span class="badge lang">Anglais spécialisé</span>
    """, unsafe_allow_html=True)


import plotly.graph_objects as go

# ---- Radar de compétences (version colorée et interactive) ----
st.header("📊 Radar de compétences")

with st.expander("Voir mes compétences par domaine", expanded=True):

    # Domaines et niveaux (1 à 5)
    categories = [
        "SIG & Cartographie",
        "Télédétection",
        "Analyse & Statistiques",
        "Bases de données",
        "Aménagement & Gestion territoriale",
        "Environnement & Ressources",
        "Développement & Automatisation",
        "Drones & Cartographie aérienne",
        "Communication & Langues"
    ]

    values = [4, 4, 4, 4, 5, 4, 3, 5, 4]

    # Fermeture du radar pour former un cercle complet
    categories += categories[:1]
    values += values[:1]

    # Couleurs par domaine
    colors = [
        "#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd",
        "#8c564b", "#e377c2", "#7f7f7f", "#17becf"
    ]
    colors += colors[:1]

    # Création du radar
    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name='Compétences',
        line=dict(color='royalblue', width=3),
        marker=dict(color='royalblue', size=8)
    ))

    # Définir les couleurs du fond pour chaque secteur
    for i in range(len(categories)-1):
        fig.add_shape(
            type="path",
            path=f"M0,0 L{values[i]}*cos({i*2*3.1415/9}) {values[i]}*sin({i*2*3.1415/9}) Z",
            fillcolor=colors[i],
            opacity=0.1,
            line_width=0,
            layer="below"
        )

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0,5],
                tickvals=[1,2,3,4,5],
                ticktext=["Débutant","Basique","Intermédiaire","Avancé","Expert"]
            )
        ),
        showlegend=False,
        margin=dict(l=40, r=40, t=40, b=40)
    )

    st.plotly_chart(fig, use_container_width=True)




   # ---- Projets de recherche en cours ----
st.header("🔬 Projets de recherche en cours")

with st.expander("Voir mes projets de recherche", expanded=False):

    st.markdown("### 🌍 Analyse des facteurs déterminants des choix de migration et de non-migration – Bassin arachidier, Diourbel")
    st.write("""
    - Étude des déterminants socio-économiques, environnementaux et territoriaux influençant les décisions de mobilité  
    - Analyse quantitative et qualitative des profils des migrants et non-migrants  
    - Utilisation des **SIG et outils géomatiques** pour cartographier les flux migratoires et les zones vulnérables  
    - Objectif : Comprendre les stratégies d’adaptation des communautés locales et proposer des recommandations pour le développement territorial durable
    """)

    st.markdown("### 🌱 Rôle de la mangrove dans la séquestration du carbone via télédétection")
    st.write("""
    - Étude des écosystèmes de mangrove pour évaluer leur capacité à stocker le carbone  
    - Utilisation de **télédétection et d’images satellitaires** pour analyser l’évolution spatiale de la mangrove  
    - Analyse des liens entre couverture végétale, densité et séquestration du carbone  
    - Objectif : Fournir des données scientifiques pour la conservation et la gestion durable des mangroves
    """)



# Centres d’intérêt détaillés
st.header("🎯 Centres d’intérêt")
with st.expander("🎯 Centres d’intérêt"):
    st.write("""
    - Recherche scientifique (dynamiques territoriales, développement durable, analyse spatiale)  
    - Lecture (ouvrages académiques, sciences sociales, géographie)  
    - Cyclisme (discipline, endurance et persévérance)
    """)


