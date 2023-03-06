---
title: "Miino's log, the 2nd day"
date: 2023-03-06T09:55:46+09:00
tags: []
featured_image: ""
description: ""
draft: true
---

---
- [サイト編集手順の確認](#サイト編集手順の確認)
  - [大まかな流れ](#大まかな流れ)
  - [細かな手順](#細かな手順)
    - [Github から clone](#github-から-clone)
    - [作業用にブランチを切る](#作業用にブランチを切る)
    - [hugo コマンドで開発用サーバの起動](#hugo-コマンドで開発用サーバの起動)
    - [記事作成・編集](#記事作成編集)
    - [main ブランチにマージ](#main-ブランチにマージ)
    - [ローカルの main ブランチを Github に push](#ローカルの-main-ブランチを-github-に-push)
    - [本番環境に pull](#本番環境に-pull)

---

# サイト編集手順の確認

## 大まかな流れ
1. Github から `clone`（初回のみ，2 回目からは `pull`）
2. 作業用にブランチを切る
3. `hugo` コマンドで開発用サーバの起動
4. 記事作成・編集
5. `main` ブランチにマージ
6. Github に `push`
7. 本番環境に `pull`

## 細かな手順
### Github から clone
テストサイトのソースファイルを
{{<exlink href="https://github.com/Yuu-Miino-NUE/nue_official_web.git" text="Github">}}
にアップロードしました．

> git はバージョン管理プログラム
> Github は git リポジトリを Web にアップロードできるサービスです．

```shell
$ git clone --recursive https://github.com/Yuu-Miino-NUE/nue_official_web.git
```

サブモジュールも合わせて `clone` する場合には，`--recursive` オプションを付与します．

`clone` はイニシャルセットアップなので，二回目以降は必要ありません．

その代わりに，開発環境を最新の状態にするために，作業前には必ず `pull` しましょう．

```shell
$ git pull --all
```

### 作業用にブランチを切る
複数人での作業を想定するため，編集を施す際にはブランチを切りましょう．
例えば，`feature/miino_logs` という名前のブランチを切る場合，下記のコマンドを実行します．

```shell
$ git branch feature/miino_logs         # ブランチ作成
$ git checkout feature/miino_logs       # ブランチへ移動

$ git checkout -b feature/miino_logs    # ブランチを作成してそこへ移動
```

ブランチをどう切るかは，組織によって予め取り決めておくのが基本のようです．
代表的な運用方法として，git flow や github flow などがあります．
両者を比較する記事は，多く存在します．例えば
{{<exlink href="https://www.geeksforgeeks.org/git-flow-vs-github-flow/" text="コチラ">}} など．

### hugo コマンドで開発用サーバの起動

```shell
$ hugo server -D
```

`-D` は下書きも表示（コンパイル）するオプション．

### 記事作成・編集
`hugo new <記事のパス>` で記事テンプレートを作成．

```shell
$ hugo new logs/miino_logs_20230306.md
```

あとはお好きなエディタで Markdown ファイルを修正します．

小まめに `commit`（セーブ）した方が良いでしょう．

```shell
$ git commit -am '執筆：Github から clone'
```

コミットが貯れば，リモートにも `push` しておきましょう．

```shell
$ git push origin feature/miino_logs
```

> リモートにブランチがない場合，`-u` の指定を促されるかもしれません．

### main ブランチにマージ
Github のデフォルトブランチは `main` です．
> `git` のデフォルトは `master` ですが，Github では `main` です．

`feature/miino_logs` での変更内容を `main` に統合（`merge`）します．
`merge` をする前にはかならず，ローカルの `main` ブランチを最新のものにしておきます．

```shell
$ git pull origin main
```

> 自分で切ったブランチを他の人も使っている，という場合には，
> `git pull --all` とした方が良いでしょう．

準備が整ったら，`main` ブランチにマージします．
`main` ブランチに移動（`checkout`）して，`feature/miino_logs` をマージします．

```shell
$ git checkout main
$ git merge feature/miino_logs
```

競合（`conflict`）がなければ，コメントを書いて統合完了です．

### ローカルの main ブランチを Github に push
```shell
$ git push origin main
```

### 本番環境に pull
本番環境で最新の `main` ブランチを `pull` します．

```shell
$ git pull origin main
```

この行程は，Github Actions で自動化できます．
具体的には，「`main` ブランチが変更されれば，本番環境にデプロイする」という
プログラムを組めます．