# Web-Personal-Blog

## Intro
This is backend pratice project. Detail Please visit Roadmap.
https://roadmap.sh/projects/personal-blog
### Design
- The project is used Bootstrap CSS framework to design the web display format.
- The project is used Flask framework to design the web server.
- The project is used HTML, CSS, JavaScript to design the web frontend.



## Menu structure

- [Intro](#Intro)
- [Setup](#Setup)
- [Start&Quit](#Start&Quit)
- [Project](#Project)
- [FileStatement](#FileStatement)
- [Usage](#Usage)
- [Contribute](#Contribute)
- [Lisence](#Lisence)




## Setup 
### python for Flask (Window Command Support!)
#### 1. Download global python (if computer does not have)
https://www.python.org/downloads/
#### 1.1 Use command in bash/cmd to check if python is installed: (recommand python version > 3.7):
```bash
python -v
```
#### 1.2 For python version < 3.4 or is not 2.7.9 (recommand install pip):
(for python 3.x install pip3) (python 2.x install pip2)
```bash
pip --version
# Check if pip is install in python already

# Use under command if your gobal python does not have pip:
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py   # Download install script
sudo python get-pip.py                                    # run install script
# Or
sudo apt-get install python-pip                           # For Linux package manager to install pip
```
#### 1.3 Install venv dependence at global python
Use pip command in bash/cmd to install venv:
```bash
pip install venv
pip list                                                  # Check all package that had install                           
```

#### 2. Setup virual python envirnment (Can skip this step! However, project dependence(package) will be install at global python envirnment, not recommand!)
```bash
cd workspaceFile                                         # Make sure new virual envirnment in project file
python -m venv myvenv                                    # New a virual python envirnment ("myvenv" canbe replaced by your named string)
source myvenv/Scripts/activate                           # Activate new created envirment. If see "(myvenv)" is sucessfully activated!
```




### Start & Quit
#### Make sure every time start project start at virual envirnment!(If use virual envirnemt)
```bash
cd workspaceFile
source myvenv/Scripts/activate                          # Activate "myvenv" virual envirnmemt
```

#### Quit virual envirnment
```bash
deactivate                                              # Quit "now-using" envirnmemt
# Quit if project not use
```

#### Prepare article data(If you do not had any article data)(No article JSON data in "articles" file)
```bash
python create_sample_data.py                            # Create JSON article data in this file setting
```
 
#### Start project  
```bash
python app.py                                           # Start and copy this link http://127.0.0.1:5000 to website
```



## Project
### Intro
A simple personal blog of web that show all articles. There are two sections -- a       <u>guest section</u> and an <u>admin section</u>.<br></br> 
`__Guest Section__` -- A **list of articles** that can be accessed by anyone:
+ __Home Page__: **Display** the list of articles published on the blog.
+ __Article Page__: Display the **content of the article** along with the **date of publication**.

`__Admin Section__` -- The pages that only you can access to **publish**, **edit**, or **delete articles**.
- __Login Page__: A form to **login** to the admin section. The form will have fields like username and password.
- __Dashboard Page__: Display the list of articles published on the blog along with the **option** to add a new article, edit an existing article, or delete an article.
- __Add Article Page__: A form to **add a new article**. The form will have fields like title, content, and date of publication.
- __Edit Article Page__: A form to **edit an existing article**. The form will have fields like title, content, and date of publication.<br></br>



## FileStatement
#### `app.py`: 
The `main Flask application file` that sets up the routes and handles the requests for the blog.
#### create_sample_data.py:
The script to create sample article data in JSON format.
#### `auth.py`:
The file that handles the authentication and authorization for the admin section of the blog.
#### `articles/`:
The directory that `stores the JSON files` for each article. Each JSON file represents an article and contains the article data.
+ article_1.json:
+ article_2.json:
+ ...
#### `templates/`:
The directory that stores the HTML templates for the blog. Each HTML template represents a web page and is rendered by Flask.
+ `article.html`: The HTML template for the article detail content page.
+ `base.html`: The base HTML template that other templates inherit from.
+ `index.html`: The HTML template for the home page where show all articles.
##### `admin/`: The directory that stores HTML templates for the admin section.
- `dashboard.html`: The HTML template for the dashboard page.
- `login.html`: The HTML template for admin's login page.
- `new_article.html`: The HTML template for the new article page.
- `edit_article.html`: The HTML template for the edit article page.
page.
#### static/:
The directory that stores static files like CSS, and images.
##### css/: 
+ style.css
+ images/: The front-end images used in the blog.
#### `utils/`:
The directory that stores utility functions used by the project.
+ `article_utils.py`:
The utility functions related to articles, such as loading article data from JSON files.
+ (__pycache__: The cache directory for Python bytecode files after running the project.)
#### .env: 
The environment variable file that stores sensitive information like secret keys.
#### secret_keyGenerater.py: 
The script to generate a secret key for the project.
#### requirements.txt:
The file that lists the project dependencies and their versions.
#### LICENSE:
The MIT license file for the project.




## Usage
### Storage
The project store article data in JSON format.
Each article data include:
+ id: Integer, unique identifier for the article.
+ title: String, title of the article.
+ content: String, content of the article.
+ date: String, date of publication in the format "YYYY-MM-DD".
+ published: Boolean, indicating whether the article is published or not.



## Contribute
GitHub account: itoeHi,<br>
Email: daiyilin1425251132@qq.com

## Lisence
MIT lisence
