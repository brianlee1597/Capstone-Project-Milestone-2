from sre_constants import SUCCESS
from flask import Flask
from flask import render_template
from flask import Response, request, jsonify, flash, redirect
import random
import heapq
app = Flask(__name__)

# for session
app.secret_key = 'iwashfiuhaihanjxznbviag'


multiple_choice_bank= [
    {
        'question': 'What is the red rose commonly used to express in Asia?',
        'type': 'multiple',
        'choice': ['Funerals and Sympathy', 'Anniversaries and Love', 'Graduations', 'Families'],
        'answer': '1',
        'img':'https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Small_Red_Rose.JPG/1200px-Small_Red_Rose.JPG',
        'hint_flower': 'Red Rose',
        'hint_content_1': 'Love and Anniversaries',
        'hint_content_2': 'Like in most cultures, red roses represent love and anniversaries in Asia.'
    },
    {
        'question': 'What emotion is the sunflower commonly used to express in Asia?',
        'type': 'multiple',
        'choice': ['Adoration', 'Sorrow', 'Joy', 'Friendship'],
        'answer': '0',
        'img':'https://hosstools.com/wp-content/uploads/2020/10/black-oil-sunflower.jpg',
        'hint_flower': 'Sunflower',
        'hint_content_1': 'Adoration and loyalty',
        'hint_content_2': ' The yellow color in Japan is associated with the end of summer, personifying the life-giving forces of the elements.'
    },
    {
        'question': 'Which culture tends to gift lilies, roses, chrysanthenum, and cornflowers for weddings?',
        'type': 'multiple',
        'choice': ['USA', 'China', 'Ghana', 'Egypt'],
        'answer': '3',
        'img': 'https://s3.envato.com/files/bd4e7c6c-f8b4-470c-af36-6d3bae5d4d6a/inline_image_preview.jpg',
        'hint_flower': 'Egypt',
        'hint_content_1': 'African cultures have their own symbolic relationship to flowers.',
        'hint_content_2': 'In Egypt, gifts of lilies, roses, chrysanthemum, and cornflowers are common at weddings.'
    },
    {
        'question': 'What does the Peony symbolize in Asia?',
        'type': 'multiple',
        'choice': ['Honor and Good Fortune', 'Financial Success', 'Love and Passion', 'Luxury and Beauty'],
        'answer': '0',
        'img':'https://asianinspirations.com.au/wp-content/uploads/2021/09/Language-of-Flowers-04-Peonies.jpg',
        'hint_flower': 'Peony',
        'hint_content_1': 'Peonies show honor and good fortune for elders.',
        'hint_content_2': ' It stands as a symbol of spring, female beauty and, not very originally, reproduction. It is also associated with wealth, honour and high social class.'
    },
    {
        'question': 'Which culture values daffodils as a symbol of rebirth?',
        'type': 'multiple',
        'choice': ['China', 'Mexico', 'France', 'Ghana'],
        'answer': '3',
        'img':'https://www.almanac.com/sites/default/files/styles/large/public/image_nodes/daffodil.jpg?itok=K-j38VoY',
        'hint_flower': 'Daffodil',
        'hint_content_1': 'Rebirth and are great for those making a life change',
        'hint_content_2': 's. They are a great gift for newlyweds who are making a big change -- from moving into a new place or living in a new city to starting a family'
    },
    {
        'question': 'What does the lotus flower symbolize in Western cultures?',
        'type': 'multiple',
        'choice': ['Rebirth', 'Patience', 'Purity', 'Beauty'],
        'answer': '2',
        'img':'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/gettyimages-590634523-2-1493049119.jpg?crop=1.00xw:0.753xh;0,0.0685xh&resize=480:*',
        'hint_flower': 'Lotus',
        'hint_content_1': 'Purity, Holiness, Divinity',
        'hint_content_2': 'Lotus is associated with holy mother Mary. According to Christian beliefs, it represents purity, holiness, divinity, and fertility.'
    },
    {
        'question': 'In which cultures is it unlucky to gift an odd number of flowers?',
        'type': 'multiple',
        'choice': ['Europe', 'Asia', 'North America', 'Africa'],
        'answer': '0',
        'img': 'https://qa-static.mywedding.com/wp-content/uploads/migrated/blog/524155954.jpg',
        'hint_flower': 'Europe',
        'hint_content_1': '',
        'hint_content_2': 'In Europe generally, it is unlucky to gift an odd number of flowers.'
    },
    {
        'question': 'For which country is flower-giving a common gift for people of all ages?',
        'type': 'multiple',
        'choice': ['France', 'China', 'USA', 'Egypt'],
        'answer': '2',
        'img':'https://hosstools.com/wp-content/uploads/2020/10/black-oil-sunflower.jpg',
        'hint_flower': 'North America',
        'hint_content_1': '',
        'hint_content_2': ' In the USA, gifting flowers is considered a common gift for all ages. The largest flower gifting day in teh USA is Valentine’s Day.'
    },
    {
        'question': 'What does the orchid mean in China?',
        'type': 'multiple',
        'choice': ['Love', 'Sorrow', 'Joy', 'Friendship'],
        'answer': '3',
        'img':'https://www.ftd.com/blog/wp-content/uploads/2018/10/caring-for-orchids-hero.jpg',
        'hint_flower': 'Orchid',
        'hint_content_1': 'Scholarly pursuits, integrity and friendship',
        'hint_content_2': ' Orchids are associated with the ancient Chinese philosopher Confucius who likened the orchid to an honourable man.'

    },
    {
        'question': 'In which country is the chrysanthemum used for funerals?',
        'type': 'multiple',
        'choice': ['Belgium', 'UK', 'Germany', 'France'],
        'answer': '0',
        'img':'https://s3.envato.com/files/bd4e7c6c-f8b4-470c-af36-6d3bae5d4d6a/inline_image_preview.jpg',
        'hint_flower': 'Chrysanthemum',
        'hint_content_1': '',
        'hint_content_2': 'In Belgium, chrysanthemum are gifted for funerals.'
    },

]


