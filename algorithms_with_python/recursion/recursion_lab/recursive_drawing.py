def drawing_figure(number: int) -> None:
    if number == 0:
        return
    
    print("*" * number)
    drawing_figure(number - 1)
    print("#" * number)

number = int(input())

drawing_figure(number)