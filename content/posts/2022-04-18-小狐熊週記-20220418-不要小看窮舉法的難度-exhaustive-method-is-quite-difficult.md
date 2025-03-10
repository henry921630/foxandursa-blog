---
title: "[小狐熊週記] 20220418 不要小看窮舉法的難度 Exhaustive method is quite difficult"
date: 2022-04-18T21:55:00+0800
draft: false
url: "/2022/04/20220418-exhaustive-method-is-quite.html"
tags: ['邏輯思考', '小狐熊週記']
---

之前曾經在小狐熊週記裡分享過MECE的思考技巧(mutually exclusive collectively exhaustive)，今天來談一個更加基本的思考方法：窮舉法。窮舉法，顧名思義就是窮盡所有可能性、通通舉列出來。簡單粗暴。
但常常我就連這麼簡單的事都做不好。分享兩個生活例子：
電梯進出可能性
有一天我們一家四口在某建築物的四樓等電梯，這棟樓最高只到六樓而已。
當時我們目睹了一台正要關門上樓的電梯裡恰有兩個人，門關上後，我們看著樓層面板，看到它到五樓時停了一下，然後到六樓也停了一下。
於是熊媽媽推測：他們一個人是去五樓、一個人是去六樓。

我立刻說這可未必，說不定他們兩個人都是去五樓、也有可能都是去六樓。畢竟我們無法肯定有沒有第三個人是要從五樓搭電梯去六樓、又或是從六樓搭下來。所以每一種進出情況都是有可能發生的！
正當我洋洋得意於自己成功地運用窮舉法完備了思考，就看到這台電梯從六樓漸漸回到了四樓。四樓電梯門一打開，剛剛那兩個人又走了出來……
我瞠目結舌……真的沒想到這兩人既不是去五樓、也不是去六樓。那他們到底在幹嘛？？？
這兩個人一出四樓電梯就開口問路，我才知道他們是要去另一棟樓的樓上，只是搭錯電梯了。
哈哈，原本我充滿自信的假說，才過不到一分鐘就被完全推翻。正好給大家都上了一課：永遠都要自己的想法保持謙虛、永遠都要對看似理所當然的事情保持質疑。你永遠不會知道那些你所不知道的事情。

銳角、鈍角與直角
有一天在公園，小狐撿了一根半折的樹枝。樹枝折而未斷，呈現出一個夾角。我們一家人就一邊撥弄這個樹枝、一邊對這個夾角做了一番討論。我說：這個夾角角度要嘛是鈍角、要嘛是銳角，要嘛就是直角！正當我洋洋得意於自己又成功地運用了窮舉法時，小狐就把這根樹枝折斷了……
……啊！根本無角，何來大小！？這下又出現我沒考慮到的情況了，我脆弱的窮舉法簡直不堪一擊。
而且這完全是個低級漏洞。好比是寫了一支很爛的程式，自以為已經考慮了全部情況：angle > 90 angle < 90angle == 90
結果卻忘了處理 angle == null 的情況……
對此我深感漸愧。繼續虛心練習。
對了，其實我的發言還有一個漏洞。因為鈍到不能再鈍的那個角，它並不叫做鈍角。它叫做平角。
所以比較完整的窮舉法至少要講成這樣：「這個樹枝夾角的角度要嘛是鈍角、要嘛是銳角、要嘛是直角、要嘛是平角，或者可能是根本沒有角。」

--
也許有讀者想抗議：這次小狐熊週記根本就沒有小狐熊的篇幅嘛！！

……嗯，你說的沒錯😄啊小狐熊雖然都全程在場，但就都沒有參與討論啊 ╮（╯＿╰）╭
![](https://blogger.googleusercontent.com/img/a/AVvXsEi4uLz5VaYMax63wVYgglMhC5X1cGm3moaNATfeZo9C-TGHyDkijhCuI0N6iyApfQ1DIvYsGDU82y9DkDyC9BeaRrgHXsOFLZjSJ7c2vbHaXBQbhaqDyKC9KpEknOUYv_yAJN1gp2wS78C6xK8pzXn-Afgbr78nExPtJNIr1HdKeDXR7_pl3VP8z655=w400-h300)


