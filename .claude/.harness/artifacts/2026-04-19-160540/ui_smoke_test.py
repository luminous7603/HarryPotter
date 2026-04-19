from playwright.sync_api import sync_playwright
import sys

BASE_URL = "http://localhost:4322"
PATHS = [
    "/",
    "/characters",
    "/characters/harry-potter",
    "/characters/hermione-granger",
    "/characters/ron-weasley",
    "/characters/albus-dumbledore",
    "/characters/lord-voldemort",
    "/books",
    "/books/01-philosophers-stone",
    "/books/07-deathly-hallows",
    "/world",
    "/world/gryffindor",
    "/world/slytherin",
    "/world/ravenclaw",
    "/world/hufflepuff",
    "/world/hogwarts",
    "/world/spells",
    "/upcoming",
]

errors = []

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    for path in PATHS:
        page = browser.new_page()
        console_errors = []

        def on_console(msg, errs=console_errors):
            if msg.type == "error":
                errs.append(msg.text)

        page.on("console", on_console)

        try:
            response = page.goto(BASE_URL + path, timeout=10000)
            if response is None:
                errors.append(f"[{path}] 응답 없음")
            elif response.status >= 400:
                errors.append(f"[{path}] HTTP {response.status}")
            elif console_errors:
                errors.append(f"[{path}] 콘솔 에러: {console_errors}")
            else:
                print(f"  PASS {path}")
        except Exception as e:
            errors.append(f"[{path}] 로드 실패: {e}")
        finally:
            page.close()

    browser.close()

if errors:
    print("\nFAIL:")
    for e in errors:
        print(f"  {e}")
    sys.exit(1)
else:
    print("\nPASS: 모든 UI 경로 정상")
