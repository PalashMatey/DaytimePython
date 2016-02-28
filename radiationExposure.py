def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)


def radiationExposure(start, stop, step):
    exposure = 0.0
    if start<0:
        return 0.0
    elif stop<=start:
        return 0.0
    else:
        timeofExposure = (stop-start)
        while stop>start:
            exposure = exposure + step*f(start)
            start = start + step
	return exposure
start = float(raw_input('Enter the start number: '))
stop = float(raw_input('Enter the stop number: '))
step = float(raw_input('Enter the step size: '))
ans = radiationExposure(start, stop, step)
print 'The amount of radiation is: ' + str(ans)

