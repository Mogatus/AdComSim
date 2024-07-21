# Simulation AdCom

import matplotlib.pyplot as plt
import numpy as np

BASELINE = [[1, 1], [1, 1], [1, 1]]  # power, time - how many, how fast per row
ROWPROPS_1 = [[1, 8], [1, 1], [1, 1]]  # power, time - how many, how fast
ROWPROPS_2 = [[1, 4], [1, 2], [1, 1]]  # power, time - how many, how fast


NUMOFSIMS = 10


def main():
    print(f'Start of program')  # Press Strg+F8 to toggle the breakpoint.
    allBaseCurVals, countBaseCurrency, countRows = init()
    xpoints, ypoints = doSim(allBaseCurVals, countBaseCurrency, countRows, BASELINE)
    doPlot(xpoints, ypoints, 'Base Line')

    allBaseCurVals, countBaseCurrency, countRows = init()
    xpoints, ypoints = doSim(allBaseCurVals, countBaseCurrency, countRows, ROWPROPS_1)
    doPlot(xpoints, ypoints, 'Increasing speed of upper row')

    allBaseCurVals, countBaseCurrency, countRows = init()
    xpoints, ypoints = doSim(allBaseCurVals, countBaseCurrency, countRows, ROWPROPS_2)
    doPlot(xpoints, ypoints, 'Increasing speed of lower row')

    plt.show()


def doSim(allBaseCurVals, countBaseCurrency, countRows, ROWPROPS):
    for i in range(NUMOFSIMS):
        for j in range(len(ROWPROPS) - 1, -1, -1):
            if j > 0:
                countRows[j - 1] = countRows[j - 1] + countRows[j] * ROWPROPS[j][0] * ROWPROPS[j][1]
            else:
                countBaseCurrency = countBaseCurrency + countRows[j] * ROWPROPS[j][0] * ROWPROPS[j][1]
                allBaseCurVals.append(countBaseCurrency)

        print(f'1, 0, base: {countRows[1]}, {countRows[0]}, {countBaseCurrency}')
    xpoints = np.array(range(0, NUMOFSIMS))
    ypoints = np.array(allBaseCurVals)
    return xpoints, ypoints


def doPlot(xpoints, ypoints, title):
    plt.plot(xpoints, ypoints, label=title)
    plt.legend()
    plt.title('AdCom Simulation')
    plt.xlabel('s')
    plt.ylabel('val')
    print(f'{title}: {ypoints}')


def init():
    countBaseCurrency = 0
    allBaseCurVals = []
    countRows = []
    for i in range(len(ROWPROPS_1)):  # incl BaseCurrency
        countRows.append(1)
    return allBaseCurVals, countBaseCurrency, countRows


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
