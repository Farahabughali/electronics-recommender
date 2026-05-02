import streamlit as st
import pandas as pd

# إعدادات الصفحة
st.set_page_config(page_title="Electronics Recommender", page_icon="📱", layout="centered")

# تنسيق الخلفية والألوان
st.markdown(
    """
    <style>
    .main {
        background-color: #f9fafb;
    }
    .stApp {
        background-color: #f9fafb;
    }
    .css-1d391kg {
        background-color: #ffffff;
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }
    .stButton>button {
        background-color: #2c3e50;
        color: white;
        border-radius: 30px;
        padding: 0.5rem 1.5rem;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #1e2b38;
        color: white;
    }
    .recommendation-box {
        background-color: #f1f3f5;
        border-radius: 15px;
        padding: 10px 15px;
        margin: 8px 0;
        font-size: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("📱 نظام توصية الإلكترونيات")
st.caption("توصيات ذكية مبنية على نموذج ItemKNN")

# قاموس الأسماء
names = {
    "item_iphone": "📱 iPhone 15 Pro",
    "item_macbook": "💻 MacBook Air M3",
    "item_airpods": "🎧 AirPods Pro",
    "item_samsung": "📱 Samsung Galaxy S24",
    "item_buds": "🎧 Galaxy Buds",
    "item_tablet": "📱 Galaxy Tab S9",
    "item_playstation": "🎮 PlayStation 5",
    "item_headset": "🎧 Sony WH-1000XM5",
    "item_controller": "🎮 DualSense Controller"
}

# تحميل البيانات
df = pd.read_csv('data/sample_electronics.inter', sep='\t')
st.success(f"✅ {len(df)} تفاعل تم تحميلها")

# تجهيز التوصيات
user_items = df.groupby('user_id:token')['item_id:token'].apply(list).to_dict()
users = list(user_items.keys())

# الشريط الجانبي
with st.sidebar:
    st.markdown("## 🔍 اختر المستخدم")
    user_id = st.selectbox("", users)
    k = st.slider("عدد التوصيات", 5, 10, 10)
    if st.button("🎯 احصل على توصيات"):
        st.subheader(f"📌 توصيات للمستخدم {user_id}")
        for i, item_id in enumerate(user_items.get(user_id, [])[:k]):
            name = names.get(str(item_id), f"⚙️ منتج {item_id}")
            st.markdown(f"<div class='recommendation-box'>{i+1}. {name}</div>", unsafe_allow_html=True)
