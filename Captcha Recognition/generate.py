#!/usr/bin/env python3

import argparse
import os
import random

import captcha.image
import cv2
import numpy


def scramble_image_name(image_name):
    import hashlib
    m = hashlib.sha1()
    m.update(image_name.encode('utf-8'))
    return m.hexdigest()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--width', help='Width of captcha image', type=int)
    parser.add_argument('--height', help='Height of captcha image', type=int)
    parser.add_argument('--length', help='Length of captchas in characters', type=int)
    parser.add_argument('--count', help='How many captchas to generate', type=int)
    parser.add_argument('--scramble', help='Whether to scramble image names', default=False, action='store_true')
    parser.add_argument('--mapping', help='Where to save the scrambled to unscrambled mapping', type=str)
    parser.add_argument('--output-dir', help='Where to store the generated captchas', type=str)
    parser.add_argument('--symbols', help='File with the symbols to use in captchas', type=str)
    parser.add_argument('--seed', help='Seed for the captcha generator', type=str)
    args = parser.parse_args()

    if args.width is None:
        print("Please specify the captcha image width")
        exit(1)

    if args.height is None:
        print("Please specify the captcha image height")
        exit(1)

    if args.length is None:
        print("Please specify the captcha length")
        exit(1)

    if args.count is None:
        print("Please specify the captcha count to generate")
        exit(1)

    if args.output_dir is None:
        print("Please specify the captcha output directory")
        exit(1)

    if args.symbols is None:
        print("Please specify the captcha symbols file")
        exit(1)

    random_seed = None
    if args.seed is not None:
        random_seed = args.seed.encode('utf-8')

    random.seed(random_seed)

    captcha_generator = captcha.image.ImageCaptcha(width=args.width, height=args.height)

    symbols_file = open(args.symbols, 'r')
    captcha_symbols = symbols_file.readline().strip()
    symbols_file.close()

    print("Generating captchas with symbol set {" + captcha_symbols + "}")

    if not os.path.exists(args.output_dir):
        print("Creating output directory " + args.output_dir)
        os.makedirs(args.output_dir)

    mapping = None
    if args.mapping is not None:
        mapping = dict()

    for i in range(args.count):
        captcha_text = ''.join([random.choice(captcha_symbols) for j in range(args.length)])
        image_name_scrambled = captcha_text
        if args.scramble:
            image_name_scrambled = scramble_image_name(captcha_text)
            if args.mapping is not None:
                mapping[image_name_scrambled+'.png'] = captcha_text
        image_path = os.path.join(args.output_dir, image_name_scrambled+'.png')
        if os.path.exists(image_path):
            version = 1
            while os.path.exists(os.path.join(args.output_dir, image_name_scrambled + '_' + str(version) + '.png')):
                version += 1
            image_path = os.path.join(args.output_dir, image_name_scrambled + '_' + str(version) + '.png')

        image = numpy.array(captcha_generator.generate_image(captcha_text))
        cv2.imwrite(image_path, image)
        
        if i % 10000 == 0:
            print(str(i) + ' Done')

    if args.mapping is not None:
        with open(args.mapping, 'w') as mapping_file:
            for (hashed_text, orig_text) in mapping.items():
                mapping_file.write(hashed_text + ", " + orig_text + "\n")

if __name__ == '__main__':
    main()
