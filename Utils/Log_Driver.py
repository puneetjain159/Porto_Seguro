import os
import logging

def get_log(Name,loglevel = 'INFO'):

#    logging.basicConfig(filename = log_dir + log_name,
#                        disable_existing_loggers = False,
#                        filemode ='w',
#                        format = '%(asctime)s %(message)s')

    
    log_dir = os.getcwd() + "/logs/"
    if not os.path.isdir(log_dir):
        os.makedirs(log_dir)

    if Name == '':
        log_name = 'run_' + "version" + '.log'
    else:
        log_name = Name + '.log'
        
    #open(log_dir + log_name, 'w').close()
        
    log_obj = logging.getLogger("__info__")

    if loglevel == 'INFO':
        log_obj.setLevel(logging.INFO)
        print(1)
    elif loglevel == 'DEBUG':
        log_obj.setLevel(logging.DEBUG)
    elif loglevel == 'ERROR':
        log_obj.setLevel(logging.ERROR)
    elif loglevel == 'WARNING':
        log_obj.setLevel(logging.WARNING)
        
    fh = logging.FileHandler(log_dir + log_name,mode = 'w')
    formatter = logging.Formatter('%(asctime)s - %(name)s -%(message)s')
    
    
    fh.setFormatter(formatter)
    
    log_obj.addHandler(fh)

    

    return log_obj


def reinitiate_logfile(log,name):
    log_dir = os.getcwd() + "/logs/"
    
    if name == '':
        log_name = 'run_' + "version" + '.log'
    else:
        log_name = name + '.log'
    
    log.handlers[0].stream.close()
    log.removeHandler(log.handlers[0])
    
    open(log_dir + log_name, 'w').close()
    
    fh = logging.FileHandler(log_dir + log_name,mode = 'w')
    formatter = logging.Formatter('%(asctime)s - %(name)s -%(message)s')
    
    
    fh.setFormatter(formatter)
    
    log.addHandler(fh)
    return log
    
    
    
    
    
    