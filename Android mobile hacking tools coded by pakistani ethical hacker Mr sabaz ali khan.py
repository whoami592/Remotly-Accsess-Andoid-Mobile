import os
import sys
import time
import subprocess

def check_adb():
    try:
        subprocess.check_output(['adb', '--version'])
    except subprocess.CalledProcessError:
        print("ADB is not installed or not in the PATH.")
        sys.exit(1)

def install_app(apk_path):
    subprocess.call(['adb', 'install', apk_path])

def uninstall_app(package_name):
    subprocess.call(['adb', 'uninstall', package_name])

def take_screenshot():
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    screenshot_name = f"screenshot_{timestamp}.png"
    subprocess.call(['adb', 'shell', 'screencap', '-p', f'/sdcard/{screenshot_name}'])
    subprocess.call(['adb', 'pull', f'/sdcard/{screenshot_name}', '.'])
    print(f"Screenshot saved as {screenshot_name}")

def record_audio():
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    audio_name = f"audio_{timestamp}.mp3"
    subprocess.call(['adb', 'shell', 'screenrecord', '--bit-rate', '320000', f'/sdcard/{audio_name}'])
    subprocess.call(['adb', 'pull', f'/sdcard/{audio_name}', '.'])
    print(f"Audio recording saved as {audio_name}")

def capture_video():
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    video_name = f"video_{timestamp}.mp4"
    subprocess.call(['adb', 'shell', 'screenrecord', f'/sdcard/{video_name}'])
    subprocess.call(['adb', 'pull', f'/sdcard/{video_name}', '.'])
    print(f"Video recording saved as {video_name}")

def main():
    check_adb()

    print("Welcome to the Android Hacking Tools!")
    print("Please select an option:")
    print("1. Install App")
    print("2. Uninstall App")
    print("3. Take Screenshot")
    print("4. Record Audio")
    print("5. Capture Video")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        apk_path = input("Enter the path to the APK file: ")
        install_app(apk_path)
    elif choice == '2':
        package_name = input("Enter the package name of the app: ")
        uninstall_app(package_name)
    elif choice == '3':
        take_screenshot()
    elif choice == '4':
        record_audio()
    elif choice == '5':
        capture_video()
    elif choice == '6':
        print("Exiting...")
        sys.exit(0)
    else:
        print("Invalid choice. Exiting...")
        sys.exit(1)

if __name__ == '__main__':
    main()