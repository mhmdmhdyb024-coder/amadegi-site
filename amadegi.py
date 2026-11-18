
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
<button onclick="showPage('events',this)">رویدادها</button>
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
آشنایی با تاریخ دفاعی ایران، رویدادهای مهم تاریخی،
اهمیت امنیت ملی و نقش آگاهی مردم در حفظ استقلال و آرامش کشور.
</p>
<div class="creator">✦ طراح و سازنده: محمد مهدی عباسی ✦</div>
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
<p>با برخی از مهم‌ترین جنگ‌ها و رویدادهای تاریخی ایران آشنا شوید.</p>
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
<h2>رویدادهای مهم تاریخی</h2>
<p>برای دیدن توضیحات هر رویداد، روی عنوان آن کلیک کنید.</p>
</div>
<input class="search" id="search" placeholder="🔍 جست‌وجو در رویدادها..." oninput="searchEvents()">
<div id="eventList">

<details class="event">
<summary>نبرد ایران و یونان در دوره هخامنشی</summary>
<p>در دوره هخامنشی، ایران و دولت‌شهرهای یونانی درگیر جنگ‌هایی شدند. این نبردها از رویدادهای مهم تاریخ جهان باستان به شمار می‌روند.</p>
</details>

<details class="event">
<summary>حمله اسکندر مقدونی به ایران</summary>
<p>در سده چهارم پیش از میلاد، اسکندر مقدونی به قلمرو هخامنشی حمله کرد. این حمله به سقوط حکومت هخامنشی انجامید.</p>
</details>

<details class="event">
<summary>فتح ایران به دست سپاهیان عرب</summary>
<p>در قرن هفتم میلادی، با ضعف حکومت ساسانی و حمله سپاهیان عرب، حکومت ساسانی پایان یافت و تغییرات سیاسی و فرهنگی گسترده‌ای ایجاد شد.</p>
</details>

<details class="event">
<summary>حمله مغول به ایران</summary>
<p>در قرن سیزدهم میلادی، حمله مغول خسارت‌های انسانی و اقتصادی فراوانی به بخش‌های مختلف ایران وارد کرد.</p>
</details>

<details class="event">
<summary>نبرد چالدران</summary>
<p>نبرد چالدران در سال ۱۵۱۴ میلادی میان صفویان و عثمانیان رخ داد.</p>
</details>

<details class="event">
<summary>جنگ‌های ایران و روسیه در دوره قاجار</summary>
<p>دو جنگ مهم میان ایران و روسیه به قراردادهای گلستان و ترکمانچای و جدا شدن بخش‌هایی از سرزمین ایران انجامید.</p>
</details>

<details class="event">
<summary>جنگ جهانی اول و دوم</summary>
<p>ایران در هر دو جنگ جهانی اعلام بی‌طرفی کرد، اما موقعیت جغرافیایی کشور باعث حضور نیروهای خارجی در بخش‌هایی از ایران شد.</p>
</details>

<details class="event">
<summary>جنگ تحمیلی عراق علیه ایران</summary>
<p>در ۳۱ شهریور ۱۳۵۹، عراق به ایران حمله کرد. این جنگ هشت سال ادامه یافت و در سال ۱۳۶۷ با پذیرش قطعنامه ۵۹۸ پایان یافت.</p>
</details>

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
</div>
</section>

</main>

<footer>
<div>وب‌سایت آموزشی آمادگی دفاعی</div>
<div>طراح و سازنده: <strong>محمد مهدی عباسی</strong></div>
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

