import subprocess
import os
import pickle
import re
import sys
import datetime

# settings
app_name = 'battery_alarm'
base_dir = os.environ['HOME'] + '/portal/' + app_name + '/'
state_file = base_dir + 'state'
batt_log_file = base_dir + 'm1pro_batt_percent.log'

def alarm(batt_percent):
    '''
    alarm work

    batt_percent: battery percent
    '''
    os.system('open ' + base_dir + app_name + '.app')

def get_batt_percent():
    '''
    배터리 퍼센트 가져오기

    return: battery percent
    '''
    cmd_result = subprocess.check_output(['pmset', '-g', 'batt'], universal_newlines=True)
    batt_percent = re.findall('\d*%', cmd_result)[0]
    batt_percent = int(batt_percent[:-1])
    return batt_percent

def read_state():
    '''
    Read state
    * state: 배터리가 경고 범위 안일 때 알람이 매 분 울리지 않고 한 번만 울리도록 조절하는 변수(state)

    return: state. default True(alarm available)
    '''
    if os.path.exists(state_file):
        with open(state_file, 'rb') as f:
            state = pickle.load(f)
        return state
    return True

def batt_check():
    '''
    배터리 잔량 체크
    '''
    percent = get_batt_percent()
    log_batt_percent(percent)
    state = read_state()
    if (percent <= 20) or (80 <= percent):
        if state:
            alarm(percent)
            state = False
    else:
        state = True
    save_state(state)

def log_batt_percent(batt_percent):
    '''
    배터리 퍼센트 로그 찍기
    '''
    with open(batt_log_file, 'a') as f:
        f.write(str(datetime.datetime.now()) + ':\t' + str(batt_percent) + '%\n')

def save_state(state):
    '''
    상태 저장
    '''
    with open(state_file, 'wb') as f:
        pickle.dump(state, f)

def main():
    # 명령행 인자
    what = sys.argv[1]
    if what == 'check':
        batt_check()
    elif what == 'state':
        print(read_state())

if __name__ == '__main__':
    main()
