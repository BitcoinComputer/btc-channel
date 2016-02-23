import getopt
import sys
import os
import subprocess
import errno


class Application(object):

    CONFIG_DIRECTORY = "/var/lib/btc-channel"
    CHANNEL_CONFIG_FILE = "channel.conf"

    def __init__(self, *args, **kwargs):

        self.request_id = None

        self.configure = False
        self.create = False
        self.body = False
        self.verify_payment = False

        self.channel = None

        self.amount = None
        self.memo = None

    @staticmethod
    def usage():
        print "\nThis is the usage function\n"
        print 'Usage: '+sys.argv[0]+' -i <file1> [option]'

    @classmethod
    def get_channel(cls):

        config_path = os.path.join(
            cls.CONFIG_DIRECTORY,
            cls.CHANNEL_CONFIG_FILE
        )

        try:
            target = open(config_path, 'r')
            return target.readline()

        except IOError as e:
            message = "Error reading " + config_path + ": " \
                                 + os.strerror(e[0])

            print >> sys.stderr, message
            sys.exit(2)

    def arguments_are_valid(self):

        is_valid = True

        if not sum(
                [
                    self.configure,
                    self.create,
                    self.verify_payment,
                    self.body,
                ]
        ) == 1:
            is_valid = False

        if self.configure and not self.channel:
            is_valid = False

        if self.create and not self.amount:
            is_valid = False

        if self.verify_payment and not self.request_id:
            is_valid = False

        return is_valid

    def run(self, argv):

        try:
            opts, args = getopt.gnu_getopt(
                argv,
                "h",
                [
                    "help",
                    "configure",
                    "create",
                    "body",
                    "verify-payment",
                    "channel=",
                    "amount=",
                    "memo=",
                ])

        except getopt.GetoptError:
            self.usage()
            sys.exit(2)
        for arg in args:
            self.request_id = arg
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                self.usage()
                sys.exit()
            elif opt == "--configure":
                self.configure = True
            elif opt == "--create":
                self.create = True
            elif opt == "--verify-payment":
                self.verify_payment = True
            elif opt == "--body":
                self.body = True
            elif opt == "--amount":
                self.amount = arg
            elif opt == "--memo":
                self.memo = arg
            elif opt == "--channel":
                self.channel = arg

        if self.arguments_are_valid():
            self.process()
        else:
            self.usage()
            sys.exit(2)

    def process(self):

        if self.configure:
            config_path = os.path.join(
                self.CONFIG_DIRECTORY,
                self.CHANNEL_CONFIG_FILE
            )

            try:
                target = open(config_path, 'w')
                target.write(self.channel)

            except IOError as e:
                message = "Error authoring " + config_path + ": " \
                                     + os.strerror(e[0])

                print >> sys.stderr, message
                sys.exit(2)

        else:
            channel = self.get_channel()

            if self.create:
                result = subprocess.check_output(
                    [
                        channel,
                        "--create",
                        "--amount=" + self.amount,
                    ],
                    stderr=subprocess.STDOUT
                )

                print result

            elif self.body:
                result = subprocess.check_output(
                    [
                        channel,
                        self.request_id,
                        "--body",
                    ],
                    stderr=subprocess.STDOUT
                )

                print result

            elif self.verify_payment:
                result = subprocess.check_output(
                    [
                        channel,
                        self.request_id,
                        "--verify-payment",
                    ],
                    stderr=subprocess.STDOUT
                )

                print result


