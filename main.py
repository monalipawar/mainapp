import streamlit as st

# ═══════════════════════════════════════════════════════════════════════════════
# CONFIG
# ═══════════════════════════════════════════════════════════════════════════════

st.set_page_config(page_title="App Universe", page_icon="🚀", layout="wide")

# ═══════════════════════════════════════════════════════════════════════════════
# THEME + SESSION STATE
# ═══════════════════════════════════════════════════════════════════════════════

THEMES = {
    "Nebula Purple": {"primary": "#a78bfa", "secondary": "#f472b6", "accent": "#818cf8"},
    "Aurora Green":  {"primary": "#34d399", "secondary": "#a3e635", "accent": "#22d3ee"},
    "Solar Flare":   {"primary": "#fb923c", "secondary": "#f87171", "accent": "#fbbf24"},
    "Deep Space":    {"primary": "#60a5fa", "secondary": "#818cf8", "accent": "#38bdf8"},
    "Rose Comet":    {"primary": "#fb7185", "secondary": "#f472b6", "accent": "#e879f9"},
}

if "selected_theme" not in st.session_state or st.session_state.selected_theme not in THEMES:
    st.session_state.selected_theme = "Nebula Purple"

# ═══════════════════════════════════════════════════════════════════════════════
# APPS LIST
# ═══════════════════════════════════════════════════════════════════════════════

