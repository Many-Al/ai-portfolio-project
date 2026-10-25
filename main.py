import os
from dotenv import load_dotenv
from litellm import completion

# 1. تحميل المتغيرات من ملف .env
load_dotenv()

# 2. إعداد الرسالة
messages = [
    {"role": "user", "content": "مرحباً! أنا أتعلم هندسة تطبيقات الذكاء الاصطناعي. هل يمكنك إعطائي نصيحة قصيرة ومحفزة للمبتدئين باللغة العربية؟"}
]

# 3. استدعاء النموذج مع معالجة الأخطاء (Error Handling)
try:
    print("⏳ جاري الاتصال بالنموذج... يرجى الانتظار.")
    
    response = completion(
        model="gemini/gemini-3.5-flash-lite",
        messages=messages
    )
    
    # طباعة الرد في حالة النجاح
    print("\n✅ رد النموذج:")
    print(response.choices[0].message.content)

except Exception as e:
    # طباعة رسالة خطأ واضحة ومفيدة في حالة الفشل
    print(f"\n❌ حدث خطأ أثناء الاتصال بالنموذج: {e}")
    print("💡 نصيحة: تحقق من اتصال الإنترنت، أو تأكد من صحة GEMINI_API_KEY في ملف .env")