dragdrop_bank = [
    {
        'question': 'Can you drag and drop flowers to their meanings in North America?',
        'type': 'dragdrop',
        'choice': ['Red Rose', 'Sunflowers', 'Orchid'],
        'answer': ['Love', 'Adoration', 'Luxury and Beauty'],
        'img':'https://hosstools.com/wp-content/uploads/2020/10/black-oil-sunflower.jpg'
    },
    {
        'question': 'Can you drag and drop flowers to their meanings in Asia?',
        'type': 'dragdrop',
        'choice': ['Orchid','Peony', 'Sunflowers'],
        'answer': ['Prosperity','Good Fortune', 'Adoration'],
        'img':'https://asianinspirations.com.au/wp-content/uploads/2021/09/Language-of-Flowers-04-Peonies.jpg'
    },
    {
        'question': 'Can you drag and drop flowers to their meanings in Africa?',
        'type': 'dragdrop',
        'choice': ['Daffodil','Lotus', 'Sunflowers'],
        'answer': ['Rebirth and Change','Rebirth and Death', 'Loyalty and Longevity'],
        'img':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRbapEe_TzDZu8gePTc4IElapjL01Ks51ZL3Q&usqp=CAU'
    },
    {
        'question': 'Can you drag and drop flowers to their meanings in Europe?',
        'type': 'dragdrop',
        'choice': ['Red Carnation','Red Flowers', 'Lilac'],
        'answer': ['Ill Will','Love', 'Deep feelings']
    },
    {
        'question': 'Can you drag and drop flowers to their meanings in Europe?',
        'type': 'dragdrop',
        'choice': ['Lotus','Red Flowers', 'Lilac'],
        'answer': ['Divinity','Love', 'Deep feelings'],
        'img':'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/gettyimages-590634523-2-1493049119.jpg?crop=1.00xw:0.753xh;0,0.0685xh&resize=480:*',
    },
    {
        'question': 'For each flower, can you drag and drop each meaning to the culture it originates from?',
        'type': 'dragdrop',
        'choice': ['Daffodil - Rebirth','Lilac - Deep Feelings', 'Orchid - Luxury and Beauty'],
        'answer': ['Ghana','France', 'USA'],
        'img':'https://www.almanac.com/sites/default/files/styles/large/public/image_nodes/daffodil.jpg?itok=K-j38VoY'
    },
    {
        'question': 'For each flower, can you drag and drop each meaning to the culture it originates from?',
        'type': 'dragdrop',
        'choice': ['Peony - Good Fortune','Lotus - Rebirth and death', 'Red Rose - Love'],
        'answer': ['China','Egypt', 'Mexio'],
        'img':'https://asianinspirations.com.au/wp-content/uploads/2021/09/Language-of-Flowers-04-Peonies.jpg'
    },
    {
        'question': 'For each flower, can you drag and drop each meaning to the culture it originates from?',
        'type': 'dragdrop',
        'choice': ['Sunflower - Loyalty and Longevity','Sunflower - Adoration and loyalty', 'Orchid - Prosperity'],
        'answer': ['Ghana','USA/Japan', 'Japan/China'],
        'img':'https://www.ftd.com/blog/wp-content/uploads/2018/10/caring-for-orchids-hero.jpg'
    },
]
questions = []
# get feedback on how data should be formatted best
learn_bank = [
    {
        'about': 'The rose in X Y Z culture signifies X Y Z respectively',
        'image': 'link to image',
    }
]

