---
title: "Javascript アプリを動かしてみた"
date: 2023-03-06T15:06:48+09:00
tags: []
featured_image: "/images/json_timetable.png"
description: ""
author: "Yuu Miino"
---

- [概要](#概要)
- [やったこと](#やったこと)
  - [JS ファイル，CSS ファイルの配置](#js-ファイルcss-ファイルの配置)
  - [HTML ファイルの配置](#html-ファイルの配置)
  - [`head-additions.html` への追記](#head-additionshtml-への追記)
- [気になること](#気になること)
- [余談：`no-print`](#余談no-print)

# 概要
別件で制作した Javascript アプリを Hugo Web サイト上に設置できるだろうと思い至り，設置してみました．

実際に作ったページは [コチラ]({{<ref "json_timetable.html">}})

# やったこと
## JS ファイル，CSS ファイルの配置
JS アプリで使用する各ファイルを Hugo 側にコピペしました．具体的には，
`/static/scripts` に JS ファイルを，`/static/styles` に CSS ファイルをそれぞれ設置しました．

## HTML ファイルの配置
`content` 下に `tools` ディレクトリを作成し，土台の HTML ファイル `json_timetable.html` を配置しました．

内容は以下の通り．

```html
---
title: "JSON 時間割"
date: "2023-03-06T00:00:00+0900"
custom_js: [
    "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.3/font/bootstrap-icons.css",
    "https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"
]
custom_js_module: [
    "scripts/index.js"
]
custom_css: [
    "https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css",
    "styles/json_timetable.css"
]
---
<div class="ttbody mx-auto">
    <div class="mb-4 no-print" id="fileUpload"></div>
    <div class="mb-4 no-print d-none" id="fileOperate"></div>
    <div class="mb-4 no-print d-none" id="filter"></div>
    <div class="my-4 no-print d-none" id="jsonWarning"></div>
    <div class="mb-4 no-print d-none" id="radiosGroup"></div>
    <div class="d-none" id="list"></div>
    <div class="d-none print" id="calendar"></div>
    <div id="modals"></div>
</div>
```

前半が Front matter，後半がコンテンツです．
`content` 内のファイルは基本，`main` タグ内の内容のみを書くので，
{{<exlink href="https://github.com/Yuu-Miino-NUE/json_timetable/blob/main/public/index.html" text="元ファイル">}}
の `body` タグの中身のみ記述すれば良いでしょう．

逆に言えば，独自の Javascript ファイルや CSS ファイルはデフォルトの仕様では読み込めません．

## `head-additions.html` への追記
これを解決するため，`/layouts/partials/head-additions.html` に下記を追記しました．
> デフォルトが空ファイルなので，追記と言うと違和感がありますが．

```go
{{ range .Params.custom_css }}
<link rel="stylesheet" href="{{ . | relURL }}">
{{ end }}

{{ range .Params.custom_js_module }}
<script type="module" src="{{ . | relURL }}"></script>
{{ end }}

{{ range .Params.custom_js }}
<script src="{{ . | relURL }}"></script>
{{ end }}
```

`.Params.custom_css` は，各ファイルの Front matter で設定された `custom_css` の配列です．
配列の各値 `{{ . }}` に対して，`stylesheet` の読み込みを行います（その他も同様）．
常に絶対パスを使う場合には `href="{{ . }}"` で良いのですが，相対パスを使うことのほうが多かろうと思いますので，
`relURL` 関数で `.Site.BaseURL` を適用できるようにしてあります．

`json_timetable.html` の場合，`head-additions.html` は下記のように展開され，`head` タグ内に記述されます．

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css">
<link rel="stylesheet" href="/styles/json_timetable.css">

<script type="module" src="/scripts/index.js"></script>

<script src="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.3/font/bootstrap-icons.css"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>
```

# 気になること
Bootstrap など使う場合，テーマの CSS を上書きしちゃうので，
右上ナビゲーションバーの高さがややズレたりして気持ち悪い...（A 型のぼやき）

# 余談：`no-print`
`no-print` というクラスは，「印刷時に表示しない」という機能を実装しています．