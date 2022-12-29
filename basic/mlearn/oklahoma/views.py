from basic.mlearn.oklahoma.services import OklahomaService

OKLAHOMA_MENUS = ["종료",
                  "데이터구조파악",
                  "변수한글화",
                  "interval변수편집",
                  "ratio변수편집",
                  "nominal변수편집",
                  "ordinal변수편집",
                  "타깃",
                  "분할"]

oklahoma_menu = {"1": lambda t: t.spec(),
                 "2": lambda t: t.rename_meta(),
                 "3": lambda t: t.interval_variables(),
                 "4": lambda t: t.ratio_variables(),
                 "5": lambda t: t.nominal_variables(),
                 "6": lambda t: t.ordinal_variables(),
                 "7": lambda t: t.target(),
                 "8": lambda t: t.partition()}

if __name__ == '__main__':
    def my_menu(ls):
        for i, j in enumerate(ls):
            print(f"{i}. {j}")
        return input('메뉴선택: ')


    if __name__ == '__main__':
        t = OklahomaService()
        while True:
            menu = my_menu(OKLAHOMA_MENUS)
            if menu == '0':
                print("종료")
                break
            else:
                oklahoma_menu[menu](t)
                try:
                    oklahoma_menu[menu](t)
                except KeyError:
                    print(" ### Error ### ")