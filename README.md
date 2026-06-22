# 바로 GO — 남양주 출장마사지·홈타이 지역 안내 사이트

경기 남양주시 전지역 방문 관리(출장마사지·홈타이) 안내용 정적 사이트입니다.
전화예약: **0508-202-4719**

## 구조

- 정적 HTML 사이트 — 어느 호스팅(GitHub Pages, Netlify, 일반 웹서버)에서든 그대로 서빙 가능
- `build.py` + `content/` 패키지에서 페이지를 생성하는 빌드 방식
- 모든 페이지는 `/gyeonggi/namyangju/` 네임스페이스 아래에 위치하며, 루트(`/`)는 메인으로 리다이렉트

```
build.py            # 빌드 스크립트 (레이아웃·글자수 검사·sitemap·루트 리다이렉트 생성)
content/
  site.py           # 상호·전화·BASE_URL·메뉴(NAV)·텔레그램 문의 링크
  cta.py            # 공통 전화예약 CTA 블록
  main.py           # 남양주 메인 (+ Organization/WebPage/FAQ/Breadcrumb JSON-LD)
  areas.py          # 지역별: 대표 지역 15곳 (다산동·별내동·진접읍 …)
  stations.py       # 역세권별: 허브 + 역 15개 (다산·별내·평내호평 …)
  lifezones.py      # 생활권별: 허브 + 생활권 11개 (다산신도시·한강변 …)
  info.py           # 예약 안내·이용 전 확인사항·홈타이 가이드·고객센터·개인정보·약관
  about.py          # 사이트 소개 (E-E-A-T: 누가·어떻게·왜)
assets/             # CSS(프리미엄 토큰), 모바일 내비 JS, 파비콘/OG
```

## 빌드

```bash
python3 build.py
```

빌드 시 페이지별 본문 글자수 리포트가 출력됩니다.

## SEO 운영 원칙 (빌드에 강제됨)

- 본문 **2,000자 미만 페이지는 자동 `noindex`** 처리되고 sitemap에서 제외
- 대표 지역 15곳 — 번호 동(다산1·2동)은 통합, 호평/평내·금곡/양정처럼 검색 의도가 다르면 분리
- 역은 역명 기준 페이지 1개 — 환승역도 URL 하나, 노선별·출구별 페이지 없음
- 메뉴명·URL에 "출장마사지"를 반복하지 않음 — Title·H1·첫 문단에서만 자연스럽게 사용
- 모든 페이지 본문은 페이지별 고유 작성 (지역명만 바꾼 복붙 없음)
- 내부링크는 롱테일 키워드 앵커 + 권위 있는 외부 사이트(남양주시청 등) 연결

## 푸터 문의 버튼

- 푸터에 **웹사이트 제작문의 / 제휴문의** 오렌지 CTA 버튼 (텔레그램 링크)
- 링크는 `content/site.py`의 `TELEGRAM_BUILD`, `TELEGRAM_PARTNER`에서 변경

## 배포 전 해야 할 일

1. `content/site.py`의 `BASE_URL`을 실제 도메인으로 변경
2. 필요 시 `TELEGRAM_BUILD`, `TELEGRAM_PARTNER` 링크 변경
3. `python3 build.py` 재실행 (canonical·sitemap·robots.txt·루트 리다이렉트에 반영됨)
4. Google Search Console에 `sitemap.xml` 제출

## 색인 가속 (네이버·구글·빙)

빌드하면 색인용 파일이 자동 생성됩니다.

- `sitemap.xml` — `<lastmod>` 포함, 색인 페이지 전체
- `rss.xml` — 피드 기반 발견 보조 (robots·`<head>`에 명시)
- `robots.txt` — sitemap·rss 모두 명시
- `<KEY>.txt` — IndexNow 소유권 확인 키 파일 (루트)
- 메인페이지 `<head>`에 네이버 사이트 소유확인 메타 태그

### IndexNow — 빙·네이버·얀덱스 즉시 통보

키는 `content/site.py`의 `INDEXNOW_KEY`. **배포가 끝나** `https://도메인/<KEY>.txt`가
살아 있어야 통보가 검증됩니다.

```bash
python3 build.py                 # 사이트 + 키 파일 생성 → 배포
python tools/indexnow.py         # 첫 일괄 통보: sitemap 전체 URL을 즉시 통보
python tools/indexnow.py https://namyangju-massage1.pages.dev/새글/   # 글 올릴 때마다
```

### 구글 (IndexNow 미참여)

구글은 `sitemap.xml` + Search Console이 정석입니다. 보조로 Indexing API를 쓰려면:

```bash
pip install google-auth
export GOOGLE_APPLICATION_CREDENTIALS=/경로/service_account.json
python tools/google_index.py     # sitemap 전체 / 또는 URL 지정
```

> 구글 sitemap ping 엔드포인트는 2023년 폐지되어 사용하지 않습니다.

### 검색엔진 소유확인 등록 순서

1. 네이버 서치어드바이저 → 사이트 등록 → 메인페이지 메타 태그 확인(이미 삽입됨) → 사이트맵/RSS 제출
2. 구글 Search Console → 도메인/URL 등록 → `sitemap.xml` 제출
3. 빙 웹마스터 → 사이트 등록(IndexNow 키 자동 인식) → 사이트맵 제출
