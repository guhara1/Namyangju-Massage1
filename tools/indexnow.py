#!/usr/bin/env python3
"""IndexNow 즉시 색인 통보 — Bing·Naver·Yandex 등 참여 검색엔진에 한 번에 통보.

사용법:
  python tools/indexnow.py                # sitemap.xml 의 모든 URL 통보(일괄)
  python tools/indexnow.py URL [URL ...]  # 지정한 URL만 통보(글 올릴 때)

준비:
  1) python3 build.py 로 사이트와 <KEY>.txt 키 파일을 생성한다.
  2) 배포(Cloudflare Pages)가 끝나 https://도메인/<KEY>.txt 가 살아 있어야 한다.
     (IndexNow 가 이 파일로 소유권을 검증한다.)

참고: 구글은 IndexNow 미참여 → 구글은 sitemap + (선택)Indexing API 로 처리.
"""
import json
import os
import re
import sys
import urllib.request
import urllib.parse

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from content.site import BASE_URL, INDEXNOW_KEY

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENDPOINT = "https://api.indexnow.org/indexnow"  # 참여 엔진 전체로 분배
HOST = urllib.parse.urlparse(BASE_URL).netloc
KEY_LOCATION = f"{BASE_URL.rstrip('/')}/{INDEXNOW_KEY}.txt"
CHUNK = 10000  # IndexNow 1회 최대 URL 수


def urls_from_sitemap() -> list:
    path = os.path.join(ROOT, "sitemap.xml")
    if not os.path.exists(path):
        sys.exit("sitemap.xml 이 없습니다. 먼저 python3 build.py 를 실행하세요.")
    xml = open(path, encoding="utf-8").read()
    return re.findall(r"<loc>(.*?)</loc>", xml)


def submit(urls: list) -> None:
    if not urls:
        sys.exit("통보할 URL이 없습니다.")
    for i in range(0, len(urls), CHUNK):
        chunk = urls[i:i + CHUNK]
        payload = json.dumps({
            "host": HOST,
            "key": INDEXNOW_KEY,
            "keyLocation": KEY_LOCATION,
            "urlList": chunk,
        }).encode("utf-8")
        req = urllib.request.Request(
            ENDPOINT, data=payload,
            headers={"Content-Type": "application/json; charset=utf-8"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                print(f"[{resp.status}] {len(chunk)}개 URL 통보 완료 → {ENDPOINT}")
        except urllib.error.HTTPError as e:
            # 202/200 이 정상. 그 외는 본문 출력.
            body = e.read().decode("utf-8", "ignore")
            print(f"[{e.code}] 응답: {body or e.reason}")
        except Exception as e:  # noqa: BLE001
            print(f"오류: {e}")


def main() -> None:
    args = sys.argv[1:]
    urls = args if args else urls_from_sitemap()
    print(f"host={HOST} key={INDEXNOW_KEY[:8]}… keyLocation={KEY_LOCATION}")
    print(f"통보 대상 {len(urls)}개 URL")
    submit(urls)


if __name__ == "__main__":
    main()
