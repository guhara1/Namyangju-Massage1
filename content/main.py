# 남양주시 메인 페이지 — 허브 역할. 키워드를 모두 밀어 넣지 않고 상세 페이지로 연결한다.
from .site import BASE, BASE_URL, BRAND, PHONE, PHONE_DISPLAY
from .cta import cta

_H = "/" + BASE  # /gyeonggi/namyangju/

_JSONLD = f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "{BRAND}",
  "url": "{BASE_URL}{_H}",
  "telephone": "{PHONE}",
  "image": {{
    "@type": "ImageObject",
    "url": "{BASE_URL}/assets/og-image.png",
    "width": 1200,
    "height": 630
  }},
  "description": "경기 남양주시 전지역 방문 출장마사지·홈타이 예약 안내",
  "areaServed": {{
    "@type": "AdministrativeArea",
    "name": "경기도 남양주시"
  }}
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "남양주시 출장마사지 · 남양주시 홈타이 지역별 예약 안내",
  "url": "{BASE_URL}{_H}",
  "inLanguage": "ko",
  "isPartOf": {{ "@type": "WebSite", "name": "{BRAND}", "url": "{BASE_URL}{_H}" }},
  "primaryImageOfPage": {{
    "@type": "ImageObject",
    "url": "{BASE_URL}/assets/og-image.png"
  }}
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {{ "@type": "ListItem", "position": 1, "name": "남양주 홈", "item": "{BASE_URL}{_H}" }}
  ]
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{
      "@type": "Question",
      "name": "남양주시 전지역 방문이 가능한가요?",
      "acceptedAnswer": {{ "@type": "Answer", "text": "예약 시간과 정확한 위치, 배정 상황에 따라 가능 여부가 달라집니다. 지역별 안내에서 다산동, 별내동, 진접읍, 호평동, 와부읍 등 대표 지역 기준으로 확인할 수 있습니다." }}
    }},
    {{
      "@type": "Question",
      "name": "다산역이나 별내역 인근도 가능한가요?",
      "acceptedAnswer": {{ "@type": "Answer", "text": "주요 역세권은 역 상세 페이지에서 주변 생활권과 함께 안내합니다. 정확한 가능 여부는 예약 시 위치를 기준으로 확인합니다." }}
    }},
    {{
      "@type": "Question",
      "name": "수동면이나 조안면 같은 외곽도 방문하나요?",
      "acceptedAnswer": {{ "@type": "Answer", "text": "수동면, 조안면 등 외곽 지역도 시간대와 차량 이동 기준에 따라 방문 가능합니다. 추가 이동비 여부는 예약 시 안내해 드립니다." }}
    }}
  ]
}}
</script>
"""

_HERO = f"""<section class="hero">
  <div class="hero-inner">
    <p class="hero-badge">Premium Visiting Care · 경기 남양주시 전지역</p>
    <h1>남양주 출장마사지·홈타이<br>지역별 예약 안내</h1>
    <p class="hero-lead">샵까지 갈 필요 없이, 계신 곳에서 받는 프리미엄 방문 관리.<br>자택·오피스텔·숙소 어디든 전화 한 통이면 예약이 끝납니다.</p>
    <div class="hero-actions">
      <a class="hero-btn primary" href="tel:{PHONE}">📞 {PHONE_DISPLAY}</a>
      <a class="hero-btn" href="{_H}#areas">지역별 안내 보기</a>
    </div>
    <ul class="hero-stats">
      <li><strong>15곳</strong><span>대표 지역</span></li>
      <li><strong>15개</strong><span>역세권 안내</span></li>
      <li><strong>11개</strong><span>생활권 안내</span></li>
      <li><strong>24시간</strong><span>예약 상담</span></li>
    </ul>
  </div>
