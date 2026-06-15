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
├─contents
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
    └─contents
            content_confirm_delete.html
            content_detail.html
            content_form.html
            content_list.html
```

## 2. 画面構成

### 2.1. 画面一覧
ファイルは共通してtemplates/base.htmlと併用。
| 画面名 | ファイル | URL |
| --- | --- | --- |
| アカウント登録画面 | templates/accounts/register.html | ログイン画面からボタン遷移
| ログイン画面 | templates/accounts/login.html | トップバーからボタン遷移 |
| 新規登録画面 | templates/contents/content_form.html | 一覧画面からボタン遷移 |
| 一覧画面 | templates/contents/content_list.html| http://localhost:8000 トップページ |
| 詳細画面 | templates/contents/content_detail.html | 一覧画面からボタン遷移 |
| 削除確認画面 | templates/contents/contents_delete.html | 詳細画面からボタン遷移 |

### 2.2. 各画面のレイアウト
#### アカウント登録画面
```
┌──────────────────────────────────────┐
│  自己紹介　　　ログイン　登録           │
│  ─────────────────────────────────   │
|  ##アカウント登録                       |
|  ユーザー名：[____]                   |
|  メールアドレス：[____]               |
|  パスワード：[____]                   |
|  パスワード確認用：[____]             |
|  [登録]                               
└──────────────────────────────────────┘
```
#### ログイン画面
```
┌──────────────────────────────────────┐
│  自己紹介　　　ログイン　登録          │
│  ─────────────────────────────────   │
│  ## ログイン                          │
│  ユーザー名：[____]                   │
|  パスワード：[____]                   |
|  [ログイン]                           |
└──────────────────────────────────────┘
```
#### 新規登録画面
```
┌──────────────────────────────────────┐
│  自己紹介　　　[ユーザー名]　ログアウト │
│  ─────────────────────────────────   │
│  ## 新規登録                         │
|  名前：[____]                        |
|  誕生日：[yyyy/mm/dd ]                |
|  趣味/特技： ┌─────────────────────┐  |
|             │                     │  |
|             │                     │  |
|             └─────────────────────┘  |
└──────────────────────────────────────┘
```
#### 一覧画面
```
┌──────────────────────────────────────┐
│  自己紹介　　　[ユーザー名]　ログアウト │
│  ─────────────────────────────────   │
│  ## 自己紹介一覧          [+新規登録] │
│  | 名前      |  作成日時  |           │
|  | 佐藤健   | 2026-06-15 |            |
|  | 瀬戸康史 | 2026-06-15 |            |
|  | 菅田将暉 | 2026-06-16 |            |
└──────────────────────────────────────┘
```
#### 詳細画面
```
┌──────────────────────────────────────┐
│  自己紹介　　　[ユーザー名]　ログアウト │
│  ─────────────────────────────────   │
│  | 佐藤健            [編集][削除] |   |
|  | 誕生日          1989年3月21日  |   |
|  | 趣味・特技       オセロ、謎解き |   |
|  | 作成日時    2026年6月15日13:00 |   |
|  [←一覧に戻る]                        |
└──────────────────────────────────────┘
```
#### 自己紹介編集画面
```
┌──────────────────────────────────────┐
│  自己紹介　　　[ユーザー名]　ログアウト │
│  ─────────────────────────────────   │
│  ## 自己紹介編集                         │
|  名前：[菅田将暉]                     |
|  誕生日：[1993/02/21 ]                |
|  趣味/特技： ┌─────────────────────┐  |
|             │ お笑い              │  |
|             │                     │  |
|             └─────────────────────┘  |
└──────────────────────────────────────┘
```
#### 削除確認画面
```
┌──────────────────────────────────────┐
│  自己紹介　　　[ユーザー名]　ログアウト │
│  ─────────────────────────────────   │
│  | タスクの削除                  |    |
|  | 「ユーザー名」を削除しますか？ |     |
|  | [削除する][キャンセル]        |     |
└──────────────────────────────────────┘
```

### 2.3. 画面遷移
```
アカウント登録画面 ─── アカウント登録 ───→ 一覧画面
           | ↑
 ボタン遷移 | |ボタン遷移
           ↓ |
      ログイン画面 ─── ログイン ───→ 一覧画面


        新規登録画面
           | ↑
キャンセル  | | 新規登録ボタン
           ↓ |
        一覧画面
          |  ↑
 名前ボタン|  | 一覧に戻るボタン
          ↓  |
        詳細画面
           | ↑
 編集ボタン | | キャンセルボタン
           ↓ |
    自己紹介編集画面


        詳細画面
           | ↑
 削除ボタン | | キャンセルボタン
           ↓ |
       削除確認画面


ログイン、アカウント登録以外の画面
            |
            |ログアウト
            ↓
        ログイン画面
```

## 3. 処理フロー

### 3.1. アカウント登録機能
```
[ユーザー、templates/accounts/register.html] アカウント情報を入力、送信
        ↓
[config/urls.py] POST accounts/リクエスト
        ↓
[accounts/urls.py] register/リクエスト
        ↓
[RegisterView(accounts/views.py)] 起動。CustomUserCreationFormでバリデーション
        ↓
[RegisterView(accounts/views.py)] model.pyのCustomUserへデータ保存
        ↓
[RegisterView(accounts/views.py)] login()で自動ログイン
        ↓
[RegisterView(accounts/views.py)] success_urlへ遷移
        ↓
[templates/intros/intro_list.html] 表示 
```

### 3.2. ログイン、ログアウト機能
#### ログイン機能
```
[ユーザー、templates/accounts/login.html] アカウント情報を入力、送信
        ↓
[config/urls.py] POST accounts/リクエスト
        ↓
[accounts/urls.py] login/リクエスト
        ↓
[auth_views.LoginView] 起動。model.pyのCustomUserのデータと照合
        ↓
[auth_views.LoginView] 照合成功後、ログイン状態確立
        ↓
[config/settings.py] LOGIN_REDIRECT_URLへ遷移
        ↓
[templates/intros/intro_list.html] 表示 
```

#### ログアウト機能
```
[ユーザー] ログアウトボタン押下
        ↓
[config/urls.py] POST accounts/リクエスト
        ↓
[accounts/urls.py] logout/リクエスト
        ↓
[auth_views.LogoutView(accounts/views.py)] 起動。ログイン状態破棄。
        ↓
[config/settings.py] LOGIN_REDIRECT_URLへ遷移
        ↓
[templates/accounts/login.html] 表示 
```

### 3.3. 新規登録機能

### 3.4. 一覧表示機能

### 3.5. 詳細表示機能

### 3.6. 自己紹介編集、削除機能

## 4. データ設計
SQLを使用。

## 5. エラー処理方針

## 6. 環境変数・設定値