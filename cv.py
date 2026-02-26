import streamlit as st
from PIL import Image

# ---- Page config ----
st.set_page_config(page_title="CV Mamadou Sounkarou Diarra", layout="wide")

# ---- Sidebar ----
st.sidebar.image("profil.jpeg", width=250)  
st.sidebar.markdown('<hr style="border:1px solid white;">', unsafe_allow_html=True)

st.sidebar.markdown("Adresse : [Dakar, Sénégal](https://maps.google.com/?q=14.722034,-17.480247)")  
 
st.sidebar.markdown("Email : sounkaroudiarra@gmail.com")  
st.sidebar.markdown('<hr style="border:1px solid white;">', unsafe_allow_html=True)

# Message de contact
st.sidebar.markdown(
    """
    <p style="color:white; font-size:1em; line-height:1.2em; text-align:center;">
    Merci de me contacter par email. Je réponds rapidement aux messages.
    </p>
    """,
    unsafe_allow_html=True
)

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
st.subheader("Géographe – Géomaticien | Aménagiste et urbaniste | Analyste territorial")


st.markdown("""
<div style="
    border: 2px solid #000000;  /* Couleur de la bordure */
    padding: 15px;               /* Espace intérieur */
    border-radius: 10px;         /* Coins arrondis */
    background-color: #ffffff;   /* Couleur de fond douce */
    font-size: 1em;
">
Professionnel en Géographie et Géomatique, spécialisé en aménagement du territoire et gestion urbaine, je transforme l’analyse spatiale et les données SIG en projets concrets à fort impact, répondant aux enjeux territoriaux, migratoires et environnementaux, tout en contribuant à l’efficacité et au succès organisationnel.
</div>
""", unsafe_allow_html=True)

# ---------------- MASTER ----------------
st.header("Formation")
with st.expander("Voir mes formations académiques"):
    st.subheader("Master - GEOGRAPHIE HUMAINE – Aménagement du Territoire & Gestion Urbaine")


# BTS Géomatique
    st.subheader("Brevet de Technique Supérieur - Géomatique")



# ---- Certification  ----
st.header("Certification")  

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
st.header("Expériences")

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
.drone { background-color: #7f7f7f; }      /* gris drones / photogrammétrie */
.lang { background-color: #17becf; }       /* cyan langues/communication */
</style>
""", unsafe_allow_html=True)

# ---- Compétences & Logiciels ----
st.header("Compétences & Logiciels")

with st.expander("Voir toutes mes compétences techniques", expanded=False):
    
    col1, col2 = st.columns(2)

    # ---- Colonne 1 : Compétences ----
    with col1:
        st.markdown("Compétences")
        st.markdown("""
        - Aménagement du territoire & urbanisme  
        - Dynamiques territoriales, migrations & population  
        - Gouvernance territoriale & développement local  
        - Analyse spatiale & modélisation  
        - Planification urbaine & prospective territoriale  
        - Gestion environnementale & risques naturels  
        - Écosystèmes, ressources & valorisation  
        - Collecte et traitement des données géographiques  
        - Levés topographiques & cartographie aérienne  
        - Cartographie thématique  
        - Numérisation & géoréférencement  
        - Analyse diachronique & changement d’usage des sols  
        - Rédaction scientifique & communication technique  
        - Automatisation de processus & analyses quantitatives
        """)

    # ---- Colonne 2 : Logiciels & Outils par catégorie ----
    with col2:
        st.markdown("Logiciels & Outils")

        st.markdown("**SIG & Cartographie**")
        st.markdown("""
        <span class="badge sig">QGIS</span>
        <span class="badge sig">ArcGIS Pro</span>
        <span class="badge sig">ArcMap</span>
        <span class="badge sig">Google Earth </span>
        """, unsafe_allow_html=True)

        st.markdown("**Télédétection & Analyse spatiale**")
        st.markdown("""
        <span class="badge tld">Landsat</span>
        <span class="badge tld">NDVI</span>
        <span class="badge tld">ERDAS</span>
        <span class="badge tld">OTB</span>
        <span class="badge tld">SNAP ESA</span>
        """, unsafe_allow_html=True)

        st.markdown("**Analyse & Statistiques**")
        st.markdown("""
        <span class="badge analyse">SphinxPlus</span>
        
        """, unsafe_allow_html=True)

        st.markdown("**Bases de données**")
        st.markdown("""
        <span class="badge bdd">MySQL</span>
        <span class="badge bdd">PostgreSQL/GIS</span>
        <span class="badge bdd">Wams</span>
        """, unsafe_allow_html=True)

        st.markdown("**Développement & Automatisation**")
        st.markdown("""
        <span class="badge dev">Python</span>
        <span class="badge dev">Streamlit</span>
        <span class="badge dev">Jupyter Notebook</span>
        <span class="badge dev">Pandas, Geopandas</span>
        <span class="badge dev">Automatisation & modélisation</span>
        """, unsafe_allow_html=True)

        st.markdown("**Drones & Cartographie aérienne**")
        st.markdown("""
        <span class="badge drone">QGroundControl</span>
        <span class="badge drone">Levés topographiques</span>
        """, unsafe_allow_html=True)

        st.markdown("**Photogrammétrie**")
        st.markdown("""
        <span class="badge drone">Agisoft Metashape</span>
        <span class="badge drone">Pix4Mapper</span>
        """, unsafe_allow_html=True)

        

        st.markdown("**Bureautique**")
        st.markdown("""
        <span class="badge lang">Suite Office</span>
        """, unsafe_allow_html=True)


import plotly.graph_objects as go
import streamlit as st

st.header("Radar de compétences")

with st.expander("Voir mes compétences par domaine", expanded=True):

    # ---- Domaines de compétences ----
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

    # ---- Valeurs (1 à 5) ----
    values = [4, 4, 4, 4, 5, 4, 3, 5, 4]

    # ---- Fermer le radar pour former un cercle ----
    categories += categories[:1]
    values += values[:1]

    # ---- Création du radar ----
    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name='Compétences',
        line=dict(color='royalblue', width=3),
        marker=dict(color='royalblue', size=8)
    ))

    # ---- Mise en forme du radar ----
    fig.update_layout(
        polar=dict(
            bgcolor="#f8f9fa",
            radialaxis=dict(
                visible=True,
                range=[0,5],
                tickvals=[1,2,3,4,5],
                ticktext=["Débutant","Basique","Intermédiaire","Avancé","Expert"]
            ),
            angularaxis=dict(
                tickfont=dict(size=12)
            )
        ),
        showlegend=False,
        margin=dict(l=30, r=30, t=30, b=30),
        paper_bgcolor='white'
    )

    st.plotly_chart(fig, use_container_width=True)





