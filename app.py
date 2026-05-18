from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from SignLanguageDetector import predict
# import pyttsx3
from flask_cors import cross_origin
from gtts import gTTS
import os
import shutil
import requests

app = Flask(__name__)
# BASE = os.getcwd()
BASE = 'http://localhost:5000/'
print('BASE', BASE)

'''
def text_to_speech(text: str, id: int):
    tts = gTTS(text, lang='ar')
    filename = str(id) + 'tts.mp3'
    tts.save(filename)
    print('filename:', filename)
    # shutil.move(filename, '/static/'+filename)
    path = '/static/'+filename
    return path
'''

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/classification', methods=['GET', 'POST'])
# @cross_origin()
def classification():
    if request.method == 'POST':
        f1 = request.files['file1']
        f2 = request.files['file2']
        f1.save(secure_filename(f1.filename))
        f2.save(secure_filename(f2.filename))
        # data = predict(f1.filename)
        # print('data:', data)
        result1, accuracy1 = predict(f1.filename)
        result2, accuracy2 = predict(f2.filename)
        if result1 == 'see u later':
            result1_arabic = 'أراك لاحقا'
            # tts1_url = 'https://drive.google.com/file/d/1fCldCMq5a_CJkRE_5aAMgXoQpie82cza/view'
            tts1_url = 'https://sndup.net/8w7f/d'
        elif result1 == 'you':
            result1_arabic = 'أنت'
            # tts1_url = 'https://drive.google.com/file/d/1XVDOg9YFa1an0RQMf0eN31bF7NaKNImf/view?usp=sharing'
            tts1_url = 'https://sndup.net/7ww2/d'
        elif result1 == 'good job':
            result1_arabic = 'عمل جيد'
            # tts1_url = 'https://drive.google.com/file/d/1V-xAcLNegnJGnQwVszIQuy6n0Ak34oXx/view?usp=sharing'
            tts1_url = 'https://sndup.net/2vsg/d'
        elif result1 == 'quotation':
            result1_arabic = 'اقتباس'
            # tts1_url = 'https://drive.google.com/file/d/13qbrtQK3_DOo8OiuzlmGo5IsBT7-pv96/view?usp=sharing'
            tts1_url = 'https://sndup.net/3s3n/d'

        if result2 == 'see u later':
            result2_arabic = 'أراك لاحقا'
            tts2_url = 'https://sndup.net/8w7f/d'
        elif result2 == 'you':
            result2_arabic = 'أنت'
            tts2_url = 'https://sndup.net/7ww2/d'
        elif result2 == 'good job':
            result2_arabic = 'عمل جيد'
            tts2_url = 'https://sndup.net/2vsg/d'
        elif result2 == 'quotation':
            result2_arabic = 'اقتباس'
            tts2_url = 'https://sndup.net/3s3n/d'

        if accuracy1 < 0.8:
            result1_arabic = 'غير معروف'
            accuracy1 = 'دقة غير موثوقة'
            # tts1_url = 'https://drive.google.com/file/d/1fV7XPZG8_Igv1as7u19xzDKXswlRBd_C/view?usp=sharing'
            tts1_url = 'https://sndup.net/47hd/d'

        if accuracy2 < 0.8:
            result2_arabic = 'غير معروف'
            accuracy2 = 'دقة غير موثوقة'
            tts2_url = 'https://sndup.net/47hd/d'

        # tts1_url = text_to_speech(result1_arabic, 1)

        # tts2_url = text_to_speech(result2_arabic, 2)

        print('tts1_url', tts1_url)
        print('tts2_url', tts2_url)

        template_data = {
            'result1': result1_arabic,
            'accuracy1': accuracy1,
            'img1_url': f1.filename,
            'tts1_url': tts1_url,
            'result2': result2_arabic,
            'accuracy2': accuracy2,
            'img2_url': f2.filename,
            'tts2_url': tts2_url,

        }

    return render_template('classification.html', data=template_data)


if __name__ == '__main__':
    app.run(debug=True)
