---
title: "記事執筆のすゝめ"
date: 2023-03-06T11:42:30+09:00
tags: []
featured_image: ""
description: ""
draft: true
---

- [基本](#基本)
- [画像挿入](#画像挿入)
- [外部リンク](#外部リンク)
- [内部リンク](#内部リンク)

# 基本
`hugo` では，`hugo new <記事のパス>` として記事のテンプレートを作成します．

```shell
$ hugo new posts/my-first-post.md
```

このコマンドは単にテンプレを指定されたパスに置いているだけなので，
`content` ディレクトリに Markdown[^1] や HTML を直接追加しても，サイトに反映されます．
例えば，`content/posts` 直下に次の内容の `my-first-post.md` を配置します．

[^1]: {{<exlink href="https://gohugo.io/content-management/formats/#learn-markdown" text="Learn Markdown">}}
でお勉強しましょうね，と公式に書いてありました．

```markdown
---
title: "テスト投稿"
date: 2023-03-02T16:12:35+09:00
draft: true
---

# 導入

これは導入テストです．


```
> `draft: true` では，下書きのままなので，公開するぞというときには `false` にしましょう．


すると，`localhost:1313/posts/my-first-post/` に Web ページが生成されます．

ファイルの書き始めに *Front matter* を入れておけば，色々と制御できます．
({{<exlink href="https://gohugo.io/content-management/front-matter/" text="Front matter の公式ドキュメント">}})

Front matter を含んだ Markdown テンプレートを生成したい場合には，`hugo new <記事のパス>` で記事テンプレートを作成しましょう．

> #### 余談
> ##### ホットリロード
> 最近の開発用サーバはホットリロードを標準搭載しており，`Hugo` もその例から漏れないようです．
> 開発用サーバを起動中に Markdown ファイルを保存すると，コンパイルなどせずとも直ちに（開発環境上の） Web ページ反映されます．
> 便利です．
> ##### `_index.md`
> `Hugo` では，`_index.md` というファイルがインデックスページとして認識されるようです．
> ({{<exlink href="https://gohugo.io/content-management/organization/#index-pages-_indexmd" text="公式ドキュメント参照">}})


# 画像挿入
画像は `static/images` フォルダに保存します．
保存した画像は，例えば次のようにして参照できます．

```markdown
![alt text](/images/center.png "マウスオーバー！")
![リンク切れだよ](/images/sonna_file_naiyo.png)
```

出力結果：

![alt text](/images/center.png "マウスオーバー！")

![リンク切れだよ](/images/dummy.png)

# 外部リンク
外部リンクは新しいウィンドウで開いてもらいたい，ですよね？
一般的な Markdown には直接 HTML を書き込むこともできますが，`Hugo` の場合は
少し設定をいじる必要があります．
面倒なので，`shortcodes` という機能を使って実装してみましょう．

`/layouts` フォルダには何度でも使い回すようなテンプレートを保存します．
`shortcodes` もそこに保存するようです．
`/layouts/shortcodes` というフォルダを作り，フォルダ内に `exlink.html` というファイルを作成しましょう．
中には以下のように記述します．

```go
{{ if .IsNamedParams }}
<a href="{{ .Get "href" }}" target="_blank" rel="noopener noreferrer">{{ if .Get "text"}}{{ .Get "text" }}{{ else }}{{ .Get "href"}}{{ end }}</a>
{{ else }}
<a href="{{ .Get 0 }}" target="_blank" rel="noopener noreferrer">{{ .Get 0 }}</a>
{{ end }}
```

> `Hugo` は Golang で書かれている訳ですが，上記の記法は Go の
> `html/template` および `text/template` ライブラリに実装されているロジックだそうです．
> ({{<exlink href="https://gohugo.io/templates/introduction/#example-4-if--else" text="公式ドキュメント">}})

`shortcodes` の使い方は以下のとおり，ファイル名で呼び出します．
例の他にもいくつかパラメタの指定方法がありますが，割愛します．詳細は参考先をご確認ください．

```html
参考：{{</*exlink href="https://blog.foresta.me/posts/hugo_shortcode_for_external_link/" text="Hugoで外部リンクを開くためのshortcodeを作った話"*/>}}
```

参考：{{<exlink href="https://blog.foresta.me/posts/hugo_shortcode_for_external_link/" text="Hugoで外部リンクを開くためのshortcodeを作った話">}}

# 内部リンク
内部リンクについては，shortcode が用意されています．
詳しくは {{<exlink href="https://gohugo.io/content-management/cross-references/" text="公式">}} 参照．

```html
[今日のログへのリンク]({{</*ref "miino_logs_20230302.md"*/>}})
[投稿一覧へのリンク]({{</*relref "../posts"*/>}})
```

[今日のログへのリンク]({{<ref "miino_logs_20230302.md">}})

[投稿一覧へのリンク]({{<relref "../posts">}})