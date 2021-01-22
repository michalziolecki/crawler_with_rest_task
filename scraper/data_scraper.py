import getopt
import sys

from rest_framework.status import HTTP_200_OK, HTTP_300_MULTIPLE_CHOICES
from scraper_src.request_controller import RequestController


def main(argv):
    url = ''
    text_lookup = False
    img_lookup = False
    try:
        opts, args = getopt.getopt(argv, 'htil:', ['help', 'text', 'img', 'link='])
    except getopt.GetoptError:
        print('Correct run: `data_scraper.py -l <link> -t -i`')
        sys.exit(11)
    for opt, arg in opts:
        if opt == '-h' or opt == '--help':
            print('data_scraper.py -l <link> -t -i'
                  ' --link -l with address as argument'
                  ' --text -t lookup text on web'
                  ' --img -i lookup images on web')
            sys.exit(0)
        elif opt in ('-i', '--img'):
            img_lookup = True
        elif opt in ('-t', '--text'):
            text_lookup = True
        elif opt in ('-l', '--link'):
            url = arg

    if not text_lookup and not img_lookup:
        print('Nothing to looking for...')
        sys.exit(0)

    if not url:
        print('Incorrect input - link is empty!')
        sys.exit(12)

    controller = RequestController()
    http_status = controller.run_request(url, text_lookup, img_lookup)

    if http_status < HTTP_200_OK or http_status > HTTP_300_MULTIPLE_CHOICES:
        print(f'operation fail - http_status={http_status}')
        sys.exit(13)

    print(f'operation success!')
    sys.exit(0)


if __name__ == '__main__':
    main(sys.argv[1:])
