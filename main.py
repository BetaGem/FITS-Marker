from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap

#初始化，创建应用实例（Flask类的对象）,配置密钥
app = Flask(__name__) 
app.config['SECRET_KEY']='zdsnswzkadxts'

#表单 Flask-WTF
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired

#画图
from fitsplot import plot,RGB

#数据
import data   

#bootstrap
bootstrap = Bootstrap(app)

contra = '0'    
contrast_list = {'-2':[-0.8,50],'-1':[-0.6,15],'0':[-0.3,6],'1':[-0.2,2],'2':[-0.1,1],}

class Form(FlaskForm):
    contrast = SelectField('Contrast',choices=[('-2','-2'),('-1','-1'),('0','0'),('1','1'),('2','2')],render_kw = { 'style':'width:120px;' }, default='0')
    submit = SubmitField('Submit')
    
#路由, index.html
@app.route('/<name>',methods=['GET', 'POST'])
def index(name):
    
    global contra, contrast_list
    contrast = contra
    form = Form()
    if form.validate_on_submit():
        contrast = form.contrast.data
        contra = contrast
    k = int(name)
    fig_g = plot(k,1,contrast_list[contrast])
    fig_r = plot(k,2,contrast_list[contrast])
    fig_i = plot(k,3,contrast_list[contrast])
    fig_c = RGB(k, contra)
    return render_template('index.html',
                           form=form, 
                           k=k,
                           contra=contra,
                           info=data.galinfo(k-1),
                           fig1=fig_g, fig2=fig_r, fig3=fig_i,fig4=fig_c,
                           Num=2088                     #总数
                          )

@app.route('/<name>/last_choice:<val>',methods=['GET', 'POST'])
def judge(name,val):
    
    k = int(name)
    v = val
    data.classify(k-1,val)
    return index(name)

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
