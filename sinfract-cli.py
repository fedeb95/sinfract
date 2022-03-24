import argparse
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write

import sinfract 

def main():
    parser = argparse.ArgumentParser(description="sinfract-cli - CLI utility for weierstrass functions & friends")
    parser.add_argument('-m',
                        '--method',
                        help="function to plot",
                        default="weierstrass",
                        type=str,
                        dest="method")
    parser.add_argument('-d',
                        '--depth',
                        help="number of recurive steps",
                        type=float,
                        default=10,
                        dest="depth")
    parser.add_argument('-s',
                        '--scale',
                        help="scaling factor at each step",
                        type=float,
                        default=2,
                        dest="scale")
    parser.add_argument('-p',
                        '--precision',
                        help="precision of the curve",
                        type=int,
                        default=100,
                        dest="precision")
    parser.add_argument('-start',
                        '--start',
                        help="starting point of plot on x axis",
                        type=float,
                        default=-2,
                        dest="xstart")
    parser.add_argument('-end',
                        '--end',
                        help="end point of plot on x axis",
                        type=float,
                        default=2,
                        dest="xend")

    parser.add_argument('-b',
                        '--b',
                        help="b parameter, use with weierstrass method",
                        type=float,
                        default=7,
                        dest="b_param")
    parser.add_argument('-a',
                        '--a',
                        help="a parameter, use with weierstrass method",
                        type=float,
                        default=0.2,
                        dest="a_param")

    parser.add_argument('-f',
                        '--frequency',
                        help="strarting frequency of function, use with bessel method",
                        type=float,
                        default=1,
                        dest="frequency")
    parser.add_argument('-fm',
                        '--mod-freq',
                        help="frequency of modulator, use with bessel method",
                        type=float,
                        default=440,
                        dest="mod_frequency")
    parser.add_argument('-beta',
                        '--beta',
                        help="beta parameter of Bessel function, use with bessel method",
                        type=float,
                        default=1.0,
                        dest="beta")

    parser.add_argument('-audio',
                        '--audio',
                        help="save wave audio file",
                        action="store_true",
                        dest="audio")

    args = parser.parse_args()

    x = np.linspace(args.xstart, args.xend, args.precision)

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    if args.method == 'bessel':
        data = sinfract.bessel(x, 
                  args.depth, 
                  args.frequency, 
                  args.mod_frequency,
                  args.beta)
    else:
        data = sinfract.weierstrass(x, 
                                    args.depth,
                                    args.a_param,
                                    args.b_param,
                                    args.frequency)

    # plot the function
    plt.plot(x, data, 'b-')

    if args.audio:
        if args.precision % 44100 != 0:
            print("WARNING: precision not a multiple of 44100")
        print("saving function as audio...")
        scaled = np.int16(data/np.max(np.abs(data)) * 32767)
        write('{}-f{}-s{}-d{}.wav', 44100, scaled)

    # show the plot
    plt.show()
if __name__=='__main__':
    main()
