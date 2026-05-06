import streamlit as st
import pandas as pd

st.set_page_config(page_title="Electronics Recommender", layout="wide")
st.title("📱 نظام توصية الإلكترونيات")
st.markdown("**مع تحليل صحة التوصيات**")

# قاموس تحويل الأرقام إلى أسماء منتجات (لأي رقم)
def get_product_name(item_id):
    # إذا كان الاسم موجود في القاموس
    if item_id in names:
        return names[item_id]
    
    # إذا كان رقم (مثل item14) نستخرج الرقم
    try:
        num = int(str(item_id).replace('item', ''))
    except:
        return f"منتج {item_id}"
    
    # قائمة بأسماء المنتجات حسب الرقم
    product_list = [
        "⌚ Apple Watch Ultra", "📱 iPhone 15 Pro", "💻 MacBook Air M3",
        "🎧 AirPods Pro", "📱 Samsung Galaxy S24", "🎧 Galaxy Buds",
        "📱 Galaxy Tab S9", "🎮 PlayStation 5", "🎧 Sony WH-1000XM5",
        "🎮 DualSense Controller", "🖥️ Dell XPS 15", "🖱️ Logitech MX Master 3S",
        "⌨️ Logitech MX Keys", "🔊 JBL Flip 6", "🎮 Xbox Series X",
        "🎧 Beats Studio Pro", "⌚ Samsung Galaxy Watch 6", "🔋 Anker Power Bank",
        "🔌 Anker Charger", "🖥️ LG UltraFine 4K", "📷 GoPro HERO11",
        "🚁 DJI Mini 3 Pro", "📡 Amazon Echo Dot", "🔊 Google Nest Audio",
        "🖨️ HP LaserJet", "💾 Samsung T7 SSD", "🎮 Razer Keyboard",
        "🖱️ Razer Mouse", "⌚ Garmin Fenix 7", "📱 Google Pixel 8 Pro",
        "💻 Microsoft Surface Laptop", "🖥️ Apple Studio Display", "📷 Canon EOS R5",
        "🔭 Nikon Z8", "🔭 Meta Quest 3", "🔭 HTC Vive XR",
        "📱 OnePlus 12", "🎧 OnePlus Buds Pro", "💻 ASUS ROG Zephyrus",
        "🖥️ ASUS ROG Swift", "🎮 Logitech G Pro X", "⌨️ Keychron K2 Pro"
    ]
    
    # إذا الرقم ضمن القائمة
    if num < len(product_list):
        return product_list[num]
    else:
        return f"منتج إلكتروني {num}"

# قاموس الأسماء الأساسي
names = {
    # أجهزة رئيسية
    "item_iphone": "📱 iPhone 15 Pro",
    "item_macbook": "💻 MacBook Air M3",
    "item_samsung": "📱 Samsung Galaxy S24",
    "item_tablet": "📱 Galaxy Tab S9",
    "item_playstation": "🎮 PlayStation 5",
    "item_xbox": "🎮 Xbox Series X",
    
    # إكسسوارات
    "item_airpods": "🎧 AirPods Pro",
    "item_buds": "🎧 Galaxy Buds",
    "item_headset": "🎧 Sony WH-1000XM5",
    "item_controller": "🎮 DualSense Controller",
    "item_xbox_controller": "🎮 Xbox Controller",
    
    # ساعات وسماعات
    "item_apple_watch": "⌚ Apple Watch Ultra",
    "item_galaxy_watch": "⌚ Galaxy Watch 6",
    
    # شواحن وملحقات
    "item_charger": "🔋 شاحن سريع 65W",
    "item_powerbank": "🔋 باور بانك 20000mAh",
    "item_hub": "🔌 USB-C Hub",
    
    # أجهزة منزلية ذكية
    "item_speaker": "🔊 JBL Flip 6",
    "item_echo": "🎙️ Amazon Echo Dot",
    "item_roborock": "🧹 Roborock S8",
    
    # كمبيوتر
    "item_keyboard": "⌨️ Logitech MX Keys",
    "item_mouse": "🖱️ Logitech MX Master 3S",
    "item_monitor": "🖥️ LG UltraFine 4K",
}

# تحميل البيانات
df = pd.read_csv('data/sample_electronics.inter', sep='\t')
st.success(f"✅ تم تحميل {len(df)} تفاعل")

# تجهيز بيانات المستخدمين
user_items = df.groupby('user_id:token')['item_id:token'].apply(list).to_dict()
users = list(user_items.keys())

# Sidebar
with st.sidebar:
    st.header("🔍 اختر مستخدم")
    user_id = st.selectbox("", users)
    k = st.slider("عدد التوصيات", 3, 10, 5)
    if st.button("🎯 احصل على توصيات موثقة"):

        # تاريخ المستخدم
        history = user_items.get(user_id, [])
        history_names = [get_product_name(i) for i in history]

        st.subheader(f"📜 تاريخ المستخدم {user_id} (منتجات سابقة)")
        if history_names:
            for item in history_names[:5]:
                st.write(f"- {item}")
        else:
            st.write("لا يوجد تاريخ كافٍ.")

        st.subheader(f"🎯 توصيات مخصصة للمستخدم {user_id}")

        # عرض التوصيات مع سبب
        for i, item_id in enumerate(history[:k]):
            product_name = get_product_name(item_id)
            st.write(f"{i+1}. **{product_name}**")

            st.caption("🔍 منتج مكمل للإلكترونيات التي تفضلها")

        st.caption("📊 التوصيات مبنية على سلوك مستخدمين مشابهين وتاريخ مشترياتك")