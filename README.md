# sinfract

![plot picture](/images/sinfract.png)

Python program to visualize, listen to and compute various fractal sinusoids.

`sinfract.py` contains methods to compute three types of functions:
- `weierstrass`: the famous [Weierstrass function](https://en.wikipedia.org/wiki/Weierstrass_function)
- `bessel`: a modified version of it adding ideas from [frequency modulation](https://en.wikipedia.org/wiki/Frequency_modulation) (TODO: explain better)
- `sinfract`: a recursive sinusoid (implemented as loop) defined as:
```
def sinfract(x, a, f, n, k):
    if n == 0:
        return 0
    return a*np.sin(2*np.pi*f*x) + sinfract(x, a/k, f*k, n-1, k)
```
it should be pretty similar to the Weierstrass function, however it gives funny outputs for instance with `s=2`.

## Quickstart

- install requirements with 
```
pip install -r requirements.txt
```
- run with
```
python sinfract-cli -anim
```
This will show an animation of the Weierstrass function.
Try other functions with the `--method` parameter, like `bessel` or `sinfract`. See below for more commands.

## Features

- plot a fractal function
- visualize and animation of a fractal function with `-anim` parameter
- listen to the sinusoids with `-audio` parameter (see below for tips)
- as a library, import `sinfract.py` to do what you want!

## Audio

Since the program needs to generate enough frames for the audio to play, and frequency shoudl be meaningful, a nice place to start is:
```
python sinfract-cli.py -m bessel -audio -f 256 -fm 1 -beta 1 -p 44100
```

In general, use `-p` with a multiple of 44100 to get some seconds of audio.

## Usage
```
usage: sinfract-cli.py [-h] [-m METHOD] [-d DEPTH] [-s SCALE] [-p PRECISION] [-start XSTART] [-end XEND]
                       [-b B_PARAM] [-a A_PARAM] [-f FREQUENCY] [-fm MOD_FREQUENCY] [-beta BETA]
                       [-audio] [-anim]

sinfract-cli - CLI utility for visualizing and listening to weierstrass functions & friends

optional arguments:
  -h, --help            show this help message and exit
  -m METHOD, --method METHOD
                        Function to plot. Values:
                            'weierstrass': classical Weierstrass function
                            'bessel': modified Weierstrass function,
                             so that a parameter equals a Bessel function of the first kind with parameter beta, 
                             and b parameter is (frequency+n*fm)^n
                            'sinfract': fractal sinusoid with amplitude a, frequency f and scale s
                                                    
  -d DEPTH, --depth DEPTH
                        number of summations to compute
  -s SCALE, --scale SCALE
                        scaling factor, use with sinfract method
  -p PRECISION, --precision PRECISION
                        precision of the x axis
  -start XSTART, --start XSTART
                        starting point of plot on x axis
  -end XEND, --end XEND
                        end point of plot on x axis
  -b B_PARAM, --b B_PARAM
                        b parameter, use with weierstrass method
  -a A_PARAM, --a A_PARAM
                        a parameter, use with weierstrass or sinfract method
  -f FREQUENCY, --frequency FREQUENCY
                        strarting frequency of function, use with bessel or sinfract method
  -fm MOD_FREQUENCY, --mod-freq MOD_FREQUENCY
                        frequency of modulator, use with bessel method
  -beta BETA, --beta BETA
                        beta parameter of Bessel function, use with bessel method
  -audio, --audio       save wave audio file
  -anim, --animate      animate plot

```
