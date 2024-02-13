#استدعاء المكاتب
from pywebio import *
from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
from pywebio import config
css ="""
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@200&display=swap');

#h3{
font-family: 'IBM Plex Sans Arabic', sans-serif;
}
#para{
font-family: 'IBM Plex Sans Arabic', sans-serif;
color:gray;
}
"""
@config(css_style=css)
def app():
   put_image('https://modo3.com/thumbs/fit630x300/79144/1569315564/%D8%AA%D8%A7%D8%B1%D9%8A%D8%AE_%D8%A7%D9%84%D9%82%D8%B1%D8%A2%D9%86_%D8%A7%D9%84%D9%83%D8%B1%D9%8A%D9%85.jpg',width='900px',height='200px')
   put_html("""
       <h3 id='h3'>تطبيق القرآن الكريم</h3>
       <p id='para'>اهلاً وسهلاً بكم في موقعي الجديد للقرآن الكريم</p>
       <ul>
            <li>حافظ القران الكريم كاملا</li>
            <li>متقن لاحكام التجويد عن خبرة سبع سنوات</li>
            <li>اشتركت في العديد من المسابقات وفزت ببعض منها</li>
        </ul>
            <details id='y'>
            <summary>سورة الرحمن</summary>
            <p>سورة الرحمن بصوتي المتواضع</p>
            <audio controls>
               <source src="https://f.top4top.io/m_2961eijk51.mp3" type="audio/mp3"> 
            </audio>
             <audio controls>
               <source src="https://f.top4top.io/m_2961eijk51.mp3" type="audio/mp3"> 
            </audio>
            </details>
            <details id='y'>
            <summary>سورة يوسف</summary>
            <p>سورة يوسف بصوتي المتواضع</p>
            <audio controls>
               <source src="https://c.top4top.io/m_2937wol2p0.mp3" type="audio/mp3"> 
            </audio>
             <audio controls>
               <source src="https://c.top4top.io/m_2937wol2p0.mp3" type="audio/mp3"> 
            </audio>
            </details>
            <hr>
            <p>جميع الحقوق محفوظة للمطور @ضياء الدين رضا</p>
            """).style('direction:rtl; text-align:right;')
start_server(app , port=34345 , debug=True)