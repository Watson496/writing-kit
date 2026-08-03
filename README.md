# writing-kit

WaTTsonの日本語長文執筆のためのガイドライン集。ブログ記事などのまとまった論を展開する文章を書くための、文体・論の進め方・表記・執筆前設計の規約をまとめている。

## 構成

- `guidelines/` — スタイルガイドライン本体
    - `style_guideline.md` — 本文のスタイルガイド。文体・語り口・論の進め方・引用出典・表記・Markdown使い方
    - `design_note_guideline.md` — 本文執筆前に文章の設計図として書くdesign noteの書き方
- `skills/` — Claude Codeのagent skill定義
    - `design-note/` — トピックや既存素材からdesign noteを作成・改善する
    - `write-body/` — design noteから style_guideline に従って本文（散文）を書き起こす
    - `style-review/` — 書いた文章（本文またはdesign note）を該当guidelineに照らしてレビューする

各skillディレクトリ内の `guidelines/` は、トップレベルの `guidelines/` へのシンボリックリンクになっている。install時に `cp -RL` で実体化する。

## 使い方

### guidelineを直接参照する

`guidelines/` 配下のファイルを執筆時に手元で参照する。または、AIツール（Claude Code等）に読み込ませて執筆・レビュー補助に使う。

### skillを介する

skill定義を `~/.claude/skills/` にコピーする。シンボリックリンクを実体化するため `-L` を付ける：

```
cp -RL skills/design-note skills/write-body skills/style-review ~/.claude/skills/
```

skillは skill 名または近い自然言語で起動する：

- **design-note作成**: 「design note作って」「構成考えて」「アウトライン作って」など
- **本文執筆**: 「本文書いて」「design noteから本文」「write-body」など
- **style-review**: 「文体チェックして」「style-review」「guidelineに照らしてレビューして」など

## 執筆の流れ

このkitが想定している執筆フローは以下：

1. トピック・素材・書きたい方向性を整理する
2. `design-note` skillでdesign noteを作る、または直接 `guidelines/design_note_guideline.md` を参照して自分で書く
3. `write-body` skillでdesign noteから本文を書き起こす、または自分で `guidelines/style_guideline.md` の規約に従って書く
4. 書き上がった本文を `style-review` skillでチェック、または自分で `guidelines/style_guideline.md` と照合する

design noteは論の設計図であり、本文の下書きではない。ここで論の流れと素材の配置を確定させ、言い回しは本文執筆時に考える。
