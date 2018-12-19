"""Client FIX"""
import sys
import argparse
import quickfix
from application import Application

def main(config_file):
    """Main"""
    try:
        settings = quickfix.SessionSettings(config_file)
        application = Application()
        storefactory = quickfix.FileStoreFactory(settings)
        logfactory = quickfix.FileLogFactory(settings)
        acceptor = quickfix.SocketAcceptor(application, storefactory, settings, logfactory)

        acceptor.start()
        application.run()
        acceptor.stop()
        

    except (quickfix.ConfigError, quickfix.RuntimeError) as e:
        print(e)
        acceptor.stop()
        sys.exit()

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='FIX Client')
    parser.add_argument('file_name', type=str, help='Name of configuration file')
    args = parser.parse_args()
    main(args.file_name)
