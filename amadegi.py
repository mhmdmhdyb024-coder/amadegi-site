from http.server import HTTPServer, BaseHTTPRequestHandler
import os

PAGE = r'''
<!doctype html><html lang="fa" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#101d36"><meta name="description" content="دانشنامه آموزشی جنگ‌ها و نبردهای تاریخ ایران"><title>آمادگی دفاعی | محمد مهدی عباسی</title><style>
@import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;500;600;700;800&display=swap');:root{--bg:#f3f5fa;--card:#fff;--text:#17233c;--muted:#66738a;--navy:#101d36;--gold:#d9ad58;--border:#e5e9f0}body.dark{--bg:#101827;--card:#1a263a;--text:#f1f4fa;--muted:#b2bfd2;--border:#2b3a51}*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;font-family:Vazirmatn,Tahoma,sans-serif;background:var(--bg);color:var(--text)}header{background:linear-gradient(120deg,#0b1529,#1b3155);color:white;padding:15px 4%;position:sticky;top:0;z-index:5}.nav{display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap}.logo{font-weight:800;color:#f0ca7d;font-size:20px}nav{display:flex;gap:4px;flex-wrap:wrap}button{font-family:inherit;cursor:pointer}nav button,.theme{background:transparent;color:white;border:1px solid #ffffff30;border-radius:9px;padding:9px 12px}nav button.active,nav button:hover{color:#f0ca7d;background:#ffffff20}.hero{text-align:center;padding:65px 6%;background:radial-gradient(circle at 15% 20%,#d9ad5830,transparent 25%),linear-gradient(120deg,#101d36,#243e68);color:white}.hero h1{font-size:clamp(27px,5vw,44px);margin:0 0 12px}.hero p{line-height:2.2;color:#d8e0ee;max-width:750px;margin:auto}.creator{display:inline-block;margin-top:18px;padding:8px 20px;border:1px solid #d9ad58;border-radius:30px;color:#f3d18e}.container{width:min(1100px,93%);margin:35px auto}.section{display:none}.section.active{display:block;animation:fade .25s}@keyframes fade{from{opacity:0;transform:translateY(7px)}to{opacity:1;transform:none}}.section-title{margin-bottom:22px}.section-title h2{font-size:26px}.section-title p,.card p,.event p{color:var(--muted);line-height:2}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:16px}.card,.event,.sources{background:var(--card);border:1px solid var(--border);border-radius:15px;padding:20px;margin-bottom:13px;box-shadow:0 5px 18px #17233c09}.btn{background:var(--gold);color:#17233c;border:0;border-radius:9px;padding:11px 18px;font-weight:700;margin:5px}.search{width:100%;padding:13px;border:1px solid var(--border);border-radius:10px;background:var(--card);color:var(--text);font:inherit;margin:0 0 18px}.event summary{cursor:pointer;font-weight:700;line-height:1.9}.event[open]{border-color:var(--gold)}.sources h2{margin-top:0}.sources li{line-height:2.2;margin:8px 0}a{color:#b18432}body.dark a{color:#f0ca7d}.small{font-size:13px;color:var(--muted)}.question{margin:18px 0}.option{display:block;padding:9px;background:var(--bg);border:1px solid var(--border);border-radius:8px;margin:7px 0}.result{display:none;padding:15px;background:#d9ad5820;border-radius:10px;line-height:2}footer{background:#101d36;color:#d8e0ee;text-align:center;padding:27px;line-height:2;margin-top:45px}footer strong{color:#f0ca7d}@media(max-width:700px){.nav{justify-content:center}.logo{width:100%;text-align:center}nav{justify-content:center}nav button{font-size:12px;padding:7px}}

/* ===== انیمیشن‌های پیشرفته ===== */
:root{--glow:rgba(217,173,88,.28)}
body{overflow-x:hidden}
header{backdrop-filter:blur(14px);box-shadow:0 8px 28px #07132635}
.hero{position:relative;isolation:isolate;overflow:hidden}
.hero:before,.hero:after{content:"";position:absolute;z-index:-1;border:1px solid #f0ca7d35;border-radius:50%;width:360px;height:360px;animation:orbit 18s linear infinite}
.hero:before{top:-230px;right:-100px;box-shadow:0 0 70px #d9ad5820}
.hero:after{bottom:-290px;left:-80px;width:430px;height:430px;animation-direction:reverse}
.hero h1{animation:heroTitle 1s cubic-bezier(.2,.8,.2,1) both;text-shadow:0 8px 30px #0005}
.hero p,.creator{animation:riseIn 1s .18s both}
.creator{box-shadow:0 0 0 0 var(--glow);animation:riseIn 1s .18s both,softPulse 3s 1.2s infinite}
@keyframes orbit{to{transform:rotate(360deg)}}
@keyframes heroTitle{from{opacity:0;transform:translateY(25px) scale(.97);filter:blur(5px)}to{opacity:1;transform:none;filter:none}}
@keyframes riseIn{from{opacity:0;transform:translateY(18px)}to{opacity:1;transform:none}}
@keyframes softPulse{0%,100%{box-shadow:0 0 0 0 #d9ad5800}50%{box-shadow:0 0 0 9px #d9ad5812}}
.card,.event,.sources{transition:transform .35s cubic-bezier(.2,.8,.2,1),box-shadow .35s,border-color .35s;transform-style:preserve-3d}
.card:hover,.event:hover,.sources:hover{transform:translateY(-6px);box-shadow:0 18px 38px #101d3620;border-color:#d9ad58}
.btn{position:relative;overflow:hidden;transition:transform .2s,box-shadow .25s,filter .25s}
.btn:hover{transform:translateY(-3px);box-shadow:0 9px 22px #d9ad5850;filter:saturate(1.15)}
.btn:active{transform:scale(.96)}
.btn:after{content:"";position:absolute;top:-60%;left:-80%;width:45%;height:220%;background:linear-gradient(90deg,transparent,#fff9,transparent);transform:rotate(25deg);transition:left .65s}
.btn:hover:after{left:140%}
nav button,.theme{transition:background .25s,color .25s,transform .2s,border-color .25s}
nav button:hover,.theme:hover{transform:translateY(-2px);border-color:#d9ad58}
.search{transition:box-shadow .25s,border-color .25s,transform .25s}
.search:focus{outline:none;border-color:#d9ad58;box-shadow:0 0 0 4px #d9ad5825;transform:translateY(-2px)}
.event{transition:all .3s}
.event[open]{box-shadow:0 12px 28px #d9ad5820}
.event summary{transition:color .2s}
.event summary:hover{color:#b18432}
.section.active{animation:sectionIn .5s cubic-bezier(.2,.8,.2,1) both}
@keyframes sectionIn{from{opacity:0;transform:translateY(16px)}to{opacity:1;transform:none}}
.reveal{opacity:0;transform:translateY(24px);transition:opacity .7s ease,transform .7s cubic-bezier(.2,.8,.2,1)}
.reveal.visible{opacity:1;transform:none}
#particleCanvas{position:fixed;inset:0;width:100%;height:100%;pointer-events:none;z-index:0;opacity:.42}
header,main,.hero,.sources,footer{position:relative}
header,.hero,main,.sources,footer{z-index:1}
body.dark #particleCanvas{opacity:.24}
.result{animation:riseIn .45s both;border:1px solid #d9ad5860}
.option{transition:transform .2s,border-color .2s,background .2s}
.option:hover{transform:translateX(-4px);border-color:#d9ad58;background:var(--card)}
footer{overflow:hidden}
footer:before{content:"";display:block;width:100px;height:2px;background:linear-gradient(90deg,transparent,#d9ad58,transparent);margin:0 auto 18px;animation:footerGlow 3s infinite}
@keyframes footerGlow{0%,100%{opacity:.4;transform:scaleX(.7)}50%{opacity:1;transform:scaleX(1.5)}}
@media(prefers-reduced-motion:reduce){*,*:before,*:after{animation-duration:.01ms!important;animation-iteration-count:1!important;scroll-behavior:auto!important;transition-duration:.01ms!important}.reveal{opacity:1;transform:none}}


/* ===== بسته انیمیشن‌های تکمیلی ===== */
html{scroll-padding-top:90px}
body:before{content:"";position:fixed;inset:-30%;z-index:-1;pointer-events:none;background:radial-gradient(circle at 20% 30%,#d9ad580c,transparent 25%),radial-gradient(circle at 80% 70%,#4169a10c,transparent 28%);animation:bgDrift 22s ease-in-out infinite alternate}
@keyframes bgDrift{0%{transform:translate3d(-2%,0,0) rotate(0)}100%{transform:translate3d(2%,-2%,0) rotate(5deg)}}
.logo{display:inline-block;animation:logoFloat 4s ease-in-out infinite;text-shadow:0 0 18px #f0ca7d30}
@keyframes logoFloat{0%,100%{transform:translateY(0)}50%{transform:translateY(-3px)}}
.hero{background-size:150% 150%;animation:heroGradient 12s ease infinite alternate}
@keyframes heroGradient{0%{background-position:0% 50%}100%{background-position:100% 50%}}
.hero:after{box-shadow:0 0 55px #d9ad5815,inset 0 0 45px #d9ad580a}
.section-title h2{position:relative;display:inline-block}
.section-title h2:after{content:"";position:absolute;right:0;bottom:-8px;width:55%;height:3px;border-radius:5px;background:linear-gradient(90deg,#d9ad58,transparent);transform-origin:right;animation:titleLine 1s .2s both}
@keyframes titleLine{from{transform:scaleX(0)}to{transform:scaleX(1)}}
.card,.event,.sources{position:relative;overflow:hidden}
.card:before,.event:before,.sources:before{content:"";position:absolute;top:0;left:-130%;width:65%;height:100%;pointer-events:none;background:linear-gradient(110deg,transparent,#d9ad5810,transparent);transform:skewX(-18deg);transition:left .8s ease}
.card:hover:before,.event:hover:before,.sources:hover:before{left:150%}
.card h3{transition:transform .25s,color .25s}
.card:hover h3{transform:translateX(-3px);color:#b18432}
.event[open] summary{color:#b18432}
.event[open] p{animation:riseIn .45s both}
.option:has(input:checked){border-color:#d9ad58;background:#d9ad5815;box-shadow:inset -3px 0 #d9ad58}
button:focus-visible,a:focus-visible,input:focus-visible{outline:3px solid #d9ad58;outline-offset:3px}
.creator{position:relative;overflow:hidden}
.creator:after{content:"";position:absolute;inset:0;transform:translateX(-120%);background:linear-gradient(100deg,transparent,#fff5,transparent);animation:badgeShine 5s 2s infinite}
@keyframes badgeShine{0%,65%{transform:translateX(-120%)}85%,100%{transform:translateX(120%)}}
#scrollProgress{position:fixed;top:0;right:0;height:3px;width:0;background:linear-gradient(90deg,#f0ca7d,#d9ad58);z-index:20;box-shadow:0 0 12px #d9ad58;pointer-events:none}
#backToTop{position:fixed;left:18px;bottom:18px;width:44px;height:44px;border:1px solid #d9ad58;background:#101d36;color:#f0ca7d;border-radius:50%;font-size:20px;opacity:0;visibility:hidden;transform:translateY(12px);transition:.3s;z-index:10;box-shadow:0 8px 22px #101d3640}
#backToTop.show{opacity:1;visibility:visible;transform:translateY(0)}
#backToTop:hover{transform:translateY(-5px) rotate(-8deg);box-shadow:0 12px 25px #d9ad5850}
@keyframes gentleBob{0%,100%{transform:translateY(0)}50%{transform:translateY(-5px)}}
.grid .card:nth-child(2n){animation-delay:.08s}
.grid .card:nth-child(3n){animation-delay:.16s}
.result{box-shadow:0 8px 25px #d9ad5818}
@media(max-width:700px){#backToTop{left:12px;bottom:12px}}


/* ===== شمشیر دنبال‌کننده نشانگر موس ===== */
#swordFollower{position:fixed;left:0;top:0;width:58px;height:58px;z-index:9998;pointer-events:none;opacity:0;transform:translate3d(-100px,-100px,0) rotate(-35deg);filter:drop-shadow(0 0 7px #f0ca7d99);will-change:transform;transition:opacity .18s ease}
#swordFollower.visible{opacity:1}
#swordFollower:after{content:"";position:absolute;width:24px;height:24px;left:5px;bottom:2px;border-radius:50%;background:#f0ca7d55;filter:blur(12px);z-index:-1}
@media(hover:none),(pointer:coarse){#swordFollower{display:none}}
@media(prefers-reduced-motion:reduce){#swordFollower{display:none}}

</style></head><body><canvas id="particleCanvas" aria-hidden="true"></canvas><header><div class="nav"><div class="logo">🛡️ آمادگی دفاعی</div><nav><button class="active" onclick="showPage('home',this)">خانه</button><button onclick="showPage('events',this)">جنگ‌ها و نبردها</button><button onclick="showPage('analysis',this)">تحلیل</button><button onclick="showPage('lessons',this)">درس‌آموخته‌ها</button><button onclick="showPage('quiz',this)">آزمون</button><button onclick="showPage('about',this)">درباره ما</button></nav><button class="theme" onclick="document.body.classList.toggle('dark')">🌙 تغییر پوسته</button></div></header>
<section class="hero"><h1>آمادگی دفاعی؛ آگاهی، امنیت، آینده</h1><p>دانشنامه آموزشی تاریخ دفاعی ایران، جنگ‌ها و نبردها، امنیت ملی و اهمیت صلح و آگاهی.</p><div class="creator">✦ طراح سایت: محمد مهدی عباسی ✦</div><p><button class="btn" onclick="showPage('events')">مطالعه جنگ‌ها</button><button class="btn" onclick="showPage('quiz')">شرکت در آزمون</button></p></section>
<main class="container"><section id="home" class="section active"><div class="section-title"><h2>به وب‌سایت آمادگی دفاعی خوش آمدید</h2><p>شناخت تاریخ، بررسی منصفانه منابع و آگاهی، پایه‌های جامعه‌ای آماده و صلح‌طلب هستند.</p></div><div class="grid"><div class="card"><h3>📜 دانشنامه تاریخ دفاعی</h3><p>مجموعه‌ای از نبردها و جنگ‌های مهم ایران از دوران باستان تا معاصر.</p><button class="btn" onclick="showPage('events')">مطالعه</button></div><div class="card"><h3>🔎 تحلیل تاریخی</h3><p>بررسی عوامل سیاسی، جغرافیایی و اقتصادی جنگ‌ها.</p><button class="btn" onclick="showPage('analysis')">مشاهده</button></div><div class="card"><h3>🎓 آزمون</h3><p>دانسته‌های خود را بسنجید.</p><button class="btn" onclick="showPage('quiz')">شروع</button></div></div></section>
<section id="events" class="section"><div class="section-title"><h2>دانشنامه جنگ‌ها و نبردهای تاریخ ایران</h2><p>این مجموعه رویدادهای مهم و مستند را دربرمی‌گیرد؛ همه درگیری‌های محلی و کوتاه‌مدت چند هزار ساله در منابع ثبت نشده‌اند. برخی تاریخ‌ها و روایت‌ها نیز محل اختلاف پژوهشگران‌اند. برای دیدن شرح هر رویداد، عنوان را باز کنید.</p><p><strong>تعداد مدخل‌ها: 41</strong></p></div><input id="search" class="search" placeholder="🔍 جست‌وجو بر اساس نام، دوره یا کشور..." oninput="searchEvents()"><div id="eventList"><details class="event"><summary>1. نبردهای ایلام با آشور و بابل (هزاره دوم تا سده هفتم پ.م.)</summary><p>ایلامیان در جنوب‌غرب فلات ایران بارها با دولت‌های میان‌رودان، به‌ویژه آشور و بابل، جنگیدند. رقابت بر سر شوش، راه‌های بازرگانی و نفوذ منطقه‌ای از عوامل اصلی بود. یورش آشوربانیپال در سده هفتم پ.م. به ویرانی شوش انجامید و قدرت سیاسی ایلام را به‌شدت کاهش داد.</p><p><strong>برای بررسی:</strong> تاریخ این رویداد را باید در پیوند با شرایط سیاسی، اقتصادی و جغرافیایی زمان خود مطالعه کرد. در مواردی که منابع اختلاف دارند، تاریخ تقریبی یا روایت‌های متفاوت باید جداگانه سنجیده شوند.</p></details>
<details class="event"><summary>2. جنگ مادها و بابلیان با آشور؛ سقوط نینوا (۶۱۲ پ.م.)</summary><p>مادها و بابلیان در ائتلافی علیه امپراتوری آشور جنگیدند. تصرف نینوا در ۶۱۲ پ.م. نقطه عطفی در پایان قدرت آشور بود و جایگاه مادها را در غرب آسیا تقویت کرد. جزئیات مراحل ائتلاف و تاریخ برخی عملیات در منابع باستانی متفاوت گزارش شده است.</p><p><strong>برای بررسی:</strong> تاریخ این رویداد را باید در پیوند با شرایط سیاسی، اقتصادی و جغرافیایی زمان خود مطالعه کرد. در مواردی که منابع اختلاف دارند، تاریخ تقریبی یا روایت‌های متفاوت باید جداگانه سنجیده شوند.</p></details>
<details class="event"><summary>3. لشکرکشی‌های کوروش و تشکیل شاهنشاهی هخامنشی (حدود ۵۵۰ تا ۵۳۹ پ.م.)</summary><p>کوروش دوم با شکست آستیاگ، پادشاهی ماد را به قدرت نوظهور پارس پیوند زد؛ سپس لیدی و بابل را فتح کرد. این فتوحات ساختار شاهنشاهی گسترده‌ای پدید آورد. اداره سرزمین‌های گوناگون و حفظ راه‌ها و ساتراپی‌ها در دوام این امپراتوری نقش مهم داشت.</p><p><strong>برای بررسی:</strong> تاریخ این رویداد را باید در پیوند با شرایط سیاسی، اقتصادی و جغرافیایی زمان خود مطالعه کرد. در مواردی که منابع اختلاف دارند، تاریخ تقریبی یا روایت‌های متفاوت باید جداگانه سنجیده شوند.</p></details>
<details class="event"><summary>4. جنگ‌های ایران و یونان (۴۹۹ تا ۴۴۹ پ.م.)</summary><p>درگیری از شورش شهرهای ایونی آغاز شد و به لشکرکشی‌های ایران به یونان انجامید. ماراتون، ترموپیل، سالامیس و پلاته از نبردهای مشهور این دوره‌اند. ایران نتوانست دولت‌شهرهای یونانی را به‌طور پایدار تابع کند، اما شاهنشاهی هخامنشی پابرجا ماند و رقابت دریایی و سیاسی ادامه یافت.</p><p><strong>برای بررسی:</strong> تاریخ این رویداد را باید در پیوند با شرایط سیاسی، اقتصادی و جغرافیایی زمان خود مطالعه کرد. در مواردی که منابع اختلاف دارند، تاریخ تقریبی یا روایت‌های متفاوت باید جداگانه سنجیده شوند.</p></details>
<details class="event"><summary>5. حمله اسکندر و سقوط هخامنشیان (۳۳۴ تا ۳۳۰ پ.م.)</summary><p>اسکندر پس از عبور از هلسپونت در گرانیک، ایسوس و گوگمل با سپاه هخامنشی جنگید. شکست داریوش سوم در گوگمل راه تصرف مراکز شاهنشاهی را گشود. تحرک سپاه مقدونی، هماهنگی فرماندهی و بحران‌های درونی دربار از عوامل مهم نتیجه جنگ بودند.</p><p><strong>برای بررسی:</strong> تاریخ این رویداد را باید در پیوند با شرایط سیاسی، اقتصادی و جغرافیایی زمان خود مطالعه کرد. در مواردی که منابع اختلاف دارند، تاریخ تقریبی یا روایت‌های متفاوت باید جداگانه سنجیده شوند.</p></details>
<details class="event"><summary>6. جنگ‌های سلوکیان و نیروهای ایرانی (سده سوم تا دوم پ.م.)</summary><p>پس از مرگ اسکندر، جانشینان او بر بخش‌هایی از ایران فرمان راندند. شورش‌ها و استقلال‌طلبی مناطق شرقی و برآمدن اشکانیان، قدرت سلوکیان را به‌تدریج محدود کرد. این روند مجموعه‌ای از جنگ‌ها و تحولات سیاسی بود، نه یک نبرد منفرد.</p><p><strong>برای بررسی:</strong> تاریخ این رویداد را باید در پیوند با شرایط سیاسی، اقتصادی و جغرافیایی زمان خود مطالعه کرد. در مواردی که منابع اختلاف دارند، تاریخ تقریبی یا روایت‌های متفاوت باید جداگانه سنجیده شوند.</p></details>
<details class="event"><summary>7. جنگ‌های اشکانیان و روم؛ نبرد حَرّان (۵۳ پ.م. و سده‌های بعد)</summary><p>رقابت ایران و روم بر سر ارمنستان و میان‌رودان چندین قرن ادامه داشت. در حَرّان، سورنا سپاه کراسوس را شکست داد. سواره‌نظام کماندار و سواران زره‌پوش اشکانی در این جنگ‌ها مؤثر بودند. مرز دو قدرت بارها تغییر کرد و شهرهایی چون تیسفون اهمیت راهبردی داشتند.</p><p><strong>برای بررسی:</strong> تاریخ این رویداد را باید در پیوند با شرایط سیاسی، اقتصادی و جغرافیایی زمان خود مطالعه کرد. در مواردی که منابع اختلاف دارند، تاریخ تقریبی یا روایت‌های متفاوت باید جداگانه سنجیده شوند.</p></details>
<details class="event"><summary>8. جنگ‌های ساسانیان و روم؛ اسارت والرین (سده سوم تا هفتم م.)</summary><p>شاپور یکم در جنگ‌های سده سوم چند بار رومیان را شکست داد و والرین، امپراتور روم، در ۲۶۰ م. اسیر شد. در دوره‌های بعد جنگ بر سر ارمنستان، میان‌رودان و قفقاز ادامه یافت. جنگ نهایی ۶۰۲ تا ۶۲۸ هر دو امپراتوری را فرسوده کرد.</p><p><strong>برای بررسی:</strong> تاریخ این رویداد را باید در پیوند با شرایط سیاسی، اقتصادی و جغرافیایی زمان خود مطالعه کرد. در مواردی که منابع اختلاف دارند، تاریخ تقریبی یا روایت‌های متفاوت باید جداگانه سنجیده شوند.</p></details>
<details class="event"><summary>9. جنگ ساسانیان با هپتالیان (سده پنجم م.)</summary><p>هپتالیان در آسیای مرکزی به قدرت رسیدند و در چند نبرد ساسانیان را شکست دادند. پیروز یکم در ۴۸۴ کشته شد. این شکست بحران سیاسی و مالی در ایران ایجاد کرد و توازن قدرت در شرق را تغییر داد.</p><p><strong>برای بررسی:</strong> تاریخ این رویداد را باید در پیوند با شرایط سیاسی، اقتصادی و جغرافیایی زمان خود مطالعه کرد. در مواردی که منابع اختلاف دارند، تاریخ تقریبی یا روایت‌های متفاوت باید جداگانه سنجیده شوند.</p></details>
<details class="event"><summary>10. جنگ‌های ایران و اعراب و پایان ساسانیان (حدود ۶۳۳ تا ۶۵۱ م.)</summary><p>پس از جنگ‌های فرسایشی با بیزانس و بحران جانشینی، سپاهیان خلافت به قلمرو ساسانی حمله کردند. قادسیه، جلولا و نهاوند از نقاط مهم این روند بودند. یزدگرد سوم به شرق عقب نشست و در ۶۵۱ کشته شد. منابع درباره تاریخ و جزئیات برخی نبردها اختلاف دارند.</p><p><strong>برای بررسی:</strong> تاریخ این رویداد را باید در پیوند با شرایط سیاسی، اقتصادی و جغرافیایی زمان خود مطالعه کرد. در مواردی که منابع اختلاف دارند، تاریخ تقریبی یا روایت‌های متفاوت باید جداگانه سنجیده شوند.</p></details>
<details class="event"><summary>11. قیام‌ها و مقاومت‌های محلی پس از فتح ایران (سده‌های هفتم تا نهم م.)</summary><p>در طبرستان، سیستان، خراسان و نواحی کوهستانی مقاومت‌ها و شورش‌های متعددی رخ داد. این رخدادها در زمان‌ها و مناطق مختلف روی دادند و یک جنگ واحد نبودند. بعدها حکومت‌های طاهری، صفاری و سامانی در بستر کاهش اقتدار خلافت گسترش یافتند.</p><p><strong>برای بررسی:</strong> تاریخ این رویداد را باید در پیوند با شرایط سیاسی، اقتصادی و جغرافیایی زمان خود مطالعه کرد. در مواردی که منابع اختلاف دارند، تاریخ تقریبی یا روایت‌های متفاوت باید جداگانه سنجیده شوند.</p></details>
<details class="event"><summary>12. جنگ‌های طاهریان و شورش‌های خراسان (سده نهم م.)</summary><p>طاهریان در خراسان با شورش‌های محلی و رقابت‌های سیاسی روبه‌رو بودند. کنترل راه‌ها، مالیات و انتصاب حاکمان از زمینه‌های تنش بود. این دوره نشان‌دهنده شکل‌گیری تدریجی قدرت‌های ایرانیِ نیمه‌مستقل در چارچوب خلافت عباسی است.</p><p><strong>برای بررسی:</strong> تاریخ این رویداد را باید در پیوند با شرایط سیاسی، اقتصادی و جغرافیایی زمان خود مطالعه کرد. در مواردی که منابع اختلاف دارند، تاریخ تقریبی یا روایت‌های متفاوت باید جداگانه سنجیده شوند.</p></details>
<details class="event"><summary>13. نبردهای یعقوب لیث صفاری و خلافت عباسی (سده نهم م.)</summary><p>یعقوب لیث از سیستان برخاست و با گسترش قلمرو خود با نیروهای خلافت درگیر شد. نبرد دیرالعاقول در ۸۷۶ م. به شکست او انجامید و پیشروی به بغداد متوقف شد. با این حال صفاریان قدرت مهمی در شرق ایران باقی ماندند.</p><p><strong>برای بررسی:</strong> تاریخ این رویداد را باید در پیوند با شرایط سیاسی، اقتصادی و جغرافیایی زمان خود مطالعه کرد. در مواردی که منابع اختلاف دارند، تاریخ تقریبی یا روایت‌های متفاوت باید جداگانه سنجیده شوند.</p></details>
<details class="event"><summary>14. جنگ‌های سامانیان با صفاریان و قدرت‌های همسایه (سده‌های نهم و دهم م.)</summary><p>سامانیان برای کنترل خراسان و فرارود با صفاریان و دیگر قدرت‌های منطقه رقابت کردند. پیروزی اسماعیل سامانی بر عمرو لیث در ۹۰۰ م. جایگاه سامانیان را تثبیت کرد و خراسان را به مرکز مهم سیاسی و فرهنگی تبدیل ساخت.</p><p><strong>برای بررسی:</strong> تاریخ این رویداد را باید در پیوند با شرایط سیاسی، اقتصادی و جغرافیایی زمان خود مطالعه کرد. در مواردی که منابع اختلاف دارند، تاریخ تقریبی یا روایت‌های متفاوت باید جداگانه سنجیده شوند.</p></details>
<details class="event"><summary>15. نبرد دندانقان؛ سلجوقیان و غزنویان (۱۰۴۰ م.)</summary><p>طغرل و چغری بیگ در دندانقان سپاه مسعود غزنوی را شکست دادند. کمبود تدارکات و فرسودگی سپاه غزنوی در کنار تحرک سلجوقیان در نتیجه نبرد مؤثر بود. پیروزی راه گسترش سلجوقیان در ایران را باز کرد.</p><p><strong>برای بررسی:</strong> تاریخ این رویداد را باید در پیوند با شرایط سیاسی، اقتصادی و جغرافیایی زمان خود مطالعه کرد. در مواردی که منابع اختلاف دارند، تاریخ تقریبی یا روایت‌های متفاوت باید جداگانه سنجیده شوند.</p></details>
<details class="event"><summary>16. جنگ‌های سلجوقیان در غرب ایران و آناتولی (سده‌های یازدهم و دوازدهم م.)</summary><p>سلجوقیان برای تثبیت قدرت با بیزانس، امیران محلی و رقیبان داخلی جنگیدند. نبرد ملازگرد در ۱۰۷۱ میان سلجوقیان روم و بیزانس رخ داد و زمینه گسترش ترکمانان در آناتولی را فراهم کرد؛ این نبرد در قلمرو ایران امروزی رخ نداد، اما در تاریخ سیاسی جهان ایرانی و همسایگان اهمیت داشت.</p><p><strong>برای بررسی:</strong> تاریخ این رویداد را باید در پیوند با شرایط سیاسی، اقتصادی و جغرافیایی زمان خود مطالعه کرد. در مواردی که منابع اختلاف دارند، تاریخ تقریبی یا روایت‌های متفاوت باید جداگانه سنجیده شوند.</p></details>
<details class="event"><summary>17. حمله مغول و جنگ با خوارزمشاهیان (از ۱۲۱۹ م.)</summary><p>پس از بحران روابط تجاری و دیپلماتیک، چنگیزخان به قلمرو خوارزمشاهیان یورش برد. بخارا، سمرقند، مرو و نیشابور آسیب دیدند. پراکندگی نیروها، تصمیم‌های ناهماهنگ و تحرک ارتش مغول از عوامل شکست بودند. پیامدها شامل ویرانی گسترده و دگرگونی ساختار سیاسی منطقه بود.</p><p><strong>برای بررسی:</strong> تاریخ این رویداد را باید در پیوند با شرایط سیاسی، اقتصادی و جغرافیایی زمان خود مطالعه کرد. در مواردی که منابع اختلاف دارند، تاریخ تقریبی یا روایت‌های متفاوت باید جداگانه سنجیده شوند.</p></details>
<details class="event"><summary>18. فتح الموت و فروپاشی قدرت نزاریان به دست مغول (۱۲۵۶ م.)</summary><p>هلاکوخان در جریان لشکرکشی به غرب آسیا دژهای اسماعیلیان نزاری را یکی پس از دیگری تصرف کرد. سقوط الموت در ۱۲۵۶ پایان قدرت مستقل سیاسی این شبکه در ایران بود؛ هرچند جامعه اسماعیلی باقی ماند.</p><p><strong>برای بررسی:</strong> تاریخ این رویداد را باید در پیوند با شرایط سیاسی، اقتصادی و جغرافیایی زمان خود مطالعه کرد. در مواردی که منابع اختلاف دارند، تاریخ تقریبی یا روایت‌های متفاوت باید جداگانه سنجیده شوند.</p></details>
<details class="event"><summary>19. فتح بغداد به دست هلاکو (۱۲۵۸ م.)</summary><p>سپاه مغول بغداد را محاصره و تصرف کرد و خلافت عباسی بغداد پایان یافت. کشتار و ویرانی شهر پیامد سنگینی داشت. این رویداد توازن قدرت در غرب آسیا را تغییر داد و حکومت ایلخانی در ایران شکل گرفت.</p><p><strong>برای بررسی:</strong> تاریخ این رویداد را باید در پیوند با شرایط سیاسی، اقتصادی و جغرافیایی زمان خود مطالعه کرد. در مواردی که منابع اختلاف دارند، تاریخ تقریبی یا روایت‌های متفاوت باید جداگانه سنجیده شوند.</p></details>
<details class="event"><summary>20. نبرد عین جالوت و توقف پیشروی مغولان (۱۲۶۰ م.)</summary><p>نیروهای مملوکی مصر در عین جالوت سپاه مغول را شکست دادند. نبرد در فلسطین امروزی رخ داد، نه ایران؛ اما برای سرنوشت ایلخانان و مرزهای غربی قلمرو آنان اهمیت داشت.</p><p><strong>برای بررسی:</strong> تاریخ این رویداد را باید در پیوند با شرایط سیاسی، اقتصادی و جغرافیایی زمان خود مطالعه کرد. در مواردی که منابع اختلاف دارند، تاریخ تقریبی یا روایت‌های متفاوت باید جداگانه سنجیده شوند.</p></details>
<details class="event"><summary>21. جنگ‌های ایلخانان با ممالیک (سده‌های سیزدهم و چهاردهم م.)</summary><p>ایلخانان برای گسترش نفوذ در شام بارها با ممالیک مصر جنگیدند. نبردهای حمص و تلاش‌های مکرر برای تصرف شام نتیجه قطعی نداشت. این جنگ‌ها منابع مالی ایلخانان را فرسود و دیپلماسی با قدرت‌های همسایه را پیچیده کرد.</p><p><strong>برای بررسی:</strong> تاریخ این رویداد را باید در پیوند با شرایط سیاسی، اقتصادی و جغرافیایی زمان خود مطالعه کرد. در مواردی که منابع اختلاف دارند، تاریخ تقریبی یا روایت‌های متفاوت باید جداگانه سنجیده شوند.</p></details>
<details class="event"><summary>22. لشکرکشی‌های تیمور به ایران (دهه ۱۳۸۰ تا اوایل سده پانزدهم م.)</summary><p>تیمور به خراسان، مازندران، فارس، عراق عجم و آذربایجان لشکر کشید. مقاومت شهرها گاه با سرکوب شدید روبه‌رو شد. این لشکرکشی‌ها ساختار حکومت‌های محلی را تضعیف کرد؛ در دوره جانشینان او برخی مراکز هنری و علمی رونق گرفتند.</p><p><strong>برای بررسی:</strong> تاریخ این رویداد را باید در پیوند با شرایط سیاسی، اقتصادی و جغرافیایی زمان خود مطالعه کرد. در مواردی که منابع اختلاف دارند، تاریخ تقریبی یا روایت‌های متفاوت باید جداگانه سنجیده شوند.</p></details>
<details class="event"><summary>23. جنگ صفویان و ازبکان؛ نبرد مرو (۱۵۱۰ م.)</summary><p>شاه اسماعیل یکم در مرو سپاه محمد شیبانی را شکست داد و نفوذ صفویان را در خراسان تقویت کرد. رقابت با ازبکان بر سر خراسان در دوره‌های بعد ادامه یافت و مرز شرقی صفویان بارها محل درگیری شد.</p><p><strong>برای بررسی:</strong> تاریخ این رویداد را باید در پیوند با شرایط سیاسی، اقتصادی و جغرافیایی زمان خود مطالعه کرد. در مواردی که منابع اختلاف دارند، تاریخ تقریبی یا روایت‌های متفاوت باید جداگانه سنجیده شوند.</p></details>
<details class="event"><summary>24. نبرد چالدران؛ صفویان و عثمانیان (۱۵۱۴ م.)</summary><p>سپاه شاه اسماعیل صفوی از ارتش سلطان سلیم اول شکست خورد. توپخانه و سلاح‌های آتشین عثمانی در برابر نیروی عمدتاً سواره صفوی نقش مهمی داشت. عثمانیان تبریز را موقتاً گرفتند اما نتوانستند نگه دارند؛ رقابت دو دولت ادامه یافت.</p><p><strong>برای بررسی:</strong> تاریخ این رویداد را باید در پیوند با شرایط سیاسی، اقتصادی و جغرافیایی زمان خود مطالعه کرد. در مواردی که منابع اختلاف دارند، تاریخ تقریبی یا روایت‌های متفاوت باید جداگانه سنجیده شوند.</p></details>
<details class="event"><summary>25. جنگ‌های صفوی و عثمانی و پیمان زهاب (سده شانزدهم تا ۱۶۳۹ م.)</summary><p>دو دولت بر سر عراق، قفقاز و آذربایجان بارها جنگیدند. شاه عباس اول بخش‌هایی از مناطق ازدست‌رفته را بازپس گرفت. پیمان زهاب در ۱۶۳۹ به تثبیت نسبی مرزها کمک کرد و از مهم‌ترین توافق‌های مرزی منطقه شد.</p><p><strong>برای بررسی:</strong> تاریخ این رویداد را باید در پیوند با شرایط سیاسی، اقتصادی و جغرافیایی زمان خود مطالعه کرد. در مواردی که منابع اختلاف دارند، تاریخ تقریبی یا روایت‌های متفاوت باید جداگانه سنجیده شوند.</p></details>
<details class="event"><summary>26. بازپس‌گیری هرمز از پرتغالی‌ها (۱۶۲۲ م.)</summary><p>نیروهای صفوی با همکاری ناوگان انگلیسی پرتغالی‌ها را از هرمز بیرون راندند. این رخداد حضور پرتغال در خلیج فارس را محدود کرد و جایگاه صفویان را در تجارت و امنیت دریایی منطقه تقویت کرد.</p><p><strong>برای بررسی:</strong> تاریخ این رویداد را باید در پیوند با شرایط سیاسی، اقتصادی و جغرافیایی زمان خود مطالعه کرد. در مواردی که منابع اختلاف دارند، تاریخ تقریبی یا روایت‌های متفاوت باید جداگانه سنجیده شوند.</p></details>
<details class="event"><summary>27. محاصره و سقوط اصفهان به دست افغان‌های هوتکی (۱۷۲۲ م.)</summary><p>در پی ضعف حکومت صفوی و بحران‌های داخلی، نیروهای محمود هوتکی اصفهان را محاصره کردند. پس از محاصره طولانی، شهر سقوط کرد و شاه سلطان حسین تسلیم شد. این رخداد آغاز دوره‌ای از آشفتگی و مداخله قدرت‌های خارجی بود.</p><p><strong>برای بررسی:</strong> تاریخ این رویداد را باید در پیوند با شرایط سیاسی، اقتصادی و جغرافیایی زمان خود مطالعه کرد. در مواردی که منابع اختلاف دارند، تاریخ تقریبی یا روایت‌های متفاوت باید جداگانه سنجیده شوند.</p></details>
<details class="event"><summary>28. جنگ‌های نادرشاه با افغان‌ها و عثمانیان (دهه ۱۷۲۰ تا ۱۷۴۰ م.)</summary><p>نادر ابتدا نیروهای افغان را شکست داد و سپس بخش‌هایی از سرزمین ایران را بازپس گرفت. جنگ با عثمانیان و روس‌ها نیز برای بازگرداندن مناطق مرزی ادامه یافت. فتوحات او قدرت مرکزی را موقتاً احیا کرد، اما هزینه لشکرکشی‌ها سنگین بود.</p><p><strong>برای بررسی:</strong> تاریخ این رویداد را باید در پیوند با شرایط سیاسی، اقتصادی و جغرافیایی زمان خود مطالعه کرد. در مواردی که منابع اختلاف دارند، تاریخ تقریبی یا روایت‌های متفاوت باید جداگانه سنجیده شوند.</p></details>
<details class="event"><summary>29. نبرد کرنال و لشکرکشی نادرشاه به هند (۱۷۳۹ م.)</summary><p>نادرشاه در کرنال سپاه گورکانی هند را شکست داد و وارد دهلی شد. این پیروزی قدرت نظامی او را نشان داد، اما غنایم و دستاوردهای کوتاه‌مدت نتوانستند مشکلات مالی و سیاسی ایران را برای همیشه حل کنند.</p><p><strong>برای بررسی:</strong> تاریخ این رویداد را باید در پیوند با شرایط سیاسی، اقتصادی و جغرافیایی زمان خود مطالعه کرد. در مواردی که منابع اختلاف دارند، تاریخ تقریبی یا روایت‌های متفاوت باید جداگانه سنجیده شوند.</p></details>
<details class="event"><summary>30. جنگ‌های داخلی پس از نادر؛ زندیه و قاجاریه (۱۷۴۷ تا اواخر سده هجدهم م.)</summary><p>پس از قتل نادرشاه، مدعیان قدرت در مناطق مختلف جنگیدند. کریم‌خان زند بخش بزرگی از ایران را متحد کرد؛ پس از مرگ او رقابت زندیان و قاجاریان شدت گرفت و آقامحمدخان قاجار حکومت تازه‌ای بنیان گذاشت.</p><p><strong>برای بررسی:</strong> تاریخ این رویداد را باید در پیوند با شرایط سیاسی، اقتصادی و جغرافیایی زمان خود مطالعه کرد. در مواردی که منابع اختلاف دارند، تاریخ تقریبی یا روایت‌های متفاوت باید جداگانه سنجیده شوند.</p></details>
<details class="event"><summary>31. نخستین جنگ ایران و روسیه (۱۸۰۴ تا ۱۸۱۳ م.)</summary><p>روسیه تزاری برای گسترش نفوذ در قفقاز با ایران جنگید. جنگ با عهدنامه گلستان پایان یافت و ایران بخش‌هایی از قفقاز را واگذار کرد. ضعف تدارکات و سازمان نظامی ایران در برابر ارتش روسیه آشکار شد.</p><p><strong>برای بررسی:</strong> تاریخ این رویداد را باید در پیوند با شرایط سیاسی، اقتصادی و جغرافیایی زمان خود مطالعه کرد. در مواردی که منابع اختلاف دارند، تاریخ تقریبی یا روایت‌های متفاوت باید جداگانه سنجیده شوند.</p></details>
<details class="event"><summary>32. دومین جنگ ایران و روسیه (۱۸۲۶ تا ۱۸۲۸ م.)</summary><p>با ازسرگیری جنگ، ایران در آغاز پیشروی‌هایی داشت اما ضدحمله روسیه نتیجه را تغییر داد. عهدنامه ترکمانچای بخش‌های دیگری از قفقاز را به روسیه واگذار کرد و غرامت و امتیازهای سنگینی بر ایران تحمیل شد.</p><p><strong>برای بررسی:</strong> تاریخ این رویداد را باید در پیوند با شرایط سیاسی، اقتصادی و جغرافیایی زمان خود مطالعه کرد. در مواردی که منابع اختلاف دارند، تاریخ تقریبی یا روایت‌های متفاوت باید جداگانه سنجیده شوند.</p></details>
<details class="event"><summary>33. جنگ ایران و بریتانیا بر سر هرات (۱۸۵۶ تا ۱۸۵۷ م.)</summary><p>ایران برای بازپس‌گیری هرات اقدام کرد و بریتانیا به جنوب ایران حمله کرد. عهدنامه پاریس در ۱۸۵۷ جنگ را پایان داد و ایران از ادعای خود بر هرات صرف‌نظر کرد. این رخداد نفوذ بریتانیا در خلیج فارس را افزایش داد.</p><p><strong>برای بررسی:</strong> تاریخ این رویداد را باید در پیوند با شرایط سیاسی، اقتصادی و جغرافیایی زمان خود مطالعه کرد. در مواردی که منابع اختلاف دارند، تاریخ تقریبی یا روایت‌های متفاوت باید جداگانه سنجیده شوند.</p></details>
<details class="event"><summary>34. انقلاب مشروطه و درگیری‌های نظامی داخلی (۱۹۰۵ تا ۱۹۱۱ م.)</summary><p>جنبش مشروطه به درگیری میان نیروهای مشروطه‌خواه و طرفداران استبداد انجامید. به توپ بستن مجلس در ۱۹۰۸ و مقاومت تبریز و فتح تهران در ۱۹۰۹ از رخدادهای مهم بود. این منازعه ساختار سیاسی ایران را دگرگون کرد و به استقرار محدود قانون‌گرایی انجامید.</p><p><strong>برای بررسی:</strong> تاریخ این رویداد را باید در پیوند با شرایط سیاسی، اقتصادی و جغرافیایی زمان خود مطالعه کرد. در مواردی که منابع اختلاف دارند، تاریخ تقریبی یا روایت‌های متفاوت باید جداگانه سنجیده شوند.</p></details>
<details class="event"><summary>35. ایران در جنگ جهانی اول (۱۹۱۴ تا ۱۹۱۸ م.)</summary><p>ایران بی‌طرفی اعلام کرد، اما نیروهای روسیه، بریتانیا و عثمانی وارد بخش‌هایی از کشور شدند. در آذربایجان، غرب و جنوب درگیری رخ داد و ناامنی، قحطی و بیماری به مردم آسیب زد. بی‌طرفی ایران عملاً رعایت نشد.</p><p><strong>برای بررسی:</strong> تاریخ این رویداد را باید در پیوند با شرایط سیاسی، اقتصادی و جغرافیایی زمان خود مطالعه کرد. در مواردی که منابع اختلاف دارند، تاریخ تقریبی یا روایت‌های متفاوت باید جداگانه سنجیده شوند.</p></details>
<details class="event"><summary>36. اشغال ایران در جنگ جهانی دوم (۱۹۴۱ م.)</summary><p>با وجود اعلام بی‌طرفی، نیروهای بریتانیا و شوروی در اوت ۱۹۴۱ وارد ایران شدند. موقعیت راهبردی، راه‌آهن و مسیر تدارکاتی به شوروی از عوامل مهم بود. رضاشاه کناره‌گیری کرد و اشغال آثار سیاسی و اقتصادی گسترده‌ای بر کشور گذاشت.</p><p><strong>برای بررسی:</strong> تاریخ این رویداد را باید در پیوند با شرایط سیاسی، اقتصادی و جغرافیایی زمان خود مطالعه کرد. در مواردی که منابع اختلاف دارند، تاریخ تقریبی یا روایت‌های متفاوت باید جداگانه سنجیده شوند.</p></details>
<details class="event"><summary>37. درگیری‌های آذربایجان و کردستان پس از جنگ جهانی دوم (۱۹۴۵ تا ۱۹۴۶ م.)</summary><p>پس از خروج نیروهای خارجی و در شرایط بحران سیاسی، حکومت‌های خودمختار در آذربایجان و مهاباد شکل گرفتند. ارتش ایران در ۱۹۴۶ به منطقه بازگشت و این حکومت‌ها فروپاشیدند. نقش شوروی و فشارهای بین‌المللی از موضوعات مهم پژوهش درباره این بحران است.</p><p><strong>برای بررسی:</strong> تاریخ این رویداد را باید در پیوند با شرایط سیاسی، اقتصادی و جغرافیایی زمان خود مطالعه کرد. در مواردی که منابع اختلاف دارند، تاریخ تقریبی یا روایت‌های متفاوت باید جداگانه سنجیده شوند.</p></details>
<details class="event"><summary>38. جنگ تحمیلی عراق علیه ایران (۱۳۵۹ تا ۱۳۶۷ / ۱۹۸۰ تا ۱۹۸۸ م.)</summary><p>عراق در ۳۱ شهریور ۱۳۵۹ حمله گسترده‌ای را آغاز کرد. اختلافات مرزی، رقابت منطقه‌ای و محاسبات حکومت صدام از زمینه‌های جنگ بود. خرمشهر در آغاز جنگ سقوط کرد و در ۱۳۶۱ آزاد شد. جنگ نزدیک به هشت سال ادامه یافت و با پذیرش قطعنامه ۵۹۸ و آتش‌بس پایان گرفت؛ خسارت انسانی و اقتصادی آن بسیار گسترده بود.</p><p><strong>برای بررسی:</strong> تاریخ این رویداد را باید در پیوند با شرایط سیاسی، اقتصادی و جغرافیایی زمان خود مطالعه کرد. در مواردی که منابع اختلاف دارند، تاریخ تقریبی یا روایت‌های متفاوت باید جداگانه سنجیده شوند.</p></details>
<details class="event"><summary>39. درگیری‌های دریایی ایران و آمریکا در خلیج فارس (۱۹۸۷ تا ۱۹۸۸ م.)</summary><p>در سال‌های پایانی جنگ ایران و عراق، تنش دریایی و حمله به کشتی‌ها افزایش یافت. آمریکا عملیات اسکورت نفتکش‌ها را اجرا کرد و در آوریل ۱۹۸۸ عملیات آخوندک را انجام داد. این رخدادها بخشی از فضای جنگ و تنش منطقه‌ای بودند و معمولاً جنگ مستقل رسمی نامیده نمی‌شوند.</p><p><strong>برای بررسی:</strong> تاریخ این رویداد را باید در پیوند با شرایط سیاسی، اقتصادی و جغرافیایی زمان خود مطالعه کرد. در مواردی که منابع اختلاف دارند، تاریخ تقریبی یا روایت‌های متفاوت باید جداگانه سنجیده شوند.</p></details>
<details class="event"><summary>40. درگیری‌های مرزی ایران و طالبان (۱۹۹۸ م.)</summary><p>پس از کشته‌شدن دیپلمات‌های ایرانی در مزارشریف و افزایش تنش با حکومت نخست طالبان، نیروهای ایران در مرز شرقی در حالت آماده‌باش گسترده قرار گرفتند. بحران با فشارهای دیپلماتیک مهار شد و به جنگ تمام‌عیار تبدیل نشد.</p><p><strong>برای بررسی:</strong> تاریخ این رویداد را باید در پیوند با شرایط سیاسی، اقتصادی و جغرافیایی زمان خود مطالعه کرد. در مواردی که منابع اختلاف دارند، تاریخ تقریبی یا روایت‌های متفاوت باید جداگانه سنجیده شوند.</p></details>
<details class="event"><summary>41. درگیری‌های مرزی و امنیتی پس از جنگ ایران و عراق (دهه ۱۳۷۰ تا امروز)</summary><p>در دوره معاصر رخدادهای مرزی، مقابله با گروه‌های مسلح و تنش‌های محدود منطقه‌ای در نقاط مختلف گزارش شده‌اند. هر مورد باید با تاریخ، مکان و منبع مستقل بررسی شود؛ نباید همه این رخدادها را یک جنگ واحد دانست.</p><p><strong>برای بررسی:</strong> تاریخ این رویداد را باید در پیوند با شرایط سیاسی، اقتصادی و جغرافیایی زمان خود مطالعه کرد. در مواردی که منابع اختلاف دارند، تاریخ تقریبی یا روایت‌های متفاوت باید جداگانه سنجیده شوند.</p></details></div></section>
<section id="analysis" class="section"><div class="section-title"><h2>تحلیل و بررسی</h2><p>جنگ‌ها را باید با توجه به شرایط زمان خود و با مقایسه منابع بررسی کرد.</p></div><div class="grid"><div class="card"><h3>اتحاد و سازماندهی</h3><p>هماهنگی سیاسی، اجتماعی و نظامی می‌تواند بر توان کشورها اثر بگذارد.</p></div><div class="card"><h3>جغرافیا و تدارکات</h3><p>راه‌ها، آب‌وهوا، منابع و فاصله از مراکز پشتیبانی در نتیجه جنگ‌ها مؤثرند.</p></div><div class="card"><h3>دیپلماسی</h3><p>پیمان‌ها و مذاکره می‌توانند از ادامه درگیری و خسارت انسانی جلوگیری کنند.</p></div></div></section>
<section id="lessons" class="section"><div class="section-title"><h2>درس‌آموخته‌های تاریخی</h2></div><div class="grid"><div class="card"><h3>🤝 همکاری</h3><p>همدلی و همکاری جامعه در بحران‌ها اهمیت دارد.</p></div><div class="card"><h3>📚 آگاهی</h3><p>شناخت منابع معتبر مانع گسترش شایعات می‌شود.</p></div><div class="card"><h3>🕊️ صلح</h3><p>گفت‌وگو و دیپلماسی راه‌هایی برای کاهش هزینه‌های انسانی جنگ هستند.</p></div><div class="card"><h3>🧠 تفکر انتقادی</h3><p>روایت‌های تاریخی باید با شواهد و منابع مختلف سنجیده شوند.</p></div></div></section>
<section id="quiz" class="section"><div class="section-title"><h2>آزمون آمادگی دفاعی</h2><p>به پرسش‌ها پاسخ دهید.</p></div><div class="card"><form id="quizForm"><div id="questions"></div><button class="btn" type="button" onclick="checkQuiz()">ثبت پاسخ‌ها</button><button class="btn" type="reset" onclick="resetQuiz()">شروع دوباره</button></form><div id="result" class="result"></div></div></section>
<section id="about" class="section"><div class="section-title"><h2>درباره این پروژه</h2></div><div class="card"><h3>هدف</h3><p>این وب‌سایت یک پروژه آموزشی برای آشنایی با تاریخ دفاعی ایران، بررسی رویدادها و تقویت سواد تاریخی است.</p><h3>طراح و سازنده</h3><p><strong>محمد مهدی عباسی</strong></p><h3>منابع و مراجع</h3><p>منابع زیر برای مطالعه و راستی‌آزمایی بیشتر پیشنهاد می‌شوند؛ درج آن‌ها به‌تنهایی به معنای استفاده مستقیم از تک‌تک منابع در نگارش همه مدخل‌ها نیست.</p><ul><li><a href="https://www.iranicaonline.org/" target="_blank" rel="noopener">دانشنامه ایرانیکا</a> – پژوهش‌های تخصصی تاریخ و فرهنگ ایران.</li>
<li><a href="https://www.iranicaonline.org/articles/iran-ii3-chronological-table/" target="_blank" rel="noopener">جدول زمانی تاریخ ایران، ایرانیکا</a> – برای تطبیق دوره‌ها و تاریخ‌ها.</li>
<li><a href="https://www.iranicaonline.org/articles/iran-ii1-pre-islamic-times/" target="_blank" rel="noopener">تاریخ ایران پیش از اسلام، ایرانیکا</a>.</li>
<li><a href="https://www.iranicaonline.org/articles/arab-ii/" target="_blank" rel="noopener">فتح ایران به دست سپاهیان عرب، ایرانیکا</a>.</li>
<li><a href="https://www.biblioiranica.info/the-comprehensive-history-of-iran/" target="_blank" rel="noopener">تاریخ جامع ایران</a> – معرفی مجموعه بیست‌جلدی مرکز دائرةالمعارف بزرگ اسلامی.</li>
<li><a href="https://www.cambridge.org/core/books/cambridge-history-of-iran/" target="_blank" rel="noopener">تاریخ ایران کمبریج</a> – مجموعه پژوهش‌های دانشگاهی درباره دوره‌های مختلف ایران.</li>
<li><a href="https://digitallibrary.un.org/record/137345" target="_blank" rel="noopener">قطعنامه ۵۹۸ شورای امنیت سازمان ملل</a> – سند مرتبط با پایان جنگ ایران و عراق.</li></ul></div></section></main>
<section class="sources container"><h2>📚 منابع و مراجع</h2><p>برای بررسی و مطالعه بیشتر از منابع پژوهشی زیر استفاده کنید:</p><ul><li><a href="https://www.iranicaonline.org/" target="_blank" rel="noopener">دانشنامه ایرانیکا</a> – پژوهش‌های تخصصی تاریخ و فرهنگ ایران.</li>
<li><a href="https://www.iranicaonline.org/articles/iran-ii3-chronological-table/" target="_blank" rel="noopener">جدول زمانی تاریخ ایران، ایرانیکا</a> – برای تطبیق دوره‌ها و تاریخ‌ها.</li>
<li><a href="https://www.iranicaonline.org/articles/iran-ii1-pre-islamic-times/" target="_blank" rel="noopener">تاریخ ایران پیش از اسلام، ایرانیکا</a>.</li>
<li><a href="https://www.iranicaonline.org/articles/arab-ii/" target="_blank" rel="noopener">فتح ایران به دست سپاهیان عرب، ایرانیکا</a>.</li>
<li><a href="https://www.biblioiranica.info/the-comprehensive-history-of-iran/" target="_blank" rel="noopener">تاریخ جامع ایران</a> – معرفی مجموعه بیست‌جلدی مرکز دائرةالمعارف بزرگ اسلامی.</li>
<li><a href="https://www.cambridge.org/core/books/cambridge-history-of-iran/" target="_blank" rel="noopener">تاریخ ایران کمبریج</a> – مجموعه پژوهش‌های دانشگاهی درباره دوره‌های مختلف ایران.</li>
<li><a href="https://digitallibrary.un.org/record/137345" target="_blank" rel="noopener">قطعنامه ۵۹۸ شورای امنیت سازمان ملل</a> – سند مرتبط با پایان جنگ ایران و عراق.</li></ul></section><footer>وب‌سایت آموزشی آمادگی دفاعی<br>طراح سایت: <strong>محمد مهدی عباسی</strong><br><span class="small">با هدف آموزش، آگاهی و شناخت تاریخ</span></footer>
<script>
function showPage(id,btn){document.querySelectorAll('.section').forEach(s=>s.classList.remove('active'));document.getElementById(id).classList.add('active');document.querySelectorAll('nav button').forEach(b=>b.classList.remove('active'));if(btn)btn.classList.add('active');window.scrollTo({top:0,behavior:'smooth'})}
function searchEvents(){let v=document.getElementById('search').value.trim().toLowerCase();document.querySelectorAll('#eventList .event').forEach(e=>e.style.display=e.innerText.toLowerCase().includes(v)?'':'none')}
const quizData=[['جنگ ایران و عراق در چه سالی آغاز شد؟',['۱۳۵۷','۱۳۵۹','۱۳۶۱','۱۳۶۷'],1],['نبرد چالدران میان چه حکومت‌هایی بود؟',['صفوی و عثمانی','ماد و آشور','قاجار و روسیه','ساسانی و روم'],0],['عهدنامه گلستان پس از کدام جنگ امضا شد؟',['جنگ ایران و روسیه','جنگ جهانی اول','جنگ ایران و عراق','جنگ با عثمانی'],0],['کدام نبرد به شکست کراسوس انجامید؟',['حَرّان','ماراتون','گوگمل','چالدران'],0],['سقوط نینوا در چه سالی بود؟',['۶۱۲ پ.م.','۳۳۰ پ.م.','۵۳ پ.م.','۶۴۲ م.'],0],['حمله مغول به قلمرو خوارزمشاهیان از چه سالی آغاز شد؟',['۱۰۴۰','۱۲۱۹','۱۵۱۴','۱۷۲۲'],1],['نبرد مرو صفویان با کدام نیرو بود؟',['ازبکان','رومیان','یونانیان','پرتغالی‌ها'],0],['جنگ جهانی دوم در چه سالی پایان یافت؟',['۱۹۱۸','۱۹۳۹','۱۹۴۵','۱۹۵۰'],2],['قطعنامه مرتبط با آتش‌بس جنگ ایران و عراق کدام است؟',['۵۹۸','۲۴۲','۱۸۱','۱۹۲'],0],['کدام روش به کاهش خطر جنگ کمک می‌کند؟',['دیپلماسی','شایعه‌پراکنی','قطع گفت‌وگو','بی‌توجهی'],0]];
function renderQuiz(){let h=document.getElementById('questions');quizData.forEach((q,i)=>{let d=document.createElement('div');d.className='question';d.innerHTML='<h3>'+(i+1)+'. '+q[0]+'</h3>'+q[1].map((a,j)=>'<label class="option"><input type="radio" name="q'+i+'" value="'+j+'"> '+a+'</label>').join('');h.appendChild(d)})}
function checkQuiz(){let score=0,answered=0;quizData.forEach((q,i)=>{let x=document.querySelector('input[name="q'+i+'"]:checked');if(x){answered++;if(+x.value===q[2])score++}});let r=document.getElementById('result');r.style.display='block';r.innerHTML='پاسخ داده‌شده: '+answered+' از ۱۰<br>پاسخ درست: '+score+' از ۱۰<br><strong>نمره: '+(score*2)+' از ۲۰</strong>'+(answered<10?'<br>برای نتیجه کامل به همه پرسش‌ها پاسخ بده.':'')}
function resetQuiz(){setTimeout(()=>document.getElementById('result').style.display='none',0)}renderQuiz();

// افکت ظاهرشدن کارت‌ها هنگام ورود به صفحه
function setupReveal(){
  const targets=document.querySelectorAll('.card,.event,.sources,.section-title');
  targets.forEach(el=>el.classList.add('reveal'));
  if(!('IntersectionObserver' in window)){targets.forEach(el=>el.classList.add('visible'));return}
  const observer=new IntersectionObserver(entries=>{
    entries.forEach(entry=>{
      if(entry.isIntersecting){entry.target.classList.add('visible');observer.unobserve(entry.target)}
    });
  },{threshold:.08});
  targets.forEach(el=>observer.observe(el));
}
const originalShowPage=showPage;
showPage=function(id,btn){
  originalShowPage(id,btn);
  setTimeout(setupReveal,60);
};
setupReveal();

// ذرات نورانی شناور در پس‌زمینه
(function(){
  const canvas=document.getElementById('particleCanvas');
  if(!canvas)return;
  const ctx=canvas.getContext('2d');
  if(!ctx)return;
  let w=0,h=0,particles=[];
  const reduce=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  function resize(){
    const dpr=Math.min(window.devicePixelRatio||1,2);
    w=window.innerWidth;h=window.innerHeight;
    canvas.width=Math.floor(w*dpr);canvas.height=Math.floor(h*dpr);
    ctx.setTransform(dpr,0,0,dpr,0,0);
    const count=Math.min(55,Math.max(18,Math.floor(w/25)));
    particles=Array.from({length:count},()=>({
      x:Math.random()*w,y:Math.random()*h,
      r:Math.random()*2+0.6,
      vx:(Math.random()-.5)*.28,vy:(Math.random()-.5)*.28-.08,
      a:Math.random()*.45+.12
    }));
  }
  function draw(){
    ctx.clearRect(0,0,w,h);
    const dark=document.body.classList.contains('dark');
    for(const p of particles){
      p.x+=p.vx;p.y+=p.vy;
      if(p.x<-5)p.x=w+5;if(p.x>w+5)p.x=-5;
      if(p.y<-5)p.y=h+5;if(p.y>h+5)p.y=-5;
      ctx.beginPath();ctx.arc(p.x,p.y,p.r,0,Math.PI*2);
      ctx.fillStyle=dark?`rgba(217,173,88,${p.a})`:`rgba(45,75,120,${p.a*.55})`;
      ctx.fill();
    }
    if(!reduce)requestAnimationFrame(draw);
  }
  resize();window.addEventListener('resize',resize,{passive:true});
  draw();
})();



// نوار پیشرفت مطالعه و دکمه بازگشت به بالای صفحه
(function(){
  const bar=document.createElement('div');bar.id='scrollProgress';document.body.appendChild(bar);
  const top=document.createElement('button');top.id='backToTop';top.type='button';top.title='بازگشت به بالا';top.setAttribute('aria-label','بازگشت به بالای صفحه');top.textContent='↑';document.body.appendChild(top);
  function update(){const max=document.documentElement.scrollHeight-innerHeight;bar.style.width=(max>0?(scrollY/max)*100:0)+'%';top.classList.toggle('show',scrollY>420)}
  addEventListener('scroll',update,{passive:true});addEventListener('resize',update,{passive:true});top.addEventListener('click',()=>scrollTo({top:0,behavior:'smooth'}));update();
})();

// ورود پلکانی کارت‌ها و عناصر فهرست برای جلوه پویاتر
(function(){
  if(!('IntersectionObserver' in window))return;
  const io=new IntersectionObserver(entries=>entries.forEach(e=>{
    if(e.isIntersecting){e.target.style.transitionDelay=Math.min((Array.from(e.target.parentElement.children).indexOf(e.target)%5)*70,280)+'ms';e.target.classList.add('visible');io.unobserve(e.target)}
  }),{threshold:.06});
  document.querySelectorAll('.grid .card,.event').forEach(el=>io.observe(el));
})();

// جلوه موجی کوچک هنگام کلیک روی دکمه‌ها
(function(){
  document.addEventListener('click',e=>{
    const b=e.target.closest('button');if(!b||b.classList.contains('theme')||b.id==='backToTop')return;
    const r=b.getBoundingClientRect(),wave=document.createElement('span');
    wave.style.cssText='position:absolute;pointer-events:none;border-radius:50%;width:12px;height:12px;background:#fff8;left:'+(e.clientX-r.left-6)+'px;top:'+(e.clientY-r.top-6)+'px;transform:scale(0);animation:clickWave .55s ease-out forwards';
    if(getComputedStyle(b).position==='static')b.style.position='relative';b.style.overflow='hidden';b.appendChild(wave);setTimeout(()=>wave.remove(),600);
  });
  const st=document.createElement('style');st.textContent='@keyframes clickWave{to{transform:scale(18);opacity:0}}';document.head.appendChild(st);
})();


// شمشیر طلایی کوچک که با حرکت موس، نرم دنبال نشانگر می‌آید
(function(){
  const finePointer=window.matchMedia&&window.matchMedia('(hover: hover) and (pointer: fine)').matches;
  const reduced=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if(!finePointer||reduced)return;
  const sword=document.createElement('div');
  sword.id='swordFollower';
  sword.setAttribute('aria-hidden','true');
  sword.innerHTML='<svg viewBox="0 0 64 64" width="58" height="58" xmlns="http://www.w3.org/2000/svg"><defs><linearGradient id="bladeGold" x1="0" y1="1" x2="1" y2="0"><stop stop-color="#9b6a22"/><stop offset=".45" stop-color="#fff1b5"/><stop offset="1" stop-color="#c28b32"/></linearGradient><linearGradient id="gripGold"><stop stop-color="#55351c"/><stop offset=".5" stop-color="#d9ad58"/><stop offset="1" stop-color="#6d421c"/></linearGradient></defs><path d="M31 7 L40 16 L22 43 L17 38 Z" fill="url(#bladeGold)" stroke="#fff0b0" stroke-width="1.2"/><path d="M31 7 L35 11 L20 39 L17 38 Z" fill="#fff8d8" opacity=".65"/><path d="M17 36 L27 46 L22 51 L12 41 Z" fill="url(#gripGold)" stroke="#f5d58b" stroke-width="1.2"/><path d="M10 43 L20 53" stroke="#f5d58b" stroke-width="4" stroke-linecap="round"/><path d="M8 51 L14 57" stroke="#9b6a22" stroke-width="5" stroke-linecap="round"/><circle cx="17" cy="42" r="2" fill="#fff2bd"/></svg>';
  document.body.appendChild(sword);
  let targetX=-100,targetY=-100,x=-100,y=-100,raf=0;
  function frame(){
    x+=(targetX-x)*.24;y+=(targetY-y)*.24;
    sword.style.transform='translate3d('+(x-29)+'px,'+(y-29)+'px,0) rotate(-35deg)';
    if(Math.abs(targetX-x)>.2||Math.abs(targetY-y)>.2){raf=requestAnimationFrame(frame)}else{raf=0}
  }
  window.addEventListener('pointermove',function(e){
    if(e.pointerType!=='mouse')return;
    targetX=e.clientX+18;targetY=e.clientY+18;
    sword.classList.add('visible');
    if(!raf)raf=requestAnimationFrame(frame);
  },{passive:true});
  document.addEventListener('pointerleave',function(){sword.classList.remove('visible')});
  window.addEventListener('blur',function(){sword.classList.remove('visible')});
})();

</script></body></html>
'''

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate")
        self.end_headers()
        self.wfile.write(PAGE.encode("utf-8"))

    def log_message(self, format, *args):
        pass

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8002))
    server = HTTPServer(("0.0.0.0", port), Handler)
    print("سایت آمادگی دفاعی فعال شد!")
    print(f"Port: {port}")
    server.serve_forever()