culture_bank = {
    1:{
        'id':'1',
        'culture':'Asia',
        'intro':'Asian culture, Chinese specifically, is filled with symbolism. Flowers can have many important meanings and implications. For example, red roses, like in most cultures represent love (and anniversaries). Flowers are popular gifts and the most popular for teachers. Peonies are often gifted at weddings, and carnations at funerals (which signify respect and gratitude).',
        'img1':'https://www.ftd.com/blog/wp-content/uploads/2018/10/caring-for-orchids-hero.jpg',
        'flower1':'Orchid',
        'meanings1':'Wealth & pursuits AND integrity & friendship',
        'origins1':'Japan AND China',
        'img2':'https://asianinspirations.com.au/wp-content/uploads/2021/09/Language-of-Flowers-04-Peonies.jpg',
        'flower2':'Peony',
        'meanings2':'For elders to show honor and good fortune',
        'origins2':'China',
        'img3':'https://hosstools.com/wp-content/uploads/2020/10/black-oil-sunflower.jpg',
        'flower3':'Sunflower',
        'meanings3':'Adoration and loyalty',
        'origins3':'Japan'
    },
    2:{
        'id':'2',
        'culture':'Africa',
        'intro':'Research is showing that precolonial African cultures absolutely did have their own symbolic relationship to flowers. For example, research reveals that a coded language of flowers largely influenced the precolonial Bunyoro in western Uganda. Flowers were used as decoration, perfume, and symbol. In Egypt, gifts of lilies, roses, chrysanthemum, and cornflowers are common at weddings. The only other time flowers are gifted in Egypt is during funerals. In South Africa, flowers are extensively exchanged during Christmas.',
        'img1':'https://www.almanac.com/sites/default/files/styles/large/public/image_nodes/daffodil.jpg?itok=K-j38VoY',
        'flower1':'Daffodil',
        'meanings1':'Rebirth and are great for those making a life change',
        'origins1':'Ghana',
        'img2':'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/gettyimages-590634523-2-1493049119.jpg?crop=1.00xw:0.753xh;0,0.0685xh&resize=480:*',
        'flower2':'Lotus',
        'meanings2':'Rebirth, sun and death',
        'origins2':'Egypt',
        'img3':'https://hosstools.com/wp-content/uploads/2020/10/black-oil-sunflower.jpg',
        'flower3':'Sunflower',
        'meanings3':'Loyalty and longevity',
        'origins3':'Ghana'
    },
    3:{
        'id':'3',
        'culture':'Europe',
        'intro':'Early Roman brides carried flowers, which they believed would not only ward off evil spirits but ensure fertility as well. A Dutch saying says that food feeds the body, but flowers feed the soul. In England, the guests bring flowers, when invited to our home. But white lilies should be avoided as they signify death. In Belgium, chrysanthemum are gifted for funerals. And in Europe generally, it is unlucky to gift an odd number of flowers. ',
        'img1':'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/gettyimages-590634523-2-1493049119.jpg?crop=1.00xw:0.753xh;0,0.0685xh&resize=480:*',
        'flower1':'Lotus',
        'meanings1':'Purity, Holiness, Divinity',
        'origins1':'France',
        'img2':'https://cdn.atwilltech.com/flowerdatabase/c/crimson-perfection-floral-arrangement.425.jpg',
        'flower2':'Red flowers',
        'meanings2':'Symbol of love and can be given to family or loved ones',
        'origins2':'Russia',
        'img3':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRbapEe_TzDZu8gePTc4IElapjL01Ks51ZL3Q&usqp=CAU',
        'flower3':'Lilac',
        'meanings3':'Delicacy, deep feelings, shyness',
        'origins3':'France'
    },
    4:{
        'id':'4',
        'culture':'North America',
        'intro':'Whether it is confessing your love to someone, sending condolences, showing gratitude or welcoming a new person, flowers say it beautifully; and for this reason they have been an indispensable part of American gifting culture. In the USA, gifting flowers is considered a common gift for all ages. The largest flower gifting day in teh USA is Valentine’s Day. In Mexico, the symbolic meaning of flowers is prominent throughout ancient Mesoamerican thought and practice. Flowers could represent anything from beauty and creation to death and destruction.', 
        'img1':'https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Small_Red_Rose.JPG/1200px-Small_Red_Rose.JPG',
        'flower1':'Red rose',
        'meanings1':'Love and fidelity',
        'origins1':'Mexico',
        'img2':'https://www.ftd.com/blog/wp-content/uploads/2018/10/caring-for-orchids-hero.jpg',
        'flower2':'Orchid',
        'meanings2':'Luxury and beauty',
        'origins2':'Mexico',
        'img3':'https://hosstools.com/wp-content/uploads/2020/10/black-oil-sunflower.jpg',
        'flower3':'Sunflower',
        'meanings3':'Adoration and loyalty',
        'origins3':'USA'
    }
}

