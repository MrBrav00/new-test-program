import threading
import time
import pyautogui

class Move(threading.Thread):
    def __init__(self):
        super(Move, self).__init__()
        self.centers = []
        self.active = False
        self.wait_time = 3.5
        self.screen_center = [756, 491]  # ← NEW for 1512 x 982
        self.running = True
        self.lock = threading.Lock()

    def update(self, centers, active, wait_time, screen_center):
        with self.lock:
            self.centers = centers
            self.active = active
            self.wait_time = wait_time
            self.screen_center = screen_center

    def run(self):
        while self.running:
            with self.lock:
                centers = self.centers[:]
                active = self.active
                wait_time = self.wait_time
                screen_center = self.screen_center

            if active and centers:
                # Sort by distance from screen center
                centers.sort(key=lambda pt: (pt[0] - screen_center[0])**2 + (pt[1] - screen_center[1])**2)
                target_x, target_y = centers[0]

                print(f"🎯 Clicking on: ({target_x}, {target_y})")
                pyautogui.moveTo(target_x, target_y, duration=0.3)
                pyautogui.click()
                time.sleep(wait_time)
            else:
                time.sleep(0.1)

    def stop(self):
        self.running = False
