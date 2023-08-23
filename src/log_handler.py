import logging

logging.basicConfig(filename='example.log', level=logging.DEBUG, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 다양한 로그 수준의 메시지 기록
logging.debug('디버그 메시지')
logging.info('정보 메시지')
logging.warning('경고 메시지')
logging.error('오류 메시지')
logging.critical('치명적 오류 메시지')
