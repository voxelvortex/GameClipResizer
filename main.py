"""
Author: Michael Scalzetti
github.com/voxelvortex
main.py

This file runs the main bit of logic for the program to run properly
"""
import encoder


def main():
    input_video = "video/sniper.mp4"
    output_video = "video/sniper_trimmed.mp4"
    encoder.trim_video(input_video, output_video, "2:55", "3:11.5")


if __name__ =="__main__":
    main()
