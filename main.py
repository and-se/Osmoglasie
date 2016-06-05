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

'''
text = """
С высоты снишел еси Благоутробне,/
погребение приял еси тридневное,/
да нас свободиши страстей,//
Животе и воскресение наше. Господи, слава Тебе.
"""
'''
text = """С высоты{0} снизше{0}л еси{0} Благоутро{0}бне,/
погребе{0}ние прия{0}л еси{0} тридне{0}вное,/
да на{0}с свободи{0}ши страсте{0}й,//
Животе{0} и воскресе{0}ние на{0}ше. Го{0}cподи, сла{0}ва Тебе{0}.
""".format(chr(0x301) if True else '')

text = """
Все́  отло́жь  мирско́е  мудрова́ние,  /
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

text =\
"""
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
    r = Osmoglasie.Markup(text, 6, "тропарь")

    print(r)

if __name__ == '__main__':
    main()
