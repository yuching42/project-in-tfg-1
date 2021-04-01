#iGame: 江湖大夢小遊戲仿作
#Author: 10730906李星辰、10730914洪于晴
#Version: 1.0
#Date: 2019/4/10
#題庫參考 http://www.taiwantestcentral.com/Quiz/Quiz.aspx?MainCategoryID=17&CategoryID=21&IsEngQ=0&ProblemCount=10

#random的函數參考資料： http://docs.python.org/lib/module-random.html

#時間函數參考http://tw.gitbook.net/python/python_date_time.html

#----------引入必要模組----------------#
import random
from os import sys

#----------設定重要全域變數----------------#

Roles = ['武當','雲夢','華山','少林','暗香','滄海',]			#角色清單
HPs = [1000,1000,2000,5000,1500,2000] 	#血量清單
Lifes = [3,4,2,1,2,2]		#生命值清單
HP = 0					  			#血量初始值
Life = 0					  		#生命值初始值
Role = 'NONAME'		  		#角色初始值
level = 1					  		#關卡初始值
XP = 0						  		#玩家經驗值

#----------SHOW GAME MESSAGE----------------#
def showGameMessage():
	print('初入江湖，聲名鵲起。\n你的江湖夢，由你自己定義......\n\n*答題時請輸入阿拉伯數字，請勿加上其他符號\n*歡迎捉蟲')

#----------Choose a Role----------------#
def chooseRole():
	global Role,HP,Life
	print('\n你是哪個門派弟子呢？')
	input('開始 ➽ (押ENTER)  ')
	global k
	k = random.randint(0,5)		#抽選角色號碼
	Role = Roles[k]
	HP += HPs[k]
	Life = Lifes[k]
	print('你是', Role ,'弟子\n\n路遇書生，手拿著書纏著你不放，堅持要問你問題。\n有什麼辦法呢？你也很無奈啊。\n"讓我來考考你！"\n')
	

#----------Show Status----------------#
def showStatus():
	print('\n目前總血量:',HP)
	print('目前生命值:',Life)
	print('目前經驗值:',XP)	
  

#----------定義關卡選單----------------#
def chooseLevel():
	print('\n*************************')
	print('1:天選初試')
	print('2:天選複試')
	print('3:天選終試')
	print('其他:Quit')
	print('\n*難易程度：初試<複試<終試\n*通過三場考試後即結束:)')
	showStatus()
	print('*************************')
	global level
	level = int(input('參加哪場考試？:'))

#----------定義GAME OVER----------------#

def endGame(): 
  global HP,XP,Life
  if Life == 0 and HP == 0:
    showStatus()
    print('\n"少俠的學問......稍嫌不足啊！"\n書生搖了搖頭，晃晃手中書卷，\n"還請多多充實自我，下回再向少俠討教！"\n\n遊戲結束，感謝支持')
    sys.exit()
  elif HP <= 0 :
    HP = HPs[k]
    Life -= 1
  if XP >= 3:
    print('\n你通過了三次測試，\n"少俠真是學富五車！"\n書生鼓鼓掌，\n"在下受益良多，下回再向少俠討教！\n\n遊戲結束，感謝支持')
    sys.exit()

#----------存放題目清單與答案清單-------#

Qx = ['招式以慈悲與佛法聞名江湖的門派是哪個？ \n1.少林\n2.雲夢\n3.華山\n4.暗香','《西遊記》中孫悟空是由(__)變化來的。 \n1.器皿\n2.頑石\n3.朽木\n4.青竹葉','荳蔻是指幾歲？ \n1.二十\n2.十八\n3.十五\n4.十三','"(____)，心有靈犀一點通" \n1.人生自古誰無死\n2.畫樓西畔桂堂東\n3.身無彩鳳雙飛翼\n4.昨夜星辰昨夜風','"詩中有畫，畫中有詩"是蘇軾對誰的評價？ \n1.杜甫\n2.白居易\n3.李白\n4.王維','楚留香以甚麼功夫聞名江湖？ \n1.輕功\n2.隱身\n3.劍術\n4.棍法','"詩仙"是指哪位詩人？ \n1.杜甫\n2.李清照\n3.王維\n4.李白','"賣炭翁，伐薪燒炭南山中"中的南山指的是？\n1.華山\n2.泰山\n3.終南山\n4.西陵山','戰國時提出"民為貴"的思想家為？ \n1.孔子\n2.孟子\n3.墨子\n4.韓非','杜甫漂泊一生，留下不少住所，其中最著名的杜甫草堂位於(__)？\n1.重慶\n2.昆明\n3.成都\n4.貴陽'] 
Ax = [1,2,4,3,4,1,4,3,2,3]

