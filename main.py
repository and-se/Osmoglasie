﻿#-------------------------------------------------------------------------------
# Name:        Основная программа
# Purpose:
#
# Author:      Танюшка
#
# Created:     15.05.2016
# Copyright:   (c) Танюшка 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import Osmoglasie

#Образец вставки текста
text = """С высоты{0} снизше{0}л еси{0} Благоутро{0}бне,/
погребе{0}ние прия{0}л еси{0} тридне{0}вное,/
да на{0}с свободи{0}ши страсте{0}й,//
Животе{0} и воскресе{0}ние на{0}ше. Го{0}cподи, сла{0}ва Тебе{0}.
""".format(chr(0x301) if True else '')


'''Обозначения:
    text -- идентификатор теста
    {0} -- спец символы ставящиеся после гласной, на которую падает ударение в слове
    .format(chr(0x301) if True else '') -- спец команда для преобразования символов в ударения
    / и // -- символы для разграничения колен
'''



'''text = """
С высоты снишел еси Благоутробне,/
погребение приял еси тридневное,/
да нас свободиши страстей,//
Животе и воскресение наше. Господи, слава Тебе.
"""
'''

text1 = """

Ка{0}мени запеча{0}тану от иуде{0}й /

и во{0}ином стрегу{0}щим Пречи{0}стое Те{0}ло Твое{0}, /

воскре{0}сл еси{0} тридне{0}вный, Спа{0}се, /

да{0}руяй ми{0}рови жи{0}знь. /

Сего{0} ра{0}ди Си{0}лы Небе{0}сныя вопия{0}ху Ти{0}, Жизнода{0}вче: /

сла{0}ва Воскресе{0}нию Твоему{0}, Христе{0}, /

сла{0}ва Ца{0}рствию Твоему{0}, //

сла{0}ва смотре{0}нию Твоему{0}, еди{0}не Человеколю{0}бче.

""".format(chr(0x301) if True else '')


text2 = """
Егда́ снизше́л еси́ к сме́рти, Животе́ Безсме́ртный,/
тогда́ а́д умертви́л еси́ блиста́нием Божества́:/
егда́ же и уме́ршия от преиспо́дних воскреси́л еси́,/
вся́ си́лы небе́сныя взыва́ху://
Жизнода́вче, Христе́ Бо́же на́ш, сла́ва Тебе́.
"""


text2_1 = """
Единоро́днаго  Сы́на  Бо́жия  возлюби́л  еси́,  /
и  Тому́  Еди́ному  служи́ти  возжеле́л  еси́,  /
свя́те  Иоа́нне,  Ему́же  вве́рился  еси́,  глаго́ля:  /
жи́знь  моя́  во  Христе́  е́сть. /
Сего́  ра́ди  потща́лся  еси́ /
вся́  ко  благоугожде́нию  Го́сподеви  //
и  му́дрствовати,  и  де́яти.
"""


text3 = """Да веселя́тся небе́сная, / да ра́дуются земна́я, / я́ко сотвори́ держа́ву /
 мы́шцею Свое́ю Госпо́дь, / попра́ сме́ртию сме́рть, / пе́рвенец ме́ртвых бы́сть; /
 из чре́ва а́дова изба́ви на́с, // и подаде́ ми́рови ве́лию ми́лость.
 """.replace(chr(0xf009), chr(0x301))

text4 = """
Све'тлую воскресе'ния про'поведь / от а'нгела уве'девша Госпо'дни учени'цы /
и пра'деднее осужде'ние отве'ргша, / апо'столом хва'лящася глаго'лаху:/
испрове'ржеся сме'рть,/ воскре'се Христо'с Бо'г,// да'руяй ми'рови ве'лию ми'лость.
""".replace("'", chr(0x301))


text4_1 = """
Еди́ному  Бо́гу  любо́вию  прилепля́яся,  свя́те  Иоа́нне,  /
 при́сно  попече́ние  о  стра́ждущих  и  отверже́нных  име́я,  /
   ско́рый  помо́щник  тем  яви́лся  еси́,  /
     сего́  ра́ди  си́ла  благода́ти  Бо́жия  /
      содева́ет  тобо́ю  ве́лия  чудеса́,  /
        обраща́я  неве́рных  к ве́ре  во  Христа́  //
          и  к  жи́зни  во  сла́ву  Бо́жию.
""".replace(chr(0xf009), chr(0x301))

