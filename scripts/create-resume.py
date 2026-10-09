from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
pdfmetrics.registerFont(TTFont('DejaVu','/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DejaVuBold','/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))
pdfmetrics.registerFontFamily('DejaVu',normal='DejaVu',bold='DejaVuBold')
s=getSampleStyleSheet()
for name in ['Normal','Heading2','Title']:s[name].fontName='DejaVu'
s['Normal'].fontSize=9;s['Normal'].leading=13;s['Heading2'].fontSize=12;s['Heading2'].leading=16;s['Heading2'].textColor=HexColor('#23543c');s['Heading2'].spaceBefore=13;s['Title'].fontSize=23;s['Title'].leading=30;s['Title'].alignment=0;s['Title'].textColor=HexColor('#23543c')
a=[]
def p(t,style='Normal'):a.append(Paragraph(t,s[style]))
p('Vijay Krishna P J','Title');p('Freelance Web Developer | Kerala, India | Remote worldwide');p('vijayishnapj5@gmail.com'.replace('vijayishnapj5','vijaykrishnapj5')+' | +91-8921330633');p('github.com/vijaykrishnapj5-source');p('linkedin.com/in/vijay-krishna-p-j-5a3a68258')
p('Profile','Heading2');p('B.Tech CSE graduate with a foundation in full-stack development, machine learning and data science. Builds responsive websites and data-driven web apps for small businesses using React, Node.js, PHP and MySQL. Foundational knowledge of AWS.')
p('Technical skills','Heading2');p('<b>Web:</b> HTML, CSS, JavaScript, React, Tailwind CSS, Node.js, PHP, REST APIs<br/><b>Database:</b> MySQL, SQL<br/><b>Cloud / tools:</b> AWS (S3, EC2, Lambda, IAM, API Gateway), Git, VS Code<br/><b>Data / ML:</b> Python, Scikit-learn, TensorFlow, Apache Spark, Matplotlib, Jupyter')
p('Experience','Heading2');p('<b>IBM Edunet - Web Development Intern | June-July 2024</b>');p('Built a responsive student portfolio web app using HTML, CSS and JavaScript for 200+ students. Ensured compatibility across 5+ screen sizes and browsers with zero reported layout issues.')
p('Selected projects','Heading2');p('<b>Inventory Management System</b> | React, Tailwind CSS, PHP, MySQL');p('Product categorization, order management, stock updates and automated low-stock alerts.');a.append(Spacer(1,7));p('<b>Hybrid Acoustic Anomaly Detection for Predictive Maintenance</b>');p('Ensemble of Deep SAD, Autoencoders, LOF, Isolation Forest and One-Class SVM on 111 acoustic features from MIMII and ToyADMOS. ROC-AUC up to 0.958. Python, TensorFlow, Scikit-learn and Librosa.');a.append(Spacer(1,7));p('<b>Telecom Customer Churn Prediction (Big Data)</b>');p('Apache Spark pipeline with a GBT model achieving AUC 0.8561 in evaluation.')
p('Education','Heading2');p('<b>B.Tech CSE, SRM University</b> | 2022-2026 | CGPA: 7.3')
p('Certifications','Heading2');p('NPTEL - The Joy of Computing using Python<br/>AWS Cloud Technical Essentials')
SimpleDocTemplate('public/resume.pdf',rightMargin=45,leftMargin=45,topMargin=38,bottomMargin=38,title='Vijay Krishna P J - Resume',author='Vijay Krishna P J').build(a)
