---
title: Miino's log, subnote of the 1st day
date: 2023-03-02T16:12:35+09:00
author: "Yuu Miino"
---
---
- [クイックスタート](#クイックスタート)
- [基本的な設定](#基本的な設定)
- [詳細な設定](#詳細な設定)
- [CSS ファイルの置き場](#css-ファイルの置き場)

---
## クイックスタート

そのまま公式ドキュメントにしたがってセットアップします．
（ゼロからサイトを作る手順です．編集のみに興味がある方は読み飛ばしてください．）

```shell
$ hugo new site test_site
$ cd test_site
$ git init
$ git submodule add https://github.com/theNewDynamic/gohugo-theme-ananke themes/ananke
$ echo "theme = 'ananke'" >> config.toml
$ hugo server
```

コマンドは上から順番に，下記を行っています．
1. 初期化
2. ディレクトリに移動
3. Git 初期化
4. Theme のダウンロード
5. Theme の設定
6. 開発サーバの起動

Web ブラウザで `localhost:1313` にアクセスすればテンプレートが構築されているのを確認できます．

## 基本的な設定

`test_site` 直下に `config.toml` というファイルがあります．
ここには基本的な設定が記載されています．
例えば

```toml
title="~~~"
```
などとあるので，これを「鳴門教育大学 情報基盤センター」に変更すれば，
図に示すように左上のサイト名が更新されます．

![sc01](/images/sc01.png)

## 詳細な設定

Hugo にデフォルトで用意されている設定の他に，Theme によって色々と調整できる項目があるようです．
`ananke` テーマのテンプレート（`/themes/exampleSite/config.toml`）からプロジェクトの
ルートディレクトリにコピペするのが一番簡単で確実かと思います．

以下，基盤センター向けに調整した内容のみ抜粋します．

```toml
# Hugo の設定
baseURL = 'http://example.org/' # 本来は実運用の URL，開発用サーバを使用している限りはこのままでも OK
languageCode = 'ja-jp'          # 日本語設定，Hugo 自体の設定でテーマに適用されない場合がある
title = '鳴門教育大学 情報基盤センター'

# Ananke テーマの設定
[params]
    hasCJKLanguage = true           # 日本語（というより CJK）の文字数を正しくカウントするため，だそう
    DefaultContentLanguage = "ja"   # 日本語設定，ananke テーマではこっちが重要
    favicon = "https://www.naruto-u.ac.jp/center/it/img/logo.gif" # favicon
    description = "鳴門教育大学 情報基盤センターの公式 Web サイトです．"
    custom_css = ["naruto.css"]             # フォント変更のための CSS
    body_classes = "jpfonts bg-near-white"  # CSS 適用
    post_content_classes = "jpfonts"        # CSS 適用
```

## CSS ファイルの置き場
`ananke` テーマの場合，`/assets/ananke/css` フォルダに置きます．