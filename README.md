# writing-kit

WaTTsonの日本語長文執筆のためのガイドライン集。ブログ記事などのまとまった論を展開する文章を書くための、文体・論の進め方・表記・執筆前設計の規約をまとめている。

## 構成

- `guidelines/` — スタイルガイドライン本体
    - `common_guideline.md` — 全文書共通のガイド。design note・本文のどちらを書くときも適用される。認識の帰属・命題/概念の扱い・修辞・論の進め方・引用出典・表記・Markdown
    - `style_desu_masu.md` — です・ます調の本文スタイルガイド。文体・語り口の表現形・段落の作り方・つなぎの言い回し・本文中の箇条書きの運用
    - `style_da_dearu.md` — だ・である調（論文のような硬めの論説文）の本文スタイルガイド。構成は`style_desu_masu.md`と同じ
    - `design_note_guideline.md` — 本文執筆前に文章の設計図として書くdesign noteの書き方
- `skills/` — Claude Codeのagent skill定義
    - `design-note/` — トピックや既存素材からdesign noteを作成・改善する
    - `write-body/` — design noteからguidelineに従って本文（散文）を書き起こす
    - `style-review/` — 書いた文章（本文またはdesign note）を該当guidelineに照らしてレビューする

各skillディレクトリ内の `guidelines/` は、トップレベルの `guidelines/` へのシンボリックリンクになっている。install時に `cp -RL` で実体化する。

## 使い方

### guidelineを直接参照する

`guidelines/` 配下のファイルを執筆時に手元で参照する。または、AIツール（Claude Code等）に読み込ませて執筆・レビュー補助に使う。何を書くときも `common_guideline.md` を土台にし、本文なら文体に応じて `style_desu_masu.md` / `style_da_dearu.md` を、design noteなら `design_note_guideline.md` を重ねて使う。

### skillを介する

skill定義を `~/.claude/skills/` にコピーする。シンボリックリンクを実体化するため `-L` を付ける：

```
cp -RL skills/design-note skills/write-body skills/style-review ~/.claude/skills/
```

skillは skill 名または近い自然言語で起動する：

- **design-note作成**: 「design note作って」「構成考えて」「アウトライン作って」など
- **本文執筆**: 「本文書いて」「design noteから本文」「write-body」など
- **style-review**: 「文体チェックして」「style-review」「writing-kitのguidelineに照らしてレビューして」など

## 執筆の流れ

このkitが想定している執筆フローは以下：

1. トピック・素材・書きたい方向性を整理する
2. `design-note` skillでdesign noteを作る、または直接 `guidelines/common_guideline.md` と `guidelines/design_note_guideline.md` を参照して自分で書く
3. `write-body` skillでdesign noteから本文を書き起こす、または自分で `guidelines/common_guideline.md` と文体別ガイド（`style_desu_masu.md` / `style_da_dearu.md`）の規約に従って書く
4. 書き上がった本文を `style-review` skillでチェック、または自分で該当guidelineと照合する

design noteは論の設計図であり、本文の下書きではない。ここで論の流れと素材の配置を確定させ、言い回しは本文執筆時に考える。定説と自分の推論のどちらなのか（認識の帰属）もdesign noteの段階で読み取れる形にしておく。