detail_bank = {
    1:{
        'id':'1',
        'culture_id':'1',
        'img':'https://www.ftd.com/blog/wp-content/uploads/2018/10/caring-for-orchids-hero.jpg',
        'flowername':'Orchid',
        'meanorigin':'For Japan: Orchid symbolism comes from Buddhism. It is a plant that grows in the stinking mud of swamps and still gives a pure white color, so it symbolizes the transition from evil to good. It was also customary to give this exotic flower to the one to whom you felt great affection, since the orchid symbolizes love. And in ancient Japan, it was a symbol of wealth; For China: Orchids symbolize scholarly pursuits, integrity and friendship and, just for a change, nobility. They are a staple of decorative wall pieces and are found all through Chinese artwork. Orchids are associated with the ancient Chinese philosopher Confucius who likened the orchid to an honourable man. You’ll also find them in religious and wedding ceremonies and decorating homes.',
        'colors':'Red, pink, white, blue, green, purple, orange, and yellow.'
    },
    2:{
        'id':'2',
        'culture_id':'1',
        'img':'https://asianinspirations.com.au/wp-content/uploads/2021/09/Language-of-Flowers-04-Peonies.jpg',
        'flowername':'Peony',
        'meanorigin':'The peony is the unofficial national flower of China. It stands as a symbol of spring, female beauty and, not very originally, reproduction. It is also associated with wealth, honour and high social class. Peonies are also the flower used to celebrate a couples 12th wedding anniversary. Peonies from Luoyang are considered the best in the country and are showcased in a festival held in Luoyang in April or May of each year.',
        'colors':'Pink, red, orange, yellow, and white'
    },
    3:{
        'id':'3',
        'culture_id':'1',
        'img':'https://hosstools.com/wp-content/uploads/2020/10/black-oil-sunflower.jpg',
        'flowername':'Sunflower',
        'meanorigin':'The Japanese name for this flower is Himawari. The yellow color in Japan is associated with the end of summer, personifying the life-giving forces of the elements. It also embodies the idea of poise, and order. Yellow flowers are given to wish good and prosperity. The number of sunflowers gifted can have different meanings - 3 is a declaration of love, 7 is a secret love, 11 is a true love, and 180 means marry me',
        'colors':'Golden yellow, orange, and ruby red, to bronze and even white'
    },
    4:{
        'id':'1',
        'culture_id':'2',
        'img':'https://www.almanac.com/sites/default/files/styles/large/public/image_nodes/daffodil.jpg?itok=K-j38VoY',
        'flowername':'Daffodil',
        'meanorigin':'Daffodils signify rebirth and new beginnings. They are a great gift for newlyweds who are making a big change -- from moving into a new place or living in a new city to starting a family',
        'colors':'White, pink and orange, with or without yellow, in intense and pastel shades'
    },
    5:{
        'id':'2',
        'culture_id':'2',
        'img':'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/gettyimages-590634523-2-1493049119.jpg?crop=1.00xw:0.753xh;0,0.0685xh&resize=480:*',
        'flowername':'Lotus',
        'meanorigin':'In ancient Egypt, the lotus represented rebirth. This meaning was inspired by the nature of the lotus petals that spread above water upon sensing sunlight and closed during the night so as for the flower to fall back under water',
        'colors':'White, pink, red, blue, purple'
    },
    6:{
        'id':'3',
        'culture_id':'2',
        'img':'https://hosstools.com/wp-content/uploads/2020/10/black-oil-sunflower.jpg',
        'flowername':'Sunflower',
        'meanorigin':'Sunflowers mean loyalty and longevity',
        'colors':'Golden yellow, orange, and ruby red, to bronze and even white'
    },
    7:{
        'id':'1',
        'culture_id':'3',
        'img':'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/gettyimages-590634523-2-1493049119.jpg?crop=1.00xw:0.753xh;0,0.0685xh&resize=480:*',
        'flowername':'Lotus',
        'meanorigin':'Christians replace the lotus flower with the sacred white-water Lily. This flower is associated with holy mother Mary. According to Christian beliefs, it represents purity, holiness, divinity, and fertility',
        'colors':'White, pink, red, blue, purple'
    },
    8:{
        'id':'2',
        'culture_id':'3',
        'img':'https://cdn.atwilltech.com/flowerdatabase/c/crimson-perfection-floral-arrangement.425.jpg',
        'flowername':'Red flowers',
        'meanorigin':'Red flowers are a symbol of love and can be given to family or loved ones',
        'colors':'Red'
    },
    9:{
        'id':'3',
        'culture_id':'3',
        'img':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRbapEe_TzDZu8gePTc4IElapjL01Ks51ZL3Q&usqp=CAU',
        'flowername':'Lilac',
        'meanorigin':'Delicacy, deep feelings, shyness. In France, the lilac flower is seen as a symbol of innocence. This is because the color of the lilac flower is often associated with purity and innocence. The lilac flower is also seen as a symbol of hope. This is because the lilac flower is known to bloom even in the coldest winters.',
        'colors':'Purple to lilac, but some cultivars can be magenta, pink, or white'
    },
    10:{
        'id':'1',
        'culture_id':'4',
        'img':'https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Small_Red_Rose.JPG/1200px-Small_Red_Rose.JPG',
        'flowername':'Red rose',
        'meanorigin':'Mexicans are passionate about expressing love and fidelity, and the Red Rose is a symbol of both these powerful emotions',
        'colors':'Red'
    },
    11:{
        'id':'2',
        'culture_id':'4',
        'img':'https://www.ftd.com/blog/wp-content/uploads/2018/10/caring-for-orchids-hero.jpg',
        'flowername':'Orchid',
        'meanorigin':'Orchids are very sturdy and many people welcome them into their homes as table centerpieces. This stunning Mexican orchid usually has pale shades of pink blossoms. It symbolizes luxury and beauty',
        'colors':'Red, pink, white, blue, green, purple, orange, and yellow'
    },
    12:{
        'id':'3',
        'culture_id':'4',
        'img':'https://hosstools.com/wp-content/uploads/2020/10/black-oil-sunflower.jpg',
        'flowername':'Sunflower',
        'meanorigin':'Sunflower meanings include happiness, optimism, honesty, longevity, peace, admiration, and devotion. The sunflower possibly surpasses all others in terms of its universal power to bring joy to people and symbolizes adoration and loyalty',
        'colors':'Golden yellow, orange, and ruby red, to bronze and even white'
    }
}

