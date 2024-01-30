from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///avto.db'

db = SQLAlchemy(app)


class Header(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    header = db.Column(db.Text, nullable=False)


class Subtitle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subtitle = db.Column(db.Text, nullable=False)


class About(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    about = db.Column(db.Text, nullable=False)


# Ниже реквизиты организации
class Inn(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    inn = db.Column(db.Text, nullable=False)


class Kpp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kpp = db.Column(db.Text, nullable=False)


class Ogrn(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ogrn = db.Column(db.Text, nullable=False)


class Bik(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bik = db.Column(db.Text, nullable=False)


class Ks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ks = db.Column(db.Text, nullable=False)


class Pc(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pc = db.Column(db.Text, nullable=False)


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.Text, nullable=False)


class Work(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    work = db.Column(db.Text, nullable=False)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<Article %r>' % self.id



@app.route('/admin')
def admin():
    header_entry = Header.query.first()
    header_value = header_entry.header if header_entry else "Default Header"  # Use a default value if no header entry is found
    subtitle_entry = Subtitle.query.first()
    subtitle_value = subtitle_entry.subtitle if subtitle_entry else "Default Subtitle"
    about_entry = About.query.first()
    about_value = about_entry.about if about_entry else "Default About"
    #  Ниже Реквизиты
    inn_entry = Inn.query.first()
    inn_value = inn_entry.inn if inn_entry else "Default INN"
    kpp_entry = Kpp.query.first()
    kpp_value = kpp_entry.kpp if kpp_entry else "Default KPP"
    ogrn_entry = Ogrn.query.first()
    ogrn_value = ogrn_entry.ogrn if ogrn_entry else "Default OGRN"
    bik_entry = Bik.query.first()
    bik_value = bik_entry.bik if bik_entry else "Default BIK"
    ks_entry = Ks.query.first()
    ks_value = ks_entry.ks if ks_entry else "Default KS"
    pc_entry = Pc.query.first()
    pc_value = pc_entry.pc if pc_entry else "Default PC"
    address_entry = Address.query.first()
    address_value = address_entry.address if address_entry else "Default ADDRESS"

    return render_template('admin.html', header=header_value, subtitle=subtitle_value, about=about_value, inn=inn_value, kpp=kpp_value, ogrn=ogrn_value, bik=bik_value, ks=ks_value, pc=pc_value, address=address_value)


@app.route('/index')
@app.route('/')
def index():
    header_entry = Header.query.first()
    header_value = header_entry.header if header_entry else "Default Header"  # Use a default value if no header entry is found
    subtitle_entry = Subtitle.query.first()
    subtitle_value = subtitle_entry.subtitle if subtitle_entry else "Default Subtitle"
    about_entry = About.query.first()
    about_value = about_entry.about if about_entry else "Default About"
    #  Ниже Реквизиты
    inn_entry = Inn.query.first()
    inn_value = inn_entry.inn if inn_entry else "Default INN"
    kpp_entry = Kpp.query.first()
    kpp_value = kpp_entry.kpp if kpp_entry else "Default KPP"
    ogrn_entry = Ogrn.query.first()
    ogrn_value = ogrn_entry.ogrn if ogrn_entry else "Default OGRN"
    bik_entry = Bik.query.first()
    bik_value = bik_entry.bik if bik_entry else "Default BIK"
    ks_entry = Ks.query.first()
    ks_value = ks_entry.ks if ks_entry else "Default KS"
    pc_entry = Pc.query.first()
    pc_value = pc_entry.pc if pc_entry else "Default PC"
    address_entry = Address.query.first()
    address_value = address_entry.address if address_entry else "Default ADDRESS"
    articles = Article.query.all()
    return render_template('index.html', header=header_value, subtitle=subtitle_value, about=about_value, inn=inn_value, kpp=kpp_value, ogrn=ogrn_value, bik=bik_value, ks=ks_value, pc=pc_value, address=address_value, articles=articles)


@app.route('/update_header', methods=['POST'])
def update_header():
    new_header = request.form['header']
    header_entry = Header.query.first()  # Предполагая, что в базе данных существует только одна запись с заголовком
    if header_entry:
        header_entry.header = new_header
    else:
        header_entry = Header(header=new_header)
        db.session.add(header_entry)
    db.session.commit()
    return redirect(url_for('admin'))


@app.route('/update_subtitle', methods=['POST'])
def update_subtitle():
    new_subtitle = request.form['subtitle']
    subtitle_entry = Subtitle.query.first()  # Предполагая, что в базе данных существует только одна запись с подзаголовком
    if subtitle_entry:
        subtitle_entry.subtitle = new_subtitle
    else:
        subtitle_entry = Subtitle(subtitle=new_subtitle)
        db.session.add(subtitle_entry)
    db.session.commit()
    return redirect(url_for('admin'))


@app.route('/update_about', methods=['POST'])
def update_about():
    new_about = request.form['about']
    about_entry = About.query.first()  # Предполагая, что в базе данных существует только одна запись с заголовком
    if about_entry:
        about_entry.about = new_about
    else:
        about_entry = About(about=new_about)
        db.session.add(about_entry)
    db.session.commit()
    return redirect(url_for('admin'))


@app.route('/update_inn', methods=['POST'])
def update_inn():
    new_inn = request.form['inn']
    inn_entry = Inn.query.first()  # Предполагая, что в базе данных существует только одна запись с заголовком
    if inn_entry:
        inn_entry.inn = new_inn
    else:
        inn_entry = Inn(inn=new_inn)
        db.session.add(inn_entry)
    db.session.commit()
    return redirect(url_for('admin'))


@app.route('/update_kpp', methods=['POST'])
def update_kpp():
    new_kpp = request.form['kpp']
    kpp_entry = Kpp.query.first()  # Предполагая, что в базе данных существует только одна запись с заголовком
    if kpp_entry:
        kpp_entry.kpp = new_kpp
    else:
        kpp_entry = Kpp(kpp=new_kpp)
        db.session.add(kpp_entry)
    db.session.commit()
    return redirect(url_for('admin'))


@app.route('/update_ogrn', methods=['POST'])
def update_ogrn():
    new_ogrn = request.form['ogrn']
    ogrn_entry = Ogrn.query.first()  # Предполагая, что в базе данных существует только одна запись с заголовком
    if ogrn_entry:
        ogrn_entry.ogrn = new_ogrn
    else:
        ogrn_entry = Ogrn(ogrn=new_ogrn)
        db.session.add(ogrn_entry)
    db.session.commit()
    return redirect(url_for('admin'))


@app.route('/update_bik', methods=['POST'])
def update_bik():
    new_bik = request.form['bik']
    bik_entry = Bik.query.first()  # Предполагая, что в базе данных существует только одна запись с заголовком
    if bik_entry:
        bik_entry.ogrn = new_bik
    else:
        bik_entry = Bik(bik=new_bik)
        db.session.add(bik_entry)
    db.session.commit()
    return redirect(url_for('admin'))


@app.route('/update_ks', methods=['POST'])
def update_ks():
    new_ks = request.form['ks']
    ks_entry = Ks.query.first()  # Предполагая, что в базе данных существует только одна запись с заголовком
    if ks_entry:
        ks_entry.ks = new_ks
    else:
        ks_entry = Ks(ks=new_ks)
        db.session.add(ks_entry)
    db.session.commit()
    return redirect(url_for('admin'))


@app.route('/update_pc', methods=['POST'])
def update_pc():
    new_pc = request.form['pc']
    pc_entry = Pc.query.first()  # Предполагая, что в базе данных существует только одна запись с заголовком
    if pc_entry:
        pc_entry.pc = new_pc
    else:
        pc_entry = Pc(pc=new_pc)
        db.session.add(pc_entry)
    db.session.commit()
    return redirect(url_for('admin'))


@app.route('/update_address', methods=['POST'])
def update_address():
    new_address = request.form['address']
    address_entry = Address.query.first()  
    if address_entry:
        address_entry.address = new_address
    else:
        address_entry = Address(address=new_address)
        db.session.add(address_entry)
    db.session.commit()
    return redirect(url_for('admin'))



@app.route('/create-article', methods=['POST', 'GET'])
def create_article():
    if request.method == 'POST':
        text = request.form['text']

        article = Article(text=text)

        try:
            db.session.add(article)
            db.session.commit()
            return redirect('posts')
        except:
            return "Произошла ошибка"
    else:
        return render_template('create-article.html')
    

@app.route('/posts')
def posts():
    articles = Article.query.all()
    return render_template('posts.html', articles=articles)



@app.route('/posts/<int:id>/del')
def posts_delete(id):
    article = Article.query.get_or_404(id)

    try:
        db.session.delete(article)
        db.session.commit()
        return redirect('/posts')
    except:
        return "При удалении услуги произошла ошибка"
    

@app.route('/posts/<int:id>/update', methods=['POST', 'GET'])
def posts_update(id):
    article = Article.query.get(id)
    if request.method == "POST":
        article.text = request.form['text']

        try:
            db.session.commit()
            return redirect('/posts')
        except:
            return "При редактировании услуги произошла ошибка"
    else:
        return render_template('post_update.html', article=article)



if __name__ == '__main__':
    app.run(debug=True)
