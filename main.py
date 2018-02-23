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


'''text = """
С высоты снишел еси Благоутробне,/
погребение приял еси тридневное,/
да нас свободиши страстей,//
Животе и воскресение наше. Господи, слава Тебе.
"""
'''
textStih1 = """Обыди{0}те лю{0}дие Сио{0}н, /
и обыми{0}те Его{0}, /
и дади{0}те сла{0}ву в не{0}м Воскре{0}сшему из ме{0}ртвых: /
я{0}ко То{0}й е{0}сть Бо{0}г на{0}ш, //
Избавле{0}й на{0}с от беззако{0}ний на{0}ших.""".format(chr(0x301) if True else '')

text1 = """С высоты{0} снизше{0}л еси{0} Благоутро{0}бне,/
погребе{0}ние прия{0}л еси{0} тридне{0}вное,/
да на{0}с свободи{0}ши страсте{0}й,//
Животе{0} и воскресе{0}ние на{0}ше. Го{0}cподи, сла{0}ва Тебе{0}.
""".format(chr(0x301) if True else '')

text2 = """
Все́  отло́жь  миро́ске  мудрова́ние,  /
поте́кл  еси́  ра́дуяся  /
в  сле́д  Христа́  Бо́га  на́шего.  /
Ему́же  во  все́м  животе́  твое́м  /
нело́жно  рабо́тая,  /
показа́л  еси́  труды́  и  по́двиги,  /
и  по́льзу  мно́гим  сотвори́л  еси́,  /
и  убели́л  еси́  ри́зу  душе́вную,
сне́га  беле́йши:  /
да  во  все́м  послушли́в  бы́в  Христу́,  //
со  дерзнове́нием  моли́ся    о  душа́х  на́ших.
"""

text3 = """
Единоро́днаго  Сы́на  Бо́жия  возлюби́л  еси́,  /
и  Тому́  Еди́ному  служи́ти  возжеле́л  еси́,  /
 свя́те  Иоа́нне,  Ему́же  вве́рился  еси́,  глаго́ля:  /
   жи́знь  моя́  во  Христе́  е́сть. /  Сего́  ра́ди  потща́лся  еси́ /
    вся́  ко  благоугожде́нию  Го́сподеви  //
     и  му́дрствовати,  и  де́яти.
""".replace(chr(0xf009), chr(0x301))

text4 = """
Еди́ному  Бо́гу  любо́вию  прилепля́яся,  свя́те  Иоа́нне,  /
 при́сно  попече́ние  о  стра́ждущих  и  отверже́нных  име́я,  /
   ско́рый  помо́щник  тем  яви́лся  еси́,  /
     сего́  ра́ди  си́ла  благода́ти  Бо́жия  /
      содева́ет  тобо́ю  ве́лия  чудеса́,  /
        обраща́я  неве́рных  к ве́ре  во  Христа́  //
          и  к  жи́зни  во  сла́ву  Бо́жию.
""".replace(chr(0xf009), chr(0x301))

text5 = """

Живонача́льною дла́нию /
 уме́ршия от мра́чных удо́лий /
  Жизнода́вец воскреси́в всех Христо́с Бог, /
   воскресе́ние подаде́ челове́ческому ро́ду: /
    е́сть бо всех Спаси́тель, // Воскресе́ние и Живо́т, и Бо́г всех.

""".replace(chr(0xf009), chr(0x301))

text6 = """
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



def main():
    glas = 1

    txt = textStih1

    r = Osmoglasie.Markup(txt, glas, "стихира")

    print(r)



if __name__ == '__main__':
    main()
