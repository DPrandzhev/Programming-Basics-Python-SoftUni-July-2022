percentage_loaded = int(input())


def loading_bar(percentage):
    percentage_symbols = percentage // 10
    dot_symbols = 10 - percentage_symbols
    bar = f"{percentage}% [{percentage_symbols * '%'}{dot_symbols * '.'}]"
    if percentage in range(0, 100):
        return f"{bar}\nStill loading..."
    elif percentage == 100:
        return f"100% Complete!\n[{percentage_symbols * '%'}]"


result = loading_bar(percentage_loaded)
print(result)