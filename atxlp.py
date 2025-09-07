# atxlp.py
import time
import threading
import random
import os
import dearpygui.dearpygui as dpg

# --- Globals ---
loading_progress = 0
max_time = 720   # full 12 min (change to smaller for testing)
running = True
DOCS_FILE = "about_docs.txt"

# --- Fake spoofing data ---
dlls = ["ntdll.dll", "kernel32.dll", "user32.dll", "dxgi.dll", "d3d11.dll"]
apis = ["VirtualAllocEx", "NtProtectVirtualMemory", "IDXGISwapChainPresent",
        "CreateProcessA", "OpenProcess", "ReadProcessMemory",
        "HWIDMask", "FortniteAuth", "SpoofGPUDriver", "RedirectEAC"]
errors = ["0xC0000005", "0x80070057", "0xDEADBEEF", "0x1337C0DE", "0xBAADF00D"]

phases = [
    "Initializing API build v0.1.27 (internal)",
    "Mounting memory pools...",
    "Checking kernel access layer...",
    "Validating EasyAntiCheat_x64.sys...",
    "Scanning offsets...",
    "Loading DirectX hooks...",
    "Injecting overlay render pipeline...",
    "Compiling shader bypass...",
    "Registering fake certificates...",
    "Patching watchdog threads...",
    "Syncing with remote build server...",
    "Finalizing API deployment..."
]

def generate_build_number():
    return f"32.{random.randint(10,99)}.{random.randint(0,9)}"

def generate_hwid():
    return f"{random.randint(1000,9999)}-{random.randint(1000,9999)}-" \
           f"{random.randint(1000,9999)}-{random.randint(1000,9999)}"

# --- Console Helpers ---
def log_to_console(msg, color=(200, 200, 200)):
    dpg.add_text(msg, parent="console", color=color)
    dpg.set_y_scroll("console", -1)

def random_log():
    c = random.choice
    return f"[{c(['INFO','WARN','ERROR','DBG'])}] {c(apis)} -> {c(dlls)} " \
           f"@0x{random.randint(0x1000,0xFFFF):04X} {c(errors)}"

def spoof_log():
    return random.choice([
        f"[INFO] Fortnite build {generate_build_number()} detected",
        f"[DBG] Applying HWID mask [{generate_hwid()}]",
        f"[INFO] Spoofing GPU driver ID {hex(random.randint(0x10000, 0xFFFFF))}",
        "[WARN] Redirecting EAC to Quacks layer",
        "[DBG] Validating spoof certificate chain",
    ])

def spam_console():
    while running:
        time.sleep(0.3)
        log_to_console(random.choice([random_log(), spoof_log()]), (150, 255, 150))

# --- Main Loading Simulation ---
def loading_thread():
    global loading_progress
    step_time = max_time // len(phases)

    for idx, phase in enumerate(phases):
        dpg.set_value("status", f"[BUILD] {phase}")
        log_to_console(f"[BUILD] {phase}", (100, 200, 255))

        # simulate work per phase
        for i in range(step_time):
            time.sleep(1)
            loading_progress += 1
            dpg.set_value("progress", loading_progress / max_time)
            dpg.set_value("status", f"[BUILD] {phase} ({loading_progress}/{max_time})")

    # Final spoof fail
    build_id = generate_build_number()
    dpg.set_value("status", f"[ERROR] Fortnite client mismatch (build {build_id})")
    log_to_console(f"[ERROR] Fortnite client mismatch (build {build_id})", (255, 80, 80))
    time.sleep(2)
    log_to_console("[ERROR] HWID spoof layer expired. Please update.", (255, 100, 100))

def start_loading():
    dpg.configure_item("start_btn", show=False)
    threading.Thread(target=loading_thread, daemon=True).start()
    threading.Thread(target=spam_console, daemon=True).start()

# --- Callbacks for UI ---
def on_checkbox(sender, app_data, user_data): log_to_console(f"[CHECKBOX] {user_data} = {app_data}")
def on_slider(sender, app_data, user_data): log_to_console(f"[SLIDER] {user_data} -> {app_data}")
def on_combo(sender, app_data, user_data): log_to_console(f"[COMBO] {user_data} = {app_data}")
def on_button(sender, app_data, user_data): log_to_console(f"[BUTTON] {user_data} clicked!")
def on_color(sender, app_data, user_data): log_to_console(f"[COLOR] {user_data} = {app_data}")

