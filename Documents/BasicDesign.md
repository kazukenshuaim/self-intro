# 基本設計書

**プロジェクト名：** 自己紹介サイト
**作成日：** 2026-06-12

## 1. システム概要

### 1.1. システム構成

```text
[ ユーザー (ブラウザ) ]
       │
       | HTTPS
       ↓
┌────────────────────────┐
│  Docker                |
│    ┌────────────────┐  │
│    │   Web アプリ    │  │
│    │    (Django)    │  │
│    └───────┬────────┘  │
|            │ SQL       |
|            ↓           |
| ┌─────────────────────┐ |
| │   データベース       │ |
| │     (PostgreSQL)    │ |
| └─────────────────────┘ |
└─────────────────────────┘
```

### 1.2. 起動ポート


### 1.3. フォルダ・ファイル構成
```
C:.
│  .env
│  .env.example
│  .gitignore
│  db.sqlite3
│  docker-compose.yml
│  Dockerfile
│  manage.py
│  README.md
│  requirements.txt
│  
├─accounts
│  │  admin.py
│  │  apps.py
│  │  forms.py
│  │  models.py
│  │  tests.py
│  │  urls.py
│  │  views.py
│  │  __init__.py
│  │  
│  ├─migrations
│  │  │  0001_initial.py
│  │  │  __init__.py
│  │  │  
│  │  └─__pycache__
│  │          0001_initial.cpython-312.pyc
│  │          __init__.cpython-312.pyc
│  │          
│  └─__pycache__
│          admin.cpython-312.pyc
│          apps.cpython-312.pyc
│          forms.cpython-312.pyc
│          models.cpython-312.pyc
│          urls.cpython-312.pyc
│          views.cpython-312.pyc
│          __init__.cpython-312.pyc
│          
├─config
│  │  asgi.py
│  │  settings.py
│  │  urls.py
│  │  wsgi.py
│  │  __init__.py
│  │  
│  └─__pycache__
│          settings.cpython-312.pyc
│          urls.cpython-312.pyc
│          wsgi.cpython-312.pyc
│          __init__.cpython-312.pyc
│          
├─tasks
│  │  admin.py
│  │  apps.py
│  │  forms.py
│  │  models.py
│  │  tests.py
│  │  urls.py
│  │  views.py
│  │  __init__.py
│  │  
│  ├─migrations
│  │  │  0001_initial.py
│  │  │  __init__.py
│  │  │  
│  │  └─__pycache__
│  │          0001_initial.cpython-312.pyc
│  │          __init__.cpython-312.pyc
│  │          
│  └─__pycache__
│          admin.cpython-312.pyc
│          apps.cpython-312.pyc
│          forms.cpython-312.pyc
│          models.cpython-312.pyc
│          urls.cpython-312.pyc
│          views.cpython-312.pyc
│          __init__.cpython-312.pyc
│          
└─templates
    │  base.html
    │  
    ├─accounts
    │      login.html
    │      register.html
    │      
    └─tasks
            task_confirm_delete.html
            task_detail.html
            task_form.html
            task_list.html
```

## 2. 画面構成

### 2.1. 画面一覧
ファイルは共通してtemplates/base.htmlと併用。
| 画面名 | ファイル | URL |
| --- | --- | --- |
| アカウント登録画面 | templates/accounts/register.html | ログイン画面からボタン遷移
| ログイン画面 | templates/accounts/login.html | トップバーからボタン遷移 |
| 自己紹介登録画面 | templates/contents/content_form.html | 一覧画面からボタン遷移 |
| 一覧画面 | templates/contents/content_list.html| http://localhost:8000 トップページ |
| 詳細画面 | templates/contents/content_detail.html | 一覧画面からボタン遷移 |
| 削除確認画面 | templates/contents/contents_delete.html | 詳細画面からボタン遷移 |

### 2.2. 各画面のレイアウト
#### アカウント登録画面
#### ログイン画面
#### 自己紹介登録画面
#### 一覧画面
#### 詳細画面
#### 削除確認画面

### 2.3. 画面遷移
```
アカウント登録画面 ─アカウント登録─→一覧画面
        ↑
        |ボタン遷移
        ↓
ログイン画面─ログイン─→一覧画面




```

