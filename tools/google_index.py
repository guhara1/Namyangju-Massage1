#!/usr/bin/env python3
"""Google Indexing API 통보 (선택) — 구글에 URL 갱신을 직접 통보.

주의·한계:
  - 구글은 IndexNow 미참여. 구글 Indexing API 는 공식적으로 JobPosting/
    BroadcastEvent 구조화 페이지를 대상으로 합니다. 일반 페이지에도 통보는
    되지만 구글이 보장하는 색인 수단은 sitemap 입니다. 일반 색인의 정석은
    sitemap.xml + Search Console 이며, 이 스크립트는 보조 수단입니다.
  - 구글은 과거 sitemap ping(google.com/ping?sitemap=) 을 2023년에 폐지했으므로
    별도 ping 은 제공하지 않습니다. Search Console 에 sitemap 을 등록하세요.

준비:
  1) Google Cloud 프로젝트에서 Indexing API 사용 설정
  2) 서비스 계정 생성 → JSON 키 발급
  3) Search Console 속성에 그 서비스 계정 이메일을 '소유자'로 추가
  4) pip install google-auth
  5) export GOOGLE_APPLICATION_CREDENTIALS=/경로/service_account.json

사용법:
  python tools/google_index.py                # sitemap.xml 전체 통보
  python tools/google_index.py URL [URL ...]  # 지정 URL 통보
"""
import json
import os
import re
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"
SCOPES = ["https://www.googleapis.com/auth/indexing"]


def access_token() -> str:
    cred_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    if not cred_path or not os.path.exists(cred_path):
        sys.exit("GOOGLE_APPLICATION_CREDENTIALS 환경변수에 서비스계정 JSON 경로를 지정하세요.")
    try:
        from google.oauth2 import service_account
        from google.auth.transport.requests import Request
    except ImportError:
        sys.exit("의존성이 필요합니다: pip install google-auth")
    creds = service_account.Credentials.from_service_account_file(cred_path, scopes=SCOPES)
    creds.refresh(Request())
    return creds.token


def urls_from_sitemap() -> list:
    path = os.path.join(ROOT, "sitemap.xml")
    if not os.path.exists(path):
        sys.exit("sitemap.xml 이 없습니다. 먼저 python3 build.py 를 실행하세요.")
    return re.findall(r"<loc>(.*?)</loc>", open(path, encoding="utf-8").read())


def publish(url: str, token: str) -> None:
    payload = json.dumps({"url": url, "type": "URL_UPDATED"}).encode("utf-8")
    req = urllib.request.Request(
        ENDPOINT, data=payload, method="POST",
        headers={"Content-Type": "application/json",
                 "Authorization": f"Bearer {token}"},
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            print(f"[{resp.status}] {url}")
    except Exception as e:  # noqa: BLE001
        print(f"오류 {url}: {e}")


def main() -> None:
    urls = sys.argv[1:] or urls_from_sitemap()
    token = access_token()
    print(f"통보 대상 {len(urls)}개 URL")
    for u in urls:
        publish(u, token)


if __name__ == "__main__":
    main()