APPS = [
    {"name": "Live Clock", "url": "https://times1.streamlit.app/", "icon": "🕒",
     "desc": "Check the exact time with this live-updating digital clock.", "tag": "Utilities"},
    {"name": "TimeKeeper", "url": "https://timekeeper1.streamlit.app/", "icon": "⏱️",
     "desc": "Track, manage and visualize your time with precision.", "tag": "Productivity"},
    {"name": "Solar AI", "url": "https://solai1.streamlit.app/", "icon": "🌌",
     "desc": "Explore NASA APOD, ISS tracking, asteroids & more.", "tag": "Space & AI"},
    {"name": "Nimbus AI", "url": "https://nimai10.streamlit.app/", "icon": "🌤️",
     "desc": "AI-powered weather intelligence and smart outfit picks.", "tag": "Weather & AI"},
    {"name": "Dice Roller", "url": "https://diceroller1.streamlit.app/", "icon": "🎲",
     "desc": "Roll any dice combination for your tabletop adventures.", "tag": "Games"},
    {"name": "Animal Dictionary", "url": "https://aniking.streamlit.app/", "icon": "🐾",
     "desc": "Explore facts, habitats & stats on animals from across the globe.", "tag": "Nature & Science"},
    {"name": "Activity Finder", "url": "https://stuff-to-do.streamlit.app/", "icon": "🎈",
     "desc": "Answer a few fun questions and discover your next kid-friendly adventure!", "tag": "Kids & Fun"},
    {"name": "Draw Finder", "url": "https://draw10.streamlit.app/", "icon": "🎨",
     "desc": "Answer a few fun questions and get a creative drawing challenge made just for you!", "tag": "Creativity"},
    {"name": "Country Explorer", "url": "https://explorer1.streamlit.app/", "icon": "🌍",
     "desc": "Discover capitals, flags, facts & stats, then quiz yourself on world geography.", "tag": "Geography"},
    {"name": "CosmicChef", "url": "https://cooking1.streamlit.app/", "icon": "🍳",
     "desc": "Enter ingredients you have on hand and discover recipes to cook tonight.", "tag": "Food & Cooking"},
    {"name": "NebulaWallet", "url": "https://wallet1.streamlit.app/", "icon": "💰",
     "desc": "Log income & expenses, track spending by category, and hit savings goals.", "tag": "Finance"},
    {"name": "OrbitMeals", "url": "https://mealplanner2.streamlit.app/", "icon": "🍽️",
     "desc": "Plan your week, generate your shopping list, orbit your kitchen with ease.", "tag": "Meal Planning"},
    {"name": "OrbitDates", "url": "https://cakes1.streamlit.app/", "icon": "🎂",
     "desc": "Never miss a birthday or anniversary again — with gift ideas built in.", "tag": "Reminders"},
    {"name": "OrbitCountdown", "url": "https://events1.streamlit.app/", "icon": "🪐",
     "desc": "Track every countdown as a planet orbiting toward its moment.", "tag": "Countdowns"},
    {"name": "Bibliocosm", "url": "https://booklink.streamlit.app/", "icon": "📚",
     "desc": "Track your reading universe, one book at a time.", "tag": "Reading"},
    {"name": "VoyagerPlan", "url": "https://triplanner1.streamlit.app/", "icon": "🧳",
     "desc": "Plan every trip — itinerary, packing list, and budget in one orbit.", "tag": "Travel"},
    {"name": "AutoNova", "url": "https://cars10.streamlit.app/", "icon": "🏎️",
     "desc": "Record-holding cars, curated — plus live search on any make & model.", "tag": "Cars & Records"},
    {"name": "VoyagerPlaylist", "url": "https://songs1.streamlit.app/", "icon": "🎧",
     "desc": "Pick a mood, discover a playlist, drift through the sound.", "tag": "Music"},
    {"name": "Stardust", "url": "https://trivia1.streamlit.app/", "icon": "✨",
     "desc": "A daily fact, plus trivia quizzes from across the universe of knowledge.", "tag": "Trivia & Facts"},
    {"name": "GalaxyGoals", "url": "https://goaltracker1.streamlit.app/", "icon": "🌠",
     "desc": "Chart your goals, break them into milestones, track progress.", "tag": "Goals & Projects"},
    {"name": "OrbitRules", "url": "https://sportrules.streamlit.app/", "icon": "🏅",
     "desc": "Quick, clear rulebooks for the world's major sports.", "tag": "Sports"},
    {"name": "OrbitRecords", "url": "https://worldr.streamlit.app/", "icon": "🏆",
     "desc": "Explore the extremes of our world — fastest, tallest, deepest, rarest.", "tag": "World Records"},
    {"name": "OrbitChat", "url": "https://chatbot10.streamlit.app/", "icon": "💬",
     "desc": "Your AI companion, powered by Gemini — free, fast, and always in orbit.", "tag": "AI Chat"},
    {"name": "GiftGenius", "url": "http://gifts1.streamlit.app/", "icon": "🎁",
     "desc": "Tell me about them, and I'll find the perfect gift.", "tag": "Gift Ideas"},
    {"name": "OrbitJournal", "url": "https://journal10.streamlit.app/", "icon": "📓",
     "desc": "A quiet space to write, reflect, and track how you're really doing.", "tag": "Journaling"},
    {"name": "OrbitTasks", "url": "https://tasks10.streamlit.app/", "icon": "✅",
     "desc": "Capture it, categorize it, cross it off.", "tag": "To-Do"},
    {"name": "OrbitGuide", "url": "https://howto1.streamlit.app/", "icon": "🧭",
     "desc": "Clear, step-by-step instructions for everyday problems.", "tag": "How-To"},
]

# ═══════════════════════════════════════════════════════════════════════════════
# GLOBAL CSS
# ═══════════════════════════════════════════════════════════════════════════════

t = THEMES[st.session_state.selected_theme]

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"] {{
    font-family: 'Outfit', sans-serif;
}}

