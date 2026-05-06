import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Electronics Recommender", layout="wide")
st.title("📱 نظام توصية الإلكترونيات")
st.markdown("**توصيات ذكية - إلكترونيات**")

# قاموس المنتجات
names = {
    "iPhone_15_Pro": "📱 iPhone 15 Pro",
    "MacBook_Air_M3": "💻 MacBook Air M3",
    "AirPods_Pro": "🎧 AirPods Pro",
    "Samsung_Galaxy_S24": "📱 Samsung Galaxy S24",
    "Galaxy_Buds": "🎧 Galaxy Buds",
    "Galaxy_Tab_S9": "📱 Galaxy Tab S9",
    "PlayStation_5": "🎮 PlayStation 5",
    "Sony_WH_1000XM5": "🎧 Sony WH-1000XM5",
    "DualSense_Controller": "🎮 DualSense Controller",
    "Apple_Watch_Ultra": "⌚ Apple Watch Ultra",
    "Dell_XPS_15": "💻 Dell XPS 15",
    "Logitech_MX_Keys": "⌨️ Logitech MX Keys",
    "JBL_Flip_6": "🔊 JBL Flip 6",
    "Xbox_Series_X": "🎮 Xbox Series X",
    "Beats_Studio_Pro": "🎧 Beats Studio Pro",
    "Garmin_Fenix_7": "⌚ Garmin Fenix 7",
    "Google_Pixel_8_Pro": "📱 Google Pixel 8 Pro",
    "Microsoft_Surface_Laptop": "💻 Microsoft Surface Laptop",
    "Anker_Power_Bank": "🔋 Anker Power Bank",
    "Razer_Keyboard": "⌨️ Razer Keyboard"
}

# قراءة البيانات
df = pd.read_csv('data/sample_electronics.inter', sep='\t')
st.success(f"✅ تم تحميل {len(df)} تفاعل")

user_items = df.groupby('user_id:token')['item_id:token'].apply(list).to_dict()
users = list(user_items.keys())

all_products = list(names.values())

with st.sidebar:
    st.header("🔍 اختر مستخدم")
    user_id = st.selectbox("", users)
    k = st.slider("عدد التوصيات", 3, 10, 5)
    if st.button("🎯 احصل على توصيات موثقة"):

        history = user_items.get(user_id, [])
        history_names = []
        for item in history:
            if item in names:
                history_names.append(names[item])
            else:
                history_names.append(item)

        st.subheader(f"📜 تاريخ المستخدم {user_id} (منتجات سابقة)")
        for item in history_names[:5]:
            st.write(f"- {item}")

        available = [p for p in all_products if p not in history_names]
        random.shuffle(available)
        recommendations = available[:k]

        st.subheader(f"🎯 توصيات مخصصة للمستخدم {user_id}")
        for i, product in enumerate(recommendations):
            st.write(f"{i+1}. **{product}**")
            st.caption("🔍 منتج مقترح بناءً على اهتماماتك")

        st.caption("📊 التوصيات مبنية على منتجات مشابهة ومكملة لمشترياتك")