scores = []
session = dict()

# menu and culture page
@app.route('/')
def index():
    return render_template('welcome.html')

@app.route('/culture/<culture_key>')
def culture(culture_key=0):
    return render_template('culture.html', culture_bank = culture_bank, key = str(culture_key) ) 
 
@app.route('/detail/<detail_key>')
def detail(detail_key=0):
    return render_template('details.html', detail_bank = detail_bank, key = str(detail_key) ) 
 

# this route is to be used for when users click on quiz
# generates a diff order for the questions
# page to display the question bank
@app.route('/quiz/all')
def quiz_questions():
    global questions
    if 'user_score' not in session:
        session['user_score']=0
    if not questions:
        questions = randomizeQuestions()
        print(questions)
    if 'answered' not in session:
        session['answered'] = []

    if  'saved_answers' not in session:
        session['saved_answers'] = dict()
    return render_template('quiz_questions.html', questions=questions, score=session['user_score'], 
                            answered=session['answered'], saved_answers=session['saved_answers'])

@app.route('/quiz/new')
def new_quiz_questions():
    global questions
    session['user_score']=0
    questions = randomizeQuestions()
    session['answered'] = []
    session['saved_answers'] = dict()
    print("new quiz")
    return render_template('quiz_questions.html', questions=questions, score=session['user_score'], 
                            answered=session['answered'], saved_answers=session['saved_answers'])


