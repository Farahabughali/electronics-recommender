import streamlit as st
import pandas as pd

st.set_page_config(page_title="Electronics Recommender", page_icon="📱")

st.title("📱 نظام توصية الإلكترونيات")

# قاموس الأسماء
names = {
    "item_iphone": "iPhone 15 Pro",
    "item_macbook": "MacBook Air M3",
    "item_airpods": "AirPods Pro",
    "item_samsung": "Samsung Galaxy S24",
    "item_buds": "Galaxy Buds",
    "item_tablet": "Galaxy Tab S9",
    "item_playstation": "PlayStation 5",
    "item_headset": "Sony WH-1000XM5",
    "item_controller": "DualSense Controller"
}

# قراءة البيانات
df = pd.read_csv('data/sample_electronics.inter', sep='\t')
st.success(f"✅ تم تحميل {len(df)} تفاعل")

user_items = df.groupby('user_id:token')['item_id:token'].apply(list).to_dict()
users = list(user_items.keys())

with st.sidebar:
    st.header("🔍 اختيار مستخدم")
    user_id = st.selectbox("", users)
    k = st.slider("عدد التوصيات", 3, 10, 5)
    if st.button("🎯 احصل على توصيات"):
        st.subheader(f"📽️ توصيات للمستخدم {user_id}")
        for i, item_id in enumerate(user_items.get(user_id, [])[:k]):
            name = names.get(str(item_id), f"منتج {item_id}")
            st.write(f"{i+1}. {name}")
