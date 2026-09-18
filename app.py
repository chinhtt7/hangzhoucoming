import streamlit as st
import streamlit.components.v1 as components
import os
import socket

# 1. Streamlit Page Configuration
st.set_page_config(
    page_title="✈️ HangzhouComing",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Design System & Streamlit Chrome Override CSS
st.markdown("""
<style>
    /* Hide Streamlit default branding & menus */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Remove padding around main container for edge-to-edge layout */
    .block-container {
        padding-top: 0 !important;
        padding-bottom: 0 !important;
        padding-left: 0 !important;
        padding-right: 0 !important;
        max-width: 100% !important;
    }
    
    /* Ensure component iframe takes full width and clean border */
    iframe {
        border: none !important;
        width: 100% !important;
        min-height: 98vh !important;
    }

    /* Streamlit background matching Design System #F5F6F8 */
    .stApp {
        background-color: #F5F6F8 !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. Supabase Credentials Handling
# Check st.secrets first, then fall back to session state / user input
default_url = "https://wzuvtyjkrtrcygfouynu.supabase.co"
default_key = "sb_publishable_ZL7gyl-nH2mvRcXXXE5Iew_lUsqdqfz"
default_user = "chinhtt"

try:
    if hasattr(st, "secrets"):
        default_url = st.secrets.get("SUPABASE_URL") or "https://wzuvtyjkrtrcygfouynu.supabase.co"
        default_key = st.secrets.get("SUPABASE_KEY") or "sb_publishable_ZL7gyl-nH2mvRcXXXE5Iew_lUsqdqfz"
        default_user = st.secrets.get("USER_ID") or "chinhtt"
except Exception:
    pass

supabase_url = default_url
supabase_key = default_key
user_id = default_user

# 4. Streamlit Sidebar Controls & Supabase Configuration
with st.sidebar:
    st.markdown("### 杭 Hangzhou 90 Settings")
    
    with st.expander("☁️ Cấu hình Supabase Cloud Sync", expanded=not bool(supabase_url and supabase_key)):
        st.caption("Nhập URL & Anon Key của Supabase để tự động đồng bộ tiến độ giữa Máy tính và Điện thoại:")
        cfg_url = st.text_input("Supabase Project URL", value=supabase_url, placeholder="https://xyz.supabase.co")
        cfg_key = st.text_input("Supabase Anon Key", value=supabase_key, type="password", placeholder="eyJhbGciOi...")
        cfg_user = st.text_input("User ID (Tên định danh)", value=user_id)
        
        if cfg_url and cfg_key:
            supabase_url = cfg_url
            supabase_key = cfg_key
            user_id = cfg_user
            st.success("✅ Đã kết nối thông tin Supabase!")
            
    st.markdown("---")
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
    except Exception:
        local_ip = "127.0.0.1"
    st.info(f"📱 **Mở trên điện thoại (Cùng Wi-Fi):**\n\n`http://{local_ip}:8501`")
    st.caption("Hangzhou 90 Days • LOG-VR Design System Standard")

# 5. Read and Render HTML Core App with Supabase Injection
current_dir = os.path.dirname(os.path.abspath(__file__))
html_file_path = os.path.join(current_dir, "index.html")

if os.path.exists(html_file_path):
    with open(html_file_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    
    # Inject Supabase Config if available
    if supabase_url and supabase_key:
        injection = f"""
        <script>
            window.SUPABASE_CONFIG = {{
                url: "{supabase_url.strip()}",
                key: "{supabase_key.strip()}",
                userId: "{user_id.strip()}"
            }};
        </script>
        """
        html_content = html_content.replace("<head>", f"<head>\n{injection}")
    
    components.html(html_content, height=1050, scrolling=True)
else:
    st.error(f"Không tìm thấy file index.html tại: {html_file_path}")
