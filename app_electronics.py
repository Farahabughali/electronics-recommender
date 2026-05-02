import streamlit as st
import pandas as pd

st.set_page_config(page_title="Electronics Recommender")
st.title("📱 نظام توصية الإلكترونيات")

# قاموس أسماء للمنتجات الإلكترونية
names = {
    "item0": "iPhone 15 Pro", "item1": "Samsung Galaxy S24", "item2": "MacBook Air M3",
    "item3": "Sony WH-1000XM5", "item4": "iPad Pro", "item5": "Dell XPS 15",
    "item10": "Google Pixel 8", "item12": "OnePlus 12", "item15": "Logitech MX Master 3S",
    "item20": "Anker Power Bank", "item22": "Razer Keyboard", "item25": "ASUS ROG Laptop",
    "item30": "Kindle Paperwhite", "item32": "Bose QC Ultra", "item35": "Apple Watch Ultra",
    "item40": "JBL Flip 6", "item42": "Xbox Series X", "item45": "PlayStation 5",
    "item48": "Meta Quest 3"
}

# قراءة البيانات
df = pd.read_csv('dataset/amazon_sample_800/amazon_sample_800.inter', sep='\t')
st.success(f"✅ تم تحميل {len(df)} تفاعل من منتجات إلكترونيات")

# تجهيز التوصيات لكل مستخدم
user_items = df.groupby('user_id:token')['item_id:token'].apply(list).to_dict()
users = list(user_items.keys())

with st.sidebar:
    st.header("🔍 اختيار مستخدم")
    user_id = st.selectbox("اختر مستخدم", users)
    if st.button("🎯 احصل على توصيات"):
        st.subheader(f"📽️ توصيات مخصصة للمستخدم {user_id}")
        for i, item_id in enumerate(user_items.get(user_id, [])[:5]):
            product_name = names.get(str(item_id), f"منتج {item_id}")
            st.write(f"{i+1}. {product_name}")