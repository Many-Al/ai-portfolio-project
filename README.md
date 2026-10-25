# 🤖 AI Portfolio Project: Gemini Chat App

تطبيق بسيط وقوي للتفاعل مع نماذج الذكاء الاصطناعي من Google (Gemini) باستخدام Python.

## 🚀 المميزات
- استخدام مكتبة **LiteLLM** للتواصل الموحد مع النماذج.
- حماية مفاتيح API باستخدام مكتبة **python-dotenv** وملف `.env`.
- معالجة أخطاء احترافية (Error Handling) باستخدام `try...except` لضمان استقرار التطبيق.

## 🛠️ متطلبات التشغيل
- Python 3.10+
- حساب Google AI Studio للحصول على API Key.

## ⚙️ كيفية التثبيت والتشغيل

1. استنساخ المستودع:
   ```bash
   git clone https://github.com/Many-Al/ai-portfolio-project.git
   cd ai-portfolio-project
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt

   GEMINI_API_KEY=your_api_key_here
   python main.py
