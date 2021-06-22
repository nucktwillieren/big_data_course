# -*- coding: utf-8 -*-

from psychopy import visual, core, event

text = """
我與父親不相見已有二年餘了，我最不能忘記的是他的背影。那年冬天，祖母死了，父親的差使也交卸了，正是禍不單行的日子，我從北京到徐州，打算跟著父親奔喪回家。到徐州見著父親，看見滿院狼籍的東西，又想起祖母，不禁簌簌地流下眼淚。

父親說，「事已如此，不必難過，好在天無絕人之路！」

回家變賣典質，父親還了虧空；又借錢辦了喪事。這些日子，家中光景很是慘淡，一半為了喪事，一半為了父親賦閒。喪事完畢，父親要到南京謀事，我也要回到北京唸書，我們便同行。

到南京時，有朋友約去遊逛，勾留了一日；第二日上午便須渡江到浦口，下午上車北去。父親因為事忙，本已說定不送我，叫旅館裏一個熟識的茶房陪我同去。他再三囑咐茶房，甚是仔細。但他終於不放心，怕茶房不妥貼；頗躊躇了一會。其實我那年已二十歲，北京已來往過兩三次，是沒有甚麼要緊的了。他躊躇了一會，終於決定還是自己送我去。我兩三回勸他不必去；他只說，「不要緊，他們去不好！」

我們過了江，進了車站。我買票，他忙著照看行李。行李太多了，得向腳夫行些小費，才可過去。他便又忙著和他們講價錢。我那時真是聰明過分，總覺他說話不大漂亮，非自己插嘴不可。但他終於講定了價錢；就送我上車。他給我揀定了靠車門的一張椅子；我將他給我做的紫毛大衣鋪好坐位。他囑我路上小心，夜裏要警醒些，不要受涼。又囑託茶房好好照應我。我心裏暗笑他的迂；他們只認得錢，託他們直是白託！而且我這樣大年紀的人，難道還不能料理自己麼？唉，我現在想想，那時真是太聰明了。

我說道，「爸爸，你走吧。」他往車外看了看，說，「我買幾個橘子去。你就在此地，不要走動。」我看那邊月台的柵欄外有幾個賣東西的等著顧客。走到那邊月台，須穿過鐵道，須跳下去又爬上去。父親是一個胖子，走過去自然要費事些。我本來要去的，他不肯，只好讓他去。我看見他戴著黑布小帽，穿著黑布大馬褂，深青布棉袍，蹣跚地走到鐵道邊，慢慢探身下去，尚不大難。可是他穿過鐵道，要爬上那邊月台，就不容易了。他用兩手攀著上面，兩腳再向上縮；他肥胖的身子向左微傾，顯出努力的樣子。這時我看見他的背影，我的淚很快地流下來了。我趕緊拭乾了淚，怕他看見，也怕別人看見。我再向外看時，他已抱了朱紅的橘子往回走了。過鐵道時，他先將橘子散放在地上，自己慢慢爬下，再抱起橘子走。到這邊時，我趕緊去攙他。他和我走到車上，將橘子一股腦兒放在我的皮大衣上。於是撲撲衣上的泥土，心裏很輕鬆似的，過一會說，「我走了，到那邊來信！」我望著他走出去。他走了幾步，回過頭看見我，說，「進去吧，裏邊沒人。」等他的背影混入來來往往的人裏，再找不著了，我便進來坐下，我的眼淚又來了。

近幾年來，父親和我都是東奔西走，家中光景是一日不如一日。他少年出外謀生，獨立支持，做了許多大事。哪知老境卻如此頹唐！他觸目傷懷，自然情不能自已。情鬱於中，自然要發之於外；家庭瑣屑便往往觸他之怒。他待我漸漸不同往日。但最近兩年不見，他終於忘卻我的不好，只是惦記著我，惦記著我的兒子。我北來後，他寫了一封信給我，信中說道，「我身體平安，惟膀子疼痛厲害，舉箸提筆，諸多不便，大約大去之期不遠矣。」我讀到此處，在晶瑩的淚光中，又看見那肥胖的，青布棉袍，黑布馬褂的背影。唉！我不知何時再能與他相見！　　　　　

1925年10月在北京
"""

fontnames =[u'標楷體', u'微軟正黑體',u'華康魏碑體',u'華康楷書體注音']
fontnames2 =[u'DFKai-SB', u'Microsoft JhengHei',u'DFWeiBei-B5',u'DFKaiChuIn']
fontfiles =['','',['../fonts/weibai.ttc'], ['../fonts/hwakaiphone.ttc']]


#create a window to draw in
win = visual.Window(fullscr=True, pos=(0,0),winType='pyglet',allowGUI=None,monitor='testMonitor', units ='deg', screen=0)

textStim = visual.TextStim(win,text=text,
    pos=(-10,0),
    anchorHoriz="center",
    anchorVert="center",
    color=[1.0,1,1],
    units='deg',
    ori=0, height = 0.50,
    font=fontnames2[2],
    fontFiles=fontfiles[2],
    wrapWidth=5,
)
textStim.draw()
win.flip()

event.waitKeys()

win.close()