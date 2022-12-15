# Line Bot Nanami Mami

## 角色介紹
![Mami](./img/Mami_profile2.png)
### 七海麻美
生日：11月13日  
星座：天蠍座  
聲優：悠木碧  
七海麻美是由宮島禮吏創作的漫畫《出租女友》及其衍生作品的登場角色。  
練馬大學一年級生，曾與木之下和也交往一個月（實際上是隨便答應的），隨後爽快地甩了他。表面上性格爽朗，實際上極度腹黑且善妒。  
是個家教嚴格的大小姊。因為小時候最心愛的娃娃被父親丟棄，以及被迫與喜歡的對象分手，造就了麻美腹黑的性格，願景是拆散世界上所有的情侶。  
本作唯一劇情推進擔當，沒有麻美沒有劇情進度，大約140話以後劇情進度開始停滯不前，然而現在已經畫到260幾話了（2022/12/15）

## Finite State Machine
![fsm](./img/fsm.png)

## 功能
* 歡迎訊息  
  （歡迎訊息截圖）
* user
  * 輸入`help`，Mami會貼心的告訴您她提供的服務項目  
  * 輸入`戀愛相談`，Mami會為您進行戀愛諮商
  * 輸入`戀人配對`，Mami會依您的生理性別為您尋找對象，還可以進一步作匹配度分析  
  * 輸入`獲取圖片`，即可以索取前一次`戀人配對`結果的照片
  * 輸入其他指令，Mami會進入*Idle*狀態，會隨機回覆一則訊息
* help  
<img
  src="/img/help1.jpg"
  alt="help1"
  title="help1"
  style="display: inline-block; margin: 0 auto; width: 400px">  
  * 點選`戀愛相談`，Mami會為您進行戀愛諮商  
  * 點選`戀人配對`，Mami會為您尋找對象  
* love_consultant `戀愛相談`  
  
* pair `戀人配對`

* idle `其他指令`  
  進入*Idle*狀態的Mami會隨機回覆一則訊息喔（共5種回覆）  
  <img
  src="/img/idle1.jpg"
  alt="idle1"
  title="idle1"
  style="display: inline-block; margin: 0 auto; height: 200px">
  <img
  src="/img/idle2.jpg"
  alt="idle2"
  title="idle2"
  style="display: inline-block; margin: 0 auto; height: 200px">
  <img
  src="/img/idle3.jpg"
  alt="idle3"
  title="idle3"
  style="display: inline-block; margin: 0 auto; height: 200px">
  <img
  src="/img/idle4.jpg"
  alt="idle4"
  title="idle4"
  style="display: inline-block; margin: 0 auto; height: 300px">
  <img
  src="/img/idle5.jpg"
  alt="idle5"
  title="idle5"
  style="display: inline-block; margin: 0 auto; height: 300px">
## 彩蛋

* mad  
  在任何時候輸入`和也`、`木之下和也`、`Kazuya`，Mami會進入*mad*狀態，會揭露她的本性  
  <img
  src="/img/kazuya1.jpg"
  alt="kazuya1"
  title="kazuya1"
  style="display: inline-block; margin: 0 auto; width: 300px">
  <img
  src="/img/kazuya2.jpg"
  alt="kazuya2"
  title="kazuya2"
  style="display: inline-block; margin: 0 auto; width: 300px">
  * pride  
  在*戀愛相談*狀態時，如果輸入的名字為`麻美`、`七海麻美`、`Mami`、`Nanami Mami`、`まみ`、`ななみまみ`、`マミ`、`ナナミマミ`，Mami會進入*pride*狀態，會狠狠的打槍您