def on_menu(sender, app_data, user_data):
    if user_data in ["About ATXLP", "Documentation"]:
        try:
            with open(DOCS_FILE, "r") as f:
                log_to_console(f"===== {user_data} =====", (200, 200, 255))
                for line in f:
                    if line.strip():
                        log_to_console(f"[DOCS] {line.strip()}", (180, 180, 255))
        except FileNotFoundError:
            log_to_console(f"[ERROR] Could not find {DOCS_FILE}", (255, 100, 100))
    elif user_data == "Report Bug":
        log_to_console("[SYSTEM] Connecting to bug tracker...", (200, 200, 100))
        time.sleep(1)
        log_to_console("[ERROR] Failed to submit ticket. Connection refused.", (255, 100, 100))
    else:
        log_to_console(f"[MENU] {user_data} selected")

# --- GUI Setup ---
dpg.create_context()
dpg.create_viewport(title="ATXLP Overlay Suite", width=1600, height=900)
dpg.setup_dearpygui()

with dpg.window(tag="root", no_title_bar=True, no_move=True, no_resize=True,
                no_collapse=True, width=1600, height=900):

    # Menu Bar
    with dpg.menu_bar():
        with dpg.menu(label="File"):
            dpg.add_menu_item(label="Open Config", callback=on_menu, user_data="Open Config")
            dpg.add_menu_item(label="Save Snapshot", callback=on_menu, user_data="Save Snapshot")
            dpg.add_menu_item(label="Exit", callback=on_menu, user_data="Exit")
        with dpg.menu(label="Tools"):
            dpg.add_menu_item(label="Force Recheck", callback=on_menu, user_data="Force Recheck")
            dpg.add_menu_item(label="Dump Memory", callback=on_menu, user_data="Dump Memory")
            dpg.add_menu_item(label="Export Logs", callback=on_menu, user_data="Export Logs")
        with dpg.menu(label="Help"):
            dpg.add_menu_item(label="About ATXLP", callback=on_menu, user_data="About ATXLP")
            dpg.add_menu_item(label="Documentation", callback=on_menu, user_data="Documentation")
            dpg.add_menu_item(label="Report Bug", callback=on_menu, user_data="Report Bug")

    # --- Panels ---
    with dpg.group(horizontal=True):
        # Control Panel
        with dpg.child_window(width=400, height=250, border=True):
            dpg.add_text("ATXLP Process Manager", color=(0, 200, 255))
            dpg.add_progress_bar(tag="progress", default_value=0.0, width=-1, height=20)
            dpg.add_text("Waiting...", tag="status")
            dpg.add_button(label="Start Loading", tag="start_btn", callback=start_loading)

        # Console
        with dpg.child_window(width=600, height=250, border=True):
            with dpg.child_window(tag="console", autosize_x=True, autosize_y=True, border=True):
                dpg.add_text(">>> Console booted", color=(100, 200, 255))

    with dpg.group(horizontal=True):
        # Memory Inspector
        with dpg.child_window(width=400, height=300, border=True):
            dpg.add_text("Memory Inspector")
            for i in range(20):  # extra lines
                row = " ".join(f"{random.randint(0,255):02X}" for _ in range(16))
                dpg.add_text(f"0x{0x1000+i*16:04X}: {row}")

        # Docs Inspector
        with dpg.child_window(width=400, height=300, border=True):
            dpg.add_text("Loaded module: EasyAntiCheat_x64.sys", color=(255, 200, 200))
            dpg.add_separator()
            dpg.add_checkbox(label="Enable Kernel Hooks", callback=on_checkbox, user_data="Enable Kernel Hooks")
            dpg.add_checkbox(label="Force Bypass Checks", callback=on_checkbox, user_data="Force Bypass Checks")
            dpg.add_slider_int(label="Scan Interval", default_value=30, max_value=120,
                               callback=on_slider, user_data="Scan Interval")
            dpg.add_input_text(label="Custom Config Path", default_value="C:/EAC/config.json")

        # Tools
        with dpg.child_window(width=350, height=300, border=True):
            dpg.add_color_picker(label="Overlay Color", default_value=(120, 180, 255, 255), width=200,
                                 callback=on_color, user_data="Overlay Color")
            dpg.add_slider_float(label="CPU Usage %", default_value=27.3, max_value=100.0,
                                 callback=on_slider, user_data="CPU Usage %")
            dpg.add_slider_float(label="GPU Usage %", default_value=65.9, max_value=100.0,
                                 callback=on_slider, user_data="GPU Usage %")
            dpg.add_combo(label="Mode", items=["Debug", "Silent", "Aggressive", "Experimental"],
                          callback=on_combo, user_data="Mode")
            dpg.add_button(label="Force Update Check", callback=on_button, user_data="Force Update Check")

dpg.show_viewport()
dpg.set_primary_window("root", True)
dpg.start_dearpygui()
running = False
dpg.destroy_context()
