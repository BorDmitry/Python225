from D_Z_4_ParsingPages import Parser


def main():
    for i in range(5, 7):
        pars = Parser(f"https://www.ixbt.com/live/index/news/page{i}", "news_of_day.txt")
        pars.run()


if __name__ == '__main__':
    main()