.stApp {{
    background: radial-gradient(ellipse at top, #1a1333 0%, #0a0715 50%, #050308 100%);
    background-attachment: fixed;
}}

.stApp::before {{
    content: "";
    position: fixed;
    top: 0; left: 0; width: 100%; height: 100%;
    background-image:
        radial-gradient(2px 2px at 20% 30%, white, transparent),
        radial-gradient(2px 2px at 60% 70%, white, transparent),
        radial-gradient(1px 1px at 80% 10%, white, transparent),
        radial-gradient(1px 1px at 40% 90%, white, transparent),
        radial-gradient(1px 1px at 90% 50%, white, transparent);
    background-size: 300px 300px;
    opacity: 0.4;
    pointer-events: none;
    z-index: 0;
}}

.main .block-container {{
    max-width: 1200px;
    padding-top: 1.5rem;
    padding-bottom: 4rem;
}}

/* Hero */
.hero {{ text-align: center; padding: 1rem 0 2rem 0; }}
.hero h1 {{
    font-size: 2.6rem;
    font-weight: 800;
    background: linear-gradient(135deg, {t['primary']}, {t['secondary']});
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    background-clip: text; margin-bottom: 0.3rem;
}}
.hero p {{ color: rgba(255,255,255,0.55); font-size: 0.95rem; margin: 0; }}

/* Cards grid */
.cards-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(230px, 1fr));
    gap: 1.1rem;
}}

.app-card {{
    background: rgba(255,255,255,0.045);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.09);
    border-radius: 18px;
    padding: 1.4rem 1.3rem;
    text-decoration: none;
    color: white;
    display: block;
    transition: all 0.25s ease;
    position: relative;
    overflow: hidden;
}}
.app-card:hover {{
    background: rgba(255,255,255,0.08);
    border-color: {t['primary']}77;
    transform: translateY(-4px);
    box-shadow: 0 10px 30px -10px {t['primary']}44;
}}

.card-icon {{ font-size: 1.9rem; margin-bottom: 0.5rem; display: block; }}
.card-name {{ font-weight: 700; font-size: 1rem; margin-bottom: 0.3rem; color: white; }}
.card-desc {{ font-size: 0.8rem; line-height: 1.35; color: rgba(255,255,255,0.55); margin-bottom: 0.7rem; }}

.card-tag {{
    display: inline-flex;
    align-items: center;
    background: linear-gradient(135deg, {t['primary']}22, {t['secondary']}22);
    border: 1px solid {t['primary']}55;
    color: {t['primary']};
    border-radius: 999px;
    padding: 2px 10px;
    font-size: 0.68rem;
    font-weight: 500;
}}

/* Theme selector */
.stSelectbox label {{
    color: rgba(255,255,255,0.6) !important;
    font-size: 0.85rem !important;
}}
.stSelectbox div[data-baseweb="select"] {{
    background: rgba(255,255,255,0.08) !important;
    border-radius: 10px !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    color: white !important;
}}

hr {{ border-color: rgba(255,255,255,0.08) !important; }}
</style>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# SIDEBAR — THEME
# ═══════════════════════════════════════════════════════════════════════════════

with st.sidebar:
    st.markdown("### 🎨 Theme")
    chosen = st.selectbox(
        "Color theme",
        list(THEMES.keys()),
        index=list(THEMES.keys()).index(st.session_state.selected_theme),
        label_visibility="collapsed",
    )
    if chosen != st.session_state.selected_theme:
        st.session_state.selected_theme = chosen
        st.rerun()

    st.markdown("---")
    st.metric("Apps in orbit", len(APPS))

# ═══════════════════════════════════════════════════════════════════════════════
# HERO
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
<div class="hero">
<h1>✦ My App Universe</h1>
<p>A growing constellation of cosmic-themed apps — pick one and launch.</p>
</div>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# CARD GRID
# ═══════════════════════════════════════════════════════════════════════════════

cards_html = '<div class="cards-grid">'
for app in APPS:
    cards_html += f'''
    <a class="app-card" href="{app["url"]}" target="_blank">
        <span class="card-icon">{app["icon"]}</span>
        <div class="card-name">{app["name"]}</div>
        <div class="card-desc">{app["desc"]}</div>
        <span class="card-tag">{app["tag"]}</span>
    </a>
    '''
cards_html += '</div>'

st.markdown(cards_html, unsafe_allow_html=True)
