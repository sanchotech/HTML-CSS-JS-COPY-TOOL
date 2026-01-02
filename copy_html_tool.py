import os
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from tqdm import tqdm

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def loading_animation():
    msg = "TOOLS IS STARTING"
    for c in msg:
        print(c, end='', flush=True)
        time.sleep(0.1)
    print("\n")
    for i in range(21):
        bar = "█" * i + '-' * (20 - i)
        print(f"\rLoading: [{bar}] {i * 5}%", end='', flush=True)
        time.sleep(0.05)
    print("\n")

def display_header():
    print("\033[1;32m╔═════════════════════════════════════╗")
    print("║    SANCHO HTML + CSS + JS COPY TOOL      ║")
    print("╚═════════════════════════════════════╝")
    print("\033[0;91m     DEVELOPED BY SANCHO TECH \033[0m\n")

def main_menu():
    print("\033[1;36m[1] COPY WEBSITE HTML + CSS + API/JS")
    print("[2] JOIN TOOL OWNER WHATSAPP CHANNEL\033[0m")
    return input("\n📥 ENTER OPTION (1/2): ").strip()

def post_copy_menu():
    print("\n\033[1;33m[1] COPY ANOTHER SITE")
    print("[2] EXIT TOOL\033[0m")
    return input("\n👉 ENTER OPTION (1/2): ").strip()

def copy_html_css_js():
    while True:
        url = input("\n🔗 Enter website link: ").strip()
        folder_path = "/sdcard/DCIM/copied_site"
        os.makedirs(folder_path, exist_ok=True)

        try:
            print("\n📥 Downloading site...")
            response = requests.get(url)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')

            # Save HTML
            with open(os.path.join(folder_path, "index.html"), "w", encoding="utf-8") as f:
                f.write(response.text)
            print("✅ HTML saved as index.html")

            # Gather CSS and JS links
            css_links = [urljoin(url, link.get("href")) for link in soup.find_all("link", rel="stylesheet") if link.get("href")]
            js_links = [urljoin(url, script.get("src")) for script in soup.find_all("script") if script.get("src")]

            all_links = css_links + js_links
            total = len(all_links)
            if total == 0:
                print("ℹ️ No CSS or JS files found.")
            else:
                print(f"📦 Downloading {total} files (CSS + JS)...")
                for i, file_url in enumerate(tqdm(all_links, desc="📊 Progress", ncols=70)):
                    try:
                        file_res = requests.get(file_url, timeout=10)
                        file_res.raise_for_status()
                        ext = ".css" if file_url.endswith(".css") else ".js"
                        file_name = f"{'style' if ext == '.css' else 'script'}_{i}{ext}"
                        with open(os.path.join(folder_path, file_name), "w", encoding="utf-8") as f:
                            f.write(file_res.text)
                    except Exception:
                        continue

            print("\n✅ All files saved in: DCIM/copied_site")

        except Exception as e:
            print(f"\n❌ Error: {e}")

        next_action = post_copy_menu()
        if next_action == "1":
            clear_screen()
            display_header()
            continue
        elif next_action == "2":
            print("\n👋 Exiting tool... Stay safe hacker 🕶️")
            break
        else:
            print("❌ Invalid option. Exiting.")
            break

def open_whatsapp_channel():
    print("\n📲 Opening WhatsApp Channel...")
    try:
        os.system("termux-open-url https://whatsapp.com/channel/0029VaxkHitE50Ujw3l8Fv2D")
    except Exception as e:
        print(f"❌ Failed to open link: {e}")

# ==== RUN TOOL ====
clear_screen()
loading_animation()
clear_screen()
display_header()
choice = main_menu()

if choice == "1":
    copy_html_css_js()
elif choice == "2":
    open_whatsapp_channel()
else:
    print("❌ Invalid option.")