</section>
"""

_BODY = f"""
<section id="intro">
<h2>남양주시에서 출장마사지를 찾을 때 먼저 확인할 기준</h2>
<p>남양주 출장마사지를 찾는 분들은 보통 현재 위치에서 가까운 방문 가능 지역을 먼저 확인합니다. 남양주시는 면적이 넓고 생활권이 뚜렷하게 나뉘는 도시라, 단순히 "남양주 전지역 가능"이라고만 적힌 안내보다 대표 지역과 역세권을 나누어 보는 편이 훨씬 정확합니다. {BRAND}는 다산동·별내동 같은 신도시 생활권부터 와부읍·화도읍·수동면·조안면 같은 외곽 생활권까지 위치별 특징과 방문 조건을 따로 정리했습니다. 예약 전에 본인 위치와 비슷한 지역 페이지를 먼저 확인하시면 예약 가능 시간, 추가 이동비, 방문 가능 주소 기준을 미리 파악할 수 있습니다. 남양주 홈타이 역시 자택·숙소·사무실 인근에서 예약 가능 여부를 확인한 뒤 이용하는 방문형 관리 서비스이므로, 같은 기준으로 안내합니다.</p>
</section>

<section id="zones">
<h2>다산·별내·진접·호평·덕소 생활권 차이</h2>
<p>남양주시는 생활권에 따라 분위기와 검색 의도가 다릅니다. 다산동은 다산신도시와 다산역 중심 생활권이고, 별내동은 별내신도시와 별내역 중심 생활권입니다. 진접읍과 오남읍은 4호선 역세권을 낀 북부 주거 생활권, 호평동과 평내동은 평내호평역 주변 동부 생활권, 와부읍은 덕소역과 한강변 생활권, 화도읍은 마석과 천마산 인접 생활권으로 볼 수 있습니다. 금곡동과 양정동은 남양주시청·홍유릉이 있는 원도심 행정 생활권이고, 수동면과 조안면은 차량 이동 기준이 중요한 외곽 생활권입니다. 같은 남양주라도 신도시·원도심·외곽이 섞여 있어, 방문 시간대와 도착 기준을 생활권별로 나누어 안내합니다. 더 넓은 묶음으로 보고 싶다면 <a href="{_H}area/">생활권 안내</a>에서 신도시·원도심·한강변·축령산 생활권을 한눈에 확인할 수 있습니다.</p>
</section>

<section id="areas">
<h2>대표 지역별 방문 가능 지역 안내</h2>
<p>지역별 안내는 남양주시 대표 지역 기준으로 구성됩니다. 각 페이지에서는 해당 생활권의 특징, 가까운 역세권, 방문 전 확인사항, 예약 가능 시간을 지역마다 고유한 내용으로 설명합니다. 다산1동·다산2동처럼 번호로 나뉜 동은 다산동 대표 페이지로 통합했고, 호평동과 평내동, 금곡동과 양정동처럼 검색 의도가 다른 곳은 각각 대표 페이지로 나눴습니다. 아래에서 거주하거나 머무시는 지역을 선택해 주세요.</p>
<ul class="card-grid">
<li><a href="{_H}dasan-dong/">다산동</a></li>
<li><a href="{_H}byeollae-dong/">별내동</a></li>
<li><a href="{_H}byeollae-myeon/">별내면</a></li>
<li><a href="{_H}jinjeop-eup/">진접읍</a></li>
<li><a href="{_H}onam-eup/">오남읍</a></li>
<li><a href="{_H}toegyewon-eup/">퇴계원읍</a></li>
<li><a href="{_H}jingeon-eup/">진건읍</a></li>
<li><a href="{_H}hopyeong-dong/">호평동</a></li>
<li><a href="{_H}pyeongnae-dong/">평내동</a></li>
<li><a href="{_H}geumgok-dong/">금곡동</a></li>
<li><a href="{_H}yangjeong-dong/">양정동</a></li>
<li><a href="{_H}wabu-eup/">와부읍</a></li>
<li><a href="{_H}hwado-eup/">화도읍</a></li>
<li><a href="{_H}sudong-myeon/">수동면</a></li>
<li><a href="{_H}joan-myeon/">조안면</a></li>
</ul>
</section>

