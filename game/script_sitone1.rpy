label sitone1:
    
    #*si_3|６月１６日（ＳＡＴ）：しとねと買い物
    
    play music "sound/bgm/bgm_002.ogg"
    
    "しかし、やっぱり他にやることも無いので、とりあえずしとねにコンタクトを取ってみよう。"
    
    "案外相手をしてくれるかもしれない。"
    
    scene bg school gate
    with Fade(1, 0, 1)
    
    "流石に明良の目の前で今日の予定を組むわけには行かないので、校門を出たところでしとねに電話をかける。"
    
    play sound "sound/se/se_080.ogg"
    with Pause(1.4)
    
    play sound "sound/se/se_081.ogg"
    
    si "『はい、雨宮です』"
    
    so "『もしもし、お兄様ですが我が妹はそちらにいらっしゃるでしょうか？』"
    
    si "『……一体どこの誰に電話しているつもりなの？』"
    
    so "『いや、電話の出だしを円滑に進める方法を考えてみたんだが、どうやらいまいちだったみたいだな』"
    
    si "『うん』"
    
    "いつものことながら冷静で歯に衣着せぬ突込み。流石妹者。"
    
    so "『まあそれはともかく、今日は用事もなく暇なのでこの前言っていた買い物をしてしまおうかと思うんだが、しとねは今日用事があったりするか？』"
    
    si "『ううん、今日は何もないから構わないよ』"
    
    so "『そうか、なら丁度いいな。ついでにまだ昼食の用意をしていないようなら繁華街で食べるのもいいんじゃないかと思うんだけど』"
    
    si "『うーん、用意はそんなにしてないから問題ないけど、おにいちゃんはもしかして制服のままで行くつもりなの？』"
    
    so "『どうした？この兄の一張羅に疑問を差し挟む余地があるだろうか。いや、ない。(反語)』"
    
    si "『それじゃあすぐ行くから入り口のところで待ってて』"
    
    play sound "sound/se/se_081.ogg"
    
    "ふむ、しとねがここまでボケのあしらいがうまくなったのは明良を家に呼んだりしたからだろう。きっとそうに違いない。"
    
    play music "sound/bgm/sitone.ogg" fadeout 2.0
    
    scene bg bg_c05
    with Fade(1, 0, 1)
    
    "そんなわけで俺としとねは入り口で合流して、軽く昼食をとった後当初の目的である買い物に向かった。"
    
    so "「なあ、しとね。最近小売業界も寡頭競争が激しくて、生き残りのためにサービスで差別化を図る必要があるという話らしいな」"
    
    show sitone si_2_01
    with dissolve
    
    si "「そうだね、この辺りでも結構お店が入れ替わってるしこの前も向こうの電気屋さんがドネルケバブ屋さんに変わっちゃったよ」"
    
    so "「そう、そしてそんな中でサービスとして定評があるのは、高齢者宅などに直接注文したものを届けてくれる配送サービスなわけだ」"
    
    si "「そうだね、やっぱり重いものを持って帰るのは大変だからそういうサービスは必要だと思うよ」"
    
    "そこで俺はしとねにたった今持ち運んでいる物を見せる。"
    
    so "「だったら、このひどく重い１０キロの米はわざわざ俺が運ばなくても、頼めば家まで店の人が持ってきてくれたんじゃないんでしょうかねええええ〜〜〜〜」"
    
    "そう、今日の買い物の目的は食料品の買出しであり、その買うべき物の中に、さっきから俺の身長を縮めるべく圧力をかけている米１０キロパックがあったわけだ。"
    
    show sitone si_2_04
    
    si "「え〜、買ったばっかのときは『俺はビリーバンド抜きでも理想的なボディを作ってやるＺＥ！』とか言ってたじゃない」"
    
    "まあそうやって調子に乗ったのは事実だ。"
    
    so "「いやいや確かにそんな発言をしましたごめんなさい。しかしまさかその後夏服を買いに行くとは思わず、正に重き荷を背負って坂道を行くが如しなのですが」"
    
    show sitone si_2_02
    
    si "「だって丁度セールをやってたし、せっかくだからおに　いちゃんに見てもらおうと思って」"
    
    so "「いや、そもそもそっちに行ってから——」"
    
    play sound "sound/se/se_002.ogg"
    
    so "「うおっ」"
    
    show sitone si_2_01
    
    "突然後ろから衝撃が加わる。"
    
    "振り向くとどうやら子供が走って来てぶつかったものだと判明する。"
    
    "子供の母親" "「すいません、どうもご迷惑をおかけして」"
    
    "少し遅れてぶつかった子供の親が追いついてきた。"
    
    so "「いえいえ」"
    
    "流石に不意を突かれたとはいえ、怪我などはあろうはずもない。"
    
    "子供の母親" "「たかし、危ないから走っちゃ駄目でしょ？」"
    
    "たかし" "「はい、お兄ちゃんごめんなさい」"
    
    "最近の子供にしては珍しく礼儀正しい子供だ。"
    
    "近頃はアクア・ネックレスを飲み込ませたくてたまらない子供が闊歩してるからな。"
    
    "子供の母親" "「本当に申し訳ありませんでした」"
    
    "そして親子はもう一度謝り、今度は手をつないで人ごみの中へと入り交じっていった。"
    
    "子供の性格というのは親に似るのか親によって自然に型にはめられていくのかという疑問はあるな。"
    
    show sitone si_2_09
    
    si "「ねえおにいちゃん」"
    
    so "「ん？」"
    
    si "「おにいちゃんって子供好き？」"
    
    "藪から棒な質問だな。"
    
    so "「そうだな、子供は時折うっとおしく感じることもあるけどあの純真さは嫌いじゃないな」"
    
    "どっちつかずの物言いではあるが、まあ正直な考えだ。"
    
    show sitone si_2_01
    
    si "「……うん、そうだよね。子供って可愛いよね」"
    
    "返ってきた言葉もあまり的を射ないものだったので多少違和感があったが、米袋を早く家に置きたいこともありしとねを促してさっさと帰ることにした。"
    
    stop music fadeout 2.0
    
    scene image "#000000"
    with Dissolve(3)
    
    jump main4