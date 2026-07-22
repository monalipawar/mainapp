import streamlit as st

# ═══════════════════════════════════════════════════════════════════════════════
# THEME + SESSION STATE
# ═══════════════════════════════════════════════════════════════════════════════
THEMES = {
    "Default":   "linear-gradient(160deg,#020617,#0f172a,#1e293b)",
    "Cyberpunk": "linear-gradient(160deg,#1a0030,#3333ff,#00ffee)",
    "Sunset":    "linear-gradient(160deg,#1a0a05,#ff5e62,#ffcc70)",
    "Ocean":     "linear-gradient(160deg,#0a1628,#2193b0,#38bdf8)",
    "Midnight":  "linear-gradient(160deg,#000000,#0f172a,#020617)",
}

if "selected_theme" not in st.session_state:
    st.session_state.selected_theme = "Default"

st.set_page_config(page_title="App Launcher", page_icon="🚀", layout="wide")

# ═══════════════════════════════════════════════════════════════════════════════
# APPS LIST
# ═══════════════════════════════════════════════════════════════════════════════
APPS = [
    {
        "name": "Live Clock",
        "url": "https://times1.streamlit.app/",
        "icon": "🕒",
        "desc": "Check the exact time with this live-updating digital clock.",
        "tag": "Utilities",
        "css_class": "card-crimson",
    },
    {
        "name": "TimeKeeper",
        "url": "https://timekeeper1.streamlit.app/",
        "icon": "⏱️",
        "desc": "Track, manage and visualize your time with precision.",
        "tag": "Productivity",
        "css_class": "card-blue",
    },
    {
        "name": "Solar AI",
        "url": "https://solai1.streamlit.app/",
        "icon": "🌌",
        "desc": "Explore NASA APOD, ISS tracking, asteroids & more.",
        "tag": "Space & AI",
        "css_class": "card-purple",
    },
    {
        "name": "Nimbus AI",
        "url": "https://nimai10.streamlit.app/",
        "icon": "🌤️",
        "desc": "AI-powered weather intelligence and smart outfit picks.",
        "tag": "Weather & AI",
        "css_class": "card-green",
    },
    {
        "name": "Dice Roller",
        "url": "https://diceroller1.streamlit.app/",
        "icon": "🎲",
        "desc": "Roll any dice combination for your tabletop adventures.",
        "tag": "Games",
        "css_class": "card-orange",
    },
    {
        "name": "Animal Dictionary",
        "url": "https://aniking.streamlit.app/",
        "icon": "🐾",
        "desc": "Explore facts, habitats & stats on animals from across the globe.",
        "tag": "Nature & Science",
        "css_class": "card-lime",
    },
    {
        "name": "Activity Finder",
        "url": "https://stuff-to-do.streamlit.app/",
        "icon": "🎈",
        "desc": "Answer a few fun questions and discover your next kid-friendly adventure!",
        "tag": "Kids & Fun",
        "css_class": "card-pink",
    },
    {
        "name": "Draw Finder",
        "url": "https://draw10.streamlit.app/",
        "icon": "🎨",
        "desc": "Answer a few fun questions and get a creative drawing challenge made just for you!",
        "tag": "Creativity",
        "css_class": "card-yellow",
    },
    {
        "name": "Country Explorer",
        "url": "https://explorer1.streamlit.app/",
        "icon": "🌍",
        "desc": "Discover capitals, flags, facts & stats, then quiz yourself on world geography.",
        "tag": "Geography",
        "css_class": "card-teal",
    },
    {
        "name": "CosmicChef",
        "url": "https://cooking1.streamlit.app/",
        "icon": "🍳",
        "desc": "Enter ingredients you have on hand and discover recipes to cook tonight.",
        "tag": "Food & Cooking",
        "css_class": "card-coral",
    },
    {
        "name": "NebulaWallet",
        "url": "https://wallet1.streamlit.app/",
        "icon": "💰",
        "desc": "Log income & expenses, track spending by category, and hit savings goals.",
        "tag": "Finance",
        "css_class": "card-indigo",
    },
    {
        "name": "OrbitMeals",
        "url": "https://mealplanner2.streamlit.app/",
        "icon": "🍽️",
        "desc": "Plan your week, generate your shopping list, orbit your kitchen with ease.",
        "tag": "Meal Planning",
        "css_class": "card-mint",
    },
    {
        "name": "OrbitDates",
        "url": "https://cakes1.streamlit.app/",
        "icon": "🎂",
        "desc": "Never miss a birthday or anniversary again — with gift ideas built in.",
        "tag": "Reminders",
        "css_class": "card-rose",
    },
    {
        "name": "OrbitCountdown",
        "url": "https://events1.streamlit.app/",
        "icon": "🪐",
        "desc": "Track every countdown as a planet orbiting toward its moment.",
        "tag": "Countdowns",
        "css_class": "card-skyblue",
    },
    {
        "name": "Bibliocosm",
        "url": "https://booklink.streamlit.app/",
        "icon": "📚",
        "desc": "Track your reading universe, one book at a time.",
        "tag": "Reading",
        "css_class": "card-violet",
    },
    {
        "name": "VoyagerPlan",
        "url": "https://triplanner1.streamlit.app/",
        "icon": "🧳",
        "desc": "Plan every trip — itinerary, packing list, and budget in one orbit.",
        "tag": "Travel",
        "css_class": "card-cerulean",
    },
    {
        "name": "AutoNova",
        "url": "https://cars10.streamlit.app/",
        "icon": "🏎️",
        "desc": "Record-holding cars, curated — plus live search on any make & model.",
        "tag": "Cars & Records",
        "css_class": "card-gold",
    },
    {
        "name": "VoyagerPlaylist",
        "url": "https://songs1.streamlit.app/",
        "icon": "🎧",
        "desc": "Pick a mood, discover a playlist, drift through the sound.",
        "tag": "Music",
        "css_class": "card-amber",
    },
    {
        "name": "Stardust",
        "url": "https://trivia1.streamlit.app/",
        "icon": "✨",
        "desc": "A daily fact, plus trivia quizzes from across the universe of knowledge.",
        "tag": "Trivia & Facts",
        "css_class": "card-crimson",
    },
    {
        "name": "GalaxyGoals",
        "url": "https://goaltracker1.streamlit.app/",
        "icon": "🌠",
        "desc": "Chart your goals, break them into milestones, track progress.",
        "tag": "Goals & Projects",
        "css_class": "card-emerald",
    },
    {
        "name": "OrbitRules",
        "url": "https://sportrules.streamlit.app/",
        "icon": "🏅",
        "desc": "Quick, clear rulebooks for the world's major sports.",
        "tag": "Sports",
        "css_class": "card-lavender",
    },
    {
        "name": "OrbitRecords",
        "url": "https://worldr.streamlit.app/",
        "icon": "🏆",
        "desc": "Explore the extremes of our world — fastest, tallest, deepest, rarest.",
        "tag": "World Records",
        "css_class": "card-champagne",
    },
    {
        "name": "OrbitChat",
        "url": "https://chatbot10.streamlit.app/",
        "icon": "💬",
        "desc": "Your AI companion, powered by Gemini — free, fast, and always in orbit.",
        "tag": "AI Chat",
        "css_class": "card-periwinkle",
    },
    {
        "name": "GiftGenius",
        "url": "http://gifts1.streamlit.app/",
        "icon": "🎁",
        "desc": "Tell me about them, and I'll find the perfect gift.",
        "tag": "Gift Ideas",
        "css_class": "card-blush",
    },
    {
        "name": "OrbitJournal",
        "url": "https://journal10.streamlit.app/",
        "icon": "📓",
        "desc": "A quiet space to write, reflect, and track how you're really doing.",
        "tag": "Journaling",
        "css_class": "card-orchid",
    },
    {
        "name": "OrbitTasks",
        "url": "https://tasks10.streamlit.app/",
        "icon": "✅",
        "desc": "Capture it, categorize it, cross it off.",
        "tag": "To-Do",
        "css_class": "card-jade",
    },
    {
        "name": "OrbitGuide",
        "url": "https://howto1.streamlit.app/",
        "icon": "🧭",
        "desc": "Clear, step-by-step instructions for everyday problems.",
        "tag": "How-To",
        "css_class": "card-cyan",
    },
]

