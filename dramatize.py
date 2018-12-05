# squashes values of x because brightness was overrepresented
# polynomial discovered by finding a few good-looking brightness points and interpolating with
# https://www.wolframalpha.com/input/?i=fit+curve+to+points+(0,0),(80,0),(160,10),(200,50),(255,255)
# the closest real math function is an exponential but i'm lazy
def dramatize(x):
    x = (1979 * x**4) / 5617920000 - (4169 * x**3) / 34048000 + (21269 * x**2) / 1478400 - (12819 * x) / 23408
    x = int(x)

    # clamp to valid values
    x = min(255, max(0, x))

    return x
