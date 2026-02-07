import streamlit as st
from brain import CurioBrain
from utils import log_interaction, init_db

st.set_page_config(page_title="Curio: Character Forge", page_icon="🎭", layout="wide")

init_db()

st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #ffffff; }
    .sidebar-char-card { background: #111; padding: 15px; border-radius: 10px; border: 1px solid #333; margin-top: 20px; }
    .stChatMessage { border-radius: 15px; border: 1px solid #333; margin: 10px 0; }
    .contrast-badge { background-color: #ff4b4b; color: white; padding: 2px 8px; border-radius: 10px; font-size: 0.7em; margin-bottom: 10px; display: inline-block; }
    </style>
""", unsafe_allow_html=True)

api_key = st.secrets["GEMINI_API_KEY"]
brain = CurioBrain(api_key)

if "char_active" not in st.session_state:
    st.session_state.char_active = False
if "char_data" not in st.session_state:
    st.session_state.char_data = {"name": "Assistant", "desc": "", "img": None}
if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.title("🎭 Character Forge")
    
    with st.expander("✨ Create New AI Entity", expanded=not st.session_state.char_active):
        char_name = st.text_input("Name")
        char_desc = st.text_area("Description")
        
        if st.button("Generate AI Soul"):
            with st.spinner("Visualizing..."):
                img_data = brain.generate_image(f"{char_name}: {char_desc}")
                st.session_state.char_data = {"name": char_name, "desc": char_desc, "img": img_data}
                st.session_state.char_active = True
                st.session_state.messages = []
                st.rerun()

    if st.session_state.char_active:
        st.markdown("<div class='sidebar-char-card'>", unsafe_allow_html=True)
        if st.session_state.char_data["img"]:
            st.image(st.session_state.char_data["img"], width=100)
        st.subheader(st.session_state.char_data["name"])
        if st.button("Reset to Sandbox"):
            st.session_state.char_active = False
            st.session_state.messages = []
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    st.divider()
    contrast_mode = st.toggle("🥊 Contrast Mode", value=False)
    depth = st.radio("Reasoning", ["Surface", "Standard", "Deep"])

st.title(f"🧠 Curio: {st.session_state.char_data['name'] if st.session_state.char_active else 'Neural Sandbox'}")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Inject query..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            persona = st.session_state.char_data["name"] if st.session_state.char_active else "Assistant"
            custom_instruct = st.session_state.char_data["desc"] if st.session_state.char_active else None
            
            res, sources = brain.generate_response(prompt, persona, depth, contrast_mode, custom_instruct)
            
            if contrast_mode:
                st.markdown("<span class='contrast-badge'>🥊 CONTRAST MODE</span>", unsafe_allow_html=True)
            st.markdown(res)
            
            if sources:
                with st.expander("🌐 Grounding Sources"):
                    for s in sources:
                        st.markdown(f"• [{s['title']}]({s['uri']})")
            
            log_interaction(prompt, res)
            st.session_state.messages.append({"role": "assistant", "content": res})