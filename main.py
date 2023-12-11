try:
    print("to be")
    def out_red(text):
        print("\033[31m{}".format(text))
    out_red("or not")
    def out_red(text):
        print("\033[0m{}".format(text))
    out_red("to be")




except Exception as e:
    print(e)