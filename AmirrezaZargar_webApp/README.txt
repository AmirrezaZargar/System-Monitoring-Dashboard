IN Terminal:
## Run Project

To run this project locally, follow the steps below:
```bash
# 1. Go to the project directory
cd AmirrezaZargar_webApp

# 2. Create a virtual environment
py -m venv venv

# 3. Activate the virtual environment
venv\Scripts\activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Start the application
py app.py



این پروژه بر اساس نیازمندی‌های تسک به این صورت پیاده‌سازی شده است:

1. پیاده‌سازی Web App با Python
   - پروژه با استفاده از Python و فریم‌ورک Flask توسعه داده شده است.
2.نمایش صفحه در مسیر root
   - صفحه اصلی در مسیر `/` در دسترس است.

3. نمایش متن ثابت
   - متن ثابت `Hello World` روی صفحه نمایش داده می‌شود.

4. نمایش تاریخ و ساعت
   - تاریخ و زمان فعلی سیستم در هر بار بارگذاری صفحه نمایش داده می‌شود.

5. نمایش میزان مصرف RAM و CPU
   - با استفاده از کتابخانه `psutil` میزان مصرف CPU و RAM خوانده و نمایش داده می‌شود.

6. حداقل 3 رنگ مختلف برای بک‌گراند
   - برنامه از چند رنگ مختلف برای پس‌زمینه استفاده می‌کند و در هر بار refresh یک رنگ جدید انتخاب می‌شود.

7. تغییر بک‌گراند در هر Refresh
   - در هر بار refresh صفحه، رنگ بک‌گراند تغییر می‌کند.

8. به‌روزرسانی datetime و resource usage در هر Refresh
   - در هر بار refresh صفحه، datetime، CPU usage و RAM usage مجدداً محاسبه و نمایش داده می‌شوند.

9. قابلیت تغییر رنگ‌ها بدون تغییر سورس و بدون build مجدد image
   - رنگ‌ها از طریق Environment Variable با نام `BACKGROUND_COLORS` قابل تنظیم هستند.

10. Dockerize شدن پروژه
    - فایل‌های `Dockerfile` و `docker-compose.yml` برای اجرای پروژه با Docker و Docker Compose ارائه شده‌اند.

11.راه‌اندازی با اسکریپت
    - فایل `run.bat` برای اجرای سریع پروژه در محیط ویندوز ارائه شده است.

12. وضعیت اجرای Docker در محیط فعلی
    - به دلیل محدودیت شبکه در دسترسی به Docker Hub، در محیط فعلی امکان pull کردن base image فراهم نشد. با این حال ساختار Docker پروژه کامل است و در محیطی با دسترسی مناسب شبکه، قابل اجرا خواهد بود.
