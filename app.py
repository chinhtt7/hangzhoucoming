import streamlit as st
import streamlit.components.v1 as components
import os
import socket

# 1. Streamlit Page Configuration
st.set_page_config(
    page_title="Hangzhou 90 — Tiếng Trung Tác Chiến",
    page_icon="杭",
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

# 3. Get local IP for mobile access on same Wi-Fi
def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

local_ip = get_local_ip()

# 4. Optional Streamlit Sidebar for Utilities & Mobile Sync
with st.sidebar:
    st.markdown("### 杭 Hangzhou 90 Settings")
    st.info(f"📱 **Mở trên điện thoại (Cùng Wi-Fi):**\n\n`http://{local_ip}:8501`")
    
    st.markdown("---")
    st.markdown("#### ☁️ Triển khai Streamlit Cloud")
    st.caption("Để mở app trên điện thoại mọi lúc mọi nơi mà không cần bật máy tính, bạn chỉ cần đưa folder này lên GitHub rồi kết nối với **share.streamlit.io** (hoàn toàn miễn phí).")
    
    st.markdown("---")
    st.caption("Hangzhou 90 Days • LOG-VR Design System Standard")

# 5. Read and Render HTML Core App
current_dir = os.path.dirname(os.path.abspath(__file__))
html_file_path = os.path.join(current_dir, "index.html")

if os.path.exists(html_file_path):
    with open(html_file_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    
    # Render component with responsive full-height viewport
    components.html(html_content, height=1050, scrolling=True)
else:
    st.error(f"Không tìm thấy file index.html tại: {html_file_path}")
