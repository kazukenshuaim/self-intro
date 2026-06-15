from django.contrib import admin
from .models import Intro

@admin.register(Intro)
class IntroAdmin(admin.ModelAdmin):
    # 1. 一覧画面に表示する項目（name や updated_at も追加して見やすく）
    list_display = ('id', 'name', 'created_by', 'birthday', 'updated_at')
    
    # 2. クリックして詳細画面に移動できるリンクにする項目
    list_display_links = ('id', 'name')
    
    # 3. 検索ボックスで検索できるようにするフィールド（name も追加）
    search_fields = ('name', 'created_by__username', 'hobby')
    
    # 4. 右側に絞り込みフィルターを設置（作成日や更新日で絞り込める）
    list_filter = ('created_at', 'updated_at')
    
    # 5. 並び順（モデル側の Meta で指定した ordering と合わせるのが綺麗です）
    ordering = ('-updated_at',)