text5 = """
Собезнача'льное Сло'во Отцу' и Ду'хови, / от Де'вы ро'ждшееся на спасе'ние на'ше,/
воспои'м, ве'рнии, и поклони'мся, / я'ко благоволи' пло'тию взы'ти на Кре'ст/
и сме'рть претерпе'ти, / и воскреси'ти уме'ршия // сла'вным воскресе'нием Свои'м.

""".replace("'", chr(0x301))


text5_1 = """
Служе'ние твое' испо'лнено сто'ном и го'рем, /
Священному'чениче Ти'хоне, Патриа'рше на'ш, /
Но бы'л еси' пра'вило ве'ры и о'браз кро'тости, /
Побежда'я ра'спри и разделе'ния, /
Си'лою смире'ния и любви' Христо'вой противоста'л еси' зло'бе сатани'нской,/
Возгла'вил еси' до'брое во'инство но'вых му'чеников//
Це'рковь Ру'сскую утверди'вших наве'ки.
""".replace("'", chr(0x301))

text6 = """

Живонача́льною дла́нию /
 уме́ршия от мра́чных удо́лий /
  Жизнода́вец воскреси́в всех Христо́с Бог, /
   воскресе́ние подаде́ челове́ческому ро́ду: /
    е́сть бо всех Спаси́тель, // Воскресе́ние и Живо́т, и Бо́г всех.
""".replace(chr(0xf009), chr(0x301))

text6_1 = """
Стра́х  Госпо́день  всели́ся  в  се́рдце  твое́,  /
и  от  сего́  разуме́л  еси́  лу́чшая,  /
е́же  по  Боже́ственному  пути́  ше́ствовати.  /
И  яви́лся  еси́  ра́вен  святы́м  отце́м,  Мака́рию  и  отцу́  Ону́фрию,  /
и  Па́влу  Фиве́йскому,  и  Макси́му  чу́дному,  и  Проко́пию:  /
си́х  подража́тель  изря́ден  бы́л  еси́  /
Ангельскаго  и  безвеще́ственнаго  жития́.  /
И  я́коже  Ангел  све́та  неизме́нно  рабо́тая  твоему́  Влады́це,/
преблаже́нне Васи́лие,  //  моли́  спасти́  ду́ши  на́ша.
""".replace(chr(0xf009), chr(0x301))


text7 = """Разру́шил еси́ Кресто́м Твои́м сме́рть, /
отве́рзл еси́ разбо́йнику ра́й, /
 мироно́сицам пла́ч преложи́л еси́, /
  и апо́столом пропове́дати повеле́л еси́, /
   я́ко воскре́сл еси́, Христе́ Бо́же, /
    дару́яй ми́рови//
     ве́лию ми́лость."""


text8 = """С высоты{0} снизше{0}л еси{0} Благоутро{0}бне,/
погребе{0}ние прия{0}л еси{0} тридне{0}вное,/ 
да на{0}с свободи{0}ши страсте{0}й,//
Животе{0} и воскресе{0}ние на{0}ше. Го{0}cподи, сла{0}ва Тебе{0}.
""".format(chr(0x301))

textStih1 = """Обыди{0}те лю{0}дие Сио{0}н, /
и обыми{0}те Его{0}, /
и дади{0}те сла{0}ву в не{0}м Воскре{0}сшему из ме{0}ртвых: /
я{0}ко То{0}й е{0}сть Бо{0}г на{0}ш, //
Избавле{0}й на{0}с от беззако{0}ний на{0}ших.""".format(chr(0x301) if True else '')

textStih1_1 = """
Стра'стию Твое'ю Христе', / от страсте'й свободи'хомся /
и воскресе'нием Твои'м из истле'ния изба'вихомся, //
Го'споди, сла'ва Тебе'.
""".replace("'", chr(0x301))

def demonstration():
    troparEx = [text1, text2, text3, text4, text5, text6, text7, text8]
    
    print("Воскресные тропари\n")
    
    for i in range(len(troparEx)):
        print("Глас", i+1, "\n")
        r = Osmoglasie.Markup(troparEx[i], i+1, "тропарь")
        print(r, "\n")
        
    print("Воскресные стихиры глас 1\n")
    
    stihEx = [textStih1, textStih1_1]
    
    for txt in stihEx:
        r = Osmoglasie.Markup(txt, 1, "стихира")
        print(r, "\n")
    


def main():
    demonstration()
    #glas = 5
    #txt = text5_1
    #r = Osmoglasie.Markup(txt, glas, "стихира")
    #r = Osmoglasie.Markup(txt, glas, "тропарь")
    #print(r)

if __name__ == '__main__':
    main()
