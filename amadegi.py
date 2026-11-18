
from http.server import HTTPServer, BaseHTTPRequestHandler
import os

PAGE = r'''<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#101d36">
<meta name="description" content="وب‌سایت آموزشی آمادگی دفاعی، تاریخ و امنیت ایران">
<title>آمادگی دفاعی | محمد مهدی عباسی</title>

<style>
@import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;500;600;700;800&display=swap');

:root{
--bg:#f3f5fa;
--card:#fff;
--text:#17233c;
--muted:#66738a;
--navy:#101d36;
--gold:#d9ad58;
--border:#e5e9f0;
}
body.dark{
--bg:#101827;
--card:#1a263a;
--text:#f1f4fa;
--muted:#b2bfd2;
--border:#2b3a51;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{
margin:0;
font-family:'Vazirmatn',Tahoma,sans-serif;
background:var(--bg);
color:var(--text);
transition:.25s;
}
header{
background:linear-gradient(120deg,#0b1529,#1b3155);
color:white;
padding:16px 5%;
position:sticky;
top:0;
z-index:10;
box-shadow:0 5px 20px #0002;
}
.nav{
display:flex;
align-items:center;
justify-content:space-between;
gap:12px;
flex-wrap:wrap;
}
.logo{font-size:20px;font-weight:800;color:#f0ca7d}
nav{display:flex;flex-wrap:wrap;gap:5px}
nav button{
background:transparent;
color:white;
border:0;
padding:9px 11px;
border-radius:9px;
cursor:pointer;
font-family:inherit;
font-size:13px;
}
nav button:hover,nav button.active{
background:#ffffff20;
color:#f0ca7d;
}
.theme{
border:1px solid #ffffff55;
background:transparent;
color:white;
border-radius:9px;
padding:9px 12px;
cursor:pointer;
font-family:inherit;
}
.hero{
padding:75px 7%;
background:
radial-gradient(circle at 15% 20%,#d9ad5830,transparent 25%),
linear-gradient(120deg,#101d36,#243e68);
color:white;
text-align:center;
}
.hero h1{font-size:clamp(27px,5vw,46px);margin:0 0 15px}
.hero p{
color:#d8e0ee;
max-width:700px;
margin:auto;
line-height:2.2;
}
.creator{
display:inline-block;
margin-top:20px;
padding:9px 20px;
border:1px solid #d9ad58a0;
border-radius:30px;
color:#f3d18e;
background:#d9ad5815;
font-size:14px;
}
.hero-actions{margin-top:25px}
.btn{
display:inline-block;
border:0;
border-radius:10px;
padding:12px 22px;
background:var(--gold);
color:#17233c;
font-family:inherit;
font-weight:700;
cursor:pointer;
margin:5px;
}
.btn.secondary{
background:transparent;
color:white;
border:1px solid #ffffff70;
}
.container{width:min(1100px,92%);margin:40px auto}
.section{display:none}
.section.active{display:block;animation:fade .3s ease}
@keyframes fade{
from{opacity:0;transform:translateY(8px)}
to{opacity:1;transform:none}
}
.section-title{margin-bottom:25px}
.section-title h2{font-size:26px;margin-bottom:5px}
.section-title p{color:var(--muted)}
.grid{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(min(100%,230px),1fr));
gap:18px;
}
.card{
background:var(--card);
border:1px solid var(--border);
padding:22px;
border-radius:17px;
box-shadow:0 5px 20px #17233c09;
}
.card h3{margin-top:0}
.card p{color:var(--muted);line-height:2}
.icon{font-size:30px;margin-bottom:10px}
.tag{
display:inline-block;
padding:4px 10px;
border-radius:20px;
background:#d9ad5825;
color:#a77925;
font-size:12px;
}
.search{
width:100%;
padding:13px;
border:1px solid var(--border);
border-radius:10px;
background:var(--card);
color:var(--text);
font:inherit;
margin-bottom:20px;
}
.event{
background:var(--card);
border:1px solid var(--border);
border-radius:14px;
padding:18px;
margin-bottom:13px;
}
.event summary{cursor:pointer;font-weight:700}
.event p{color:var(--muted);line-height:2}
.question{margin-bottom:20px}
.option{
display:block;
padding:10px 13px;
margin:8px 0;
background:var(--bg);
border:1px solid var(--border);
border-radius:9px;
cursor:pointer;
}
.option:hover{border-color:var(--gold)}
.option input{margin-left:8px}
.result{
padding:15px;
margin-top:20px;
border-radius:12px;
background:#d9ad5820;
line-height:2;
display:none;
}
footer{
background:#101d36;
color:#d8e0ee;
text-align:center;
padding:30px 15px;
margin-top:60px;
line-height:2;
}
footer strong{color:#f0ca7d}

.sources{
  background:var(--card);
  border:1px solid var(--border);
  border-radius:17px;
  padding:24px;
  margin:35px auto 0;
  box-shadow:0 5px 20px #17233c09;
}
.sources h2{margin-top:0;color:var(--text)}
.sources p{color:var(--muted);line-height:2}
.sources ul{padding-right:22px;margin-bottom:0}
.sources li{margin:12px 0;line-height:2;color:var(--text)}
.sources a{color:#b18432;text-decoration:none;font-weight:600}
.sources a:hover{text-decoration:underline}
body.dark .sources a{color:#f0ca7d}
.small{font-size:13px;color:var(--muted)}
@media(max-width:700px){
header{padding:13px 4%}
.nav{justify-content:center}
.logo{width:100%;text-align:center}
nav{justify-content:center}
nav button{font-size:12px;padding:8px}
.hero{padding:55px 5%}
.container{width:94%}
}
</style>
</head>

<body>

<header>
<div class="nav">
<div class="logo">🛡️ آمادگی دفاعی</div>
<nav>
<button class="active" onclick="showPage('home',this)">خانه</button>
<button onclick="showPage('events',this)">جنگ‌ها و نبردها</button>
<button onclick="showPage('analysis',this)">تحلیل</button>
<button onclick="showPage('lessons',this)">درس‌آموخته‌ها</button>
<button onclick="showPage('quiz',this)">آزمون</button>
<button onclick="showPage('about',this)">درباره ما</button>
</nav>
<button class="theme" onclick="toggleTheme()">🌙 تغییر پوسته</button>
</div>
</header>

<section class="hero">
<h1>آمادگی دفاعی؛ آگاهی، امنیت، آینده</h1>
<p>
آشنایی با تاریخ دفاعی ایران، جنگ‌ها و نبردهای تاریخی،
اهمیت امنیت ملی و نقش آگاهی مردم در حفظ استقلال و آرامش کشور.
</p>
<div class="creator">✦ طراح سایت: محمد مهدی عباسی ✦</div>
<div class="hero-actions">
<button class="btn" onclick="showPage('events')">مشاهده رویدادهای تاریخی</button>
<button class="btn secondary" onclick="showPage('quiz')">شرکت در آزمون</button>
</div>
</section>

<main class="container">

<section id="home" class="section active">
<div class="section-title">
<h2>به وب‌سایت آمادگی دفاعی خوش آمدید</h2>
<p>دانش تاریخی و آگاهی، پایه‌های امنیت و پیشرفت هستند.</p>
</div>
<div class="grid">
<div class="card">
<div class="icon">📜</div>
<h3>تاریخ دفاعی ایران</h3>
<p>با مجموعه‌ای گسترده از جنگ‌ها، یورش‌ها و نبردهای مهم ایران از دوران باستان تا معاصر آشنا شوید.</p>
<button class="btn" onclick="showPage('events')">مطالعه</button>
</div>
<div class="card">
<div class="icon">🔎</div>
<h3>تحلیل تاریخی</h3>
<p>علت‌ها و پیامدهای برخی رویدادهای مهم تاریخ ایران را بررسی کنید.</p>
<button class="btn" onclick="showPage('analysis')">مشاهده</button>
</div>
<div class="card">
<div class="icon">🎓</div>
<h3>آزمون آموزشی</h3>
<p>دانسته‌های خود را با یک آزمون کوتاه ده‌سؤالی بسنجید.</p>
<button class="btn" onclick="showPage('quiz')">شروع آزمون</button>
</div>
</div>
</section>

<section id="events" class="section">
<div class="section-title">
<h2>دانشنامه جنگ‌ها و نبردهای مهم ایران</h2>
<p>از دوران باستان تا جنگ ایران و عراق؛ برای مطالعه جزئیات هر نبرد، عنوان آن را باز کنید. فهرست زیر مهم‌ترین جنگ‌ها، یورش‌ها و نبردهای شناخته‌شده در تاریخ ایران را پوشش می‌دهد؛ ثبت تمام درگیری‌های محلی و کوتاه‌مدت چند هزار ساله ممکن نیست و درباره برخی تاریخ‌های باستانی نیز اختلاف نظر وجود دارد.</p>
</div>
<input class="search" id="search" placeholder="🔍 جست‌وجو بر اساس نام جنگ، دوره یا کشور..." oninput="searchEvents()">
<div id="eventList">

<details class="event"><summary>۱. نبردهای ایلام با آشور و بابل (هزاره دوم تا سده هفتم پیش از میلاد)</summary>
<p>ایلامیان در جنوب‌غرب فلات ایران، بارها با قدرت‌های میان‌رودان از جمله آشور و بابل درگیر شدند. این درگیری‌ها گاهی به یورش آشوریان به شوش و گاهی به حمله ایلامیان به سرزمین‌های همسایه انجامید. در سده هفتم پیش از میلاد، آشوربانیپال به ایلام حمله کرد و شوش را ویران ساخت. این جنگ‌ها نشان می‌دهد که کنترل راه‌های بازرگانی، زمین‌های حاصلخیز و نفوذ سیاسی در میان‌رودان از عوامل مهم نبردها بود.</p>
<p><strong>نتیجه و پیامد:</strong> قدرت سیاسی ایلام به‌شدت تضعیف شد و زمینه برای برآمدن قدرت‌های ایرانی، به‌ویژه مادها و پارس‌ها، فراهم‌تر شد.</p></details>

<details class="event"><summary>۲. جنگ مادها با آشور و سقوط نینوا (سده هفتم پیش از میلاد؛ ۶۱۲ پ.م.)</summary>
<p>مادها که در غرب و شمال‌غرب فلات ایران قدرت گرفته بودند، همراه با بابلیان علیه امپراتوری آشور متحد شدند. ائتلاف آنان در سال ۶۱۲ پیش از میلاد شهر نینوا، پایتخت آشور، را تصرف کرد. این رویداد یکی از نقاط عطف تاریخ خاور نزدیک باستان بود.</p>
<p><strong>علل و پیامد:</strong> گسترش‌طلبی آشور و مقاومت دولت‌های منطقه از عوامل اصلی بود. سقوط نینوا به پایان قدرت امپراتوری آشور انجامید و جایگاه مادها را در منطقه تقویت کرد.</p></details>

<details class="event"><summary>۳. لشکرکشی‌های کوروش بزرگ و شکل‌گیری شاهنشاهی هخامنشی (حدود ۵۵۰ تا ۵۳۹ پ.م.)</summary>
<p>کوروش دوم ابتدا بر مادها چیره شد، سپس دولت لیدی در آسیای صغیر را شکست داد و در سال ۵۳۹ پیش از میلاد بابل را تصرف کرد. این لشکرکشی‌ها در دوره‌ای کوتاه قلمرو هخامنشی را به یکی از بزرگ‌ترین قدرت‌های جهان باستان تبدیل کرد.</p>
<p><strong>نکته تاریخی:</strong> این رویدادها مجموعه‌ای از جنگ‌ها و فتوحات بودند، نه یک نبرد واحد. شیوه اداره سرزمین‌های گوناگون پس از فتح نیز در دوام شاهنشاهی اهمیت داشت.</p></details>

<details class="event"><summary>۴. جنگ‌های ایران و یونان در دوره هخامنشی (۴۹۹ تا ۴۴۹ پ.م.)</summary>
<p>درگیری‌ها با شورش شهرهای ایونیِ زیر فرمان هخامنشیان آغاز شد و سپس به جنگ میان شاهنشاهی ایران و برخی دولت‌شهرهای یونانی گسترش یافت. نبردهای ماراتون (۴۹۰ پ.م.)، ترموپیل و سالامیس (۴۸۰ پ.م.) و پلاته (۴۷۹ پ.م.) از مشهورترین رویدادهای این دوره‌اند. خشایارشا در لشکرکشی بزرگ خود از راه خشکی و دریا به یونان رفت، اما ناوگان ایران در سالامیس آسیب دید و سپاه ایران پس از آن از یونان عقب نشست.</p>
<p><strong>نتیجه و پیامد:</strong> ایران نتوانست یونان را به‌طور پایدار تابع خود کند، اما شاهنشاهی هخامنشی همچنان قدرت بزرگی باقی ماند. این جنگ‌ها ترکیبی از رقابت سیاسی، شورش ایونی و تلاش برای کنترل مناطق راهبردی بودند.</p></details>

<details class="event"><summary>۵. حمله اسکندر مقدونی و سقوط هخامنشیان (۳۳۴ تا ۳۳۰ پ.م.)</summary>
<p>اسکندر مقدونی در سال ۳۳۴ پیش از میلاد از تنگه داردانل گذشت و به قلمرو هخامنشی حمله کرد. نبرد گرانیک (۳۳۴)، ایسوس (۳۳۳) و گوگمل (۳۳۱ پ.م.) از مراحل اصلی جنگ بودند. داریوش سوم پس از شکست در گوگمل نتوانست ارتش و حکومت را دوباره سازمان دهد و اسکندر وارد مراکز مهم شاهنشاهی از جمله تخت‌جمشید شد.</p>
<p><strong>علل شکست:</strong> برتری تحرک و هماهنگی سپاه مقدونی، ضعف هماهنگی در فرماندهی هخامنشی در آن مقطع و اختلافات داخلی دربار از عوامل مطرح‌شده‌اند. <strong>پیامد:</strong> شاهنشاهی هخامنشی پایان یافت و دوره فرمانروایی مقدونیان و سپس سلوکیان آغاز شد.</p></details>

<details class="event"><summary>۶. جنگ‌های اشکانیان و روم (از سده اول پ.م. تا سده سوم م.)</summary>
<p>اشکانیان و جمهوری/امپراتوری روم برای نفوذ بر ارمنستان و میان‌رودان و کنترل مرزهای غربی بارها جنگیدند. در نبرد حَرّان یا کارهه در سال ۵۳ پیش از میلاد، سورنا سپاه کراسوس رومی را شکست داد. لشکرکشی مارک آنتونی در ۳۶ پ.م. نیز به نتیجه مورد انتظار روم نرسید. در سده‌های بعد، شهرهایی مانند تیسفون و ارمنستان بارها در مرکز رقابت دو قدرت قرار گرفتند.</p>
<p><strong>اهمیت:</strong> سواره‌نظام کماندار و سواران زره‌پوش اشکانی در جنگ‌های این دوره نقش برجسته‌ای داشتند. مرز ایران و روم برای چند قرن یکی از مهم‌ترین مرزهای نظامی جهان بود.</p></details>

<details class="event"><summary>۷. جنگ‌های ساسانیان با روم و بیزانس (۲۲۴ تا ۶۲۸ م.)</summary>
<p>ساسانیان پس از برانداختن اشکانیان با روم و سپس امپراتوری بیزانس بر سر ارمنستان، میان‌رودان، قفقاز و شهرهای مرزی جنگیدند. شاپور یکم در سده سوم میلادی چند بار رومیان را شکست داد و امپراتور والرین را در سال ۲۶۰ میلادی اسیر کرد. در دوره‌های بعد، جنگ‌ها با دوره‌های صلح و پیمان جایگزین می‌شدند. آخرین جنگ بزرگ در سال‌های ۶۰۲ تا ۶۲۸ میلادی میان خسرو پرویز و بیزانس رخ داد.</p>
<p><strong>پیامد:</strong> هر دو امپراتوری در پایان جنگ طولانی فرسوده شدند. هزینه‌های سنگین، بحران سیاسی و فشارهای مرزی، توان ساسانیان را در برابر یورش‌های بعدی کاهش داد.</p></details>

<details class="event"><summary>۸. جنگ‌های ساسانیان با هپتالیان (هون‌های سفید؛ سده پنجم میلادی)</summary>
<p>هپتالیان از قدرت‌های مهم آسیای مرکزی بودند و در چند مرحله با ساسانیان جنگیدند. پیروز یکم در نبردی در سال ۴۸۴ میلادی شکست خورد و کشته شد. این شکست برای حکومت ساسانی ضربه‌ای بزرگ بود و بر توازن قدرت در شرق ایران اثر گذاشت.</p>
<p><strong>پیامد:</strong> ساسانیان ناچار شدند برای مدتی با هپتالیان کنار بیایند و پرداخت خراج و تغییرات سیاسی در دربار، موقعیت حکومت را دشوارتر کرد.</p></details>

<details class="event"><summary>۹. جنگ‌های ایران و اعراب و سقوط دولت ساسانی (حدود ۶۳۳ تا ۶۵۱ م.)</summary>
<p>پس از درگذشت خسرو پرویز و بحران‌های پیاپی در دربار، سپاهیان خلافت نوپای اسلامی به قلمرو ساسانی حمله کردند. نبرد قادسیه (حدود ۶۳۶)، جلولا و نهاوند (حدود ۶۴۲) از نقاط مهم این روند بودند. یزدگرد سوم به شرق ایران عقب نشست و در سال ۶۵۱ میلادی کشته شد. تاریخ دقیق و جزئیات برخی نبردهای این دوره در منابع متفاوت است.</p>
<p><strong>علل و پیامد:</strong> جنگ‌های طولانی ایران و بیزانس، بحران جانشینی، اختلافات اشراف و فشار مالی، دولت ساسانی را تضعیف کرده بود. فتح ایران به پایان شاهنشاهی ساسانی و آغاز دگرگونی‌های سیاسی، دینی و فرهنگی گسترده انجامید.</p></details>

<details class="event"><summary>۱۰. درگیری‌های ایرانیان با خلافت و قیام‌های محلی (سده‌های هفتم تا نهم میلادی)</summary>
<p>پس از فتح ساسانی، کنترل همه مناطق ایران یک‌باره و بدون مقاومت برقرار نشد. در بخش‌هایی از طبرستان، خراسان، سیستان و نواحی کوهستانی، شورش‌ها و مقاومت‌های محلی رخ داد. بعدها حکومت‌هایی مانند طاهریان، صفاریان و سامانیان در بستر تضعیف اقتدار خلافت شکل گرفتند و قدرت سیاسی محلی را گسترش دادند.</p>
<p><strong>نکته:</strong> این عنوان به مجموعه‌ای از قیام‌ها و نبردهای منطقه‌ای اشاره دارد و یک جنگ واحد با تاریخ آغاز و پایان مشخص نیست.</p></details>

<details class="event"><summary>۱۱. جنگ‌های سلجوقیان و نبرد دندانقان (۱۰۴۰ م.)</summary>
<p>سلجوقیان که از آسیای مرکزی به خراسان آمده بودند، با غزنویان برای کنترل شرق ایران جنگیدند. در نبرد دندانقان در سال ۱۰۴۰ میلادی، طغرل و چغری بیگ بر مسعود غزنوی پیروز شدند. این پیروزی راه گسترش قدرت سلجوقیان در ایران و بخش بزرگی از خاورمیانه را باز کرد.</p>
<p><strong>پیامد:</strong> قدرت غزنویان در خراسان کاهش یافت و حکومت سلجوقی به یکی از قدرت‌های اصلی جهان اسلام تبدیل شد.</p></details>

<details class="event"><summary>۱۲. حمله مغول به ایران و جنگ با خوارزمشاهیان (از ۱۲۱۹ م.)</summary>
<p>پس از تنش میان خوارزمشاهیان و مغولان و ماجرای کشته‌شدن بازرگانان و فرستادگان مغول در قلمرو خوارزمشاهی، چنگیزخان در سال ۱۲۱۹ میلادی حمله‌ای گسترده را آغاز کرد. شهرهایی چون بخارا، سمرقند، مرو و نیشابور آسیب فراوان دیدند. سلطان محمد خوارزمشاه عقب نشست و حکومت خوارزمشاهی فروپاشید.</p>
<p><strong>علل شکست:</strong> پراکندگی نیروها، تصمیم‌های ناهماهنگ فرماندهی، توان بالای تحرک و محاصره مغولان و اختلافات سیاسی از عوامل مهم بودند. <strong>پیامد:</strong> ویرانی و کاهش جمعیت در بسیاری از مناطق و سپس شکل‌گیری حکومت ایلخانی در ایران.</p></details>

<details class="event"><summary>۱۳. یورش‌های مغولان در دوره ایلخانی و فتح بغداد (۱۲۵۶ تا ۱۲۵۸ م.)</summary>
<p>هلاکوخان در میانه سده سیزدهم به ایران آمد، اسماعیلیان نزاری را شکست داد و در سال ۱۲۵۸ میلادی بغداد را تصرف کرد؛ رخدادی که به پایان خلافت عباسی بغداد انجامید. این لشکرکشی بخشی از گسترش قدرت مغول در غرب آسیا بود.</p>
<p><strong>پیامد:</strong> ساختار سیاسی منطقه دگرگون شد و حکومت ایلخانان در ایران شکل گرفت. این دوره هم‌زمان با خشونت و ویرانی‌های جنگ و سپس بازسازی برخی نهادهای اداری و اقتصادی بود.</p></details>

<details class="event"><summary>۱۴. حمله تیمور به ایران (از دهه ۱۳۸۰ تا اوایل سده پانزدهم م.)</summary>
<p>تیمور گورکانی در چند لشکرکشی پیاپی به خراسان، مازندران، فارس، عراق عجم و آذربایجان حمله کرد. اصفهان در سال ۱۳۸۷ میلادی پس از شورش مردم به‌شدت سرکوب شد. تیمور همچنین به سوی قفقاز، آناتولی و هند لشکر کشید.</p>
<p><strong>پیامد:</strong> بسیاری از شهرها و مراکز اقتصادی آسیب دیدند و حکومت‌های محلی تضعیف شدند؛ با این حال در دوره جانشینان تیمور، برخی مراکز فرهنگی و هنری رونق یافتند.</p></details>

<details class="event"><summary>۱۵. جنگ‌های صفویان و ازبکان؛ نبرد مرو (۱۵۱۰ م.)</summary>
<p>در آغاز حکومت صفوی، ازبکان به رهبری محمد شیبانی در خراسان قدرت گرفته بودند. شاه اسماعیل یکم در سال ۱۵۱۰ میلادی در نبرد مرو آنان را شکست داد و خراسان را برای مدتی به قلمرو صفوی پیوند زد.</p>
<p><strong>اهمیت:</strong> این پیروزی جایگاه صفویان را در شرق تقویت کرد، اما رقابت با ازبکان بر سر خراسان در دوره‌های بعد نیز ادامه یافت.</p></details>

<details class="event"><summary>۱۶. جنگ صفویان و عثمانیان؛ نبرد چالدران (۱۵۱۴ م.)</summary>
<p>رقابت صفویان و عثمانیان بر سر نفوذ در آناتولی شرقی، عراق و قفقاز به جنگ انجامید. در نبرد چالدران در ۲۳ اوت ۱۵۱۴ میلادی، سپاه شاه اسماعیل صفوی از ارتش سلطان سلیم اول شکست خورد. استفاده گسترده عثمانیان از توپخانه و سلاح‌های آتشین در برابر نیروی عمدتاً سواره صفوی، از عوامل مهم نتیجه نبرد بود.</p>
<p><strong>پیامد:</strong> عثمانیان موقتاً تبریز را گرفتند، اما نتوانستند آن را نگه دارند. رقابت دو دولت برای چندین نسل ادامه یافت و سرانجام پیمان زهاب در ۱۶۳۹ به تثبیت نسبی مرزها کمک کرد.</p></details>

<details class="event"><summary>۱۷. جنگ‌های بعدی صفویان و عثمانیان (سده‌های شانزدهم و هفدهم)</summary>
<p>پس از چالدران، جنگ‌ها بر سر عراق، قفقاز، آذربایجان و مناطق مرزی بارها از سر گرفته شد. شاه عباس یکم در اوایل سده هفدهم بخش‌هایی از سرزمین‌های ازدست‌رفته را بازپس گرفت و بغداد نیز چند بار میان دو قدرت دست‌به‌دست شد.</p>
<p><strong>نتیجه:</strong> پیمان زهاب در سال ۱۶۳۹ میلادی به یکی از مبانی تاریخی مرز ایران و عثمانی تبدیل شد، هرچند اختلافات مرزی در دوره‌های بعد نیز ادامه یافت.</p></details>

<details class="event"><summary>۱۸. نبردهای صفویان با پرتغالی‌ها و بازپس‌گیری هرمز (۱۶۲۲ م.)</summary>
<p>پرتغالی‌ها از اوایل سده شانزدهم در جزیره هرمز و مسیرهای دریایی خلیج فارس حضور نظامی و تجاری داشتند. در سال ۱۶۲۲، نیروهای صفوی با کمک ناوگان انگلیسیِ کمپانی هند شرقی، پرتغالی‌ها را از هرمز بیرون راندند.</p>
<p><strong>اهمیت:</strong> این رویداد جایگاه صفویان را در خلیج فارس تقویت کرد و نمونه‌ای از همکاری نظامی محدود با یک قدرت اروپایی برای مقابله با قدرت دریایی رقیب بود.</p></details>

<details class="event"><summary>۱۹. حمله افغان‌های هوتکی و سقوط اصفهان (۱۷۲۲ م.)</summary>
<p>در پی ضعف حکومت صفوی، نارضایتی‌های محلی و بحران اداره کشور، نیروهای محمود هوتکی از قندهار به ایران حمله کردند. آنان پس از محاصره طولانی در سال ۱۷۲۲ میلادی اصفهان را تصرف کردند و شاه سلطان حسین صفوی تسلیم شد.</p>
<p><strong>پیامد:</strong> حکومت صفوی عملاً سقوط کرد و کشور وارد دوره‌ای از آشفتگی، رقابت مدعیان قدرت و مداخله خارجی شد.</p></details>

<details class="event"><summary>۲۰. جنگ‌های نادرشاه با افغان‌ها، عثمانیان و گورکانیان هند (دهه ۱۷۲۰ تا ۱۷۴۰ م.)</summary>
<p>نادر ابتدا نیروهای افغان را شکست داد و سپس بخش‌هایی از ایران را از اشغال بیرون آورد. او در جنگ با عثمانیان و روس‌ها نیز برای بازگرداندن مناطق مرزی تلاش کرد. در سال ۱۷۳۹ به هند لشکر کشید و در نبرد کرنال سپاه گورکانی را شکست داد و وارد دهلی شد.</p>
<p><strong>پیامد و ارزیابی:</strong> فتوحات نادر قلمرو و نفوذ ایران را موقتاً گسترش داد، اما لشکرکشی‌های پرهزینه و فشار مالی و نظامی بر جامعه سنگین بود. پس از قتل او در ۱۷۴۷، کشمکش‌های داخلی شدت گرفت.</p></details>

<details class="event"><summary>۲۱. جنگ‌ها و کشمکش‌های داخلی پس از نادرشاه (میانه و اواخر سده هجدهم)</summary>
<p>پس از مرگ نادرشاه، مدعیان مختلف قدرت در ایران با یکدیگر جنگیدند. کریم‌خان زند پس از سال‌ها کشمکش توانست بخش بزرگی از کشور را زیر فرمان خود بیاورد، اما پس از مرگ او رقابت زندیان و قاجاریان ادامه یافت و آقامحمدخان قاجار سرانجام حکومت قاجار را بنیان گذاشت.</p>
<p><strong>پیامد:</strong> این جنگ‌های داخلی موجب ناامنی و آسیب به اقتصاد و جمعیت برخی مناطق شد و تمرکز قدرت را برای مدتی طولانی دشوار کرد.</p></details>

<details class="event"><summary>۲۲. نخستین جنگ ایران و روسیه در دوره قاجار (۱۸۰۴ تا ۱۸۱۳ م.)</summary>
<p>روسیه تزاری برای گسترش نفوذ خود در قفقاز با ایران وارد جنگ شد. جنگ با وجود مقاومت نیروهای ایرانی و برخی پیروزی‌های مقطعی، به‌دلیل برتری سازمان و تجهیزات ارتش روسیه و مشکلات مالی و نظامی ایران به زیان قاجار پایان یافت. عهدنامه گلستان در سال ۱۸۱۳ امضا شد.</p>
<p><strong>پیامد:</strong> ایران بخش‌هایی از قفقاز از جمله گرجستان و برخی خان‌نشین‌ها را از دست داد. این جنگ ضرورت اصلاح ارتش و ساختار اداری را آشکار کرد.</p></details>

<details class="event"><summary>۲۳. دومین جنگ ایران و روسیه (۱۸۲۶ تا ۱۸۲۸ م.)</summary>
<p>با آغاز دوباره جنگ، نیروهای ایران در ابتدا پیشروی‌هایی داشتند، اما روسیه ضدحمله کرد و ارتش ایران شکست خورد. عهدنامه ترکمانچای در سال ۱۸۲۸ امضا شد.</p>
<p><strong>پیامد:</strong> بخش‌های بیشتری از قفقاز به روسیه واگذار شد و غرامت و امتیازهای سنگینی بر ایران تحمیل گردید. این شکست یکی از نقاط مهم در تاریخ روابط ایران و روسیه است.</p></details>

<details class="event"><summary>۲۴. جنگ ایران و بریتانیا بر سر هرات (۱۸۵۶ تا ۱۸۵۷ م.)</summary>
<p>ایران در دوره ناصرالدین‌شاه برای بازپس‌گیری هرات اقدام کرد. بریتانیا که با گسترش نفوذ ایران در افغانستان مخالف بود، به جنوب ایران حمله کرد و جزیره خارک و بخش‌هایی از سواحل و بنادر را هدف گرفت. جنگ با عهدنامه پاریس در سال ۱۸۵۷ پایان یافت.</p>
<p><strong>پیامد:</strong> ایران از ادعای خود بر هرات صرف‌نظر کرد و متعهد شد در امور افغانستان مداخله نکند. این جنگ نفوذ بریتانیا در خلیج فارس را افزایش داد.</p></details>

<details class="event"><summary>۲۵. ایران در جنگ جهانی اول (۱۹۱۴ تا ۱۹۱۸ م.)</summary>
<p>دولت ایران بی‌طرفی خود را اعلام کرد، اما به‌دلیل موقعیت راهبردی کشور، نیروهای روسیه، بریتانیا و عثمانی وارد بخش‌هایی از خاک ایران شدند. در آذربایجان، غرب و جنوب کشور درگیری‌هایی رخ داد و ناامنی، قحطی و بیماری به مردم آسیب رساند.</p>
<p><strong>پیامد:</strong> بی‌طرفی ایران عملاً رعایت نشد و ضعف دولت مرکزی و فشارهای اقتصادی و انسانی تشدید شد. درباره میزان تلفات و جزئیات برخی رویدادها در منابع اختلاف وجود دارد.</p></details>

<details class="event"><summary>۲۶. اشغال ایران در جنگ جهانی دوم (۱۹۴۱ م.)</summary>
<p>با وجود اعلام بی‌طرفی ایران در جنگ جهانی دوم، نیروهای بریتانیا و شوروی در اوت ۱۹۴۱ به ایران حمله کردند. از دلایل اعلام‌شده، نگرانی متفقین از حضور کارشناسان آلمانی و اهمیت راه‌آهن و مسیر انتقال تدارکات به شوروی بود. رضاشاه کناره‌گیری کرد و نیروهای خارجی تا پایان جنگ در کشور ماندند.</p>
<p><strong>پیامد:</strong> ایران به مسیر مهم انتقال کمک‌های متفقین به شوروی تبدیل شد، اما اشغال، کمبود کالا و فشار اقتصادی و سیاسی زیادی بر کشور وارد کرد.</p></details>

<details class="event"><summary>۲۷. جنگ تحمیلی عراق علیه ایران (۱۳۵۹ تا ۱۳۶۷ / ۱۹۸۰ تا ۱۹۸۸ م.)</summary>
<p>عراق در ۳۱ شهریور ۱۳۵۹ حمله گسترده‌ای را با حملات هوایی و تهاجم زمینی به مرزهای ایران آغاز کرد. اختلافات مرزی، رقابت سیاسی منطقه‌ای، محاسبات حکومت صدام حسین درباره وضعیت ایران پس از انقلاب و مناقشه بر سر اروندرود از زمینه‌های جنگ بودند. خرمشهر در آغاز جنگ سقوط کرد و در اردیبهشت ۱۳۶۱ آزاد شد. عملیات‌های بزرگ و نبردهای زمینی، هوایی و دریایی در سال‌های بعد ادامه یافتند.</p>
<p><strong>پایان و پیامد:</strong> دو کشور قطعنامه ۵۹۸ شورای امنیت را پذیرفتند و آتش‌بس در سال ۱۳۶۷ برقرار شد. جنگ نزدیک به هشت سال طول کشید، تلفات انسانی و خسارت اقتصادی گسترده‌ای برجای گذاشت و مرزهای بین‌المللی دو کشور در نهایت تغییر اساسی نکرد.</p></details>

<details class="event"><summary>۲۸. درگیری‌های دریایی ایران و آمریکا در خلیج فارس (۱۹۸۷ تا ۱۹۸۸ م.)</summary>
<p>در سال‌های پایانی جنگ ایران و عراق، تنش در خلیج فارس و حمله به کشتی‌ها افزایش یافت. آمریکا برای حفاظت از کشتیرانی، عملیات اسکورت نفتکش‌ها را اجرا کرد و در آوریل ۱۹۸۸ در عملیات «آخوندک» به چند شناور و تأسیسات دریایی ایران حمله کرد.</p>
<p><strong>نکته:</strong> این درگیری‌ها بخشی از فضای منطقه‌ای جنگ ایران و عراق بود و معمولاً به‌عنوان یک جنگ مستقل و رسمی میان دو کشور طبقه‌بندی نمی‌شود.</p></details>

</div>
</section>

<section id="analysis" class="section">
<div class="section-title">
<h2>تحلیل و بررسی</h2>
<p>نگاهی به عوامل و پیامدهای رویدادهای تاریخی.</p>
</div>
<div class="grid">
<div class="card">
<span class="tag">تحلیل تاریخی</span>
<h3>اهمیت اتحاد ملی</h3>
<p>همبستگی اجتماعی و همکاری مردم می‌تواند در زمان بحران، توانایی یک کشور را برای مقابله با مشکلات افزایش دهد.</p>
</div>
<div class="card">
<span class="tag">امنیت</span>
<h3>اهمیت موقعیت جغرافیایی</h3>
<p>موقعیت جغرافیایی ایران در طول تاریخ بر روابط سیاسی، اقتصادی و امنیتی آن تأثیر گذاشته است.</p>
</div>
<div class="card">
<span class="tag">آموزشی</span>
<h3>نقش آگاهی عمومی</h3>
<p>شناخت تهدیدها، آموزش صحیح و افزایش سواد رسانه‌ای به تصمیم‌گیری بهتر در شرایط دشوار کمک می‌کند.</p>
</div>
</div>
</section>

<section id="lessons" class="section">
<div class="section-title">
<h2>درس‌آموخته‌های تاریخی</h2>
<p>چند نکته مهم که می‌توان از تاریخ آموخت.</p>
</div>
<div class="grid">
<div class="card">
<div class="icon">🤝</div>
<h3>همدلی و همکاری</h3>
<p>همکاری مردم و مسئولان در زمان بحران، به حفظ آرامش و عبور از مشکلات کمک می‌کند.</p>
</div>
<div class="card">
<div class="icon">📚</div>
<h3>آموزش و آگاهی</h3>
<p>آموزش عمومی و شناخت درست خطرها، آمادگی جامعه را افزایش می‌دهد.</p>
</div>
<div class="card">
<div class="icon">🕊️</div>
<h3>اهمیت صلح</h3>
<p>گفت‌وگو و دیپلماسی می‌توانند از بسیاری از درگیری‌ها و خسارت‌های انسانی جلوگیری کنند.</p>
</div>
<div class="card">
<div class="icon">🧠</div>
<h3>تفکر انتقادی</h3>
<p>بررسی منابع معتبر و پرهیز از شایعات، درک درست‌تری از رویدادها ایجاد می‌کند.</p>
</div>
</div>
</section>

<section id="quiz" class="section">
<div class="section-title">
<h2>آزمون آمادگی دفاعی</h2>
<p>به ده سؤال زیر پاسخ دهید و در پایان نتیجه را ببینید.</p>
</div>
<div class="card">
<form id="quizForm">
<div id="questions"></div>
<button class="btn" type="button" onclick="checkQuiz()">ثبت پاسخ‌ها و مشاهده نتیجه</button>
<button class="btn" type="reset" onclick="resetQuiz()">شروع دوباره</button>
</form>
<div id="result" class="result"></div>
</div>
</section>

<section id="about" class="section">
<div class="section-title">
<h2>درباره این پروژه</h2>
<p>معرفی وب‌سایت آموزشی آمادگی دفاعی.</p>
</div>
<div class="card">
<h3>هدف از ساخت سایت</h3>
<p>این وب‌سایت با هدف معرفی رویدادهای مهم تاریخ ایران، افزایش آگاهی تاریخی و آموزش مفاهیم مرتبط با امنیت و آمادگی دفاعی طراحی شده است.</p>
<h3>طراح و سازنده</h3>
<p><strong>محمد مهدی عباسی</strong></p>
<h3>موضوع پروژه</h3>
<p>فعالیت آموزشی درس آمادگی دفاعی</p>
<p class="small">این وب‌سایت یک پروژه آموزشی دانش‌آموزی است.</p>
<h3>📚 منابع و مراجع</h3>
<p>برای مطالعه بیشتر و بررسی مطالب تاریخی سایت، منابع زیر پیشنهاد می‌شوند:</p>
  <ul>
    <li>
      <a href="https://www.iranicaonline.org/articles/iran-ii1-pre-islamic-times/" target="_blank" rel="noopener noreferrer">
        دانشنامه ایرانیکا – تاریخ ایران در دوران پیش از اسلام
      </a>
      <span class="small">برای آشنایی با تاریخ ایران باستان و دوره هخامنشی.</span>
    </li>
    <li>
      <a href="https://www.iranicaonline.org/articles/iran-ii2-islamic-period-page-1/" target="_blank" rel="noopener noreferrer">
        دانشنامه ایرانیکا – تاریخ ایران در دوره اسلامی
      </a>
      <span class="small">مروری بر دوره‌های تاریخی ایران، از جمله حمله مغول و تحولات پس از آن.</span>
    </li>
    <li>
      <a href="https://www.iranicaonline.org/articles/iran-ii2-islamic-period-page-3/" target="_blank" rel="noopener noreferrer">
        دانشنامه ایرانیکا – بخش مربوط به حمله مغول
      </a>
      <span class="small">برای مطالعه زمینه‌ها و پیامدهای یورش مغول به ایران.</span>
    </li>
    <li>
      <a href="https://www.iranicaonline.org/articles/boundaries-i/" target="_blank" rel="noopener noreferrer">
        دانشنامه ایرانیکا – مرزهای ایران و امپراتوری عثمانی
      </a>
      <span class="small">شامل اطلاعاتی درباره نبرد چالدران و تحولات مرزی ایران و عثمانی.</span>
    </li>
    <li>
      <a href="https://www.iranicaonline.org/articles/russia-i-relations/" target="_blank" rel="noopener noreferrer">
        دانشنامه ایرانیکا – روابط ایران و روسیه تا انقلاب بلشویکی
      </a>
      <span class="small">برای بررسی روابط و جنگ‌های ایران و روسیه در دوره قاجار.</span>
    </li>
    <li>
      <a href="https://www.iranicaonline.org/articles/golestan-treaty/" target="_blank" rel="noopener noreferrer">
        دانشنامه ایرانیکا – عهدنامه گلستان
      </a>
      <span class="small">اطلاعات تاریخی درباره پایان نخستین جنگ ایران و روسیه.</span>
    </li>
    <li>
      <a href="https://www.iranicaonline.org/articles/arab-ii/" target="_blank" rel="noopener noreferrer">
        دانشنامه ایرانیکا – فتح ایران به دست سپاهیان عرب
      </a>
      <span class="small">برای مطالعه پایان حکومت ساسانی و تحولات پس از آن.</span>
    </li>
    <li>
      <a href="https://www.iranicaonline.org/articles/anglo-iranian-relations-ii/" target="_blank" rel="noopener noreferrer">
        دانشنامه ایرانیکا – روابط ایران و بریتانیا در دوره قاجار
      </a>
      <span class="small">شامل مطالبی درباره وضعیت ایران در جریان جنگ جهانی اول.</span>
    </li>
    <li>
      <a href="https://www.iranicaonline.org/articles/iran-ii3-chronological-table/" target="_blank" rel="noopener noreferrer">
        دانشنامه ایرانیکا – جدول زمانی تاریخ ایران
      </a>
      <span class="small">برای تطبیق دوره‌ها و تاریخ رویدادهای تاریخی از دوران باستان تا دوره معاصر.</span>
    </li>
    <li>
      <a href="https://www.iranicaonline.org/articles/army-i/" target="_blank" rel="noopener noreferrer">
        دانشنامه ایرانیکا – ارتش در ایران پیش از اسلام
      </a>
      <span class="small">برای آشنایی با سازمان، تجهیزات و شیوه‌های جنگی ارتش‌های ایران باستان.</span>
    </li>
    <li>
      <a href="https://www.iranicaonline.org/articles/iran-ii1-pre-islamic-times/" target="_blank" rel="noopener noreferrer">
        دانشنامه ایرانیکا – تاریخ ایران پیش از اسلام
      </a>
      <span class="small">مروری بر دوره‌های ماد، هخامنشی، اشکانی و ساسانی.</span>
    </li>
    <li>
      <a href="https://www.iranicaonline.org/articles/iran-ii2-islamic-period-page-1/" target="_blank" rel="noopener noreferrer">
        دانشنامه ایرانیکا – تاریخ ایران در دوره اسلامی
      </a>
      <span class="small">برای مطالعه دوره‌های پس از فتح ایران، سلجوقیان، مغولان، تیموریان، صفویان و قاجار.</span>
    </li>
    <li>
      <a href="https://www.iranicaonline.org/articles/iraq-vii-iran-iraq-war/" target="_blank" rel="noopener noreferrer">
        دانشنامه ایرانیکا – جنگ ایران و عراق
      </a>
      <span class="small">بررسی زمینه‌ها، روند و پایان جنگ هشت‌ساله.</span>
    </li>
    <li>
      <a href="https://assets.cambridge.org/97811084/78427/excerpt/9781108478427_excerpt.pdf" target="_blank" rel="noopener noreferrer">
        انتشارات دانشگاه کمبریج – تاریخ ناتمام جنگ ایران و عراق
      </a>
      <span class="small">پژوهش دانشگاهی درباره زمینه‌ها و تاریخ‌نگاری جنگ ایران و عراق.</span>
    </li>
    <li>
      <a href="https://digitallibrary.un.org/record/137345" target="_blank" rel="noopener noreferrer">
        کتابخانه دیجیتال سازمان ملل متحد – قطعنامه ۵۹۸ شورای امنیت (۱۹۸۷)
      </a>
      <span class="small">سند رسمی سازمان ملل درباره آتش‌بس و روند پایان جنگ ایران و عراق.</span>
    </li>
  </ul>
</div>
</section>

</main>


<section class="sources" id="sources">
  <h2>📚 منابع و مراجع برای مطالعه و بررسی</h2>
  <p>
    برای بررسی و تکمیل مطالب تاریخی این وب‌سایت، می‌توانید از منابع پژوهشی و اسناد زیر استفاده کنید.
    این فهرست، منابع پیشنهادی مرتبط با موضوعات سایت است و لزوماً به معنای استفاده مستقیم از همه آن‌ها
    در نگارش نسخه اولیه مطالب نیست.
  </p>
  <ul>
    <li>
      <a href="https://www.iranicaonline.org/articles/iran-ii1-pre-islamic-times/" target="_blank" rel="noopener noreferrer">
        دانشنامه ایرانیکا – تاریخ ایران در دوران پیش از اسلام
      </a>
      <span class="small">برای آشنایی با تاریخ ایران باستان و دوره هخامنشی.</span>
    </li>
    <li>
      <a href="https://www.iranicaonline.org/articles/iran-ii2-islamic-period-page-1/" target="_blank" rel="noopener noreferrer">
        دانشنامه ایرانیکا – تاریخ ایران در دوره اسلامی
      </a>
      <span class="small">مروری بر دوره‌های تاریخی ایران، از جمله حمله مغول و تحولات پس از آن.</span>
    </li>
    <li>
      <a href="https://www.iranicaonline.org/articles/iran-ii2-islamic-period-page-3/" target="_blank" rel="noopener noreferrer">
        دانشنامه ایرانیکا – بخش مربوط به حمله مغول
      </a>
      <span class="small">برای مطالعه زمینه‌ها و پیامدهای یورش مغول به ایران.</span>
    </li>
    <li>
      <a href="https://www.iranicaonline.org/articles/boundaries-i/" target="_blank" rel="noopener noreferrer">
        دانشنامه ایرانیکا – مرزهای ایران و امپراتوری عثمانی
      </a>
      <span class="small">شامل اطلاعاتی درباره نبرد چالدران و تحولات مرزی ایران و عثمانی.</span>
    </li>
    <li>
      <a href="https://www.iranicaonline.org/articles/russia-i-relations/" target="_blank" rel="noopener noreferrer">
        دانشنامه ایرانیکا – روابط ایران و روسیه تا انقلاب بلشویکی
      </a>
      <span class="small">برای بررسی روابط و جنگ‌های ایران و روسیه در دوره قاجار.</span>
    </li>
    <li>
      <a href="https://www.iranicaonline.org/articles/golestan-treaty/" target="_blank" rel="noopener noreferrer">
        دانشنامه ایرانیکا – عهدنامه گلستان
      </a>
      <span class="small">اطلاعات تاریخی درباره پایان نخستین جنگ ایران و روسیه.</span>
    </li>
    <li>
      <a href="https://www.iranicaonline.org/articles/arab-ii/" target="_blank" rel="noopener noreferrer">
        دانشنامه ایرانیکا – فتح ایران به دست سپاهیان عرب
      </a>
      <span class="small">برای مطالعه پایان حکومت ساسانی و تحولات پس از آن.</span>
    </li>
    <li>
      <a href="https://www.iranicaonline.org/articles/anglo-iranian-relations-ii/" target="_blank" rel="noopener noreferrer">
        دانشنامه ایرانیکا – روابط ایران و بریتانیا در دوره قاجار
      </a>
      <span class="small">شامل مطالبی درباره وضعیت ایران در جریان جنگ جهانی اول.</span>
    </li>
    <li>
      <a href="https://www.iranicaonline.org/articles/iran-ii3-chronological-table/" target="_blank" rel="noopener noreferrer">
        دانشنامه ایرانیکا – جدول زمانی تاریخ ایران
      </a>
      <span class="small">برای تطبیق دوره‌ها و تاریخ رویدادهای تاریخی از دوران باستان تا دوره معاصر.</span>
    </li>
    <li>
      <a href="https://www.iranicaonline.org/articles/army-i/" target="_blank" rel="noopener noreferrer">
        دانشنامه ایرانیکا – ارتش در ایران پیش از اسلام
      </a>
      <span class="small">برای آشنایی با سازمان، تجهیزات و شیوه‌های جنگی ارتش‌های ایران باستان.</span>
    </li>
    <li>
      <a href="https://www.iranicaonline.org/articles/iran-ii1-pre-islamic-times/" target="_blank" rel="noopener noreferrer">
        دانشنامه ایرانیکا – تاریخ ایران پیش از اسلام
      </a>
      <span class="small">مروری بر دوره‌های ماد، هخامنشی، اشکانی و ساسانی.</span>
    </li>
    <li>
      <a href="https://www.iranicaonline.org/articles/iran-ii2-islamic-period-page-1/" target="_blank" rel="noopener noreferrer">
        دانشنامه ایرانیکا – تاریخ ایران در دوره اسلامی
      </a>
      <span class="small">برای مطالعه دوره‌های پس از فتح ایران، سلجوقیان، مغولان، تیموریان، صفویان و قاجار.</span>
    </li>
    <li>
      <a href="https://www.iranicaonline.org/articles/iraq-vii-iran-iraq-war/" target="_blank" rel="noopener noreferrer">
        دانشنامه ایرانیکا – جنگ ایران و عراق
      </a>
      <span class="small">بررسی زمینه‌ها، روند و پایان جنگ هشت‌ساله.</span>
    </li>
    <li>
      <a href="https://assets.cambridge.org/97811084/78427/excerpt/9781108478427_excerpt.pdf" target="_blank" rel="noopener noreferrer">
        انتشارات دانشگاه کمبریج – تاریخ ناتمام جنگ ایران و عراق
      </a>
      <span class="small">پژوهش دانشگاهی درباره زمینه‌ها و تاریخ‌نگاری جنگ ایران و عراق.</span>
    </li>
    <li>
      <a href="https://digitallibrary.un.org/record/137345" target="_blank" rel="noopener noreferrer">
        کتابخانه دیجیتال سازمان ملل متحد – قطعنامه ۵۹۸ شورای امنیت (۱۹۸۷)
      </a>
      <span class="small">سند رسمی سازمان ملل درباره آتش‌بس و روند پایان جنگ ایران و عراق.</span>
    </li>
  </ul>
  <p class="small">تاریخ دسترسی به پیوندها: آبان ۱۴۰۵</p>
</section>

<footer>
<div>وب‌سایت آموزشی آمادگی دفاعی</div>
<div>طراح سایت: <strong>محمد مهدی عباسی</strong></div>
<div class="small">با هدف آموزش، آگاهی و شناخت تاریخ</div>
</footer>

<script>
const quizData = [
{q:"جنگ تحمیلی عراق علیه ایران در چه تاریخی آغاز شد؟",a:["۱۳۵۷","۳۱ شهریور ۱۳۵۹","۱۳۶۷","۱۳۵۰"],c:1},
{q:"جنگ ایران و عراق چند سال طول کشید؟",a:["۴ سال","۶ سال","۸ سال","۱۰ سال"],c:2},
{q:"نبرد چالدران میان کدام حکومت‌ها رخ داد؟",a:["صفویان و عثمانیان","هخامنشیان و یونانیان","قاجار و روسیه","ساسانیان و روم"],c:0},
{q:"کدام قرارداد پس از جنگ‌های ایران و روسیه در دوره قاجار امضا شد؟",a:["ترکمانچای","پاریس","ورسای","لوزان"],c:0},
{q:"هدف اصلی آمادگی دفاعی چیست؟",a:["افزایش آگاهی و آمادگی","افزایش اختلاف","گسترش شایعات","نادیده گرفتن خطرها"],c:0},
{q:"کدام مورد به امنیت جامعه کمک می‌کند؟",a:["شایعه‌پراکنی","آگاهی و همکاری","بی‌توجهی","خشونت"],c:1},
{q:"جنگ جهانی دوم در چه سالی پایان یافت؟",a:["۱۹۱۸","۱۹۳۹","۱۹۴۵","۱۹۵۰"],c:2},
{q:"حمله مغول به ایران در کدام قرن رخ داد؟",a:["قرن دهم","قرن سیزدهم","قرن شانزدهم","قرن هجدهم"],c:1},
{q:"کدام گزینه به کاهش خطر درگیری کمک می‌کند؟",a:["گفت‌وگو و دیپلماسی","تهدید دائمی","انتشار اخبار جعلی","قطع ارتباط"],c:0},
{q:"در بررسی اخبار و رویدادها چه کاری درست‌تر است؟",a:["باور فوری هر خبر","بررسی منابع معتبر","بازنشر شایعات","نادیده گرفتن حقیقت"],c:1}
];

function showPage(id,btn){
document.querySelectorAll('.section').forEach(s=>s.classList.remove('active'));
document.getElementById(id).classList.add('active');
document.querySelectorAll('nav button').forEach(b=>b.classList.remove('active'));
if(btn)btn.classList.add('active');
window.scrollTo({top:0,behavior:'smooth'});
}

function toggleTheme(){
document.body.classList.toggle('dark');
}

function searchEvents(){
const value=document.getElementById('search').value.trim().toLowerCase();
document.querySelectorAll('#eventList .event').forEach(event=>{
event.style.display=event.innerText.toLowerCase().includes(value)?'':'none';
});
}

function renderQuiz(){
const holder=document.getElementById('questions');
holder.innerHTML='';
quizData.forEach((item,i)=>{
let html=`<div class="question"><h3>${i+1}. ${item.q}</h3>`;
item.a.forEach((answer,j)=>{
html+=`<label class="option"><input type="radio" name="q${i}" value="${j}"> ${answer}</label>`;
});
html+='</div>';
holder.innerHTML+=html;
});
}

function checkQuiz(){
let score=0,answered=0;
quizData.forEach((item,i)=>{
const selected=document.querySelector(`input[name="q${i}"]:checked`);
if(selected){
answered++;
if(Number(selected.value)===item.c)score++;
}
});
const result=document.getElementById('result');
result.style.display='block';
result.innerHTML=`تعداد پاسخ‌های داده‌شده: ${answered} از ۱۰<br>
پاسخ‌های درست: ${score} از ۱۰<br>
<strong>نمره شما: ${score*2} از ۲۰</strong><br>
${answered<10?'برای نتیجه کامل، به همه سؤال‌ها پاسخ دهید.':(score>=8?'آفرین! عملکرد بسیار خوبی داشتی.':'خوب بود! با مطالعه بیشتر می‌توانی بهتر شوی.')}`;
}

function resetQuiz(){
setTimeout(()=>{
document.getElementById('result').style.display='none';
},0);
}
renderQuiz();
</script>
</body>
</html>'''

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
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