Qy = ['"北冥有魚，其名為鯤"出自？ \n1.老子\n2.孟子\n3.論語\n4.莊子','《水滸傳》中綽號"神行太保"的是？ \n1.吳用\n2.戴宗\n3.盧俊義\n4.公孫勝','西湖白堤是因紀念某個詩人而得名。"賣炭翁，伐薪燒炭南山中"是他的作品。試問此詩人為誰？ \n1.杜甫\n2.李白\n3.白居易\n4.白娘子','趙州橋始建於哪個朝代？ \n1.隋朝\n2.戰國\n3.北宋\n4.唐朝','"李長吉"是？ \n1.李鬼\n2.李賀\n3.李世民','《水滸傳》中，綽號為"一枝花"的是（__） \n1.蔡福\n2.燕青\n3.蔡慶\n4.李俊','"鍥而捨之，（__）；鍥而不捨，（__）"  \n1.與山間之明月；耳得之而為聲\n2.望帝春心托杜鵑；滄海月明珠有淚\n3.朽木不折；金石可鏤\n4.千里澄江似練；征帆去棹殘陽裡','諸葛亮曾在襄陽隆中隱居，躬耕苦讀幾年？ \n1.五年\n2.十年\n3.十五年\n4.二十年','"文章合為時而著，歌詩合為事而作"是由誰提出的？ \n1.劉禹錫\n2.周敦頤\n3.柳宗元\n4.白居易','"兩情若是長久時，又豈在朝朝暮暮"語出：\n1.曾鞏\n2.蘇軾\n3.秦觀\n4.李清照']
Ay = [4,2,3,1,2,3,3,2,4,3]

Qz = ['"將相和"這個故事的主人公是趙國的(_) \n1.廉頗與藺相如\n2.大將秦瓊與秦國的丞相\n3.呂不韋與嬴政','"入木三分"原意用來形容（__） \n1.射箭本領高\n2.雕刻技術高\n3.書法筆力強勁\n4.文章深刻','"新來瘦，非乾病酒，不是悲秋"出自以下哪個詞人？ \n1.辛棄疾\n2.蘇軾\n3.李煜\n4.李清照','漢代編戶制度實施的主要目的是？ \n1.實行寬舒政策\n2.組織農業生產\n3.控制和剝削人民\n4.抵抗水旱災害','"曉看紅濕處，花重錦官城"中所指的"錦官城"是指現代的哪座城市？ \n1.成都\n2.揚州\n3.杭州\n4.蘇州','以下歷史事件中，與關羽無關的是： \n1.大意失荊州\n2.單刀赴會\n3.水淹七軍\n4.七擒七縱','孫悟空為醫活人參樹，去三島求方，請問是哪三島？ \n1.蓬萊、瀛洲、瑤池\n2.蓬萊、瀛洲、方丈\n3.蓬萊、普陀、方丈\n4.蓬萊、普陀、瑤池','歷史上"圍魏救趙"戰術最初運用於（__）之戰 \n1.城淮\n2.桂陵\n3.馬陵\n4.長平','朱震亨是金元時期傑出的醫學家，他學醫雖晚，但終成大器，這主要得益於他潛心研究了被後人奉為"醫家之宗"的典籍（__） \n1.《黃帝內經》\n2.《千金方》\n3.《唐本草》\n4.《本草綱目》','下列史實，在《史記》和《漢書》中皆有記載的是（__） \n1.班超出使西域\n2.評定七國之亂\n3.城濮之戰\n4.設西域都護',]
Az = [1,3,4,3,1,4,2,2,1,2]

#----------定義遊戲關卡----------------#
def first():
  global HP
  items = range(9)
  nums = random.sample(items,5)
  
  for n in nums:
    endGame()
    print('\n'+ Qx[n])
    ans = int(input('你的回答：'))
    if ans == Ax[n]:
      print('正確答案！')
    else:
      HP += -500
      print('答錯囉，正確答案是' , Ax[n] , '\n血量扣500')
    showStatus()

def level1():
	global XP
	print('*************************')
	print('天選初試')
	first()
	XP += 1


#----------定義遊戲關卡----------------#
  
def second():
  global HP
  items = range(9)
  nums = random.sample(items,5)

  for n in nums:
    endGame()
    print('\n' + Qy[n])
    ans = int(input('你的回答：'))
    if ans == Ay[n]:
      print('正確答案！')
    else:
      HP += -500
      print('答錯囉，正確答案是' , Ay[n])
    showStatus()

def level2():        
	global XP
	print('*************************')
	print('天選複試')
	second()
	XP += 1	


#----------定義遊戲關卡----------------#

def third():
  global HP
  items = range(9)
  nums = random.sample(items,5)

  for n in nums:
    endGame()
    print('\n' + Qz[n])
    ans = int(input('你的回答：'))
    if ans == Az[n]:
      print('正確答案！')
    else:
      HP += -500
      print('答錯囉，正確答案是' , Az[n])
    showStatus()

def level3():        
	global XP
	print('*************************')
	print('天選終試')
	third()
	XP += 1	

#----------設計主程式流程----------------#

showGameMessage()
chooseRole()
while True:
  endGame()
  chooseLevel()
  
  if level==1:
    level1()
  elif level==2:
    level2()
  elif level==3:
    level3()
  else:
    print('\n書生猶豫片刻後點了點頭，\n"罷了，改日再向少俠討教！"\n他朝你一揖，\n"有緣江湖再會！"\n\n遊戲結束，謝謝支持')
    break
    
#----------程式結束----------------#