import subprocess
import time


def get_latest_emulator() -> str:
    """Returns the most recently created AVD emulator name."""
    result = subprocess.run(
        ["emulator", "-list-avds"], capture_output=True, text=True
    )
    emulators = result.stdout.strip().split("\n")

    if not emulators:
        raise RuntimeError(
            "❌ No available emulators! Create one using AVD Manager."
        )

    return emulators[-1]


def is_emulator_running() -> bool:
    """Checks if an Android emulator is running."""
    result = subprocess.run(["adb", "devices"], capture_output=True, text=True)
    return "emulator-" in result.stdout


def wait_for_emulator_boot(timeout: int = 120) -> bool:
    """Waits until the emulator is fully booted."""
    start_time = time.time()
    while time.time() - start_time < timeout:
        result = subprocess.run(
            ["adb", "shell", "getprop", "sys.boot_completed"],
            capture_output=True,
            text=True,
        )
        if result.stdout.strip() == "1":
            print("✅ Emulator is ready!")
            return True
        time.sleep(5)
    raise RuntimeError("❌ Emulator did not boot in time!")


def start_emulator():
    """Starts an emulator if one is not already running."""
    if is_emulator_running():
        print("✅ Emulator is already running.")
        return

    emulator_name = get_latest_emulator()
    print(f"🚀 Starting emulator: {emulator_name}...")

    subprocess.Popen(
        ["emulator", "-avd", emulator_name, "-no-snapshot-load"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    if wait_for_emulator_boot():
        print("✅ Emulator started successfully!")


if __name__ == "__main__":
    print(start_emulator())
