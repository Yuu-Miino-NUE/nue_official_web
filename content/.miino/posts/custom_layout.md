---
title: "レイアウトをカスタマイズしてみた"
date: 2023-03-06T14:32:07+09:00
tags: []
featured_image: ""
description: ""
author: "Yuu Miino"
---

- [手順](#手順)
- [実際に施した変更](#実際に施した変更)
  - [`_default/single.html`](#_defaultsinglehtml)
  - [`partials/page-header.html`](#partialspage-headerhtml)
  - [`partials/head-additions.html`](#partialshead-additionshtml)


# 手順
既存のテンプレートを元にレイアウトをカスタマイズするには，変更したいテンプレートが何であるかを知ることが肝要です．
{{<exlink href="https://gohugo.io/templates/" text="公式ドキュメント">}}
で勉強すると良いでしょう．

変更したいテンプレートがわかったら，以下の手順でテンプレートを変更します．

1. `/themes/ananke/layouts` から変更したいテンプレートを開発環境の `/layouts` にコピペ
2. コピペしたテンプレートを変更

例えば，Single Page Template を変更したい場合，まずは
`/themes/ananke/exampleSite/layouts/_default` に入っている `single.html`
を `/layouts/_default` にコピーしてきます．

```shell
$ cp /themes/ananke/layouts/_default/single.html /layouts/_default/single.html
```

その後，`/layouts/_default/single.html` を好きなように変更すれば，Web サイトに反映されます．

> 変更時にインデント等まで変更すると `diff` が取りにくいのでオススメしません．

# 実際に施した変更
## `_default/single.html`
* `aside` の削除
* `div` の横幅変更（`w-100`）
* `header` への `no-print` クラスの付与

```shell
$ diff ./themes/ananke/layouts/_default/single.html ./layouts/_default/single.html
```

```diff
9,16c9
<     <header class="mt4 w-100">
<       <aside class="instapaper_ignoref b helvetica tracked">
<           {{/*
<           CurrentSection allows us to use the section title instead of inferring from the folder.
<           https://gohugo.io/variables/page/#section-variables-and-methods
<           */}}
<         {{with .CurrentSection.Title }}{{. | upper }}{{end}}
<       </aside>
---
>     <header class="mt4 w-100 no-print">
50c43
<     <div class="nested-copy-line-height lh-copy {{ $.Param "post_content_classes"  | default "serif"}} f4 nested-links {{ $.Param "text_color" | default "mid-gray" }} {{ cond (eq $.Site.Language.LanguageDirection "rtl") "pl4-l" "pr4-l" }} w-two-thirds-l">
---
>     <div class="nested-copy-line-height lh-copy {{ $.Param "post_content_classes"  | default "serif"}} f4 nested-links {{ $.Param "text_color" | default "mid-gray" }} {{ cond (eq $.Site.Language.LanguageDirection "rtl") "pl4-l" "pr4-l" }} w-100">
63,66d55
<     <aside class="w-30-l mt6-l">
<       {{- partial "menu-contextual.html" . -}}
<     </aside>
< 
```

## `partials/page-header.html`
* `header` への `no-print` クラスの付与（[別記事]({{<ref "custom_js.md">}}) にて説明）

```shell
$ diff ./themes/ananke/layouts/partials/page-header.html ./layouts/partials/page-header.html
```

```diff
4c4
<   <header class="cover bg-top" style="background-image: url('{{ $featured_image }}');">
---
>   <header class="cover bg-top no-print" style="background-image: url('{{ $featured_image }}');">
20c20
<   <header>
---
>   <header class="no-print">
```

## `partials/head-additions.html`
* カスタム CSS，カスタム JS 用のスクリプトを追加

```shell
diff ./themes/ananke/layouts/partials/head-additions.html ./layouts/partials/head-additions.html
```

```diff
0a1,11
> {{ range .Params.custom_css }}
> <link rel="stylesheet" href="{{.}}">
> {{ end }}
> 
> {{ range .Params.custom_js_module }}
> <script type="module" src="{{.}}"></script>
> {{ end }}
> 
> {{ range .Params.custom_js }}
> <script src="{{.}}"></script>
> {{ end }}
```

ここでは，各ページで Front matter に `custom_css` や `custom_js` が設定されていれば，
そのページ専用の CSS，JS として読み込む仕組みを作っています．