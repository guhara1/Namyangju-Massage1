# 사이트 공통 설정
# 배포 도메인 확정 후 BASE_URL 을 실제 도메인으로 변경하세요.
BASE_URL = "https://namyangju-massage1.pages.dev"

BRAND = "바로 GO"
BRAND_MARK = "GO"
PHONE = "0508-202-4719"
PHONE_DISPLAY = "0508-202-4719"

# 제작·제휴 문의 텔레그램 링크
TELEGRAM_BUILD = "https://t.me/googleseolab"   # 웹사이트 제작문의
TELEGRAM_PARTNER = "https://t.me/googleseolab"  # 제휴문의

# IndexNow 키 (Bing·Naver·Yandex 즉시 색인 통보용)
# 빌드 시 루트에 <KEY>.txt 파일이 생성되며, 배포 후 그 URL이 살아 있어야 통보가 검증된다.
INDEXNOW_KEY = "ab63fa24781c488f832870f492ae79cadd7a765382f84397a36d15f16b2867c6"

# 경로 접두사 — 루트(/)에서 바로 서빙한다. (네임스페이스 없음)
BASE = ""

# 상단 메뉴 — 메뉴명·URL에는 "출장마사지"를 반복하지 않고 지역명·역명·생활권만 표시한다.
NAV = [
    ("남양주 홈", f"/{BASE}", []),
    ("지역별 안내", f"/{BASE}#areas", [
        ("다산동", f"/{BASE}dasan-dong/"),
        ("별내동", f"/{BASE}byeollae-dong/"),
        ("별내면", f"/{BASE}byeollae-myeon/"),
        ("진접읍", f"/{BASE}jinjeop-eup/"),
        ("오남읍", f"/{BASE}onam-eup/"),
        ("퇴계원읍", f"/{BASE}toegyewon-eup/"),
        ("진건읍", f"/{BASE}jingeon-eup/"),
        ("호평동", f"/{BASE}hopyeong-dong/"),
        ("평내동", f"/{BASE}pyeongnae-dong/"),
        ("금곡동", f"/{BASE}geumgok-dong/"),
        ("양정동", f"/{BASE}yangjeong-dong/"),
        ("와부읍", f"/{BASE}wabu-eup/"),
        ("화도읍", f"/{BASE}hwado-eup/"),
        ("수동면", f"/{BASE}sudong-myeon/"),
        ("조안면", f"/{BASE}joan-myeon/"),
    ]),
    ("역세권 안내", f"/{BASE}station/", [
        ("역 전체", f"/{BASE}station/"),
        ("다산역", f"/{BASE}station/dasan-station/"),
        ("별내역", f"/{BASE}station/byeollae-station/"),
        ("별내별가람역", f"/{BASE}station/byeollae-byeolgaram-station/"),
        ("진접역", f"/{BASE}station/jinjeop-station/"),
        ("오남역", f"/{BASE}station/onam-station/"),
        ("퇴계원역", f"/{BASE}station/toegyewon-station/"),
        ("사릉역", f"/{BASE}station/sareung-station/"),
        ("금곡역", f"/{BASE}station/geumgok-station/"),
        ("평내호평역", f"/{BASE}station/pyeongnae-hopyeong-station/"),
        ("마석역", f"/{BASE}station/maseok-station/"),
        ("천마산역", f"/{BASE}station/cheonmasan-station/"),
        ("덕소역", f"/{BASE}station/deokso-station/"),
        ("도심역", f"/{BASE}station/dosim-station/"),
        ("팔당역", f"/{BASE}station/paldang-station/"),
        ("운길산역", f"/{BASE}station/ungilsan-station/"),
    ]),
    ("생활권 안내", f"/{BASE}area/", [
        ("생활권 전체", f"/{BASE}area/"),
        ("다산신도시 생활권", f"/{BASE}area/dasan-newtown/"),
        ("별내신도시 생활권", f"/{BASE}area/byeollae-newtown/"),
        ("진접·오남 생활권", f"/{BASE}area/jinjeop-onam/"),
        ("호평·평내 생활권", f"/{BASE}area/hopyeong-pyeongnae/"),
        ("금곡·양정 원도심 생활권", f"/{BASE}area/geumgok-yangjeong/"),
        ("덕소·와부 생활권", f"/{BASE}area/deokso-wabu/"),
        ("마석·화도 생활권", f"/{BASE}area/maseok-hwado/"),
        ("퇴계원·진건 생활권", f"/{BASE}area/toegyewon-jingeon/"),
        ("팔당·조안 한강변 생활권", f"/{BASE}area/paldang-joan/"),
        ("수동·축령산 생활권", f"/{BASE}area/sudong-chungnyeongsan/"),
        ("별내면·청학 생활권", f"/{BASE}area/byeollae-myeon-cheonghak/"),
    ]),
    ("예약 안내", f"/{BASE}reservation/", [
        ("예약 가능 지역 확인", f"/{BASE}reservation/#area"),
        ("예약 가능 시간 안내", f"/{BASE}reservation/#hours"),
        ("추가 이동비 안내", f"/{BASE}reservation/#move"),
        ("결제 방식 안내", f"/{BASE}reservation/#payment"),
        ("예약 변경·취소 기준", f"/{BASE}reservation/#change"),
    ]),
    ("이용 전 확인사항", f"/{BASE}checklist/", [
        ("방문 가능 주소 확인", f"/{BASE}checklist/#address"),
        ("자택 이용 전 확인", f"/{BASE}checklist/#home"),
        ("숙소 이용 전 확인", f"/{BASE}checklist/#stay"),
        ("개인정보 처리 기준", f"/{BASE}checklist/#privacy"),
        ("불법·선정적 서비스 불가", f"/{BASE}checklist/#prohibited"),
    ]),
    ("홈타이 이용 가이드", f"/{BASE}hometai-guide/", [
        ("홈타이란?", f"/{BASE}hometai-guide/#what"),
        ("출장마사지와 차이", f"/{BASE}hometai-guide/#diff"),
        ("이용 전 기준", f"/{BASE}hometai-guide/#standard"),
        ("처음 이용 안내", f"/{BASE}hometai-guide/#first"),
    ]),
    ("고객센터", f"/{BASE}support/", [
        ("문의하기", f"/{BASE}support/#contact"),
        ("자주 묻는 질문", f"/{BASE}support/#faq"),
        ("운영 기준", f"/{BASE}support/#rule"),
        ("사이트 소개", f"/{BASE}about/"),
        ("개인정보 처리방침", f"/{BASE}privacy/"),
        ("이용약관", f"/{BASE}terms/"),
    ]),
]