<section id="stations">
<h2>다산역·별내역·진접역·평내호평역 역세권 안내</h2>
<p>역세권 안내는 경춘선, 4호선(진접선), 8호선 별내선, 경의중앙선이 지나는 남양주 주요 역을 기준으로 구성합니다. 다산역 출장마사지, 별내역 출장마사지, 진접역 출장마사지, 평내호평역 출장마사지, 마석역 출장마사지, 덕소역 출장마사지처럼 실제 검색어와 가까운 위치 기준으로 정리했으며, 환승역이라도 노선별로 쪼개지 않고 역명 기준 한 페이지만 운영합니다. 역마다 인접 생활권과 대표 동을 연결해 설명하니, 위치를 역 기준으로 떠올리는 분은 아래에서 가까운 역을 선택해 주세요.</p>
<ul class="card-grid">
<li><a href="{_H}station/dasan-station/">다산역</a></li>
<li><a href="{_H}station/byeollae-station/">별내역</a></li>
<li><a href="{_H}station/jinjeop-station/">진접역</a></li>
<li><a href="{_H}station/onam-station/">오남역</a></li>
<li><a href="{_H}station/pyeongnae-hopyeong-station/">평내호평역</a></li>
<li><a href="{_H}station/maseok-station/">마석역</a></li>
<li><a href="{_H}station/deokso-station/">덕소역</a></li>
<li><a href="{_H}station/">역 전체 보기</a></li>
</ul>
</section>

<section id="check">
<h2>남양주시 홈타이 예약 전 확인사항</h2>
<p>남양주 홈타이와 출장마사지 예약 전에는 방문 가능 지역, 예약 가능 시간, 추가 이동비, 결제 방식, 취소 기준, 개인정보 처리 기준을 먼저 확인하는 것이 좋습니다. 다산동과 별내동처럼 접근성이 좋은 신도시도 있지만, 수동면·조안면·별내면 일부 지역은 시간대에 따라 차량 이동 기준이 달라질 수 있습니다. 그래서 각 페이지에는 지역별 이동 기준을 분명하게 적어 두었습니다. 자세한 절차는 <a href="{_H}reservation/">예약 안내</a>에서, 방문 전 준비사항은 <a href="{_H}checklist/">이용 전 확인사항</a>에서 확인하실 수 있습니다. 홈타이와 출장마사지의 차이가 궁금하시면 <a href="{_H}hometai-guide/">홈타이 이용 가이드</a>를 참고해 주세요.</p>
</section>

<section id="dedup">
<h2>남양주시 페이지 중복 방지 운영 기준</h2>
<p>이 사이트는 지역명만 바꾼 비슷한 페이지를 만들지 않습니다. 다산1동·다산2동은 다산동 한 페이지로 통합하고, 다산동 페이지와 다산역 페이지는 같은 본문을 쓰지 않습니다. 별내동과 별내면은 신도시와 청학리 외곽으로 역할을 나누고, 호평동과 평내동은 평내호평역 키워드를 반복하는 대신 생활권 차이를 둡니다. 역세권은 역명 기준 한 URL만 만들고, 예정역이나 미개통역은 단독 페이지로 만들지 않습니다. 메뉴명과 URL에는 "출장마사지"를 붙이지 않고, 제목과 본문 첫 문단에서만 자연스럽게 사용합니다. 이렇게 구성하면 출장마사지·홈타이 키워드를 담으면서도 중복 콘텐츠 위험을 줄일 수 있습니다.</p>
</section>

<section id="howto">
<h2>남양주시 출장마사지 사이트 이용 방법</h2>
<p>이용 순서는 간단합니다. 먼저 <a href="{_H}#areas">지역별 안내</a>에서 본인 위치와 가까운 대표 지역을 고르고, 위치를 역 기준으로 떠올린다면 <a href="{_H}station/">역세권 안내</a>를, 더 넓은 묶음으로 보고 싶다면 <a href="{_H}area/">생활권 안내</a>를 확인합니다. 그다음 <a href="{_H}reservation/">예약 안내</a>에서 가능 시간과 추가 이동비를 확인하고, 전화로 위치와 희망 시간을 알려주시면 가능 여부를 바로 확인해 드립니다. 메인페이지는 남양주 전체 구조를 설명하는 허브이고, 실제 세부 정보는 각 지역·역·생활권 페이지에 담겨 있습니다.</p>
</section>
""" + cta("남양주시 어느 지역이든 위치와 희망 시간만 알려주시면 가능 여부를 바로 확인해 드립니다.")

PAGE = {
    "path": BASE,
    "title": "남양주시 출장마사지｜다산·별내·진접·호평 홈타이 지역 안내",
    "desc": "남양주시 출장마사지·홈타이 예약 전 다산동, 별내동, 진접읍, 호평동, 덕소 생활권을 확인하세요.",
    "h1": "남양주시 출장마사지 · 남양주시 홈타이 지역별 예약 안내",
    "body": _BODY,
    "extra_head": _JSONLD,
    "breadcrumb": [],
    "hero": _HERO,
}
