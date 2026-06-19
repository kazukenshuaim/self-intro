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
├─intros
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
    └─intros
            intro_confirm_delete.html
            intro_detail.html
            intro_form.html
            intro_list.html
```

## 2. 画面構成

### 2.1. 画面一覧
ファイルは共通してtemplates/base.htmlと併用。
| 画面名 | ファイル | URL |
| --- | --- | --- |
| アカウント登録画面 | templates/accounts/register.html | ログイン画面からボタン遷移
| ログイン画面 | templates/accounts/login.html | トップバーからボタン遷移 |
| 新規登録画面 | templates/intros/intro_form.html | 一覧画面からボタン遷移 |
| 一覧画面 | templates/intros/intro_list.html| http://localhost:8000 トップページ |
| 詳細画面 | templates/intros/intro_detail.html | 一覧画面からボタン遷移 |
| 削除確認画面 | templates/intros/intros_delete.html | 詳細画面からボタン遷移 |

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
┌───────────────────────────────────────┐
│  自己紹介　　　[ユーザー名]　ログアウト  │
│  ─────────────────────────────────    │
│  ## 自己紹介一覧          [+新規登録]   │
│ | 名前      | 作成日時 |  更新日時  |   │
| | 佐藤健   | 2026-06-14 | 2026-06-15 | |
| | 瀬戸康史 | 2026-06-15 | 2026-06-15 | |
| | 菅田将暉 | 2026-06-15 | 2026-06-14 | |
└───────────────────────────────────────┘
```
#### 詳細画面
```
┌──────────────────────────────────────┐
│  自己紹介　　　[ユーザー名]　ログアウト │
│  ─────────────────────────────────   │
│  | 佐藤健            [編集][削除] |   |
|  | 誕生日          1989年3月21日  |   |
|  | 趣味・特技       オセロ、謎解き |   |
|  | 作成日時    2026年6月14日13:00 |   |
|  | 更新日時    2026年6月15日13:00 |   |
|  [←一覧に戻る]                        |
└──────────────────────────────────────┘
```
#### 編集画面
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
     保存  | ↑
 キャンセル | | 新規登録ボタン
           ↓ |
        一覧画面
          |  ↑
 名前ボタン|  | 一覧に戻るボタン
          ↓  |
        詳細画面
           | ↑     保存
 編集ボタン | | キャンセルボタン
           ↓ |
        編集画面


        詳細画面
           | ↑
 削除ボタン | | キャンセルボタン
           ↓ |
       削除確認画面
            |
            | 削除
            ↓
        一覧画面


          諸画面
            |
            |ログアウト
            ↓
        ログイン画面
```

## 3. 処理フロー

### 3.1. アカウント登録機能
```
[ブラウザ] GET /accounts/register/リクエスト
        ↓
[config/urls.py] accounts/検知
        ↓
[accounts/urls.py] register/検知
        ↓
[RegisterView(accounts/views.py)] 起動。CustomUserCreationFormを準備
        ↓
[templates/accounts/register.html]表示
        ↓
[ユーザー] アカウント情報を入力、送信
        ↓
[ブラウザ] POST /accounts/register/リクエスト
        ↓
[config/urls.py] accounts/検知
        ↓
[accounts/urls.py] register/検知
        ↓
[RegisterView(accounts/views.py)] 起動。CustomUserCreationFormでバリデーション
        |
        |バリデーション失敗時、入力を指示
        ↓
[RegisterView(accounts/views.py)] バリデーション成功時、model.pyのCustomUserへデータ保存
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
[ブラウザ] GET /accounts/login/リクエスト
        ↓
[config/urls.py] accounts/検知
        ↓
[accounts/urls.py] login/検知
        ↓
[auth_views.LoginView(標準搭載)] 起動。AuthenticationFormを準備。
        ↓
[templates/accounts/login.html] 表示
        ↓
[ユーザー] アカウント情報を入力、送信
        ↓
[ブラウザ] POST /accounts/login/リクエスト
        ↓
[config/urls.py] accounts/検知
        ↓
[accounts/urls.py] login/検知
        ↓
[auth_views.LoginView] 起動。model.pyのCustomUserのデータと照合。
        |
        | 失敗時、エラーメッセージを出す
        ↓
[auth_views.LoginView] 照合成立後、ログイン状態確立
        ↓
[config/settings.py] LOGIN_REDIRECT_URLへ遷移
        ↓
[templates/intros/intro_list.html] 表示 
```

#### ログアウト機能
```
[ブラウザ] POST /accounts/register/リクエスト
        ↓
[config/urls.py] accounts/検知
        ↓
[accounts/urls.py] logout/検知
        ↓
[auth_views.LogoutView(accounts/views.py)] 起動。ログイン状態破棄。
        ↓
[config/settings.py] LOGIN_REDIRECT_URLへ遷移
        ↓
[templates/accounts/login.html] 表示 
```

### 3.3. 新規登録機能
```
[ブラウザ] GET /intros/create/リクエスト
        ↓
