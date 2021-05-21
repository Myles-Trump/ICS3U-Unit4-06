#!/usr/bin/env python3

# Created by: Myles Trump
# Created on: May 2021
# This program prints every RGB combo


def main():
    # this function prints every RGB combo
    red = 0
    green = 0
    blue = 0

    # process & output
    for red in range(0, 256):
        for green in range(0, 256):
            for blue in range(0, 256):
                print("RGB ({0}, {1}, {2})".format(red, green, blue))


if __name__ == "__main__":
    main()
