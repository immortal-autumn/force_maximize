# -*- coding: UTF-8 -*-

import time

import win32gui, win32api, pyautogui, win32con

title = {}
# Get system resolution
m_width, m_height = win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)


def get_hwnd(hwnd, mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
        text = win32gui.GetWindowText(hwnd)
        if text:
            title.update({hwnd: text})


win32gui.EnumWindows(get_hwnd, 0)

for h, t in title.items():
    if t:
        print(h, t)


def window_maximize(hwnd):
    win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)


# Automatically update the system - Assume w > h
def window_auto_update(hwnd):
    # Auto update
    # nw = int(m_width * (h / m_height))
    nw = int(m_height / h * w)
    # Centralise
    left = int((m_width - nw) / 2)
    win32gui.MoveWindow(hwnd, left if left > 0 else 0, 0, nw, m_height, True)


# Manually update
def window_manual_update(hwnd):
    nw = int(input('> New width is:'))
    nh = int(input('> New height is:'))
    left: int = (m_width - nw) / 2
    if left < 0:
        left = 0
    up: int = (m_height - nh) / 2
    if up < 0:
        up = 0
    win32gui.MoveWindow(hwnd, int(left), int(up), nw, nh, True)


options = {
    '0': exit,
    '1': window_maximize,
    '2': window_auto_update,
    '3': window_manual_update
}

# win32gui.SetForegroundWindow(c_hw)
# win32gui.ShowWindow(c_hw, win32con.SW_MAXIMIZE)
# win32gui.MoveWindow(6032768, 0, 0, 1920, 1080, True)
if __name__ == '__main__':
    print('Select your handle here (请选择窗口句柄-数字): ')
    selected_handle = int(input('>'))
    if selected_handle not in title.keys():
        print('Invalid input! Application will exit in 5 second...')
        time.sleep(5)
    lx, ly, rx, ry = win32gui.GetWindowRect(selected_handle)
    w = rx - lx
    h = ry - ly
    print(f'窗口高度为：{h}, 宽度为：{w}')
    print(f'Height：{h}, Width：{w}')
    print(f'Please select the following options:')
    print('1. Maximize the window - 窗口最大化')
    print('2. Modify the window automatically - 自动调整窗口 (长宽比不变)')
    print('3. Modify manually - 手动调节窗口')
    print('0. Exit - 退出')
    user_s = input('>')
    options[user_s](selected_handle)
    print('Finished! Issues please post on my github! Console will closed in 5 second!')
    time.sleep(5)
