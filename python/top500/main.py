# -*- coding: utf-8 -*-
#top500中文名转全拼
#使用：https://pypi.python.org/pypi/pinyin4py ps这个说明文档简直shit！


from   pinyin import *


NameList=['张伟','王伟','王芳','李伟','李娜','张敏','李静','王静','刘伟','王秀英','张丽','李秀英','王丽','张静','张秀英','李强','王敏','李敏','王磊','刘洋','王艳','王勇','李军','张勇','李杰','张杰','张磊','王强','李娟','王军','张艳','张涛','王涛','李艳','王超','李明','李勇','王娟','刘杰','刘敏','李霞','李丽','张军','王杰','张强','王秀兰','王刚','王平','刘芳','张燕','刘艳','刘军','李平','王辉','王燕','陈静','刘勇','李玲','李桂英','王丹','李刚','李丹','李萍','王鹏','刘涛','陈伟','张华','刘静','李涛','王桂英','张秀兰','李红','李超','刘丽','张桂英','王玉兰','李燕','张鹏','李秀兰','张超','王玲','张玲','李华','王飞','张玉兰','王桂兰','王英','刘强','陈秀英','李英','李辉','李梅','陈勇','王鑫','李芳','张桂兰','李波','杨勇','王霞','李桂','王斌','李鹏','张平','张莉','张辉','张宇','刘娟','李斌','王浩','陈杰','王凯','陈丽','陈敏','王秀','李玉','刘秀','王萍','张波','刘桂','杨秀','张英','杨丽','张健','李俊','李莉','王波','张红','刘丹','李鑫','王莉','杨静','刘超','张娟','杨帆','刘燕','刘英','李雪','李秀','张鑫','王健','刘玉','刘辉','刘波','张浩','张明','陈燕','张霞','陈艳','杨杰','王帅','李慧','王雪','杨军','张旭','刘刚','王华','杨敏','王宁','李宁','王俊','刘斌','张萍','王婷','陈涛','王玉','王娜','张斌','陈龙','李林','张凤','王红','李凤','杨洋','李婷','张俊','王林','陈英','陈军','刘霞','陈浩','张凯','王晶','陈芳','张婷','杨涛','杨波','陈红','刘欢','陈娟','陈刚','王慧','张颖','张林','张娜','张玉','王凤','刘佳','刘磊','张倩','刘鹏','王旭','张雪','李阳','张秀','王梅','王建','王颖','刘平','杨梅','李飞','王亮','李磊','李建','王宇','陈玲','张建','刘鑫','王倩','张帅','李健','陈林','李洋','陈强','赵静','王成','陈超','陈亮','刘娜','王琴','张兰','张慧','刘畅','李倩','杨艳','张亮','李云','张琴','王兰','刘萍','陈桂','刘颖','杨超','张梅','陈平','刘红','赵伟','张云','张宁','杨林','张洁','高峰','杨阳','陈华','杨华','杨柳','刘阳','王淑','杨芳','李春','刘俊','王海','刘玲','陈晨','王欢','李冬','张龙','陈波','陈磊','王云','王峰','王瑞','李琴','陈鹏','王莹','刘飞','陈明','王桂','李浩','王志','张丹','李峰','刘凤','李佳','陈辉','张芳','李兰','陈玉','陈霞','刘凯','刘华','李兵','张雷','王东','王琳','李颖','杨伟','王龙','刘婷','陈秀','刘明','周敏','黄伟','张海','李志','杨磊','李晶','刘建','赵敏','陈云','李海','张桂','张晶','刘莉','李凯','张峰','张志','李龙','李帅','李欣','刘云','李洁','王春','陈斌','张莹','陈飞','王博','刘浩','黄秀','李淑','黄勇','周伟','李彬','王坤','刘慧','李想','张瑞','刘帅','张飞','王洋','陈洁','王荣','吴秀','杨明','马丽','刘倩','杨玲','杨平','王彬','李亮','李荣','李琳','李岩','王兵','王明','陈梅','张春','李杨','王岩','王冬','刘峰','杨雪','马秀','张淑','李小','张博','王欣','赵丽','张琳','黄敏','杨娟','王金','周杰','王雷','陈建','刘梅','杨桂','孙秀','赵军','赵勇','刘兵','杨斌','李文','陈琳','陈萍','孙伟','张利','陈俊','张楠','刘宇','赵秀','李博','王利','张荣','张帆','张瑜','周勇','张坤','徐伟','刘琴','周静','徐敏','徐静','杨红','王璐','张文','杨燕','周丽','陈鑫','马超']

s=Converter()

f = open('top500Name.txt','w')
for i in NameList:
    tmp = s.convert(i)
    tmp = tmp.split(' ')
    tmp = ''.join(tmp)
    print tmp
    f.write('%s\n'%tmp)
f.close()