# ═══════════════════════════════════════════════════════════════════════════════
# GLOBAL CSS
# ═══════════════════════════════════════════════════════════════════════════════
bg = THEMES[st.session_state.selected_theme]

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700;800&display=swap');
html, body, [data-testid="stAppViewContainer"] {{ background: {bg} !important; font-family: 'Outfit', sans-serif !important; }}
.launcher-wrap {{ padding: 2rem; }}
.launcher-header {{ text-align: center; margin-bottom: 2rem; }}
.launcher-header h1 {{ color: white; font-weight: 800; }}
.cards-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 1rem; }}
.app-card {{ 
    background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); 
    border-radius: 16px; padding: 1.5rem; text-decoration: none; color: white;
    transition: 0.3s; display: block;
}}
.app-card:hover {{ background: rgba(255,255,255,0.1); transform: translateY(-5px); }}
.card-icon {{ font-size: 2rem; }}
.card-name {{ font-weight: 700; margin: 0.5rem 0; }}
.card-desc {{ font-size: 0.8rem; opacity: 0.7; }}
</style>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# RENDER UI
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown('<div class="launcher-wrap"><div class="launcher-header"><h1>✦ My App Universe</h1></div><div class="cards-grid">', unsafe_allow_html=True)

for app in APPS:
    st.markdown(f'''
    <a class="app-card" href="{app["url"]}" target="_blank">
        <div class="card-icon">{app["icon"]}</div>
        <div class="card-name">{app["name"]}</div>
        <div class="card-desc">{app["desc"]}</div>
    </a>
    ''', unsafe_allow_html=True)

st.markdown('</div></div>', unsafe_allow_html=True)

# THEME SELECTOR
chosen = st.selectbox("🎨 Theme", list(THEMES.keys()), index=list(THEMES.keys()).index(st.session_state.selected_theme))
if chosen != st.session_state.selected_theme:
    st.session_state.selected_theme = chosen
    st.rerun()
