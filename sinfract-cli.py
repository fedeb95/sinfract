import argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.io.wavfile import write

import sinfract 

SPEED = 1.1

def animate(frame, args, ax):
    if frame == 0:
        frame = 1
    start = args.xstart / (SPEED**frame)
    end = args.xend / (SPEED**frame)
    x = np.linspace(start, end, args.precision)
    data = calc_data(x, args)   
    #line.set_ydata(data)
    ax.clear()
    return ax.plot(x, data)


def calc_data(x, args):
    if args.method == 'bessel':
        return sinfract.bessel(x, 
                  args.depth, 
                  args.frequency, 
                  args.mod_frequency,
                  args.beta)
    elif args.method == 'sinfract':
        return sinfract.sinfract(x,
                args.depth,
                args.a_param,
                args.frequency,
                args.scale)
    else:
        return sinfract.weierstrass(x, 
                                    args.depth,
                                    args.a_param,
                                    args.b_param,
                                    args.frequency)


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
                        type=int, 
                        default=100,
                        dest="depth")
    parser.add_argument('-s',
                        '--scale',
                        help="scaling factor at each step, use with sinfract method",
                        type=float,
                        default=2,
                        dest="scale")
    parser.add_argument('-p',
                        '--precision',
                        help="precision of the x axis",
                        type=int,
                        default=1000,
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
                        help="a parameter, use with weierstrass or sinfract method",
                        type=float,
                        default=0.2,
                        dest="a_param")

    parser.add_argument('-f',
                        '--frequency',
                        help="strarting frequency of function, use with bessel or sinfract method",
                        type=float,
                        default=1,
                        dest="frequency")
    parser.add_argument('-fm',
                        '--mod-freq',
                        help="frequency of modulator, use with bessel method",
                        type=float,
                        default=1,
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
    parser.add_argument('-anim',
                        '--animate',
                        help="animate plot",
                        action="store_true",
                        dest="anim")


    args = parser.parse_args()

    x = np.linspace(args.xstart, args.xend, args.precision)

    fig, ax = plt.subplots()
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    data = calc_data(x, args)
    line, = ax.plot(x, data)

    print(args.depth)

    if args.anim:
        anim_running = True
        anim = animation.FuncAnimation(
            fig, animate, fargs=(args,ax), interval=50)
        def onClick(event):
            nonlocal anim_running
            if anim_running:
                anim.event_source.stop()
                anim.frame_seq = anim.new_frame_seq()
                anim_running = False
            else:
                anim.event_source.start()
                anim_running = True
        fig.canvas.mpl_connect('button_press_event', onClick)
    else:
        plt.plot(x, data, 'b-')
    
    mng = plt.get_current_fig_manager()
    mng.resize(*mng.window.maxsize())
    plt.show()

    if args.audio:
        if args.precision % 44100 != 0:
            print("WARNING: precision not a multiple of 44100")
        print("saving function as audio...")
        scaled = np.int16(data/np.max(np.abs(data)) * 32767)
        write('{}-f{}-s{}-d{}.wav'.format(args.method, args.frequency, args.scale, args.depth), 44100, scaled)

    # show the plot
    plt.show()
if __name__=='__main__':
    main()
