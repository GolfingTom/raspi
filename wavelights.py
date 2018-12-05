def wave(strip, colorgreen=1, colorred=0, colorblue=0, iterations=10000, wait_ms=1, delay_ms=0):
    """   b   """
    direction = 1
    for i in range(iterations):
        for j in range(strip.numPixels()):
            resultant = math.sin(i /40 - j /3) * 128 + 128
            intensity = abs(resultant)
            strip.setPixelColor(j, int(colorgreen*intensity))
        strip.show()
        time.sleep(wait_ms/1000.0)
    time.sleep(delay_ms/1000.0)
