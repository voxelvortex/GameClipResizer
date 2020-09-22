"""
Author: Michael Scalzetti
github.com/voxelvortex
encoder.py

This file runs the main bit of logic for the program to run properly
"""
import os


def trim_video(in_filename, out_filename, start, end):
    """
    This function trims videos using ffmpeg

    :param in_filename: relative path to the file that will be trimmed
    :param out_filename: relative path to where the script will write the output
    :param start: the start time in seconds, can include decimals
    :param end: the end time in seconds, can include decimals

    :return: None
    """
    command = "ffmpeg -i {0} -ss {2} -to {3} -c:v copy -c:a copy {1}".format(in_filename, out_filename, start, end)
    os.system(command)

