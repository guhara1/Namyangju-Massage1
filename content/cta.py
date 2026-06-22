# 공통 예약 CTA 블록 — 메인·지역·역·생활권 페이지 공용 컴포넌트
from .site import PHONE, PHONE_DISPLAY


def cta(text="방문 위치와 희망 시간을 알려주시면 가능 여부를 바로 확인해 드립니다."):
    return f"""
<section class="cta">
<h2>전화예약</h2>
<p>{text}</p>
<a class="cta-phone" href="tel:{PHONE}">{PHONE_DISPLAY}</a>
<p class="cta-sub">연중무휴 24시간 상담 · 경기 남양주시 전지역 방문</p>
</section>
"""


CTA = cta()
