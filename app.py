from flask import Flask, render_template, request, redirect, url_for, flash, abort
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
import os
import json
from datetime import datetime, timedelta
from dotenv import load_dotenv
from flask_wtf import CSRFProtect                                         # CSRF 保护
from utils.article_handler import (
    get_all_articles,
    get_article_by_id,
    create_article,
    update_article,
    delete_article,
    get_next_id
)
from auth import User

# 加载 .env 文件中的环境变量
load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY') or 'dev-secret-key-123'
# 会话安全配置
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=25)  # 25分钟会话过期
app.config['SESSION_COOKIE_SECURE'] = True # 仅通过HTTPS传输cookie（生产环境）
app.config['SESSION_COOKIE_HTTPONLY'] = True # 防止JavaScript访问cookie
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax' # 限制跨站cookie发送

csrf = CSRFProtect(app)                                                  # 启用 CSRF 保护

# Setup login managment
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'admin_login'
login_manager.login_message = 'Please login first and visit this page'

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

# 上下文处理器 - 注入当前时间到所有模板
@app.context_processor
def inject_now():
    return {'now': datetime.now()}

# Ensure file exist
os.makedirs('articles', exist_ok=True)

# # 实现密码重置功能
# @app.route('/admin/reset_password', methods=['GET', 'POST'])
# def reset_password():
#     # 密码重置逻辑
#     if request.method == 'POST':
#         username = request.form.get('username')
#         new_password = request.form.get('new_password')

#         user = User.authenticate(username, new_password)
#         if user:
#             # 更新密码
#             user.password = generate_password_hash(new_password)
#             flash('代码更新成功', 'success')
#             return redirect(url_for('admin_login'))
#         else:
#             flash('Username or password wrong', 'error')

#     return render_template('admin/reset_password.html')

# Guest section router
@app.route('/')
def index():
    """Main page - Display all articles"""
    articles = get_all_articles()

    # 按发布日期倒序排列
    articles.sort(key=lambda x: x['date'], reverse=True)
    return render_template('index.html', articles=articles)

@app.route('/article/<int:article_id>')
def show_article(article_id):
    """article detail page"""
    article = get_article_by_id(article_id)
    if not article:
        abort(404)
    return render_template('article.html', article=article)

# Admin section router
@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    """Admin login page"""
    if current_user.is_authenticated:
        return redirect(url_for('admin_dashboard'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.authenticate(username, password)
        if user:
            login_user(user)
            return redirect(url_for('admin_dashboard'))
        else:
            flash('Username or password wrong', 'error')

    return render_template('admin/login.html')

@app.route('/admin/logout')
@login_required
def admin_logout():
    """Admin logout"""
    logout_user()
    return redirect(url_for('index'))

@app.route('/admin')
@login_required
def admin_dashboard():
    """admin dash board"""
    articles = get_all_articles()
    articles.sort(key=lambda x:x['date'], reverse=True)
    return render_template('admin/dashboard.html', articles=articles)

@app.route('/admin/new', methods=['GET', 'POST'])
@login_required
def new_article():
    """Add new article pages"""
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        date_str = request.form.get('date')

        if not title or not content or not date_str:
            flash('请填写所有字段', 'error')
            return render_template('admin/new_article.html')
    
        try:
            # testify date format
            date = datetime.strptime(date_str, '%Y-%m-%d').strftime('%B %d, %Y')
        except ValueError:
            flash('日期格式错误，请使用 YYYY-MM-DD 格式', 'error')
            return render_template('admin/new_article.html')
        
        article_id = get_next_id()
        article = {
            'id': article_id,
            'title': title,
            'content': content,
            'date': date,
            'created_at': datetime.now().isoformat()
        }

        if create_article(article):
            flash('文章创建成功', 'sucess')
            return redirect(url_for('admin_dashboard'))
        else:
            flash('创建文章时出错', 'error')
    
    # GET 请求时，传递当前日期作为默认值
    today = datetime.now().strftime('%Y-%m-%d')
    return render_template('admin/new_article.html', today=today)

@app.route('/admin/edit/<int:article_id>', methods=['GET', 'POST'])
@login_required
def edit_article(article_id):
    """Edit article page"""
    article = get_article_by_id(article_id)
    if not article:
        abort(404)

    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        date_str = request.form.get('date')

        if not title or not content or not date_str:
            flash('请填写所有字段', 'error')
            return render_template('admin/edit_article.html', article=article)
        
        try:
            # 转换日期格式
            date = datetime.strptime(date_str, '%Y-%m-%d').strftime('%B %d, %Y')
        except ValueError:
            flash('日期格式错误，请使用 YYYY-MM-DD 格式', 'error')
            return render_template('admin/edit_article.html', article=article)
        
        update_article_data = {
            'id': article_id,
            'title': title,
            'content': content,
            'date': date,
            'updated_at': datetime.now().isoformat()
        }

        # 保留原始创建时间
        if 'created_at' in article:
            update_article_data['created_at'] = article['created_at']

        if update_article(article_id, update_article_data):
            flash('文章更新成功', 'success')
            return redirect(url_for('admin_dashboard'))
        else:
            flash('更新文章时出错', 'error')

    # 将日期转换回输入格式
    try:
        article['date_input'] = datetime.strptime(article['date'], '%B %d, %Y').strftime('%Y-%m-%d')
    except:
        article['date_input'] = article['date']

    return render_template('admin/edit_article.html', article=article)

@app.route('/admin/delete<int:article_id>', methods=['POST'])
@login_required
def delete_article_route(article_id):
    """delete article"""
    if delete_article(article_id):
        flash('文章删除成功', 'success')
    else:
        flash('删除文章时出错', 'error')
    
    return redirect(url_for('admin_dashboard'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
