def tempr(temp):
    def tempinf(temp):
        if isinstance(temp, int):
            return (9*temp/5)+32
    forein = tempinf(temp)
    print(forein)


tempr(50)
