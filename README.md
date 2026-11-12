# TS3 Blacklist Bypass & Cache Cleaner

## Download

- **Prebuilt release:** Download [TS3-Bypass.exe](https://github.com/abolfazlsamini/Teamspeak-Client-Blacklist-Bypass-Python/releases/download/release/TS3-Bypass.exe) or browse [Releases](../../releases).  
  Run the program as Administrator. No Python installation is required.
- **Source script:** `ts-bypass.py`
- **Build it yourself (Windows):** Run `build.bat` from the `build/windows` folder to build the script from source.

## دانلود

- **نسخه آماده:** فایل اجرایی [TS3-Bypass.exe](https://github.com/abolfazlsamini/Teamspeak-Client-Blacklist-Bypass-Python/releases/download/release/TS3-Bypass.exe) را دانلود کنید یا از صفحه [Releases](../../releases) دریافت کنید.  
  برنامه را به صورت Run As Administrator اجرا کنید. نیازی به نصب پایتون نیست.
- **فایل سورس:** `ts-bypass.py`
- **بیلد دستی (ویندوز):** فایل `build.bat` را از پوشه `build/windows` اجرا کنید تا اسکریپت از سورس بیلد شود.

## About the Tool (FA / EN)

This Python script is designed to bypass the TeamSpeak 3 blacklist and clear the TS3 client cache.  
It fixes the annoying **"This server is blacklisted. Refusing to connect."** error and works on **Windows**, **Linux**, and **macOS** with admin/root rights.

این اسکریپت پایتونی برای دور زدن بلاک‌لیست سرورهای TeamSpeak 3 طراحی شده است.  
با اجرای آن می‌توانید خطاهای **"This server is blacklisted. Refusing to connect."** را برطرف کرده و کش کلاینت TS3 را پاک کنید.  
ابزار روی **ویندوز**، **لینوکس** و **مک** قابل اجراست و نیاز به دسترسی ادمین/روت دارد.

## Features

- Automatically adds blacklist domains to the system `hosts` file
- Creates a backup of the `hosts` file before making changes
- Clears the TeamSpeak 3 cache directory
- Professional colored logging with timestamps
- Cross-platform path detection and privilege check
- Simple interactive menu

- افزودن خودکار دامنه‌های بلاک‌لیست به فایل `hosts` سیستم
- پشتیبان‌گیری خودکار از فایل `hosts` قبل از تغییر
- پاکسازی پوشه کش TeamSpeak 3
- نمایش پیام‌های رنگی و لاگ‌های حرفه‌ای با زمان‌بندی
- تشخیص خودکار سیستم‌عامل و مسیرهای مورد نیاز
- منوی تعاملی ساده و کاربرپسند

## Requirements

- Python 3.6 or higher
- **Administrator** (Windows) or **root** (Linux/macOS) privileges
- No external dependencies (uses only the Python standard library)

- پایتون 3.6 یا بالاتر
- دسترسی **Administrator** (ویندوز) یا **root** (لینوکس/مک)
- کتابخانه‌های استاندارد پایتون (بدون نیاز به نصب چیز اضافه)

## How to Use

### 1. Download

Download the prebuilt release from [Releases](../../releases) or directly download [TS3-Bypass.exe](https://github.com/abolfazlsamini/Teamspeak-Client-Blacklist-Bypass-Python/releases/download/release/TS3-Bypass.exe), or save `ts-bypass.py` anywhere on your system.  
To build it yourself on Windows, run `build.bat` from the `build/windows` folder.

### 2. Run with elevated privileges

#### Windows

Run the prebuilt executable as **Administrator**.  
If you are using the Python script, right-click `ts-bypass.py` and choose **Run as Administrator**.  
Ensure Python is in your system PATH.

#### Linux / macOS

```bash
sudo python3 ts-bypass.py
```

If you downloaded a prebuilt release, run it with `sudo`.

### 3. Choose an action

After the banner, select one of the following:

- **1**: Add bypass entries to the hosts file
- **2**: Clear TeamSpeak 3 cache
- **3**: Exit

## نحوه استفاده

### 1. دانلود

نسخه آماده را از صفحه [Releases](../../releases) یا فایل اجرایی [TS3-Bypass.exe](https://github.com/abolfazlsamini/Teamspeak-Client-Blacklist-Bypass-Python/releases/download/release/TS3-Bypass.exe) دانلود کنید، یا فایل `ts-bypass.py` را در سیستم خود ذخیره کنید.  
برای بیلد دستی در ویندوز، فایل `build.bat` را از پوشه `build/windows` اجرا کنید.

### 2. اجرا با دسترسی بالا

#### ویندوز

فایل اجرایی نسخه آماده را با دسترسی **Administrator** اجرا کنید.  
اگر از اسکریپت پایتون استفاده می‌کنید، روی `ts-bypass.py` راست‌کلیک کرده و **Run as Administrator** را انتخاب کنید.  
مطمئن شوید Python در PATH باشد.

#### لینوکس / مک

```bash
sudo python3 ts-bypass.py
```

اگر نسخه آماده را دانلود کرده‌اید، آن را با `sudo` اجرا کنید.

### 3. انتخاب عملیات

پس از نمایش بنر، یکی از گزینه‌های زیر را وارد کنید:

- **1**: افزودن خطوط بای‌پس به فایل hosts
- **2**: پاک کردن کش TeamSpeak 3
- **3**: خروج

## Warnings

- Editing the hosts file is a system-level operation. The tool saves a backup (`hosts.bak`) before any changes.
- Using this tool might violate your network or server policies. Use it at your own risk.
- After applying the bypass, you might need to restart the TS3 client.

- ویرایش فایل `hosts` یک عملیات سیستمی است. ابزار پیش از تغییر یک نسخه پشتیبان (`hosts.bak`) ذخیره می‌کند.
- استفاده از این ابزار ممکن است با قوانین شبکه یا سرور شما مغایرت داشته باشد. مسئولیت استفاده بر عهده کاربر است.
- پس از اعمال بای‌پس، ممکن است لازم باشد کلاینت TS3 را دوباره راه‌اندازی کنید.

## License

This project is released for educational purposes only. The user assumes all responsibility for its use.

این پروژه صرفاً برای اهداف آموزشی منتشر شده است. هرگونه استفاده نادرست بر عهده کاربر می‌باشد.

## Credits

This repository is a fork of [AsmrCodeZ-YT/Teamspeak-Client-Blacklist-Bypass-Python](https://github.com/AsmrCodeZ-YT/Teamspeak-Client-Blacklist-Bypass-Python).

این مخزن فورک‌شده از [AsmrCodeZ-YT/Teamspeak-Client-Blacklist-Bypass-Python](https://github.com/AsmrCodeZ-YT/Teamspeak-Client-Blacklist-Bypass-Python) است.
