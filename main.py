# 数据
import data
# 画图
from fitsplot import plot
# 表单 Flask-WTF
from wtforms.validators import DataRequired
from wtforms import SelectField, SubmitField
from flask_wtf import FlaskForm
from flask import Flask, render_template, url_for
# UI
from flask_bootstrap import Bootstrap

# 初始化, 创建应用实例（Flask类的对象）, 配置密钥
app = Flask(__name__)
app.config['SECRET_KEY'] = 'zxcvbnm'
bootstrap = Bootstrap(app)

contra = '0'
contrast_list = {'-2': [-0.5, 150], '-1': [-0.5, 60],
                 '0': [-0.3, 10], '1': [-0.2, 1.5], '2': [-0.1, 0.5]}


class Form(FlaskForm):
    # 设置图像对比度
    contrast = SelectField('Contrast',
                           choices=[('-2', '-2'), ('-1', '-1'),
                                    ('0', '0'), ('1', '1'), ('2', '2')],
                           render_kw={'style': 'width:120px;'},
                           default='0')
    # 提交按钮
    submit = SubmitField('Submit')

# welcome


@app.route('/', methods=['GET', 'POST'])
def welcome():
    return render_template('welcome.html')

# bands.html


@app.route('/<name>', methods=['GET', 'POST'])
def bands(name):

    global contra, contrast_list
    contrast = contra
    form = Form()
    if form.validate_on_submit():
        contrast = form.contrast.data
        contra = contrast
    k = int(name)
    # g,r,i 画三个波段图像
    fig_g = plot(k, 1, contrast_list[contrast], con=0)
    fig_r = plot(k, 2, contrast_list[contrast], con=0)
    fig_i = plot(k, 3, contrast_list[contrast], con=0)
    #fig_c = RGB(k, contra)
    return render_template('bands.html',
                           form=form,
                           k=k,
                           contra=contra,
                           info=data.galinfo(k-1),
                           fig1=fig_g, fig2=fig_r, fig3=fig_i,  # fig4=fig_c,
                           Num=2                    # 图像总数
                           )


@app.route('/<name>/last_choice:<val>', methods=['GET', 'POST'])
def judge(name, val):
    k = int(name)
    v = val
    data.classify(k-1, val)
    return bands(name)


@app.route('/stat/stat')
def stat():
    form = FlaskForm()
    return render_template('stat.html',
                           form=form,
                           stat=data.stat(),
                           )


@app.route('/stat/stat/<val>')
def LIST(val):
    form = FlaskForm()
    return render_template('list.html',
                           form=form,
                           val=int(val),
                           LIST=data.LIST(val),
                           )


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')