@app.route('/quiz/<quiz_id>')
def quiz_question(quiz_id):

    question = questions[int(quiz_id)-1]
    #print(question)

    q_type = question['type']
    print(session)
    if q_type == 'multiple':
        return render_template('choice.html', question=question,score=session['user_score'],quiz_id=int(quiz_id),answered=session['answered'], saved_answers=session['saved_answers'])
    elif q_type == 'dragdrop':
        return render_template('dragdrop.html', question=question,score=session['user_score'],quiz_id=int(quiz_id),answered=session['answered'], saved_answers=session['saved_answers'])




@app.route('/score')
def score():
    current_score = 0
    global questions
    if 'user_score' in session:
        current_score = session['user_score']
        scores.append(current_score)
        print('scores: ' + str(scores))
        session.pop('user_score', None) # delete visits
    if 'answered' in session:
        session.pop('answered')
    if 'answer_data' in session:
        session.pop('answer_data')
    top_scores = []
    questions = []
    if len(scores) < 5:
        top_scores = heapq.nlargest(len(scores), scores)
    else:
        top_scores = heapq.nlargest(5,scores)
    return render_template('score.html', current_score=current_score, top_scores=top_scores)


@app.route('/update_score', methods=['POST'])
def update_score():
    correct = request.get_json()['correct']
    plus = request.get_json()['plus']
    minus = request.get_json()['minus']
    
    answer = request.get_json()['answer']
    quiz_id = request.get_json()['quiz_id']
    if quiz_id not in session['answered']:
        session['answered'].append(quiz_id)
    if quiz_id not in session['saved_answers'].keys():
        session['saved_answers'][quiz_id] = ""
    session['saved_answers'][quiz_id] += answer

    if correct: 
        session['user_score'] = session['user_score']+plus
    else:
        session['user_score'] = session['user_score']-minus
    print(session)
    return jsonify(session['user_score'])

@app.route('/update_answered', methods=['POST'])
def update_answered_next():
    print("updating questions answered")
    quiz_id  = request.get_json()['quiz_id']
    if quiz_id not in session['answered']:
        answered = session['answered']
        answered.append(quiz_id)
        session['answered'] = answered
    print(session['answered'])
    return jsonify(session['answered'])

@app.route('/update_answered/<from_id>_<to_id>')
def update_answered_nav(from_id, to_id):
    print("question nav link clicked")
    if int(from_id) not in session['answered']:
        answered = session['answered']
        answered.append(int(from_id))
        session['answered'] = answered
    print(session['answered'])
    return redirect('/quiz/' + str(to_id))

# randomize order of the questions 
def randomizeQuestions():
    new_quiz_questions = []
    random.shuffle(multiple_choice_bank)
    random.shuffle(dragdrop_bank)
    # consistent number of multiple choice and drag and drop questions
    for i in range(6):
        curr_question = multiple_choice_bank[i]
        new_quiz_questions.append(curr_question)
    for i in range(4):
        curr_question = dragdrop_bank[i]
        new_quiz_questions.append(curr_question)
    random.shuffle(new_quiz_questions)
    for i in range(len(new_quiz_questions)):
        new_quiz_questions[i]['id'] = str(i+1)
        new_quiz_questions[i]['next_question'] = i+2
    return new_quiz_questions


if __name__ == '__main__':
   app.run(debug = True)