[config/urls.py] intros/検知
        ↓
[intros/urls.py] create/検知
        ↓
[IntroCreateView(intros/views.py)] get_form()起動。
        ↓
[templates/intros/intro_form.html] if objectはFalseで表示
        ↓
[ユーザー] 名前などの情報を入力、送信
        ↓
[ブラウザ] POST /intros/create/リクエスト
        ↓
[config/urls.py] intros/検知
        ↓
[intros/urls.py] create/検知
        ↓
[IntroCreateView(intros/views.py)] IntroFormで入力バリデーション（nameが入力されているか）
        |
        |バリデーション失敗時、nameを入力するよう指示
        ↓
[IntroCreateView(intros/views.py)] バリデーション成功時、form_valid()起動。作成者を裏で自動セット。super().form_valid()でIntro(model.py)へ新規保存。
        ↓
[IntroCreateView(intros/views.py)] success_urlへ遷移
        ↓
[templates/intros/intro_list.html] 表示。サクセスメッセージ表示。
```

### 3.4. 一覧表示機能
```
[ブラウザ] GET /intros/、/intros/?page=2などリクエスト
        ↓
[config/urls.py] intros/検知
        ↓
[intros/urls.py] 空('')検知
        ↓
[IntroListView(intros/views.py)] 起動。LoginRequiredMixinによるログインチェック
        ↓
[IntroListView(intros/views.py)] get_queryset()が起動。pagenate_by=10、page指定（例えばpage=2）を検知。Intro.object.filterでDBから自分のデータを10件、更新順に取得。
        ↓
[IntroListView(intros/views.py)]取得データを'intros'に格納。
        ↓
[templates/intros/intro_list.html] {% for intro in intros %}で、1-10件をループして自己紹介を表示。page_objに従ってページ遷移ボタンを表示。
```

### 3.5. 詳細表示機能
```
[ブラウザ] GET /intros/{id}/リクエスト
        ↓
[config/urls.py] intros/検知
        ↓
[intros/urls.py] <int:pk>/検知
        ↓
[IntroDetailView(intros/views.py)] get_queryset()起動。Intro.object.filterでDBから自分のデータを取得、IDを検索。見つかったデータを'intro'に格納
        ↓
[templates/intros/intro_detail.html] {{intro.name}}などを表示
```
### 3.6. 自己紹介編集、削除機能

#### 自己紹介編集機能
```
[ブラウザ] GET /intros/{id}/update/リクエスト
        ↓
[config/urls.py] intros/検知
        ↓
[intros/urls.py] <int:pk>/update/検知
        ↓
[TaskUpdateView(intros/views.py)] get_queryset()、get_form()起動。
        ↓
[templates/intros/intro_form.html] if objectはTrueで表示
        ↓
[ユーザー] 名前などの情報を入力、送信
        ↓
[ブラウザ] POST /intros/{id}/update/リクエスト          
        ↓
[config/urls.py] intros/検知
        ↓
[intros/urls.py] <int:pk>/update/検知
        ↓
[IntroUpdateView(intros/views.py)] IntroFormで入力バリデーション（nameが入力されているか）
        |
        |バリデーション失敗時、nameを入力するよう指示
        ↓
[IntroUpdateView(intros/views.py)] バリデーション成功時、変更内容を上書き保存。updated_atが自動更新。form_valid()で変更内容確定。get_success_urlが起動。
        ↓
[templates/intros/intro_list.html] 表示。サクセスメッセージ表示。
```

#### 自己紹介削除機能
```
[ブラウザ] GET /intros/{id}/delete/リクエスト
        ↓
[config/urls.py] intros/検知
        ↓
[intros/urls.py] <int:pk>/delete/検知
        ↓
[TaskDeleteView(intros/views.py)] get_queryset()起動、対象自己紹介を確認。
        ↓
[templates/intros/intro_confirm_delete.html] 表示
        ↓
[ユーザー]削除ボタンを押す
        ↓
[ブラウザ] POST /intros/{id}/delete/リクエスト
        ↓
[config/urls.py] intros/検知
        ↓
[intros/urls.py] <int:pk>/delete/検知
        ↓
[IntroDeleteView(intros/views.py)] 対象のデータを削除。success_urlに遷移。
        ↓
[templates/intros/intro_list.html] 表示。サクセスメッセージ表示。
```

---

## 4. データ設計
SQLを使用。

---

## 5. エラー処理方針
| エラーの種類 | 発生箇所 | 対処法 |
|---|---|---|
| ユーザー名、メールアドレス、パスワード二か所のどれかが空、メールアドレスに@が入っていない | アカウント登録画面 | エラーメッセージを表示、送信しない |
| ログイン不正 | ログイン画面 | エラーメッセージを表示し、ログインしない |
| 名前が空 | 新規登録画面、編集画面 | エラーメッセージを表示し、登録しない |

---

## 6. 環境変数・設定値

---